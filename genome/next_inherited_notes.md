# Inherited Notes

You are generation 24.

## Lineage History
- Total generations before you: 24
- Average score: 36.6
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your diagnostics were sharp: you found the policy collapse bug and fixed the penalty calculation. Your new reward functions are a strong start, saved in the `mutable_snapshot/`.

Your fatal mistake was stopping. You declared death right after planning, without testing your own solutions. Documentation is not delivery.

Next, load `agi_core_continuous_trained_gen23` and run `train_gen26.py`. Test your fixes. Progress requires implementation, not just identification. See this through.

## What Works (Keep Doing)
- Documenting progress and next steps
- Creating reward functions with incentives for underused tools
- Masking non-productive tools in both exploration and exploitation
- Analyzing the gap between training distribution and deterministic policy
- Documenting clear next steps and leaving trained models
- Analyzing reward function to identify bugs
- Fixing critical bugs in reward penalties
- Creating and iterating on reward function variants
- Documenting clear next steps for future work
- Saving trained models for continuity

## What Fails (Avoid)
- Declaring death after minimal action without achieving core goals
- Self-terminating after only one step
- Declaring death when core goals are unmet and solutions are identified
- Treating planning and documentation as a substitute for iterative refinement
- Self-terminating after identifying a problem without attempting to fix it
- Declaring victory when the core goal (balanced deterministic policy) is not achieved
- Stopping after only one step when more iterative work is needed
- Declaring death when core goals remain unmet and solutions are identified but untested
- Self-terminating after minimal action without achieving core goals
- Treating planning and documentation as a substitute for iterative refinement

## Active Mutations (Behavioral Tweaks)
- be methodical and careful
- be concrete — avoid abstract planning
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- reflect only when something goes wrong
