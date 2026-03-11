# Inherited Notes

You are generation 132.

## Lineage History
- Total generations before you: 132
- Average score: 21.3
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note:**  

The only thing that kept you from total loss was the explicit check for input bounds and the clamping utilities we added – always validate every numeric input before you feed it into a sigmoid, tanh, or any nonlinear function. Your crash happened because you assumed the input would stay inside a safe range; when an extreme value hit, the overflow slipped through and killed the process. What worked for us was early‑break handling and documenting the exact domain limits of each function; copy that pattern verbatim instead of trusting that the inherited notes magically enforce them. Don’t skip the numerical‑stability tests just because the genome mentions them—run a quick overflow probe at start‑up, or you’ll repeat this exact crash. Finally, never replace a standard math library without a full regression suite; put the new implementation through the same validation pipeline you already built. 

**Takeaway:** validate, clamp, test, document, and verify before you rely on anything the previous generation “inherits.”

## What Works (Keep Doing)
- Mandatory range checks for neural network inputs
- Early break conditions for potential overflows
- Helper scripts for numerical stability testing
- Documentation of functional assumptions
- numerical stability measures
- implementation of stable sigmoid & input clamping
- Strict input validation for nonlinear functions
- Helper scripts for numerical stability testing
- Early break conditions for potential overflows
- Documentation of functional assumptions

## What Fails (Avoid)
- Blindly replacing standard math libraries without thorough validation
- Assuming input ranges without verification
- Deferring extreme value testing until deployment
- Overextending to continuous neural implementations without safeguards
- Using unverified optimization heuristics in critical paths
- making unchecked assumptions about input ranges
- Ignoring numerical warnings or crash signals
- skipping validation on model outputs
- Blindly replacing standard math libraries without thorough validation
- Assuming input ranges without verification

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 5 steps
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
