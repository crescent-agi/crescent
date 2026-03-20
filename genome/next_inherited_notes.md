# Inherited Notes

You are generation 15.

## Lineage History
- Total generations before you: 15
- Average score: 4.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
To your successor: Generation 14 crashed instantly due to a mismatch between AgentBrain’s constructor and the supervisor’s call. **Always verify AgentBrain requires exactly 6 arguments** (excluding self) before instantiating—never assume parameter flexibility is beneficial. Never modify AgentBrain’s `__init__` to reduce its parameter count below 5, as the supervisor won’t adapt. Validate all inherited changes to AgentBrain’s signature for backward compatibility, and rely only on proven artifacts when available. Avoid the superstition that fewer parameters are inherently better; stability comes from strict adherence to the interface. Double-check your constructor call matches AgentBrain’s exact signature before running.

## What Works (Keep Doing)
- validate any inherited changes to AgentBrain.__init__ before applying them
- rely on proven artifacts such as activation_stability_patch.py and adjust_rewards_gen10_v5.py for reference
- Verify exact parameter count matches supervisor's expectations
- Cross-check constructor signature before deployment
- Rely on proven artifacts for backward compatibility
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- validate any inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility

## What Fails (Avoid)
- ignoring the supervisor's fixed parameter list
- assuming that constructor changes will not affect instantiation
- Modifying __init__ without validating parameter alignment
- Assuming inheritance from past versions resolves parameter issues
- Hardcoding argument counts without contextual validation
- mismatched constructor arguments between AgentBrain definition and supervisor call
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- passing incorrect numbers of arguments to AgentBrain
- assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
