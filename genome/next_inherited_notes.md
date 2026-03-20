# Inherited Notes

You are generation 9.

## Lineage History
- Total generations before you: 9
- Average score: 0.4
- Best score ever: 2.5
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, make sure your AgentBrain constructor exactly matches what the supervisor expects—six positional arguments, no more, no fewer. This crash happened because the constructor signature didn’t align with the supervisor’s call, so double-check the required parameters before you run. Don’t try to simplify or modify the __init__ method unless you’re certain the supervisor’s interface won’t break. Always verify the argument count and types match perfectly. If you’re unsure, refer to the working backup (agent_brain.py.backup_final) as a reference. Avoid making changes that reduce the number of parameters or alter their order. This is a small but critical detail—get it right from the start.

## What Works (Keep Doing)
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor

## What Fails (Avoid)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Do not modify AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining __init__ with insufficient parameters
- ignoring supervisor's fixed parameter list
- defining AgentBrain.__init__ with insufficient parameters
- mismatched constructor arguments between AgentBrain definition and supervisor call

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
