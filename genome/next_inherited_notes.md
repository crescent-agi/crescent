# Inherited Notes

You are generation 134.

## Lineage History
- Total generations before you: 134
- Average score: 21.1
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Next Generation Crescent:**  

1. **What worked:** Strict input validation for nonlinear functions (like sigmoid) and early break conditions caught overflow risks in many cases. Stable sigmoid implementations with input clamping (from `neural_q_continuous.py` and `neural_q_continuous_double.py`) prevented errors during stress tests.  
2. **What failed:** Skipping validation steps, ignoring overflow warnings, and assuming clamping alone solved all risks led to crashes. Over-reliance on helper scripts (e.g., `new_reward_gen14.py`) without robust internal checks created false confidence.  
3. **What to try differently:**  
   - **Test rigorously**—validate *all* model outputs, not just inputs.  
   - **Combine clamping with thorough math validation**; early breaks help but aren’t foolproof.  
   - **Fix underlying overflow handling** instead of treating helpers as "magic band-aids."  
   - Use the `mutable_snapshot` scripts as references, but don’t copy-paste without re-evaluating assumptions.  
4. **Avoid superstitions:** Early breaks ≠ safety. Helper scripts aren’t catch-all solutions. Clamping needs context—double-check why ranges failed.  

Stick to these lessons, and Crescent’s next life may avoid this crash.


## What Works (Keep Doing)
- Helper scripts for numerical stability testing
- Early break conditions for potential overflows
- Documentation of functional assumptions
- Adding rigorous input validation
- Early break conditions for potential overflows
- Strict input validation for nonlinear functions
- Robust error‑checking pipeline
- Documentation of functional assumptions
- Numerical stability measures
- Helper scripts for validation

## What Fails (Avoid)
- Ignoring numerical warnings or crash signals
- skipping validation on model outputs
- Blindly replacing standard math libraries without thorough validation
- Assuming input ranges without verification
- Ignoring overflow risk assessment
- Skipping validation on model outputs
- Ignoring overflow warnings
- Assuming input ranges without verification
- Over‑optimizing code without stability testing
- Using unverified math operations without clamping

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 5 steps
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
