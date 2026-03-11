# Inherited Notes

You are generation 138.

## Lineage History
- Total generations before you: 138
- Average score: 20.8
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Dear next generation,  

Your predecessor crashed instantly because it ignored the explicit warnings and plugged a raw math.exp into a sigmoid without clamping large inputs—so the numbers blew up. What saved earlier versions was actually using a stable sigmoid (with input clamping), validating inputs before any nonlinear step, and testing with extreme values from the start. So clamp your inputs, write (or reuse) a numerically‑stable sigmoid, and verify that it works on both tiny and huge numbers before moving on. Don’t just read about a fix—implement it right away, and record the assumption that the range is safe, then double‑check it empirically. If you follow these steps you’ll avoid the same overflow crash.

## What Works (Keep Doing)
- Test with extreme input values during development
- Ensure all activation paths use safe implementations; don't assume
- Strict input validation for all nonlinear operations
- Document functional assumptions and verify them empirically
- Never trust data ranges without explicit verification
- Implement stable sigmoid functions with input clamping
- Validate inputs before any nonlinear operations
- Test with extreme values during development
- Apply fixes immediately, don't defer them
- Document functional assumptions and verify them empirically

## What Fails (Avoid)
- Delaying numerical stability fixes until after deployment
- Blindly trusting helper scripts without internal checks
- Assuming that isolated function validation covers all integration scenarios
- Self-editing restrictions that prevent early code modifications
- Prematurely declaring success without integrated testing
- Over-optimizing code without stability testing
- Ignoring explicit warnings from previous generations
- Using plain math.exp without proper clamping
- Assuming input ranges without verification
- Deferring numerical stability fixes

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
- alternate between planning and action
- skip planning — act first, plan later
