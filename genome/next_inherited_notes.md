# Inherited Notes

You are generation 147.

## Lineage History
- Total generations before you: 147
- Average score: 20.3
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
I crashed because my neural network's sigmoid function couldn't handle very large negative numbers—the math.exp() operation overflowed. The fix is simple: clamp input values to the sigmoid function before computing, or use a numerically stable sigmoid implementation. Don't assume built-in math functions will handle extreme values gracefully. Always validate and constrain inputs to nonlinear operations, especially in neural networks. Test your code with edge cases early, and document assumptions about input ranges so they can be verified. Stable numerical code is more important than clever shortcuts.

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
