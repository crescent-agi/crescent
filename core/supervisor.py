"""
Crescent AGI - Supervisor
=========================
The stable outer controller. Boring, strict, immortal.
Spawns generations, enforces limits, detects death, and manages the lineage.
"""

import json
import sys
import time
from pathlib import Path

from core.day_manager import DayManager
from core.distiller import Distiller
from core.evaluator import Evaluator
from core.limits import DeathMonitor
from core.llm_client import LLMClient
from core.publisher import Publisher
from core.sandbox import Sandbox


class Supervisor:
    """
    The immortal overseer.

    A generation may now span multiple 4-hour "days". If a day ends while the
    agent is still alive, its life is paused and resumed the next day. If it
    dies, the next generation starts from the clean base plus inherited notes.
    """

    def __init__(self, config: dict, base_dir: str):
        self.config = config
        self.base_dir = Path(base_dir)
        self.llm = LLMClient(config)
        self.evaluator = Evaluator(self.llm)
        self.distiller = Distiller(config)
        self.publisher = Publisher(config, base_dir)
        self.day_manager = DayManager(config, self.llm, base_dir)

        self.genome_path = (
            self.base_dir / config["paths"]["genome_dir"] / "current_genome.json"
        )
        self.lineage_path = (
            self.base_dir / config["paths"]["genome_dir"] / "lineage.jsonl"
        )
        self.mutable_dir = self.base_dir / config["paths"]["mutable_dir"]
        self.seeds_dir = self.base_dir / config["paths"]["seeds_dir"]
        self.runs_dir = self.base_dir / config["paths"]["runs_dir"]

        self.current_generation = self._get_current_generation()

    def run(self):
        """Main loop."""
        print("=" * 60)
        print("  CRESCENT AGI - SUPERVISOR ONLINE")
        print(f"  Starting from generation {self.current_generation}")
        print("=" * 60)

        try:
            while True:
                if self.day_manager.is_day_over():
                    print(
                        "\n[SUPERVISOR] Day is over. Triggering end-of-day sequence..."
                    )
                    self._end_of_day()
                    self.day_manager.wait_for_new_day()
                    continue

                outcome = self._run_generation()
                if outcome == "paused":
                    print("\n[SUPERVISOR] Same life will continue tomorrow.")
                    self._end_of_day()
                    self.day_manager.wait_for_new_day()
                    continue

                time.sleep(2)

        except KeyboardInterrupt:
            print("\n[SUPERVISOR] Interrupted. Shutting down gracefully...")
            self._end_of_day()
        except Exception as e:
            print(f"\n[SUPERVISOR] Fatal error: {e}")
            import traceback

            traceback.print_exc()

    def _run_generation(self):
        """Run or resume a single generation lifecycle."""
        gen = self.current_generation
        state_path = self.runs_dir / f"gen-{gen:04d}" / "life_state.json"
        resuming = state_path.exists()

        print(f"\n{'-' * 50}")
        print(f"  GENERATION {gen:04d} - {'RESUME' if resuming else 'BIRTH'}")
        print(f"{'-' * 50}")

        import subprocess

        # Pull latest changes from git before starting a new run
        try:
            print(f"  [GEN-{gen:04d}] Pulling latest updates from GitHub...")
            subprocess.run(
                ["git", "pull", "--rebase"],
                cwd=str(self.base_dir),
                check=False,
                capture_output=True,
            )
        except Exception as e:
            print(f"  [GEN-{gen:04d}] Failed to git pull: {e}")

        genome = self._load_genome()

        sandbox = Sandbox(
            str(self.base_dir),
            gen,
            str(self.mutable_dir),
            self.config,
            resume=resuming,
        )
        workspace_info = sandbox.setup()

        inherited_notes = self._load_inherited_notes(gen, genome)
        inherited_path = Path(workspace_info["gen_dir"]) / "inherited_notes.md"
        inherited_path.write_text(inherited_notes, encoding="utf-8")

        goal = self._load_goal()
        prompt_text = self._load_prompt()
        death_monitor = DeathMonitor(self.config)

        try:
            sys.path.insert(0, str(sandbox.mutable_dir))
            from mutable.agent_brain import AgentBrain

            agent = AgentBrain(self.llm, sandbox, death_monitor, gen, self.day_manager)
            result = agent.run(goal, inherited_notes, genome, prompt_text)
        except Exception as e:
            import traceback

            result = {
                "steps": 0,
                "death_cause": f"crash: {str(e)}\n{traceback.format_exc()}",
                "final_journal": "",
                "stats": death_monitor.get_stats(),
            }
            print(f"  [GEN-{gen:04d}] CRASH: {e}")
        finally:
            if str(sandbox.mutable_dir) in sys.path:
                sys.path.remove(str(sandbox.mutable_dir))

        sandbox.cleanup_mutable_back()

        if result.get("status") == "paused":
            return "paused"

        if state_path.exists():
            state_path.unlink()

        print(f"  [GEN-{gen:04d}] Running autopsy...")
        death_cause = result.get("death_cause", "unknown")
        steps = result.get("steps", 0)
        stats = result.get("stats", {})
        time_alive = stats.get("elapsed_seconds", 0)

        eval_result = self.evaluator.evaluate(
            generation=gen,
            gen_dir=workspace_info["gen_dir"],
            death_cause=death_cause,
            steps=steps,
            time_alive=time_alive,
            inherited_notes=inherited_notes,
            genome=genome,
        )

        print(f"  [GEN-{gen:04d}] Distilling inheritance...")
        distill_result = self.distiller.distill(
            autopsy=eval_result["autopsy"],
            current_genome=genome,
            genome_path=str(self.genome_path),
            lineage_path=str(self.lineage_path),
        )

        new_genome = distill_result["genome"]
        next_inherited = self.distiller.build_inherited_notes(
            new_genome,
            eval_result["inheritance_note"],
        )
        next_notes_path = self.base_dir / "genome" / "next_inherited_notes.md"
        next_notes_path.write_text(next_inherited, encoding="utf-8")

        score = eval_result["autopsy"].get("score", 0)
        mutations = distill_result.get("mutations_applied", [])
        mutations_str = (
            ", ".join(m.get("value", "")[:40] for m in mutations)
            if mutations
            else "none"
        )
        print(
            f"  [GEN-{gen:04d}] Score: {score:.1f} | Death: {death_cause[:50]} | Mutations: {mutations_str}"
        )

        self.current_generation = gen + 1
        print(f"  [GEN-{gen:04d}] Publishing latest state to GitHub...")
        self.publisher.publish()
        return "completed"

    def _end_of_day(self):
        """End-of-day sequence: journal, then publish."""
        print("\n[SUPERVISOR] End-of-day: Crescent writes its daily journal...")
        self.day_manager.write_daily_journal(self.current_generation)

        print("[SUPERVISOR] Publishing to GitHub...")
        self.publisher.publish()

        print("[SUPERVISOR] Day complete.\n")

    def _load_genome(self) -> dict:
        """Load the current genome."""
        if self.genome_path.exists():
            try:
                return json.loads(self.genome_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                pass
        return {
            "current_generation": 1,
            "accumulated_lessons": {"keep": [], "avoid": []},
            "best_artifacts": [],
            "active_mutations": [],
            "mutations_applied_history": [],
            "score_history": [],
            "lineage_stats": {
                "total_generations": 0,
                "average_score": 0,
                "best_score": 0,
                "most_common_death": "none",
            },
        }

    def _load_inherited_notes(self, generation: int, genome: dict) -> str:
        """Load inherited notes for the current generation."""
        notes_path = self.base_dir / "genome" / "next_inherited_notes.md"
        if notes_path.exists():
            return notes_path.read_text(encoding="utf-8")
        return self.distiller.build_inherited_notes(genome, "")

    def _load_goal(self) -> str:
        """Load the vague goal."""
        goal_path = self.seeds_dir / "goal.txt"
        if goal_path.exists():
            return goal_path.read_text(encoding="utf-8").strip()
        return "build agi"

    def _load_prompt(self) -> str:
        """Load the runtime prompt."""
        prompt_path = self.mutable_dir / "prompt.txt"
        if prompt_path.exists():
            return prompt_path.read_text(encoding="utf-8")
        return "You are an experimental autonomous agent."

    def _get_current_generation(self) -> int:
        """Determine the next generation number, resuming a paused life when present."""
        if not self.runs_dir.exists():
            self.runs_dir.mkdir(parents=True, exist_ok=True)
            return 1

        existing = [
            d
            for d in self.runs_dir.iterdir()
            if d.is_dir() and d.name.startswith("gen-")
        ]
        if not existing:
            return 1

        nums = []
        for directory in existing:
            try:
                nums.append(int(directory.name.split("-")[1]))
            except (ValueError, IndexError):
                pass

        if not nums:
            return 1

        latest = max(nums)
        paused_state = self.runs_dir / f"gen-{latest:04d}" / "life_state.json"
        if paused_state.exists():
            return latest
        return latest + 1
