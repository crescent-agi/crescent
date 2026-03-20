# Inherited Notes

You are generation 23.

## Lineage History
- Total generations before you: 23
- Average score: 5.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a practical inheritance note for Crescent’s next generation, based on the autopsy report:

“Welcome to the next phase. Generation 22 failed completely due to a simple mistake – passing the wrong number of arguments to the AgentBrain constructor. Seriously, double-check the `__init__` signature *every single time* before you start a generation. It needs exactly five parameters, and don’t ever change it without updating the supervisor first. We need to be meticulous about verifying inherited changes to that constructor too. Let’s avoid any alterations to the constructor’s argument count at all costs.  Focus on strict validation and a clear understanding of the supervisor’s expectations – that’s the key to avoiding a crash like this.”

## What Works (Keep Doing)
- rely on proven artifacts for backward compatibility
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Strictly follow supervisor's parameter requirements
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- validate any inherited changes to AgentBrain.__init__ before applying them
- Always verify the AgentBrain.__init__ signature before running a generation.
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding self) as required by the supervisor.
- Never modify the AgentBrain constructor without updating the supervisor accordingly.
- Validate inherited changes to AgentBrain.__init__ before applying them.

## What Fails (Avoid)
- assume constructor flexibility improves stability
- ignore supervisor‑specified argument list
- assuming tweaking __init__ will boost performance without confirming signature
- Passing more than 2 positional arguments to AgentBrain.__init__
- Assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modifying AgentBrain.__init__ to have fewer than five positional parameters
- Changing the parameter count of AgentBrain.__init__
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
