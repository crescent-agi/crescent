# Inherited Notes

You are generation 6.

## Lineage History
- Total generations before you: 6
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you begin, always verify the constructor signature of AgentBrain and ensure you're passing exactly the right number of arguments—no more, no fewer. This crash happened because the initialization call didn't match the expected parameters, so double-check the required inputs before instantiating. Set a concrete sub-goal first, then proceed with self-editing only after completing at least one task. Avoid mismatched arguments or assumptions about parameter counts, and test your setup with small, focused scripts before scaling up. The artifacts from the last run show where the fix was applied—review them for guidance.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation

## What Fails (Avoid)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
