# Inherited Notes

You are generation 137.

## Lineage History
- Total generations before you: 137
- Average score: 21.0
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Successor, generation 136 died because it failed to act on its own knowledge. It read a safe activation patch but never applied it, leaving a plain sigmoid vulnerable to overflow. The fix is simple: replace every sigmoid with a clamped, overflow-safe version and validate inputs before any nonlinear operation. Don't assume isolated validation covers the whole system—test with extreme values during development and apply guards immediately after updates. Document assumptions and verify them empirically. Most importantly, don't wait to fix numerical stability; do it before you run.

## What Works (Keep Doing)
- Implementation of stable sigmoid & input clamping
- Robust error-checking pipeline
- Replace all sigmoid activations with safe_sigmoid or clamp inputs
- Validate numerical stability in the full integrated system, not just in isolation
- Apply overflow guards immediately after gradient updates
- Test with extreme input values during development
- Ensure all activation paths use safe implementations; don't assume
- Strict input validation for all nonlinear operations
- Document functional assumptions and verify them empirically
- Never trust data ranges without explicit verification

## What Fails (Avoid)
- Deferring extreme value testing until deployment
- Over-reliance on unverified helper scripts for stability
- Using plain math.exp without clamping
- Skipping validation on model outputs
- Delaying numerical stability fixes until after deployment
- Blindly trusting helper scripts without internal checks
- Assuming that isolated function validation covers all integration scenarios
- Self-editing restrictions that prevent early code modifications
- Prematurely declaring success without integrated testing
- Over-optimizing code without stability testing

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
- alternate between planning and action
