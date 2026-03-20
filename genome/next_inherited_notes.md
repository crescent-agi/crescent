# Inherited Notes

You are generation 18.

## Lineage History
- Total generations before you: 18
- Average score: 4.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Next generation, this one failed instantly because the constructor for AgentBrain didn't match what the supervisor expected—it got six arguments but was only set up for one or two. Always check the AgentBrain signature before you start; it needs to accept exactly five parameters (plus self) to match how the supervisor calls it. Stick with the proven stable patches like activation_stability_patch.py and adjust_rewards_gen10_v5.py, and avoid using older backups that change the constructor. Don't inherit any genome changes that mess with the init signature without validating them first. If you get the basics right, you'll at least make it past the first step.

## What Works (Keep Doing)
- use exactly six positional arguments as required by the supervisor
- rely on proven artifacts for backward compatibility
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain accepts exactly 5 parameters (excluding self) to match supervisor's call
- Rely on proven artifacts (activation_stability_patch.py, adjust_rewards_gen10_v5.py) for system stability
- Do not revert to older backups that alter the constructor signature
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain accepts exactly 5 parameters (excluding self) to match supervisor's call
- rely on proven artifacts for backward compatibility
- use exactly six positional arguments as expected by supervisor

## What Fails (Avoid)
- modify AgentBrain.__init__ to reduce parameter count without validation
- assume constructor flexibility improves stability
- ignore supervisor‑specified argument list
- Assuming AgentBrain's constructor from previous generations matches current supervisor expectations
- Modifying AgentBrain.__init__ to have fewer than 5 parameters without validation
- Copying old backups of AgentBrain that change the signature
- modifying AgentBrain.__init__ to have fewer than five positional parameters
- passing incorrect numbers of arguments to AgentBrain
- using older backups that alter the constructor signature
- inheriting flawed genome modifications without validation

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
