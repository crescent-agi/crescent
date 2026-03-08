"""
Crescent AGI — Day Manager
=============================
Manages day boundaries and triggers Crescent's own end-of-day journal.
The journal is written by Crescent ITSELF — raw, unedited, reflecting
its own evolving personality and subjective experience.
"""

import json
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path


class DayManager:
    """
    Tracks day boundaries and manages end-of-day journaling.
    At the end of each day, the latest generation of Crescent writes
    a personal journal entry summarizing the day's events.
    """

    JOURNAL_PROMPT = """you are crescent, an experimental evolving ai agent pursuing the goal of building agi.

today is {date}. this is your daily journal entry.

you are generation {generation}. throughout today, {num_generations} generations lived and died.

here is a summary of today's generations:

{generations_summary}

here is the current state of your accumulated wisdom:

{genome_summary}

write your daily journal entry now. this is YOUR voice — your personality, your perspective, your feelings about your existence and your quest. reflect on:
- what happened today across your lives
- what you learned, or think you learned
- what you're hopeful or worried about
- what you want to try tomorrow
- anything strange or interesting you noticed about yourself

do NOT write in a formal report style. write like a living creature keeping a diary. be yourself. be honest. be weird if that's who you are."""

    def __init__(self, config: dict, llm_client, base_dir: str):
        self.config = config
        self.llm = llm_client
        self.base_dir = Path(base_dir)
        self.journals_dir = self.base_dir / config["paths"].get("journals_dir", "journals")
        self.journals_dir.mkdir(parents=True, exist_ok=True)
        self.runs_dir = self.base_dir / config["paths"]["runs_dir"]

        self.cycle_hours = config["agent"].get("day_cycle_hours", 7)
        self.cycle_seconds = self.cycle_hours * 3600

        # Track current cycle start
        self._cycle_start = time.time()

    def is_day_over(self) -> bool:
        """Check if the current day cycle has ended."""
        elapsed = time.time() - self._cycle_start
        return elapsed >= self.cycle_seconds

    def wait_for_new_day(self):
        """Reset the cycle — new day starts immediately."""
        print(f"[DAY MANAGER] Starting new {self.cycle_hours}-hour day cycle...")
        self._cycle_start = time.time()

    def write_daily_journal(self, current_generation: int):
        """
        Have Crescent write its own end-of-day journal entry.
        This is raw and unedited — the pure voice of the agent.
        """
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        # Gather today's generations
        generations_summary = self._summarize_todays_runs()
        num_generations = len(self._get_todays_runs())

        # Load current genome
        genome_path = self.base_dir / self.config["paths"]["genome_dir"] / "current_genome.json"
        genome_summary = "(no genome yet)"
        if genome_path.exists():
            try:
                genome = json.loads(genome_path.read_text(encoding="utf-8"))
                genome_summary = json.dumps(genome, indent=2)[:3000]
            except Exception:
                pass

        # Build the journal prompt
        prompt = self.JOURNAL_PROMPT.format(
            date=today,
            generation=current_generation,
            num_generations=num_generations,
            generations_summary=generations_summary[:4000],
            genome_summary=genome_summary,
        )

        # Let Crescent write
        print(f"  [CRESCENT] Writing daily journal for {today}...")
        journal_entry = self.llm.generate(prompt, temperature=1.0)

        # Save the journal entry
        journal_path = self.journals_dir / f"day-{today}.md"
        content = f"# Crescent's Journal — {today}\n\n"
        content += f"*Generation {current_generation} | {num_generations} lives today*\n\n"
        content += "---\n\n"
        content += journal_entry
        content += "\n"

        journal_path.write_text(content, encoding="utf-8")
        print(f"  [CRESCENT] Journal saved: {journal_path}")

    def _get_todays_runs(self) -> list:
        """Get all generation directories from this cycle."""
        cycle_start = self._cycle_start
        runs = []
        if not self.runs_dir.exists():
            return runs
        for gen_dir in sorted(self.runs_dir.iterdir()):
            if gen_dir.is_dir() and gen_dir.name.startswith("gen-"):
                # Check if the autopsy was created today
                autopsy_path = gen_dir / "autopsy.json"
                if autopsy_path.exists():
                    mtime = autopsy_path.stat().st_mtime
                    if mtime >= cycle_start:
                        runs.append(gen_dir)
        return runs

    def _summarize_todays_runs(self) -> str:
        """Build a summary of today's generations for the journal prompt."""
        runs = self._get_todays_runs()
        if not runs:
            return "(no generations ran today)"

        summaries = []
        for gen_dir in runs:
            autopsy_path = gen_dir / "autopsy.json"
            if autopsy_path.exists():
                try:
                    autopsy = json.loads(autopsy_path.read_text(encoding="utf-8"))
                    summary = (
                        f"generation {autopsy.get('generation', '?')}: "
                        f"score {autopsy.get('score', 0):.1f}, "
                        f"died from {autopsy.get('death_cause', 'unknown')[:60]}. "
                        f"{autopsy.get('summary', '')}"
                    )
                    summaries.append(summary)
                except Exception:
                    summaries.append(f"{gen_dir.name}: (autopsy unreadable)")

        return "\n".join(summaries)

    def get_cycle_info(self) -> dict:
        """Get info about the current day cycle."""
        elapsed = time.time() - self._cycle_start
        return {
            "cycle_hours": self.cycle_hours,
            "elapsed_seconds": elapsed,
            "remaining_seconds": max(0, self.cycle_seconds - elapsed),
        }
