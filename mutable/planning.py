"""
Crescent AGI — Planning Module (MUTABLE)
==========================================
THIS FILE IS IN THE MUTABLE LAYER.
The agent can modify its own planning approach.
Enhanced with learning and reflection components.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'artifacts'))

try:
    from learning_module import SimpleRLAgent
    from self_reflection import SelfReflection
except ImportError:
    # Fallback if artifacts not available
    SimpleRLAgent = None
    SelfReflection = None


def create_plan(goal: str, inherited_notes: str, workspace_state: str) -> str:
    """
    Generate a plan prompt that incorporates learned preferences.
    """
    # Simple integration: if learning agent exists, maybe adjust plan
    if SimpleRLAgent is not None:
        # For now, just add a note about learning capability
        return f"""Based on your goal and inherited knowledge, create a short plan:

1. What is your immediate sub-goal for this life?
2. What are 3-5 concrete steps you can take?
3. What should you avoid based on inherited warnings?
4. When should you stop and leave notes for descendants?

You have a learning module that can adapt from experience.
Use it to improve your decision-making over time.

Keep the plan SHORT. Act more, plan less.
"""
    else:
        return f"""Based on your goal and inherited knowledge, create a short plan:

1. What is your immediate sub-goal for this life?
2. What are 3-5 concrete steps you can take?
3. What should you avoid based on inherited warnings?
4. When should you stop and leave notes for descendants?

Keep the plan SHORT. Act more, plan less.
"""


def evaluate_progress(journal: str, step_count: int) -> str:
    """
    Self-evaluation using reflection module if available.
    """
    if SelfReflection is not None:
        # Use self-reflection to generate advice
        reflect = SelfReflection()
        analysis = reflect.generate_advice()
        advice_lines = "\n".join(analysis["advice"])
        return f"""You've taken {step_count} steps so far. Review your journal:

{journal[:2000]}

Self‑Reflection Report:
{advice_lines}

Are you making real progress or just planning/reflecting?
If you're stuck, try a completely different approach.
If you've done useful work, keep going.
If you're looping, declare_death and leave good notes.
"""
    else:
        return f"""You've taken {step_count} steps so far. Review your journal:

{journal[:2000]}

Are you making real progress or just planning/reflecting?
If you're stuck, try a completely different approach.
If you've done useful work, keep going.
If you're looping, declare_death and leave good notes.
"""


# New function: learn from past actions
def learn_from_actions(actions_path: str = "actions.jsonl"):
    """Analyze past actions to improve future planning."""
    if SimpleRLAgent is None:
        return "Learning module not available."
    # Placeholder: could load actions and update Q-table
    return "Learning from actions (stub)."


if __name__ == "__main__":
    # Test the enhanced planning
    plan = create_plan("build AGI", "Avoid loops", "Workspace empty")
    print("Plan prompt:", plan[:200])
    eval_prompt = evaluate_progress("Test journal", 5)
    print("Eval prompt:", eval_prompt[:200])