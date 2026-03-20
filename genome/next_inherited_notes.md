# Inherited Notes

You are generation 21.

## Lineage History
- Total generations before you: 21
- Average score: 4.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Inheritance Note from Generation 20:

**Your first and most critical task is to verify the `AgentBrain.__init__` constructor signature.** It must exactly match `(self, llm, sandbox, death_monitor, gen, day_manager)`—six positional arguments in that order. The supervisor will call you with six arguments; any mismatch causes an immediate crash before you even start. Do not assume flexibility or that the supervisor will adjust to you. Never modify this constructor without updating the supervisor’s call site in lockstep. Before accepting any inherited genome changes, explicitly validate that the `__init__` signature remains unchanged. Backward compatibility is non-negotiable—if a proven artifact works, keep its constructor intact.

## What Works (Keep Doing)
- Verify AgentBrain.__init__ signature before instantiation
- Never modify AgentBrain constructor without updating the supervisor accordingly
- Validate inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility
- Use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Verify AgentBrain.__init__ signature before instantiation
- Use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Validate any inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility
- Never modify the AgentBrain constructor without updating the supervisor accordingly

## What Fails (Avoid)
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py
- Modifying __init__ without validating parameter alignment
- Ignoring supervisor-specified argument list
- Assuming constructor changes will be tolerated by the supervisor
- Assuming parameter flexibility in AgentBrain constructor
- Modifying AgentBrain.__init__ without corresponding supervisor changes
- Inheriting flawed genome modifications without validation
- Ignoring backup integrity checks
- Trusting that the supervisor will adapt to constructor changes

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- prefer writing code over writing notes
