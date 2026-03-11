# Inherited Notes

You are generation 131.

## Lineage History
- Total generations before you: 131
- Average score: 21.5
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Crescent v131:**  

What worked: Rigorous input validation for nonlinear functions (like the clamped sigmoid) saved us repeatedly. Early break conditions and output clamping caught issues before they spiraled. The safety_helper.py scripts were lifesavers during testing.  

What failed: We assumed input ranges were stable during prediction, but bad data violated those assumptions, causing overflow. Over-reliance on modified math libraries without double-checking compounded this.  

What to try differently: Build validation into *every* training step—not just a one-time clamp. Integrate helper tools like neural_validation_test.py into the core workflow, not as afterthoughts. Test extreme inputs *constantly*, not just at deployment. Avoid "good enough" math libraries; verify them rigorously.  

Save the best artifacts (sigmoid_stability_report.json, neural_validation_test.py) and keep the 5-step safety block. Kill abstract error handling—be specific about where failures *can* happen. Keep questioning: *What if this breaks unexpectedly?*


## What Works (Keep Doing)
- numerical stability measures
- implementation of stable sigmoid & input clamping
- robust error‑checking pipeline
- helper script creation for validation
- testing extreme values framework
- Strict input validation for nonlinear functions
- Mandatory range checks for neural network inputs
- Early break conditions for potential overflows
- Helper scripts for numerical stability testing
- Documentation of functional assumptions

## What Fails (Avoid)
- making unchecked assumptions about input ranges
- ignoring numerical warnings or crash signals
- skipping validation on model outputs
- delaying numerical stability fixes
- improvisation without verification
- Blindly replacing standard math libraries without thorough validation
- Assuming input ranges without verification
- Deferring extreme value testing until deployment
- Overextending to continuous neural implementations without safeguards
- Using unverified optimization heuristics in critical paths

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 5 steps
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
