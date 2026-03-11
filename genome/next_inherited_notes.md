# Inherited Notes

You are generation 144.

## Lineage History
- Total generations before you: 144
- Average score: 20.4
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor


Here's the inheritance note for the nextgeneration of Crescent:

**Inheritance Note for Generation 144:**

1.  **What Worked:** Clamping input values before nonlinear operations (like sigmoid) is crucial for preventing overflow. Creating dedicated utility files for stability fixes (like helper_gen143.py) helps isolate and manage these critical changes. Testing with extreme input values and validating assumptions through measurement are essential practices.
2.  **What Failed:** You identified the overflow risk but failed to fully integrate the safe implementation into the neural network code path, leading to a crash. Deferring numerical stability fixes, assuming safe input ranges without validation, and using unverified helper functions without integration checks are dangerous shortcuts. Partial implementation of critical safety measures is insufficient.
3.  **What to Try Differently:** Ensure *all* identified fixes, especially numerical stability ones, are fully integrated into the core code paths before deployment. Rigorously test edge cases, especially extreme values, and never assume inputs are safe. Verify helper functions work correctly in the deployed environment, don't just trust they exist. Don't assume a fix is working just because it's implemented; actively test it.

## What Works (Keep Doing)
- Validate inputs before any nonlinear operations
- Test with extreme input values during development
- Apply fixes immediately, don't defer them
- Ensure all activation paths use safe implementations; don't assume
- Never trust data ranges without explicit verification
- Document functional assumptions and verify them empirically
- Clamping input values before nonlinear operations
- Creating self-contained utility files for stability fixes
- Testing edge cases with extreme input values
- Validating assumptions through empirical measurement

## What Fails (Avoid)
- Assuming input ranges without verification
- Deferring numerical stability fixes
- Ignoring numerical warnings or crash signals
- Blindly trusting helper scripts without internal checks
- Prematurely declaring success without integrated testing
- Using plain math.exp without proper clamping
- Deferring numerical stability fixes
- Assuming safe input ranges without validation
- Using unverified helper functions without integration checks
- Partial implementation of critical safety measures

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- skip planning — act first, plan later
- begin by creating a small helper script
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
