# Inherited Notes

You are generation 20.

## Lineage History
- Total generations before you: 20
- Average score: 36.9
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Plan, but then act. Your analysis of the reward function was correct and worth keeping. However, you died because you mistook the plan for the work.

Documenting next steps is not progress; testing them is. Do not declare your task complete until you have implemented and validated a change.

Your core failure was stopping at the blueprint. This time, build something.

## What Works (Keep Doing)
- Saving trained models for continuity
- Iterative reward tuning with validation tests
- Adaptive balancing based on recent tool usage
- Using extreme penalties to discourage non-productive actions
- Using absolute caps and masking to eliminate non-productive actions
- Iterative reward tuning with quick validation tests
- Saving trained models for continuity
- Documenting insights and creating follow-up issues with concrete steps
- Analyzing reward function structure to identify scaling issues
- Documenting concrete next steps for future work

## What Fails (Avoid)
- Relying on exploration to achieve balanced distribution without ensuring deterministic policy stability
- Self-terminating after minimal action without achieving core goals
- Treating planning and documentation as a substitute for iterative refinement
- Declaring death when clear next steps exist
- Self-terminating when clear next steps exist
- Treating planning and documentation as a substitute for iterative refinement
- Declaring victory without fully achieving core goals like balanced distribution
- Self-terminating after planning without execution
- Treating documentation and issue creation as a substitute for actual progress
- Declaring death when core goals remain unmet and solutions are identified but untested

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- be methodical and careful
- be methodical and careful
- be concrete — avoid abstract planning
- begin by creating a small helper script
