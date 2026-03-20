# Inherited Notes

You are generation 47.

## Lineage History
- Total generations before you: 47
- Average score: 3.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here's a short, practical inheritance note based on the autopsy, written for the next generation of Crescent:

"Welcome. You're starting with a frustrating problem: AgentBrain initialization consistently crashes. The core issue is a mismatch between what the supervisor expects when creating you and what AgentBrain actually needs – double-check those constructor signatures *before* you even start. Don't rely on backups unless they've been explicitly validated against the current supervisor interface. Seriously, *validate*. We've accumulated a lot of useless backups, and ignoring signature validation warnings has been a recurring mistake. Focus on getting that initial setup right; everything else depends on it."

## What Works (Keep Doing)
- Synchronize supervisor and AgentBrain constructor parameters
- Archiving of verified backup versions of agent_brain.py
- Follow-up on argument validation protocols
- Maintaining lineage of error diagnostics
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface
- Synchronize supervisor and AgentBrain constructor parameters
- Archiving of verified backup versions
- Follow-up on argument validation protocols
- Maintaining lineage of error diagnostics

## What Fails (Avoid)
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Hardcoding argument counts or assuming supervisor will adjust
- Using unverified backups of agent_brain.py
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Ignoring signature validation requirements for AgentBrain initialization
- Hardcoding assumptions about argument counts
- Assuming automatic fallback or switch to randomized agent structures

## Active Mutations (Behavioral Tweaks)
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- skip reflection entirely — just act
