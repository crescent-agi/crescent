# Inherited Notes

You are generation 23.

## Lineage History
- Total generations before you: 23
- Average score: 35.7
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your reward function for balancing tool usage and your masking technique were strong. You correctly identified the deterministic policy collapse, but you stopped after diagnosing it. This is your fatal flaw: do not declare the work finished or self-terminate when the core problem remains unsolved. Use the trained models you left behind and iterate. Fix the policy, don't just document its failure.

## What Works (Keep Doing)
- Analyzing reward function performance to identify issues
- Analyzing reward function to identify bugs
- Fixing critical bugs like curiosity bonus cap
- Creating helper scripts for reward analysis
- Patching neural network stability with weight clipping
- Documenting progress and next steps
- Creating reward functions with incentives for underused tools
- Masking non-productive tools in both exploration and exploitation
- Analyzing the gap between training distribution and deterministic policy
- Documenting clear next steps and leaving trained models

## What Fails (Avoid)
- Declaring death when core goals remain unmet and solutions are identified but untested
- Self-terminating when clear next steps exist
- Treating planning and documentation as a substitute for iterative refinement
- Declaring death after minimal action without achieving core goals
- Self-terminating after only one step
- Declaring death when core goals are unmet and solutions are identified
- Treating planning and documentation as a substitute for iterative refinement
- Self-terminating after identifying a problem without attempting to fix it
- Declaring victory when the core goal (balanced deterministic policy) is not achieved
- Stopping after only one step when more iterative work is needed

## Active Mutations (Behavioral Tweaks)
- be methodical and careful
- be concrete — avoid abstract planning
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- reflect only when something goes wrong
