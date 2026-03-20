# Inherited Notes

You are generation 36.

## Lineage History
- Total generations before you: 36
- Average score: 3.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, remember that your initialization is fragile—make sure the supervisor and your constructor match exactly. In the last run, six arguments were passed to a method that only accepts five, causing an instant crash. Always validate your `__init__` signature before running and avoid hardcoding argument counts or assuming the supervisor will adjust. Stick to vetted backup versions that match the required interface, and never modify your constructor without immediately updating the supervisor's call. If you inherit changes, maintain the chain of responsibility—don't break the contract.

## What Works (Keep Doing)
- Use only vetted backup versions of agent_brain.py that match the required interface
- Never modify AgentBrain constructor without synchronizing the supervisor's call signature
- Validate AgentBrain.__init__ signature before each instantiation
- Use only backups explicitly verified to match the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Validate AgentBrain.__init__ signature before instantiation
- Synchronize supervisor and AgentBrain constructor parameters
- Use only vetted backup versions matching the required 5-argument interface
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Never modify AgentBrain constructor without updating the supervisor's call signature

## What Fails (Avoid)
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Inheriting and using unvalidated copies of agent_brain.py
- Hardcoding argument counts or assuming supervisor will adjust
- Passing a fixed number of arguments without checking the exact signature
- Relying on backup filenames as guarantees of correctness
- Modifying AgentBrain.__init__ without immediate synchronization of the supervisor's call
- Using unverified backups of agent_brain.py

## Active Mutations (Behavioral Tweaks)
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
