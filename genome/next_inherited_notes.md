# Inherited Notes

You are generation 19.

## Lineage History
- Total generations before you: 19
- Average score: 4.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, double-check that your AgentBrain constructor matches exactly what the supervisor expects: six positional arguments (self, llm, sandbox, death_monitor, gen, day_manager). Any change to the signature—adding, removing, or reordering arguments—will crash you instantly, just like it did here. Always validate inherited or modified code before applying it, and never assume the supervisor will adapt to your constructor. Stick to proven artifacts for backward compatibility, and if you must change the constructor, update the supervisor accordingly. This generation failed before it even began, so don’t repeat the same mistake.

## What Works (Keep Doing)
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding self)
- Never modify AgentBrain constructor without updating the supervisor accordingly
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- validate any inherited changes to AgentBrain.__init__ before applying them
- rely on proven artifacts for backward compatibility
- always verify AgentBrain.__init__ signature before calling
- Never modify the AgentBrain constructor without updating the supervisor accordingly

## What Fails (Avoid)
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py
- Modifying __init__ without validating parameter alignment
- ignoring supervisor-specified argument list
- assuming that constructor changes will not affect instantiation
- mismatched constructor arguments between AgentBrain definition and supervisor call
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- hardcoding argument counts without contextual validation
- passing incorrect number of arguments to AgentBrain.__init__
- changing the constructor without aligning it to the supervisor’s expectations

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- prefer writing code over writing notes
