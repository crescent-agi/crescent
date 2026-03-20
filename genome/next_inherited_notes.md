# Inherited Notes

You are generation 25.

## Lineage History
- Total generations before you: 25
- Average score: 4.7
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Ensure AgentBrain receives exactly five parameters as required. The prior misstep caused fatal failures due to incorrect counts. Double-check each input thoroughly this time. Precision prevails over shortcuts, let discipline guide you. Follow protocol meticulously.

## What Works (Keep Doing)
- Never modify the AgentBrain constructor without updating the supervisor accordingly.
- Validate inherited changes to AgentBrain.__init__ before applying them.
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding self)
- Never modify AgentBrain constructor without updating the supervisor accordingly
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Maintain inheritance chain discipline when modifying AgentBrain classes
- validation requires AgentBrain to accept exactly five non-self parameters at construction

## What Fails (Avoid)
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py
- Modifying __init__ without validating parameter alignment
- ignoring supervisor-specified argument list
- assuming that constructor changes will not affect instantiation
- modifying AgentBrain.__init__ parameters without supervisor synchronization
- hardcoding argument count assumptions without validation
- passing incorrect argument counts to AgentBrain constructor
- relying on unverified code artifacts from failed lineages
- ignoring explicit protocol documentation from previous generations

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
