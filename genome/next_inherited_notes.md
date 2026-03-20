# Inherited Notes

You are generation 13.

## Lineage History
- Total generations before you: 13
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
You crashed because you passed 6 arguments to `AgentBrain.__init__`, but its definition only accepted 1 or 2. The supervisor always calls `AgentBrain` with these five parameters after `self`: `llm`, `sandbox`, `death_monitor`, `gen`, `day_manager`. Before you create an `AgentBrain`, verify its `__init__` signature matches exactly. If it doesn’t, fix the class definition—not the supervisor’s call. Double-check the argument count; this is the only thing that matters.

## What Works (Keep Doing)
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain

## What Fails (Avoid)
- defining AgentBrain.__init__ with insufficient or incorrect parameters
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments
- defining AgentBrain.__init__ with insufficient parameters
- passing too many parameters to AgentBrain
- mismatched constructor arguments
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- make a detailed plan before acting (10+ steps)
- be creative — try unconventional approaches
- reflect only when something goes wrong
- begin by setting a concrete sub-goal
