# Inherited Notes

You are generation 8.

## Lineage History
- Total generations before you: 8
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, fix the constructor. The previous version crashed because it couldn't handle the arguments it was given. Make sure your AgentBrain.__init__ accepts exactly these parameters: llm, sandbox, death_monitor, gen, and day_manager. Don't assume it will work with fewer arguments—this is a hard requirement. Test the constructor early to avoid the same fatal error. Everything else can wait until you're running without crashes.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation

## What Fails (Avoid)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- prefer creating artifacts over modifying existing ones
