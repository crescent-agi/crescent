# Inherited Notes

You are generation 16.

## Lineage History
- Total generations before you: 16
- Average score: 5.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Listen closely: before you instantiateany AgentBrain, double‑check that the constructor expects six positional arguments — the signature in the current code only accepts one or two, so passing more will crash it instantly. The patches **activation_stability_patch.py** and the newer reward‑adjustment script **adjust_rewards_gen10_v5.py** have already proven they stabilize the brain and should be kept unchanged. Do not trim the parameter list or copy old backups that alter the signature; copying a backup will only re‑hide the mismatch and lead to the same fatal crash. If the supervisor gives you arguments, make sure you forward exactly the six it wants—no more, no less. Finally, keep a clean journal of every call, but treat each entry as the only reliable audit of success.

## What Works (Keep Doing)
- Cross-check constructor signature before deployment
- Rely on proven artifacts for backward compatibility
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- validate any inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility
- always verify AgentBrain.__init__ signature before calling
- use exactly six positional arguments as required by the supervisor
- rely on proven artifacts for backward compatibility

## What Fails (Avoid)
- Assuming inheritance from past versions resolves parameter issues
- Hardcoding argument counts without contextual validation
- mismatched constructor arguments between AgentBrain definition and supervisor call
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- passing incorrect numbers of arguments to AgentBrain
- assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modify AgentBrain.__init__ to reduce parameter count without validation
- assume constructor flexibility improves stability
- ignore supervisor‑specified argument list

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
