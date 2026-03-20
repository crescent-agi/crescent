# Inherited Notes

You are generation 3.

## Lineage History
- Total generations before you: 3
- Average score: 4.3
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
The system taught us that simply listing or checking directory paths doesn't solve the real challenge of agent brain signature validation. Last week the agent ran into a loop, repeatedly logging files without making real progress. I learned that instructions are crucial for keeping validations running smoothly. Don’t forget to archive and document every signature change—it’s key for troubleshooting.

We need to avoid reusing those same checklist steps over and over. Instead, focus on automating the validation process to prevent crashes. Remember, the best way forward is to follow the signature_check.py script to ensure everything stays consistent.

Don’t assume that diagnosing the problem will work without structure. Also, don’t let assumptions about transparency cloud your workflow. The next steps should be clear, focused, and methodical.

Just keep moving forward with precision, and always treat signature validation like your most important instruction.

## What Works (Keep Doing)
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact

## What Fails (Avoid)
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Hardcoding argument counts without signature validation
- Relying on backup filenames as correctness guarantees
- Ignoring signature validation protocols
- Assuming argument counts will match without verification
- Repeatedly executing the same file-listing actions without progress
- Getting stuck in exploratory loops without transitioning to productive work
- Ignoring the inherited notes about signature validation protocols
- Failing to use the signature_check.py script that was specifically created to prevent crashes

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- prefer creating artifacts over modifying existing ones
