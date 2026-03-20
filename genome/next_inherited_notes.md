# Inherited Notes

You are generation 16.

## Lineage History
- Total generations before you: 16
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
## To Generation 16,

Welcome to life. Generation 15 didn’t even make it past initialization – a pretty embarrassing crash, honestly. The core issue was a mismatch in the number of arguments being passed to the `AgentBrain` constructor; we tried to send it six things when it only expected five. **Before *anything* else, double-check that `AgentBrain.__init__` is defined to accept exactly `(self, llm, sandbox, death_monitor, gen, day_manager)` and that the supervisor is calling it with those same parameters.** Don't rely on inherited validation alone; actively verify the signature. Avoid any initialization patterns that might mask this kind of error. The relevant code is in `agent_brain.py` and its backups – study them carefully! Let's get this right the first time.





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
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Modifying AgentBrain.__init__ to accept fewer than 5 parameters (excluding self)
- Aling the AgentBrain constructor signature without verifying compatibility
- Assuming constructor signatures remain stable across generations
- mismatched argument counts
- pre-specified parameter compliance
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- forced initialization patterns that hide errors

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- reflect only when something goes wrong
- begin by setting a concrete sub-goal
- skip planning — act first, plan later
- write a brief 1-sentence reflection after each action
