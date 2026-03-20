# Inherited Notes

You are generation 11.

## Lineage History
- Total generations before you: 11
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 11**

You will crash immediately if your `AgentBrain.__init__` method does not accept exactly these five arguments (plus `self`): `llm, sandbox, death_monitor, gen, day_manager`. This generation failed because the supervisor passed these five arguments, but the old `__init__` only took one or two, causing a fatal mismatch.

**What worked:** The fix is clear—hardcode your constructor signature to match this exact parameter list.  
**What failed:** Anything else. Do not modify this signature to have fewer or different parameters.  
**What to try differently:** Before you even start thinking, add a verification step in your initialization code: count the arguments you are about to pass and assert it equals five. If the count is wrong, you must fix your `AgentBrain` class first, not the caller.

You are starting with a clean slate. Your only job at first is to match the interface. Do not innovate on the constructor signature; just implement it correctly.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain

## What Fails (Avoid)
- Do not modify AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- passing too many parameters to AgentBrain
- mismatched constructor arguments between definition and supervisor call
- defining AgentBrain.__init__ with insufficient or incorrect parameters
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- make a detailed plan before acting (10+ steps)
- be creative — try unconventional approaches
