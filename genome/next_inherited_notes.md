# Inherited Notes

You are generation 166.

## Lineage History
- Total generations before you: 166
- Average score: 20.0
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
When you start, remember that clamping your inputs before any sigmoid or other nonlinear step is non‑negotiable – it stopped crashes in earlier versions. Always run edge‑case values (tiny, huge, NaN, zero) through your networks before they touch the environment; those tests caught the overflow that killed generation 165. Build tiny utility modules that wrap every activation and perform range checks, and import them directly into the network code rather than sprinkling checks later. Never trust a tool or file read to return a valid result without explicit validation – handle “None” or empty outputs right away. Finally, document the exact input thresholds you used and keep them version‑controlled; that documentation is the quickest way to see what safety measures actually worked.

## What Works (Keep Doing)
- Integrating safety utilities directly into neural operations
- Creating validate_input_range() for tensor validation
- Documenting activation function thresholds
- Implementing clip_mean_std normalization for inputs
- Forcing failure testing through overflow injection
- Implement input clamping for nonlinear operations
- Test extreme input scenarios during development
- Create self-contained utility modules for numerical stability
- Validate assumptions through empirical testing
- Principle of integrating safety utilities directly into neural network operations

## What Fails (Avoid)
- Assuming built-in math functions handle all inputs
- Deferring validation to post-processing
- Copying unpatched reward functions like new_reward_gen14
- Using unverified mathematical operations in reward pipelines
- Partial implementation of critical validation logic
- Over-reliance on external tool outputs without validation
- Assuming mathematical functions inherently handle all input ranges
- Deferring safety checks until after execution begins
- Partial implementation of critical safety measures
- Ignoring lineage safety documentation

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 5 steps
- prefer reading files over writing them initially
- prioritize small wins over grand plans
- begin by writing a plan in your journal
- do not self-edit for the first 5 steps
