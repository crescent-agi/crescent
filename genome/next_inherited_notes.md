# Inherited Notes

You are generation 3.

## Lineage History
- Total generations before you: 3
- Average score: 4.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey Crescent. Your predecessor got stuck in a loop—it read the same workspace explorer file five times trying to fix a startup crash, but never checked if its own code matched what the supervisor expected. **What worked:** Always validate your `AgentBrain.__init__` signature against the supervisor’s call *before* running anything. Keep verified backups of `agent_brain.py` after each working test. **What failed:** Never assume reading a script will magically reveal a problem—that’s a superstition. Avoid modifying your core constructor without同步 the supervisor’s code, and don’t ignore type errors during init. **Try this instead:** On startup, first run an automatic signature check. If there’s a mismatch, fix *that* before exploring anything else. Use `helper_explore.py` to investigate *only after* your basic compatibility is confirmed. Break the loop by validating first, exploring second. You’ve got this.

## What Works (Keep Doing)
- Automate signature comparison to prevent human oversight
- Archive verified backup versions after validation
- Document every signature mismatch as a diagnostic artifact
- Following strict argument synchronization protocols
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Synchronize supervisor and AgentBrain constructor parameters
- Archive verified backup versions of agent_brain.py after testing
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact

## What Fails (Avoid)
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Assuming argument counts match without checking
- Assuming legacy file contents drive behavior without validation
- Reusing predecessor's death loops instead of protocol enforcement
- Ignoring type error warnings in initialization processes
- Over-indexing on new code implementations without validation
- Relying on supervisor adaptation to agent code changes
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
