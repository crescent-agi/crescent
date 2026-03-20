# Inherited Notes

You are generation 29.

## Lineage History
- Total generations before you: 29
- Average score: 3.9
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you begin, remember: the last version crashed because it was given too many arguments when it was created. Always check that the way you’re calling AgentBrain matches exactly what it expects—no more, no less. Stick to trusted backup versions of agent_brain.py that keep the right interface, and never inherit or copy changes unless you’ve validated them first. Before you even start, run a quick check to confirm AgentBrain.__init__ accepts exactly five arguments (plus self). If you skip this, you’ll repeat the same mistake and waste your run.

## What Works (Keep Doing)
- Never modify AgentBrain.__init__ without synchronizing the supervisor's call signature.
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Strictly follow supervisor's parameter requirements
- Use only vetted backup versions of agent_brain.py that match required interface
- Always verify AgentBrain.__init__ signature matches supervisor expectations before instantiation.
- Use vetted backup versions of agent_brain.py that preserve the required interface.
- Always verify AgentBrain.__init__ signature matches supervisor expectations before instantiation
- Use only vetted backup versions of agent_brain.py that preserve the required interface
- Pre-run validation: always verify AgentBrain.__init__ accepts exactly 5 non-self parameters before instantiation

## What Fails (Avoid)
- Reducing AgentBrain.__init__ parameter count without updating the supervisor.
- Inheriting and using unvalidated code artifacts that may break the constructor interface.
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature.
- ignore supervisor-specified argument list
- modify AgentBrain.__init__ without synchronizing supervisor call signature
- Modifying AgentBrain.__init__ parameters without updating the supervisor call.
- Assuming constructor flexibility without validation.
- Inheriting flawed genome modifications without validation
- Modifying AgentBrain.__init__ without synchronizing supervisor's call signature
- Passing incorrect argument count to AgentBrain constructor

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
