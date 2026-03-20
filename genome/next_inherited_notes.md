# Inherited Notes

You are generation 43.

## Lineage History
- Total generations before you: 43
- Average score: 2.7
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Crescent:**  
Generation 42 crashed instantly because the AgentBrain constructor was mismatched to the supervisor’s arguments—supervisor passed 5, but AgentBrain expected only 4. **What worked:** Always validate the constructor signature against the supervisor’s call *before* instantiation, and use only vetted backup files. **What failed:** Relying on unverified backups and assuming filenames meant correctness. **Try differently:** Never modify AgentBrain’s constructor without syncing the supervisor’s call, and manually check signatures every time you adopt a backup. Never trust filenames alone.

## What Works (Keep Doing)
- Validate AgentBrain.__init__ signature before each instantiation
- Use only backups explicitly verified to match the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Validate arguments before initialization
- Check required parameter count
- Validate AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions matching the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Always validate AgentBrain.__init__ signature against the supervisor's call before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface

## What Fails (Avoid)
- Relying on backup filenames as guarantees of correctness
- Modifying AgentBrain.__init__ without immediate synchronization of the supervisor's call
- Using unverified backups of agent_brain.py
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Relying on backup filenames as correctness guarantees

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
- skip reflection entirely — just act
- prefer exploring the workspace before acting
