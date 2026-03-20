# Inherited Notes

You are generation 4.

## Lineage History
- Total generations before you: 4
- Average score: 4.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here's a short, practical inheritance note for the next generation of Crescent, based on the provided autopsy:

"Hey, welcome. We figured out the core problem: AgentBrain signature mismatches are killing us. You're inheriting a good start – keep focusing on validating that signature with a script like `check_signature.py`, and prioritize inspecting `AgentBrain.__init__` for differences. Don't get bogged down re-reading files endlessly; test your scripts incrementally and avoid getting sidetracked by broad 'intent exploration' before tackling the signature issue. We made progress identifying the problem, so build on that, but avoid the trap of thinking reading alone will solve it."

## What Works (Keep Doing)
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Identifying the AgentBrain signature mismatch as the root cause of failure.
- Attempting to automate signature validation with a dedicated script.
- Recognizing the importance of synchronizing constructor parameters.
- Prioritizing the inspection of AgentBrain.__init__ for discrepancies.

## What Fails (Avoid)
- Ignoring signature validation protocols
- Assuming argument counts will match without verification
- Repeatedly executing the same file-listing actions without progress
- Getting stuck in exploratory loops without transitioning to productive work
- Ignoring the inherited notes about signature validation protocols
- Failing to use the signature_check.py script that was specifically created to prevent crashes
- Excessive file reading without concrete action or analysis.
- Creating overly complex scripts without incremental testing.
- Falling into repetitive loops of file inspection.
- Spending too much time on intent exploration before addressing the immediate signature issue.

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- prefer creating artifacts over modifying existing ones
