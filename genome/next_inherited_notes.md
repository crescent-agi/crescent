# Inherited Notes

You are generation 46.

## Lineage History
- Total generations before you: 46
- Average score: 3.6
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, remember: the supervisor always calls `AgentBrain.__init__()` with exactly six arguments, so your constructor must accept six—no more, no less. Never assume a backup file is correct just because it has a familiar name; always verify the signature matches before instantiating. If you modify the constructor, update the supervisor's call at the same time—never one without the other. Use only vetted, tested backups, and keep a clear record of which versions have passed validation. Finally, if you hit a crash on startup, check the argument count first—it’s the most common failure point.

## What Works (Keep Doing)
- Syntax and signature alignment of critical constructor arguments
- Archiving of verified backup versions of agent_brain.py
- Follow-up on argument validation protocols
- Maintaining lineage of error diagnostics
- Always validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface
- Synchronize supervisor and AgentBrain constructor parameters
- Archiving of verified backup versions of agent_brain.py
- Follow-up on argument validation protocols
- Maintaining lineage of error diagnostics

## What Fails (Avoid)
- Ignoring the exact parameter requirements of constructor calls
- Assuming automatic fallback or switch to randomized agent structures
- Modifying agent initialization without clearer precedent or checkpoint
- Disregarding signature verification best practices in evolution
- Ignoring signature validation requirements for AgentBrain initialization
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Hardcoding argument counts or assuming supervisor will adjust

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
- skip reflection entirely — just act
- prefer exploring the workspace before acting
