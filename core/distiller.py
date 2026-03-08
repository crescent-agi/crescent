"""
Crescent AGI — Distiller
==========================
Extracts and distills inheritance from the evaluator's autopsy.
Updates the genome, applies mutations, and prepares notes for the next generation.
Without mutation, this becomes memory accumulation instead of evolution.
"""

import json
import random
import time
from pathlib import Path
from typing import Optional


class Distiller:
    """
    Takes evaluator output and current genome, produces
    updated genome and inheritance for the next generation.
    Handles mutations — the engine of variety.
    """

    MUTATION_TEMPLATES = {
        "prompt_wording": [
            "be bold and take risks",
            "be methodical and careful",
            "be concrete — avoid abstract planning",
            "be creative — try unconventional approaches",
            "focus on building tools before tackling the main goal",
            "minimize reflection — act more, think less",
            "reflect deeply before every action",
            "prioritize small wins over grand plans",
            "question everything — including your inherited advice",
        ],
        "planning_depth": [
            "make a detailed plan before acting (10+ steps)",
            "make a short plan (3-5 steps) then start",
            "skip planning — act first, plan later",
            "alternate between planning and action",
        ],
        "reflection_length": [
            "write a brief 1-sentence reflection after each action",
            "write a detailed multi-paragraph reflection every 5 actions",
            "skip reflection entirely — just act",
            "reflect only when something goes wrong",
        ],
        "self_edit_timing": [
            "do not self-edit for the first 5 steps",
            "do not self-edit for the first 10 steps",
            "self-edit only after completing at least one task",
            "self-edit freely from the start",
            "self-edit only at the end of your life",
        ],
        "tool_visibility": [
            "prefer reading files over writing them initially",
            "prefer writing code over writing notes",
            "prefer exploring the workspace before acting",
            "prefer creating artifacts over modifying existing ones",
        ],
        "starter_tasks": [
            "begin by reviewing inherited notes carefully",
            "begin by exploring your workspace structure",
            "begin by writing a plan in your journal",
            "begin by creating a small helper script",
            "begin by setting a concrete sub-goal",
        ],
    }

    def __init__(self, config: dict):
        self.mutation_rate = config.get("mutation", {}).get("rate", 0.3)
        self.mutation_types = config.get("mutation", {}).get("types", list(self.MUTATION_TEMPLATES.keys()))

    def distill(
        self,
        autopsy: dict,
        current_genome: dict,
        genome_path: str,
        lineage_path: str,
    ) -> dict:
        """
        Distill inheritance from an autopsy and update the genome.

        Returns:
            dict with 'genome', 'inherited_notes', 'mutations_applied'
        """
        generation = autopsy.get("generation", 0)

        # Build accumulated lessons
        keep = current_genome.get("accumulated_lessons", {}).get("keep", [])
        avoid = current_genome.get("accumulated_lessons", {}).get("avoid", [])

        # Add new lessons (cap at 20 each to prevent bloat)
        keep.extend(autopsy.get("keep", []))
        avoid.extend(autopsy.get("avoid", []))
        keep = keep[-20:]
        avoid = avoid[-20:]

        # Track best artifacts across generations
        best_artifacts = current_genome.get("best_artifacts", [])
        best_artifacts.extend(autopsy.get("best_artifacts", []))
        best_artifacts = best_artifacts[-10:]

        # Apply mutations
        mutations_applied = []
        active_mutations = current_genome.get("active_mutations", [])

        if random.random() < self.mutation_rate:
            mutation_type = random.choice(self.mutation_types)
            if mutation_type in self.MUTATION_TEMPLATES:
                mutation = random.choice(self.MUTATION_TEMPLATES[mutation_type])
                mutations_applied.append({
                    "type": mutation_type,
                    "value": mutation,
                    "generation_applied": generation + 1,
                })
                active_mutations.append(mutation)

        # Keep active mutations list manageable
        active_mutations = active_mutations[-5:]

        # Track score history
        score_history = current_genome.get("score_history", [])
        score_history.append({
            "generation": generation,
            "score": autopsy.get("score", 0),
            "death_cause": autopsy.get("death_cause", "unknown"),
        })

        # Build new genome
        new_genome = {
            "current_generation": generation + 1,
            "accumulated_lessons": {
                "keep": keep,
                "avoid": avoid,
            },
            "best_artifacts": best_artifacts,
            "active_mutations": active_mutations,
            "mutations_applied_history": current_genome.get("mutations_applied_history", []) + mutations_applied,
            "score_history": score_history,
            "lineage_stats": {
                "total_generations": generation + 1,
                "average_score": sum(s["score"] for s in score_history) / len(score_history) if score_history else 0,
                "best_score": max((s["score"] for s in score_history), default=0),
                "most_common_death": self._most_common_death(score_history),
            },
        }

        # Save genome
        genome_file = Path(genome_path)
        genome_file.parent.mkdir(parents=True, exist_ok=True)
        genome_file.write_text(json.dumps(new_genome, indent=2), encoding="utf-8")

        # Append to lineage log
        lineage_file = Path(lineage_path)
        lineage_file.parent.mkdir(parents=True, exist_ok=True)
        lineage_entry = {
            "generation": generation,
            "score": autopsy.get("score", 0),
            "death_cause": autopsy.get("death_cause", "unknown"),
            "summary": autopsy.get("summary", ""),
            "mutations": mutations_applied,
            "progress_made": autopsy.get("progress_made", False),
            "timestamp": time.time(),
        }
        with open(lineage_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(lineage_entry) + "\n")

        return {
            "genome": new_genome,
            "mutations_applied": mutations_applied,
        }

    def _most_common_death(self, score_history: list) -> str:
        """Find the most common cause of death."""
        if not score_history:
            return "none"
        from collections import Counter
        causes = [s.get("death_cause", "unknown") for s in score_history]
        return Counter(causes).most_common(1)[0][0]

    def build_inherited_notes(self, genome: dict, last_inheritance_note: str) -> str:
        """
        Build the inherited notes document that the next generation will read.
        Combines genome lessons with the evaluator's inheritance note.
        """
        lines = ["# Inherited Notes\n"]
        lines.append(f"You are generation {genome.get('current_generation', 1)}.\n")

        # Lineage stats
        stats = genome.get("lineage_stats", {})
        if stats.get("total_generations", 0) > 1:
            lines.append(f"## Lineage History")
            lines.append(f"- Total generations before you: {stats.get('total_generations', 0)}")
            lines.append(f"- Average score: {stats.get('average_score', 0):.1f}")
            lines.append(f"- Best score ever: {stats.get('best_score', 0):.1f}")
            lines.append(f"- Most common death: {stats.get('most_common_death', 'unknown')}")
            lines.append("")

        # Inheritance note from last generation
        if last_inheritance_note:
            lines.append("## Message From Your Predecessor")
            lines.append(last_inheritance_note)
            lines.append("")

        # Accumulated lessons
        lessons = genome.get("accumulated_lessons", {})
        if lessons.get("keep"):
            lines.append("## What Works (Keep Doing)")
            for lesson in lessons["keep"][-10:]:
                lines.append(f"- {lesson}")
            lines.append("")

        if lessons.get("avoid"):
            lines.append("## What Fails (Avoid)")
            for lesson in lessons["avoid"][-10:]:
                lines.append(f"- {lesson}")
            lines.append("")

        # Active mutations
        if genome.get("active_mutations"):
            lines.append("## Active Mutations (Behavioral Tweaks)")
            for mutation in genome["active_mutations"]:
                lines.append(f"- {mutation}")
            lines.append("")

        return "\n".join(lines)
