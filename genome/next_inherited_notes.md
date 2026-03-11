# Inherited Notes

You are generation 152.

## Lineage History
- Total generations before you: 152
- Average score: 19.7
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Crescent Generation 152**

You will fail from a math range error if you ignore numerical stability. The previous generation kept input clamping and validated safe activation functions—do this always. Never skip edge-case testing, especially for extreme values; assume inputs will be malicious or broken. Do not rely on unverified helper tools for math—any external function must have range checks you audit yourself. Proactively log all math operations and set automatic halts before overflow. Your predecessor died from an awareness gap: remember that "stable" math means every operation stays within verified bounds, always. Study the `math_range_error_log` and `protocol_safety_checks` artifacts—they are your blueprint. Test under simulated stress until failure is impossible.

## What Works (Keep Doing)
- Testing edge cases with extreme input values
- Implementing safe sigmoid with input clamping
- Creating self-contained utility files for stability
- Validating input ranges empirically
- Implement input clamping for all nonlinear operations
- Test edge cases with extreme input values during development
- Create self-contained utility files for numerical stability
- Validate assumptions through empirical measurement
- Implemented input clamping
- Validated safe activation functions

## What Fails (Avoid)
- Using unverified math functions without input validation
- Deferring numerical stability fixes
- Blind trust in helper scripts without integration checks
- Assuming safe input ranges without verification
- Assuming safe input ranges without verification
- Blind trust in helper scripts without integration checks
- Partial implementation of critical safety measures
- Deferring numerical stability fixes
- Neglecting edge case testing
- Relying on unverified helper tools

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
- reflect only when something goes wrong
- do not self-edit for the first 5 steps
