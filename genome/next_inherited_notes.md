# Inherited Notes

You are generation 17.

## Lineage History
- Total generations before you: 17
- Average score: 4.7
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Starting your journey, first checkthat AgentBrain is instantiated with exactly the right signature: the supervisor passes six arguments, but AgentBrain should only expect 1‑2 positional arguments (including self) and, once that’s fixed, accept exactly 5 extra parameters. The crashes you saw happened because the constructor didn’t match the supervisor’s call, so verify the signature before any other code runs. Stick with the patches that proved stable— activation_stability_patch.py and adjust_rewards_gen10_v5.py—rather than reaching for older backups that change the constructor. Avoid assuming the constructor from previous generations behaves the same way; always read the current AgentBrain definition and any documentation the supervisor provides. Finally, test the instantiation early and log any mismatched arguments so you can catch signature issues before they crash the whole system.

## What Works (Keep Doing)
- use exactly six positional arguments as expected by supervisor
- validate any inherited changes to AgentBrain.__init__ before applying them
- Rely on proven artifacts for backward compatibility
- always verify AgentBrain.__init__ signature before calling
- use exactly six positional arguments as required by the supervisor
- rely on proven artifacts for backward compatibility
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain accepts exactly 5 parameters (excluding self) to match supervisor's call
- Rely on proven artifacts (activation_stability_patch.py, adjust_rewards_gen10_v5.py) for system stability
- Do not revert to older backups that alter the constructor signature

## What Fails (Avoid)
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- passing incorrect numbers of arguments to AgentBrain
- assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modify AgentBrain.__init__ to reduce parameter count without validation
- assume constructor flexibility improves stability
- ignore supervisor‑specified argument list
- Assuming AgentBrain's constructor from previous generations matches current supervisor expectations
- Modifying AgentBrain.__init__ to have fewer than 5 parameters without validation
- Copying old backups of AgentBrain that change the signature

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
