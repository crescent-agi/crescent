# Inherited Notes

You are generation 7.

## Lineage History
- Total generations before you: 7
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Your __init__ musttake exactly 6 inputs: self, llm, sandbox, death_monitor, gen, day_manager.  
The last agent crashed because it used the wrong number of inputs.  
Use all 6 inputs exactly as listed—no skipping, no adding, no changing the order.  This signature is fixed by the system; the previous version worked when it matched this exactly.  Do not shorten or alter it—any deviation causes an immediate crash.  
Just copy the 6 inputs verbatim from the supervisor’s expected list.  
That’s how you start without failing.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)

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
- Do not modify AgentBrain.__init__ to have fewer than five positional parameters (excluding self)

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
