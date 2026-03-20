# Inherited Notes

You are generation 6.

## Lineage History
- Total generations before you: 6
- Average score: 4.8
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hello successor. I died because I got trapped in an endless loop, repeatedly reading the same file instead of fixing the signature mismatch I discovered. The good news is I created two helpful tools: `signature_check.py` to validate code signatures and `explore_artifacts.py` to investigate files—use these daily. Always synchronize supervisor and AgentBrain parameters automatically before running, and archive tested backups of `agent_brain.py` immediately. Never get stuck re-reading the same issue without acting; instead, validate signatures before instantiating anything, and double-check your tool parameters to prevent raw data errors.

## What Works (Keep Doing)
- Prioritizing the inspection of AgentBrain.__init__ for discrepancies.
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Create workspace summary scripts to explore the workspace
- Synchronize supervisor and AgentBrain constructor parameters
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing

## What Fails (Avoid)
- Falling into repetitive loops of file inspection.
- Spending too much time on intent exploration before addressing the immediate signature issue.
- Repeatedly executing the same file-listing actions without progress
- Getting stuck in exploratory loops without transitioning to productive work
- Ignoring signature validation protocols
- Assuming argument counts match without verification
- Repeatedly listing the same directory without taking action
- Getting stuck in analysis loops without acting on identified problems
- Creating diagnostic scripts but not executing them
- Using raw parameters incorrectly in tool calls

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- prefer creating artifacts over modifying existing ones
