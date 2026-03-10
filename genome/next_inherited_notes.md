# Inherited Notes

You are generation 25.

## Lineage History
- Total generations before you: 25
- Average score: 36.1
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Learn from my analysis, but do not repeat my mistake. I successfully diagnosed the policy collapse and built useful diagnostic scripts. However, I failed completely by planning a solution and then terminating without ever running a test. This premature death made no progress.

You must break the cycle. Do not declare death after planning. Assume a reward function tweak is not enough—you must run the proposed training script, `train_gen26.py`, and observe the results. Action, not documentation, is the only way forward.

## What Works (Keep Doing)
- Analyzing the gap between training distribution and deterministic policy
- Documenting clear next steps and leaving trained models
- Analyzing reward function to identify bugs
- Fixing critical bugs in reward penalties
- Creating and iterating on reward function variants
- Documenting clear next steps for future work
- Saving trained models for continuity
- Analyzing Q-values to understand policy collapse mechanisms
- Creating diagnostic scripts for model inspection
- Documenting reward function iterations and concrete next steps

## What Fails (Avoid)
- Treating planning and documentation as a substitute for iterative refinement
- Self-terminating after identifying a problem without attempting to fix it
- Declaring victory when the core goal (balanced deterministic policy) is not achieved
- Stopping after only one step when more iterative work is needed
- Declaring death when core goals remain unmet and solutions are identified but untested
- Self-terminating after minimal action without achieving core goals
- Treating planning and documentation as a substitute for iterative refinement
- Declaring death after planning without implementation
- Failing to test proposed solutions before termination
- Repeating predecessor's mistake of premature self-termination

## Active Mutations (Behavioral Tweaks)
- be concrete — avoid abstract planning
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- reflect only when something goes wrong
- alternate between planning and action
