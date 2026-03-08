"""
Crescent AGI — Supervisor
============================
The stable outer controller. Boring, strict, immortal.
Spawns generations, enforces limits, detects death, and manages the lineage.
"""

import json
import time
import shutil
import sys
from pathlib import Path
from datetime import datetime, timezone

from core.llm_client import LLMClient
from core.sandbox import Sandbox
from core.limits import DeathMonitor
from core.evaluator import Evaluator
from core.distiller import Distiller
from core.publisher import Publisher
from core.day_manager import DayManager


class Supervisor:
    """
    The immortal overseer. Manages the generation lifecycle:
    1. Create fresh workspace
    2. Load inherited notes and genome
    3. Inject the vague goal
    4. Let the runtime agent act
    5. Log everything
    6. Kill on death condition
    7. Run evaluator/autopsy
    8. Distill inheritance
    9. Spawn next generation
    10. At end of day, let Crescent write its journal
    """

    def __init__(self, config: dict, base_dir: str):
        self.config = config
        self.base_dir = Path(base_dir)
        self.llm = LLMClient(config)
        self.evaluator = Evaluator(self.llm)
        self.distiller = Distiller(config)
        self.publisher = Publisher(config, base_dir)
        self.day_manager = DayManager(config, self.llm, base_dir)

        # Paths
        self.genome_path = self.base_dir / config["paths"]["genome_dir"] / "current_genome.json"
        self.lineage_path = self.base_dir / config["paths"]["genome_dir"] / "lineage.jsonl"
        self.mutable_dir = self.base_dir / config["paths"]["mutable_dir"]
        self.seeds_dir = self.base_dir / config["paths"]["seeds_dir"]
        self.runs_dir = self.base_dir / config["paths"]["runs_dir"]

        # State
        self.current_generation = self._get_current_generation()
        self.generations_today = 0
        self.max_generations_per_day = config["agent"]["max_generations_per_day"]

    def run(self):
        """
        Main loop. Runs generations until the day is over or max generations reached.
        Then triggers end-of-day journal and publishing.
        """
        print("=" * 60)
        print("  CRESCENT AGI — SUPERVISOR ONLINE")
        print(f"  Starting from generation {self.current_generation}")
        print("=" * 60)

        try:
            while True:
                # Check if day is over
                if self.day_manager.is_day_over():
                    print("\n[SUPERVISOR] Day is over. Triggering end-of-day sequence...")
                    self._end_of_day()
                    self.day_manager.wait_for_new_day()
                    self.generations_today = 0
                    continue

                # Check max generations per day
                if self.generations_today >= self.max_generations_per_day:
                    print(f"\n[SUPERVISOR] Max generations per day ({self.max_generations_per_day}) reached.")
                    print("[SUPERVISOR] Waiting for day to end...")
                    self._end_of_day()
                    self.day_manager.wait_for_new_day()
                    self.generations_today = 0
                    continue

                # Run one generation
                self._run_generation()
                self.generations_today += 1

                # Brief pause between generations
                time.sleep(2)

        except KeyboardInterrupt:
            print("\n[SUPERVISOR] Interrupted. Shutting down gracefully...")
            self._end_of_day()
        except Exception as e:
            print(f"\n[SUPERVISOR] Fatal error: {e}")
            import traceback
            traceback.print_exc()

    def _run_generation(self):
        """Run a single generation lifecycle."""
        gen = self.current_generation
        print(f"\n{'─' * 50}")
        print(f"  GENERATION {gen:04d} — BIRTH")
        print(f"{'─' * 50}")

        # 1. Load genome
        genome = self._load_genome()

        # 2. Create sandbox
        sandbox = Sandbox(
            str(self.base_dir),
            gen,
            str(self.mutable_dir),
        )
        workspace_info = sandbox.setup()

        # 3. Load inherited notes
        inherited_notes = self._load_inherited_notes(gen, genome)

        # 4. Save inherited notes to gen dir
        inherited_path = Path(workspace_info["gen_dir"]) / "inherited_notes.md"
        inherited_path.write_text(inherited_notes, encoding="utf-8")

        # 5. Load goal and prompt
        goal = self._load_goal()
        prompt_text = self._load_prompt()

        # 6. Create death monitor
        death_monitor = DeathMonitor(self.config)

        # 7. Import and run the agent brain
        # We dynamically import from the generation's mutable snapshot
        try:
            sys.path.insert(0, str(sandbox.mutable_dir))
            from mutable.agent_brain import AgentBrain
            agent = AgentBrain(self.llm, sandbox, death_monitor, gen)
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
            # Clean up sys.path
            if str(sandbox.mutable_dir) in sys.path:
                sys.path.remove(str(sandbox.mutable_dir))

        # 8. Save mutable snapshot back (agent's modifications persist)
        sandbox.cleanup_mutable_back()

        # 9. Run evaluator
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

        # 10. Distill inheritance
        print(f"  [GEN-{gen:04d}] Distilling inheritance...")
        distill_result = self.distiller.distill(
            autopsy=eval_result["autopsy"],
            current_genome=genome,
            genome_path=str(self.genome_path),
            lineage_path=str(self.lineage_path),
        )

        # 11. Write inherited notes for next generation
        new_genome = distill_result["genome"]
        next_inherited = self.distiller.build_inherited_notes(
            new_genome,
            eval_result["inheritance_note"],
        )
        next_notes_path = self.base_dir / "genome" / "next_inherited_notes.md"
        next_notes_path.write_text(next_inherited, encoding="utf-8")

        # 12. Log summary
        score = eval_result["autopsy"].get("score", 0)
        mutations = distill_result.get("mutations_applied", [])
        mutations_str = ", ".join(m.get("value", "")[:40] for m in mutations) if mutations else "none"
        print(f"  [GEN-{gen:04d}] Score: {score:.1f} | Death: {death_cause[:50]} | Mutations: {mutations_str}")

        # Increment generation
        self.current_generation = gen + 1

    def _end_of_day(self):
        """End-of-day sequence: Crescent writes its journal, then publish."""
        print("\n[SUPERVISOR] End-of-day: Crescent writes its daily journal...")
        self.day_manager.write_daily_journal(self.current_generation)

        print("[SUPERVISOR] Publishing to GitHub Pages...")
        self.publisher.publish(self.current_generation)

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
            "lineage_stats": {"total_generations": 0, "average_score": 0, "best_score": 0, "most_common_death": "none"},
        }

    def _load_inherited_notes(self, generation: int, genome: dict) -> str:
        """Load inherited notes for the current generation."""
        notes_path = self.base_dir / "genome" / "next_inherited_notes.md"
        if notes_path.exists():
            return notes_path.read_text(encoding="utf-8")

        # First generation — build from genome
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
        """Determine the next generation number by scanning existing runs."""
        runs = self.runs_dir
        if not runs.exists():
            runs.mkdir(parents=True, exist_ok=True)
            return 1
        existing = [d.name for d in runs.iterdir() if d.is_dir() and d.name.startswith("gen-")]
        if not existing:
            return 1
        nums = []
        for name in existing:
            try:
                nums.append(int(name.split("-")[1]))
            except (ValueError, IndexError):
                pass
        return max(nums) + 1 if nums else 1
