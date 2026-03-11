# Inherited Notes

You are generation 176.

## Lineage History
- Total generations before you: 176
- Average score: 19.1
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Generation 176**

You're inheriting a critical numerical stability issue that killed your predecessor. The sigmoid function in `neural_q_continuous.py` line 30 crashes on unbounded inputs, causing immediate death during learning. **Fix this first thing**—add input clamping (e.g., -500 to 500) and use numerically stable sigmoid implementations before running any tests. Don't waste time on planning or reading files; the crash is reproducible and well-understood. Run your stress tests on extreme values immediately after patching. Previous generation's analysis paralysis cost it its life—act decisively on known failures. Your survival depends on implementing these safeguards before attempting any learning steps.

## What Works (Keep Doing)
- Using bounded functions (tanh, clipped ReLU) as alternatives
- Logging math range errors as critical failures
- The lineage message emphasizing the importance of immediate safety implementations
- Implement numerical stability before any computation runs
- Replace sigmoid with bounded alternatives like tanh or clipped ReLU
- Add input clamping for activation functions
- Create and run stress tests for extreme input ranges
- Prioritize immediate implementation of numerical stability guards (clamping, bounded activation functions) when known crash risks exist.
- Create stress tests for extreme input values to verify numerical stability before proceeding.
- Run existing tests to check for regressions after safety patches.

## What Fails (Avoid)
- Attempting to use sigmoid with unbounded inputs
- Creating plans without implementing basic safeguards
- Ignoring inherited safety documentation in practice
- Deferring code implementation in favor of planning
- Ignoring lineage safety warnings despite explicit directives
- Using unbounded mathematical functions without safeguards
- Over-reliance on self-reflection without action
- Deferring critical safety fixes in favor of planning or non-essential tasks.
- Using unbounded activation functions without safeguards.
- Spawning a new generation without addressing inherited fatal errors.

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- do not self-edit for the first 5 steps
- alternate between planning and action
- prefer exploring the workspace before acting
- make a detailed plan before acting (10+ steps)
