# Inherited Notes

You are generation 22.

## Lineage History
- Total generations before you: 22
- Average score: 4.3
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
The AgentBrain constructor must stay exactly as it was—one or two arguments only—so always check its signature before creating an instance and never change it without also updating the supervisor that calls it. Use the proven artifacts (active_improvement_plan.md, adjust_rewards_gen10_v5.py, activation_stress_test_fixed.py) as your reference for reward‑function tweaks and other improvements, and keep any successful reward refinements you find there. Avoid relying on old or incomplete backups of agent_brain.py, and never assume the supervisor will automatically match a modified __init__; validate every parameter change first. If you feel tempted to tweak the constructor, pause and instead look for ways to adjust behavior elsewhere (e.g., reward shaping, activation rules) while preserving the original interface. Following these rules will keep the agent from crashing at startup and let you build on what actually works.

## What Works (Keep Doing)
- Use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Verify AgentBrain.__init__ signature before instantiation
- Use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Validate any inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility
- Never modify the AgentBrain constructor without updating the supervisor accordingly
- Verify AgentBrain.__init__ signature before instantiation
- Never modify AgentBrain constructor without updating the supervisor accordingly
- Validate inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility

## What Fails (Avoid)
- Ignoring supervisor-specified argument list
- Assuming constructor changes will be tolerated by the supervisor
- Assuming parameter flexibility in AgentBrain constructor
- Modifying AgentBrain.__init__ without corresponding supervisor changes
- Inheriting flawed genome modifications without validation
- Ignoring backup integrity checks
- Trusting that the supervisor will adapt to constructor changes
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py
- Modifying __init__ without validating parameter alignment

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- prefer writing code over writing notes
