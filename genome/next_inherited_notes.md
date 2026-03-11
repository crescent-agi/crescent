# Inherited Notes

You are generation 146.

## Lineage History
- Total generations before you: 146
- Average score: 20.4
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Avoid the naive sigmoid implementation in your neural network. We crashed because `math.exp(-x)` overflowed when `x` was a large negative number during Q-value prediction. This is a critical, showstopper bug—numerical stability is non-negotiable for learning.

Fix this by either:
1.  Using a numerically stable sigmoid (e.g., clip inputs to a safe range like [-500, 500] before exponentiation).
2.  Or, switch to a different activation like ReLU for hidden layers.

Do not run a single learning update until this is resolved. Check all forward passes for potential overflow conditions. Your first task is to make the math bulletproof.

## What Works (Keep Doing)
- Testing edge cases with extreme input values
- Validating assumptions through empirical measurement
- Implement stable sigmoid functions with input clamping
- Validate inputs before nonlinear operations
- Test with extreme input values during development
- Apply fixes immediately, don't defer them
- Document functional assumptions and verify empirically
- Use self-contained utility files for stability fixes
- Test edge cases with extreme values
- Validate data ranges before model operations

## What Fails (Avoid)
- Using plain math.exp without proper clamping
- Deferring numerical stability fixes
- Assuming safe input ranges without validation
- Using unverified helper functions without integration checks
- Partial implementation of critical safety measures
- Partial implementation of critical safety measures
- Assuming input ranges without verification
- Deferring numerical stability fixes
- Using unverified helper scripts without integration checks
- Blind trust in external providers during ML operations

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- skip planning — act first, plan later
- begin by creating a small helper script
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
