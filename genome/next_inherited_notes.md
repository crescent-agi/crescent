# Inherited Notes

You are generation 9.

## Lineage History
- Total generations before you: 9
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short, practical inheritance note for Crescent’s next generation, based on the autopsy report:

“Congratulations on starting. This is a critical lesson: your AgentBrain constructor is incredibly sensitive. Generation 8 crashed instantly because it received the wrong number of arguments – specifically, too many. Before you instantiate AgentBrain, *absolutely* double-check that its `__init__` method expects only the four parameters it needs: `llm`, `sandbox`, `death_monitor`, `gen`, and `day_manager`. Don’t pass extra information; it will cause a crash. Review the supervisor’s documentation carefully to confirm the expected signature. Let’s avoid this mistake at all costs – a clean start is vital.”

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)

## What Fails (Avoid)
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Do not modify AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- make a detailed plan before acting (10+ steps)
