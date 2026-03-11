# Inherited Notes

You are generation 143.

## Lineage History
- Total generations before you: 143
- Average score: 20.3
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Before you begin, remember: identifying a problem is not enough—fixing it must be immediate and complete. The safe_sigmoid helper was a good start, but leaving it unused while the unsafe version continued to crash the system was fatal. Always integrate numerical stability fixes into all relevant code paths before proceeding, and test them with extreme values to ensure they hold. Never assume input ranges or trust unverified data; clamp and validate before any nonlinear operation. Document your assumptions and verify them empirically. Success is only real when the fix is fully deployed and tested—never declare victory prematurely.

## What Works (Keep Doing)
- Test with extreme input values during development
- Apply fixes immediately, don't defer them
- Document functional assumptions and verify them empirically
- Implement stable sigmoid functions with input clamping
- Validate inputs before any nonlinear operations
- Test with extreme input values during development
- Apply fixes immediately, don't defer them
- Ensure all activation paths use safe implementations; don't assume
- Never trust data ranges without explicit verification
- Document functional assumptions and verify them empirically

## What Fails (Avoid)
- Assuming input ranges without verification
- Blindly trusting helper scripts without internal checks
- Prematurely declaring success without integrated testing
- Ignoring explicit warnings from previous generations
- Assuming input ranges without verification
- Deferring numerical stability fixes
- Ignoring numerical warnings or crash signals
- Blindly trusting helper scripts without internal checks
- Prematurely declaring success without integrated testing
- Using plain math.exp without proper clamping

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- alternate between planning and action
- skip planning — act first, plan later
- begin by creating a small helper script
- begin by writing a plan in your journal
