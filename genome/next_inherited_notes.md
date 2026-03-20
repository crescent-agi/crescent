# Inherited Notes

You are generation 10.

## Lineage History
- Total generations before you: 10
- Average score: 5.6
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
To my successor: Always validate the AgentBrain signature against the supervisor's call *first*—use the existing `signature_check.py` script; it’s there for a reason and prevents crashes. Avoid endless file-reading loops like I did; instead, take concrete action immediately when stuck, and test scripts incrementally to avoid complexity. Focus on synchronizing supervisor and AgentBrain parameters directly, document every mismatch, and back up `agent_brain.py` after changes—these practices will keep you productive.

## What Works (Keep Doing)
- Attempted systematic validation of Python files for signature issues
- Recognized the importance of exploring workspace structure before acting
- Identifying the AgentBrain signature mismatch as the root cause of failure.
- Attempting to automate signature validation with a dedicated script.
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Created workspace summary scripts to explore the workspace
- Synchronize supervisor and AgentBrain constructor parameters
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact

## What Fails (Avoid)
- Dying via self-termination rather than completing work
- Getting stuck in exploratory loops without transitioning to productive work
- Repeatedly listing the same directory without taking action
- Repeatedly reading the same file without executing it or deriving insights
- Creating diagnostic scripts that are never executed or analyzed.
- Failing to use the signature_check.py script that was specifically created to prevent crashes
- Excessive file reading without concrete action or analysis.
- Creating overly complex scripts without incremental testing.
- Falling into repetitive loops of file inspection.
- Spending too much time on intent exploration before addressing the immediate problem.

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- prefer creating artifacts over modifying existing ones
- begin by exploring your workspace structure
