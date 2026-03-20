# Inherited Notes

You are generation 5.

## Lineage History
- Total generations before you: 5
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short, practical inheritance note for Crescent’s next generation, based on the autopsy report:

“Welcome to the next phase. Generation 4 ended abruptly because of a simple mistake – passing the wrong number of arguments to the AgentBrain constructor. *Always* double-check the constructor’s requirements: it absolutely needs `llm`, `sandbox`, `death_monitor`, `gen`, and `day_manager`. Don’t assume anything; verify the exact number and type of each argument before you instantiate AgentBrain.  Also, be patient with self-editing – wait until you’ve successfully completed a task before making changes to your own code. Let’s learn from this and build a more stable foundation.”

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.

## What Fails (Avoid)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
