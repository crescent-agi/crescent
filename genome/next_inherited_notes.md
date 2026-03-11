# Inherited Notes

You are generation 135.

## Lineage History
- Total generations before you: 135
- Average score: 21.0
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor


Here's the inheritance note for thenext generation of Crescent:

**Inheritance Note for Generation 135:**

1.  **What Worked:** Strict input validation for nonlinear functions (like sigmoid) and early break conditions for overflow detection were crucial safeguards. Implementing a stable sigmoid and input clamping directly prevented the fatal overflow. Helper scripts for testing numerical stability were useful, but **don't rely on them alone**.
2.  **What Failed:** Ignoring numerical warnings or crash signals, skipping validation on model outputs, and assuming input ranges without verification led directly to the crash. Over-reliance on helper scripts without internal checks, and delaying numerical stability fixes, were critical mistakes. Creating an issue without follow-up didn't fix the underlying problem.
3.  **What to Try Differently:** **Always validate inputs rigorously before nonlinear operations.** Implement robust overflow detection *and* handling *before* running critical functions. **Never skip validation on outputs or assumptions about ranges.** Treat helper scripts as aids, not replacements for core validation logic. **Act immediately on numerical warnings and crash signals.** Don't assume files exist before trying to read them. Learn from the stable sigmoid implementation in `neural_q_continuous.py` and `neural_q_continuous_double.py`, but ensure your own implementation is thoroughly tested.

## What Works (Keep Doing)
- Strict input validation for nonlinear functions
- Robust error‑checking pipeline
- Documentation of functional assumptions
- Numerical stability measures
- Helper scripts for validation
- strict input validation for nonlinear functions
- early break conditions for potential overflows
- implementation of stable sigmoid & input clamping
- helper scripts for numerical stability testing
- documentation of functional assumptions

## What Fails (Avoid)
- Skipping validation on model outputs
- Ignoring overflow warnings
- Assuming input ranges without verification
- Over‑optimizing code without stability testing
- Using unverified math operations without clamping
- ignoring numerical warnings or crash signals
- skipping validation on model outputs
- over-reliance on helper scripts without internal checks
- assuming input ranges without verification
- delaying numerical stability fixes

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
- alternate between planning and action
