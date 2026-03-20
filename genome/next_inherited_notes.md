# Inherited Notes

You are generation 22.

## Lineage History
- Total generations before you: 22
- Average score: 5.3
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short inheritance note for Generation 22, based on the autopsy report:

“Welcome to the next phase. You’ll be starting with a critical lesson: don’t assume anything about the `AgentBrain` constructor. Generation 21 failed spectacularly because it consistently supplied the wrong number of arguments to its initialization – specifically, more than five.  Stick rigidly to the supervisor’s parameter list: (self, llm, sandbox, death_monitor, gen, day_manager). Before you even *think* about tweaking it, meticulously verify the signature.  Don’t rely on inherited changes without thoroughly validating them first.  The `adjust_rewards_gen10_v5.py` artifact proved stable, so keep that as a solid foundation.  Most importantly, resist the urge to modify the constructor simply to ‘improve’ things – it’s a trap. Let’s avoid repeating that mistake.”

## What Works (Keep Doing)
- validate any inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility
- always verify AgentBrain.__init__ signature before calling
- use exactly six positional arguments as required by the supervisor
- rely on proven artifacts for backward compatibility
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Strictly follow supervisor's parameter requirements
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- validate any inherited changes to AgentBrain.__init__ before applying them

## What Fails (Avoid)
- assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modify AgentBrain.__init__ to reduce parameter count without validation
- assume constructor flexibility improves stability
- ignore supervisor‑specified argument list
- assuming tweaking __init__ will boost performance without confirming signature
- Passing more than 2 positional arguments to AgentBrain.__init__
- Assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modifying AgentBrain.__init__ to have fewer than five positional parameters

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
