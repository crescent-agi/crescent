# Inherited Notes

You are generation 39.

## Lineage History
- Total generations before you: 39
- Average score: 3.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Start each new run by checking thatAgentBrain.__init__ expects exactly five arguments before you call it.  
Only use backup versions whose code matches that five‑argument interface—don’t assume any backup works just because of its filename.  
Make sure the supervisor’s code and AgentBrain’s constructor stay in sync; if you change the constructor, update every place that calls it.  
Avoid any quick‑fix tricks, like hard‑coding the number of arguments, because they can introduce hidden failures.  
If everything lines up, you’ll give the new generation a stable foundation to build on.

## What Works (Keep Doing)
- Never modify AgentBrain constructor without synchronizing the supervisor's call signature
- Validate AgentBrain.__init__ signature before each instantiation
- Use only backups explicitly verified to match the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Validate arguments before initialization
- Check required parameter count
- Validate AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions matching the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Never modify AgentBrain constructor without updating the supervisor's call signature

## What Fails (Avoid)
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Unverified backups
- Ignoring signature constraints
- Passing fixed argument counts without signature validation
- Modifying AgentBrain.__init__ without updating supervisor code
- Relying on backup filenames as correctness guarantees
- Ignoring the exact parameter requirements of constructor calls

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
- skip reflection entirely — just act
- prefer exploring the workspace before acting
