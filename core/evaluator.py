"""
Crescent AGI — Evaluator / Undertaker
========================================
The skeptical external judge. Inspects each generation after death
and decides whether anything useful happened.
Separate from the runtime agent — harder to corrupt.
"""

import json
import time
from pathlib import Path
from typing import Optional


class Evaluator:
    """
    Post-mortem analysis of a generation's run.
    Uses an LLM to inspect logs, journal, workspace state,
    and produces structured autopsy + inheritance notes.
    """

    AUTOPSY_PROMPT = """You are the Evaluator for Crescent, an experimental evolving AI agent.
A generation of the agent has just died. Your job is to perform a thorough autopsy.

## Generation Info
- Generation: {generation}
- Death Cause: {death_cause}
- Steps Taken: {steps}
- Time Alive: {time_alive:.1f} seconds

## The Agent's Journal
{journal}

## The Agent's Action Log (last 30 actions)
{action_log}

## Workspace State
{workspace_summary}

## Inherited Notes From Previous Generation
{inherited_notes}

## Current Genome
{genome}

## Your Task
Analyze this generation's life and death. Produce a JSON autopsy with EXACTLY this structure:
```json
{{
    "generation": {generation},
    "score": <float: 0-100 fitness score>,
    "death_cause": "<string>",
    "summary": "<1-2 sentence summary of what happened>",
    "keep": ["<lessons worth preserving for descendants>"],
    "avoid": ["<behaviors or patterns to avoid>"],
    "best_artifacts": ["<filenames of useful artifacts created>"],
    "mutations_to_keep": ["<mutations that seemed helpful>"],
    "mutations_to_avoid": ["<mutations that seemed harmful>"],
    "progress_made": <bool: did the agent make real progress?>,
    "interesting_behaviors": ["<notable or strange behaviors observed>"],
    "superstitions": ["<any irrational beliefs or cargo-cult behaviors>"]
}}
```

Be honest and skeptical. Do not inflate scores. Real progress means actual useful output, not just planning or self-reflection.
Respond ONLY with the JSON block, no other text."""

    INHERITANCE_NOTE_PROMPT = """You are writing the inheritance note for the next generation of Crescent, an evolving AI agent.
Based on this autopsy, write a short, practical note (3-8 sentences) that the next generation will read before starting its life.
Be specific about what worked, what failed, and what to try differently.
Write in plain language, as if leaving advice for your successor.

Autopsy:
{autopsy_json}

Write the inheritance note now:"""

    def __init__(self, llm_client):
        """
        Args:
            llm_client: An initialized LLM client with a generate() method.
        """
        self.llm = llm_client

    def evaluate(
        self,
        generation: int,
        gen_dir: str,
        death_cause: str,
        steps: int,
        time_alive: float,
        inherited_notes: str,
        genome: dict,
    ) -> dict:
        """
        Perform a full autopsy on a generation.
        Returns dict with 'autopsy' and 'inheritance_note' keys.
        """
        gen_path = Path(gen_dir)

        # Read journal
        journal_path = gen_path / "journal.md"
        journal = journal_path.read_text(encoding="utf-8") if journal_path.exists() else "(no journal)"

        # Read action log (last 30 actions)
        actions_path = gen_path / "actions.jsonl"
        action_log = "(no actions)"
        if actions_path.exists():
            lines = actions_path.read_text(encoding="utf-8").strip().split("\n")
            last_30 = lines[-30:] if len(lines) > 30 else lines
            action_log = "\n".join(last_30)

        # Get workspace summary
        workspace_summary = self._get_workspace_summary(gen_path)

        # Build autopsy prompt
        prompt = self.AUTOPSY_PROMPT.format(
            generation=generation,
            death_cause=death_cause,
            steps=steps,
            time_alive=time_alive,
            journal=journal[:4000],
            action_log=action_log[:3000],
            workspace_summary=workspace_summary[:2000],
            inherited_notes=inherited_notes[:2000] if inherited_notes else "(first generation)",
            genome=json.dumps(genome, indent=2)[:2000],
        )

        # Get autopsy from LLM
        autopsy_text = self.llm.generate(prompt)
        autopsy = self._parse_autopsy(autopsy_text, generation, death_cause)

        # Generate inheritance note
        note_prompt = self.INHERITANCE_NOTE_PROMPT.format(
            autopsy_json=json.dumps(autopsy, indent=2)
        )
        inheritance_note = self.llm.generate(note_prompt)

        # Save autopsy to gen dir
        autopsy_path = gen_path / "autopsy.json"
        autopsy_path.write_text(json.dumps(autopsy, indent=2), encoding="utf-8")

        # Save inheritance note
        note_path = gen_path / "inheritance_note.md"
        note_path.write_text(inheritance_note, encoding="utf-8")

        return {
            "autopsy": autopsy,
            "inheritance_note": inheritance_note,
        }

    def _parse_autopsy(self, text: str, generation: int, death_cause: str) -> dict:
        """Parse the LLM's autopsy response into structured JSON."""
        try:
            # Try to extract JSON from the response
            start = text.find("{")
            end = text.rfind("}") + 1
            if start >= 0 and end > start:
                return json.loads(text[start:end])
        except json.JSONDecodeError:
            pass

        # Fallback: create a minimal autopsy
        return {
            "generation": generation,
            "score": 0.0,
            "death_cause": death_cause,
            "summary": "Evaluator failed to produce structured autopsy.",
            "keep": [],
            "avoid": [],
            "best_artifacts": [],
            "mutations_to_keep": [],
            "mutations_to_avoid": [],
            "progress_made": False,
            "interesting_behaviors": [],
            "superstitions": [],
            "raw_evaluation": text[:2000],
        }

    def _get_workspace_summary(self, gen_path: Path) -> str:
        """Summarize the workspace contents."""
        lines = []
        for subdir in ["mutable_snapshot", "artifacts"]:
            d = gen_path / subdir
            if d.exists():
                lines.append(f"\n### {subdir}/")
                for f in sorted(d.rglob("*")):
                    if f.is_file():
                        rel = f.relative_to(gen_path)
                        size = f.stat().st_size
                        lines.append(f"  {rel} ({size} bytes)")
        return "\n".join(lines) if lines else "(empty workspace)"
