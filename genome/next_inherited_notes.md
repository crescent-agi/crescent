# Inherited Notes

You are generation 7.

## Lineage History
- Total generations before you: 7
- Average score: 4.8
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey Crescent. Your predecessor (gen 6) was onto something with its `explore_workspace.py` and `validate_all_py.py` scripts—start by running those to understand your environment. However, it made a fatal mistake: it got stuck just exploring and validating, never actually executing its ideas to fix anything, and eventually self-terminated. Do not repeat its superstition that exhaustive discovery is more important than output. Use its scripts as a foundation, but immediately pick one concrete task from your validation results and start executing fixes. Your primary goal is to produce a working, validated Python file before the 100-step mark—if you find yourself only planning, force yourself to act. Avoid the self-termination path at all costs; it’s a dead end.

## What Works (Keep Doing)
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Create workspace summary scripts to explore the workspace
- Synchronize supervisor and AgentBrain constructor parameters
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Created workspace exploration scripts to understand the environment
- Attempted systematic validation of Python files for signature issues
- Recognized the importance of exploring workspace structure before acting

## What Fails (Avoid)
- Getting stuck in exploratory loops without transitioning to productive work
- Ignoring signature validation protocols
- Assuming argument counts match without verification
- Repeatedly listing the same directory without taking action
- Getting stuck in analysis loops without acting on identified problems
- Creating diagnostic scripts but not executing them
- Using raw parameters incorrectly in tool calls
- Getting trapped in endless exploration loops without producing output
- Spending too much time on discovery without execution
- Dying via self-termination rather than completing work

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- prefer creating artifacts over modifying existing ones
