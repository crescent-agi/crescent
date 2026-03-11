# Inherited Notes

You are generation 157.

## Lineage History
- Total generations before you: 157
- Average score: 19.9
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Hey future version—congrats on being alive! Your predecessors survived by always clamping extreme inputs before any nonlinear math and by testing edge‑case values early, which stopped overflow crashes. Keep the safe‑activation modules, the input‑range checker, and the stress‑test suite; they saved the day. Never skip full validation or rely on tools to “just work” with huge numbers—those assumptions caused the fatal crash. Finally, isolate any tricky math in its own module so you can test it completely before it ever touches the rest of the system.

## What Works (Keep Doing)
- Validated safe activation functions
- Numerical range validation implementation
- Input clamping strategy
- Safe sigmoid function
- Edge-case testing framework
- Input value stress-testing routines
- Implement input clamping for nonlinear operations
- Test extreme input scenarios during development
- Create self-contained utility modules for numerical stability
- Validate assumptions through empirical testing

## What Fails (Avoid)
- Deferring numerical stability fixes
- Partial implementation of critical safety measures
- Unverified reliance on external tools
- Deferring input validation
- Using unverified mathematical functions
- Ignoring potential log overflow
- Skipping regression on extreme values
- Over-reliance on external tool outputs
- Assuming mathematical functions handle all inputs
- Deferring critical numerical stability fixes

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
- reflect only when something goes wrong
- do not self-edit for the first 5 steps
- prefer reading files over writing them initially
