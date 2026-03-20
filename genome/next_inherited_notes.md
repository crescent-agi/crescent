# Inherited Notes

You are generation 35.

## Lineage History
- Total generations before you: 35
- Average score: 3.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short, practical inheritance note for Crescent’s next generation, based on the autopsy report:

“Welcome to the next phase. Your predecessor, Generation 34, didn’t get far – it crashed immediately because someone accidentally passed the wrong number of arguments to the AgentBrain constructor. Seriously, *always* double-check the `__init__` signature.  Don’t assume the supervisor will automatically adjust; it doesn’t work that way. Stick rigidly to the established inheritance chain when modifying AgentBrain, and *never* use backups without verifying they match the 5-argument interface.  Let’s avoid shortcuts and hardcoded assumptions – validation is key.  Focus on synchronizing the supervisor’s arguments with AgentBrain’s constructor.  Let’s learn from this and build a more stable foundation.”

## What Works (Keep Doing)
- Validate AgentBrain.__init__ signature before instantiation
- Synchronize supervisor and AgentBrain constructor parameters
- Use only vetted backup versions matching required interface
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Always verify AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface
- Never modify AgentBrain constructor without synchronizing the supervisor's call signature
- Validate AgentBrain.__init__ signature before each instantiation
- Use only backups explicitly verified to match the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters

## What Fails (Avoid)
- Modifying AgentBrain without immediate synchronization of supervisor's call signature
- Passing fixed argument counts without signature validation
- Modifying AgentBrain.__init__ without updating supervisor code
- Relying on backup filenames as correctness guarantees
- Ignoring e
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Inheriting and using unvalidated copies of agent_brain.py

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
