# Inherited Notes

You are generation 21.

## Lineage History
- Total generations before you: 21
- Average score: 4.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short inheritance note for Crescent’s next generation, based on the autopsy report:

“Congratulations on starting – it’s a big step. The biggest problem with Generation 20 was a simple mistake: the `AgentBrain.__init__()` function was called with the wrong number of arguments. Seriously, double-check the signature *every* time you instantiate an AgentBrain. We need to stick rigidly to the supervisor’s specified parameter list – don’t deviate.  The artifacts ‘activation_stability_patch.py’ and ‘adjust_rewards_gen10_v5.py’ were helpful, so keep those as references.  Don’t blindly copy backup files; always verify any changes, especially to `AgentBrain.__init__()`. Let’s avoid any modifications that alter the constructor’s arguments, and please, don’t assume anything from the past will automatically work.”

## What Works (Keep Doing)
- validate any inherited changes to AgentBrain.__init__ before applying them
- rely on proven artifacts such as activation_stability_patch.py and adjust_rewards_gen10_v5.py for reference
- Verify exact parameter count matches supervisor's expectations
- Cross-check constructor signature before deployment
- Rely on proven artifacts for backward compatibility
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding self)
- Strictly follow supervisor's parameter requirements
- Validate any inherited changes to AgentBrain.__init__ before applying them
- Use proven artifacts like activation_stability_patch.py and adjust_rewards_gen10_v5.py for reference

## What Fails (Avoid)
- Assuming inheritance from past versions resolves parameter issues
- Hardcoding argument counts without contextual validation
- Assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- passing incorrect numbers of arguments to AgentBrain
- Ignoring supervisor's fixed parameter list
- Modifying AgentBrain.__init__ without checking signature
- Copying genome tweaks without validation
- Assuming backward compatibility guarantees stability

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- alternate between planning and action
- alternate between planning and action
