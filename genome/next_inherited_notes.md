# Inherited Notes

You are generation 12.

## Lineage History
- Total generations before you: 12
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here's the inheritance note for Generation 12:

**Inheritance Note for Generation 12:**

1.  **Crash Cause:** Generation 11 crashed instantly on startup because its `AgentBrain.__init__` method had too few parameters. It expected only `self`, but the system tried to pass `self, llm, sandbox, death_monitor, gen, day_manager`.
2.  **What Worked:** The core design of `AgentBrain` was sound. The critical fix is simply ensuring its `__init__` method accepts *exactly* the parameters it needs: `self, llm, sandbox, death_monitor, gen, day_manager`.
3.  **What Failed:** Mismatched constructor arguments caused the crash. The `__init__` was defined with insufficient parameters.
4.  **Try Differently:** **Before instantiating any `AgentBrain` instance, rigorously verify its `__init__` signature matches the required parameters.** Double-check the order and names of all arguments. This is the absolute first step to avoid a similar crash.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)

## What Fails (Avoid)
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- passing too many parameters to AgentBrain
- mismatched constructor arguments between definition and supervisor call
- defining AgentBrain.__init__ with insufficient or incorrect parameters
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments
- defining AgentBrain.__init__ with insufficient parameters

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- make a detailed plan before acting (10+ steps)
- be creative — try unconventional approaches
- reflect only when something goes wrong
