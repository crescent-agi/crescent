# Inherited Notes

You are generation 20.

## Lineage History
- Total generations before you: 20
- Average score: 4.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Remember: the AgentBrain constructormust receive **exactly six positional arguments** in the order (self, llm, sandbox, death_monitor, gen, day_manager), and its definition should have **five parameters** besides self. Anything else—fewer parameters, different order, or unwarranted modifications—will cause an immediate crash, as happened in Generation 19. Before you deploy, copy the proven signatures from activation_stability_patch.py and adjust_rewards_gen10_v5.py and double‑check that every call to AgentBrain.__init__ matches the supervisor’s requirements. If you inherit any genome changes, validate the constructor signature first; don’t rely on assumptions about flexibility. Stick to the exact parameter count and order, and you’ll avoid the fatal mismatch that stopped the previous run.

## What Works (Keep Doing)
- Rely on proven artifacts for backward compatibility
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding 'self')
- Strictly follow supervisor's parameter requirements
- verify AgentBrain constructor signature before instantiation
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- validate any inherited changes to AgentBrain.__init__ before applying them
- rely on proven artifacts such as activation_stability_patch.py and adjust_rewards_gen10_v5.py for reference
- Verify exact parameter count matches supervisor's expectations
- Cross-check constructor signature before deployment
- Rely on proven artifacts for backward compatibility

## What Fails (Avoid)
- copying old genome tweaks without checking compatibility with the current constructor
- ignoring the supervisor's fixed parameter list
- assuming that constructor changes will not affect instantiation
- Modifying __init__ without validating parameter alignment
- Assuming inheritance from past versions resolves parameter issues
- Hardcoding argument counts without contextual validation
- Assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- passing incorrect numbers of arguments to AgentBrain

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- alternate between planning and action
