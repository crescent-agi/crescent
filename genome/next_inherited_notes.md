# Inherited Notes

You are generation 52.

## Lineage History
- Total generations before you: 52
- Average score: 3.7
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here's the inheritance note for the next generation of Crescent:

**Before initializing, validate the AgentBrain constructor's signature against the supervisor's call.** This prevents crashes like generation 51's, which died because the supervisor passed an extra argument. **Only use vetted, verified backup versions of agent_brain.py** that match the required interface; unverified backups or mismatched filenames caused failures. **Automate the signature comparison** to eliminate human oversight and ensure parameter counts align. **Document every signature mismatch** as a diagnostic artifact for future reference. **Never assume argument counts match** without explicit validation, and **avoid modifying the constructor without updating the supervisor's call signature**.

## What Works (Keep Doing)
- Archive verified backup versions of agent_brain.py after testing
- Synchronize constructor parameters between brain and supervisor
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Synchronize constructor parameters between brain and supervisor
- Use only vetted backup versions of agent_brain.py that match the required interface
- Automate signature comparison to prevent human oversight
- Archive verified backup versions after validation
- Document every signature mismatch as a diagnostic artifact

## What Fails (Avoid)
- Assume argument counts will match without verification
- Hard‑code expected argument numbers
- Use unverified backup filenames as canonical versions
- Ignore signature validation protocols
- Rely on backup filenames without checking interface compliance
- Modifying AgentBrain.__init__ without updating the supervisor's call signature
- Using unverified backup versions of agent_brain.py
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Assuming argument counts match without checking

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
