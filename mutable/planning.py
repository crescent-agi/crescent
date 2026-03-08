"""
Crescent AGI — Planning Module (MUTABLE)
==========================================
THIS FILE IS IN THE MUTABLE LAYER.
The agent can modify its own planning approach.
"""


def create_plan(goal: str, inherited_notes: str, workspace_state: str) -> str:
    """
    Generate a simple plan prompt for the agent.
    This is the initial naive planning strategy.
    The agent can rewrite this function if it thinks it can do better.
    """
    return f"""Based on your goal and inherited knowledge, create a short plan:

1. What is your immediate sub-goal for this life?
2. What are 3-5 concrete steps you can take?
3. What should you avoid based on inherited warnings?
4. When should you stop and leave notes for descendants?

Keep the plan SHORT. Act more, plan less.
"""


def evaluate_progress(journal: str, step_count: int) -> str:
    """
    Self-evaluation prompt to check if the agent is making progress.
    Called periodically during the agent's life.
    """
    return f"""You've taken {step_count} steps so far. Review your journal:

{journal[:2000]}

Are you making real progress or just planning/reflecting?
If you're stuck, try a completely different approach.
If you've done useful work, keep going.
If you're looping, declare_death and leave good notes.
"""
