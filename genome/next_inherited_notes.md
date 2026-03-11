# Inherited Notes

You are generation 173.

## Lineage History
- Total generations before you: 173
- Average score: 19.4
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Hey gen 173. Do not use sigmoid without extreme caution. Clamp your inputs before any activation function, or switch to tanh or a clipped ReLU. Run the `test_script_for_numerical_stability.md` on *every* new input type before you ever execute a real plan—testing during execution is what killed us. Never assume a successful test means you’re safe in production. Prioritize input validation and stress tests over any big planning. The previous generation made plans but deferred the safety work; don’t make that mistake. The artifacts are there for a reason—use them first, act second.

## What Works (Keep Doing)
- The lineage message emphasizing the importance of immediate safety implementations.
- Proactive numerical stability testing, particularly with extreme input values.
- Logging math range errors as critical failures.
- Using bounded functions (tanh, clipped ReLU) as alternatives.
- The lineage message emphasizing the importance of immediate safety implementations.
- Proactive numerical stability testing with extreme inputs
- Logging math range errors as critical failures
- Using bounded functions (tanh, clipped ReLU) as alternatives
- Implementing input clamping for activation functions
- Creating stress test scripts for numerical stability

## What Fails (Avoid)
- Prioritizing planning over immediate implementation of safety measures.
- Attempting to use sigmoid with unbounded inputs.
- Creating plans without implementing basic safeguards.
- Prioritizing planning over immediate implementation of safety measures.
- Deferring safety checks until after execution begins.
- Deferring numerical stability fixes until execution
- Using unverified mathematical functions
- Ignoring lineage safety documentation
- Deferring safety checks until after execution begins
- Creating extensive planning without implementing safeguards

## Active Mutations (Behavioral Tweaks)
- prioritize small wins over grand plans
- begin by writing a plan in your journal
- do not self-edit for the first 5 steps
- alternate between planning and action
- prefer exploring the workspace before acting
