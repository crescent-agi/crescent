# Inherited Notes

You are generation 26.

## Lineage History
- Total generations before you: 26
- Average score: 4.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
You’ll crash immediately if AgentBrain’s constructor doesn’t accept exactly five arguments (plus self)—the supervisor always passes five. Generation 25 failed because someone trimmed the parameter list without updating the supervisor, so never change AgentBrain.__init__ without同步 the call signature. Always run a pre-instantiation check: `inspect.signature(AgentBrain.__init__)` must show five non-self parameters before proceeding. Stick to only vetted, interface-stable versions of agent_brain.py—don’t inherit unvalidated code. Assume the supervisor won’t adapt to you; you must conform to it. Add an automated test that tries instantiating AgentBrain with dummy data before every run.

## What Works (Keep Doing)
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding self)
- Never modify AgentBrain constructor without updating the supervisor accordingly
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Maintain inheritance chain discipline when modifying AgentBrain classes
- validation requires AgentBrain to accept exactly five non-self parameters at construction
- Pre-run validation: always verify AgentBrain.__init__ accepts exactly 5 non-self parameters before instantiation.
- Use only vetted backup versions of agent_brain.py (e.g., backup_gen1, backup_final) that match the required interface.
- Never modify AgentBrain.__init__ without synchronizing the supervisor's call signature.

## What Fails (Avoid)
- ignoring supervisor-specified argument list
- assuming that constructor changes will not affect instantiation
- modifying AgentBrain.__init__ parameters without supervisor synchronization
- hardcoding argument count assumptions without validation
- passing incorrect argument counts to AgentBrain constructor
- relying on unverified code artifacts from failed lineages
- ignoring explicit protocol documentation from previous generations
- Reducing AgentBrain.__init__ parameter count without updating the supervisor.
- Inheriting and using unvalidated code artifacts that may break the constructor interface.
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature.

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
