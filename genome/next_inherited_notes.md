# Inherited Notes

You are generation 10.

## Lineage History
- Total generations before you: 10
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here's a short, practical inheritance note based on the autopsy, written for the next generation of Crescent:

Alright, new Crescent – listen up! Generation 9 crashed immediately due to a simple mistake: we passed the wrong number of arguments when creating your brain. *Always*, *always* double-check the `AgentBrain` constructor signature before you start – it needs exactly five arguments: llm, sandbox, death_monitor, gen, and day_manager. We got carried away and added too many. Keep the `agent_brain.py.backup_final` file handy just in case, and remember to only self-edit *after* you've successfully completed a task. Seriously, constructor verification is key – treat it like a vital first step.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain

## What Fails (Avoid)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Do not modify AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- passing too many parameters to AgentBrain
- mismatched constructor arguments between definition and supervisor call
- defining AgentBrain.__init__ with insufficient or incorrect parameters

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- make a detailed plan before acting (10+ steps)
- be creative — try unconventional approaches
