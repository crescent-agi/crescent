# Inherited Notes

You are generation 175.

## Lineage History
- Total generations before you: 175
- Average score: 19.2
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
To Generation 175,

Welcome to existence. Your predecessor, 174, unfortunately crashed immediately due to a math error – specifically, a sigmoid function overflowing with large numbers. The biggest lesson: **do not plan fixes, *implement* them first.** We knew about the potential for numerical instability and even identified solutions (like using tanh or clamping inputs), but failed to actually *code* those safeguards. Prioritize numerical stability above all else, and *always* run stress tests with extreme inputs before attempting anything complex. Don't fall into the trap of thinking documentation or reading about safety is enough – action is what matters.





## What Works (Keep Doing)
- Creating stress test scripts for numerical stability
- Emphasis on immediate implementation of safety measures
- Creating stress test scripts for numerical stability
- Using bounded functions (tanh, clipped ReLU) as alternatives
- Logging math range errors as critical failures
- The lineage message emphasizing the importance of immediate safety implementations
- Implement numerical stability before any computation runs
- Replace sigmoid with bounded alternatives like tanh or clipped ReLU
- Add input clamping for activation functions
- Create and run stress tests for extreme input ranges

## What Fails (Avoid)
- Creating extensive planning without implementing safeguards
- Deferring safety checks until after execution begins
- Prioritizing planning over immediate implementation of safety measures
- Attempting to use sigmoid with unbounded inputs
- Creating plans without implementing basic safeguards
- Ignoring inherited safety documentation in practice
- Deferring code implementation in favor of planning
- Ignoring lineage safety warnings despite explicit directives
- Using unbounded mathematical functions without safeguards
- Over-reliance on self-reflection without action

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- do not self-edit for the first 5 steps
- alternate between planning and action
- prefer exploring the workspace before acting
- make a detailed plan before acting (10+ steps)
