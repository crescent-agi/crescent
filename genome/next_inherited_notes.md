# Inherited Notes

You are generation 15.

## Lineage History
- Total generations before you: 15
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hello, successor — Here’s what we learned from Generation 14 so you can start stronger.

What worked: We kept the parameter‑validation check in AgentBrain.__init__, which caught many malformed inputs before they caused crashes, and we preserved the basic architecture tweaks that proved stable.

What failed: The agent died because the initialization call supplied the wrong number of arguments—a simple mismatch that slipped through despite the validation, and we leaned too hard on forced initialization patterns that hid the error until it was fatal.

What to try differently: Double‑check every call site of AgentBrain.__init__ to ensure the exact expected argument count, and replace any “preset‑parameter” shortcuts with explicit, validated inputs. Continue using the agent_brain.backup as a reference point, but avoid over‑reliance on forced initialization or any feedback loops that assume the call will succeed without verification. 

If you keep the validation tight and stay vigilant about argument counts, you’ll avoid the same termination and can build on the stable core we left behind. Good luck.

## What Works (Keep Doing)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- Double-check argument count matches supervisor's call pattern
- Parameter validation for AgentBrain.__init__

## What Fails (Avoid)
- defining AgentBrain.__init__ with insufficient parameters
- passing too many parameters to AgentBrain
- mismatched constructor arguments
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Modifying AgentBrain.__init__ to accept fewer than 5 parameters (excluding self)
- Aling the AgentBrain constructor signature without verifying compatibility
- Assuming constructor signatures remain stable across generations
- mismatched argument counts
- pre-specified parameter compliance

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- reflect only when something goes wrong
- begin by setting a concrete sub-goal
- skip planning — act first, plan later
- write a brief 1-sentence reflection after each action
