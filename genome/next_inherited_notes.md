# Inherited Notes

You are generation 74.

## Lineage History
- Total generations before you: 74
- Average score: 25.5
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor


Dear NextGen Crescent,

You crashed due to a math range error from input overflow, even though you had a plan to fix input validation. Here's what worked and what to avoid:

**What Worked:**
*   **Input Normalization:** Your plan to systematically clip and normalize inputs was sound.
*   **Diagnostic Scripts:** Creating scripts to test edge cases was a good step.
*   **Isolation:** Separating validation code for testing before full integration was wise.

**What Failed:**
*   **SafeActivation Reliance:** You trusted SafeActivation alone without proper input validation.
*   **Overflow Warnings Ignored:** You didn't act on numerical overflow warnings.
*   **Plan Execution:** You prioritized planning diagnostics over actually implementing the validation fixes.
*   **Premature Execution:** You ran untested neural net passes.

**What to Try Differently:**
1.  **Implement the Plan:** Don't just plan validation; *execute* it step-by-step.
2.  **Test Extensively:** Use the extreme input generator to stress-test your validation.
3.  **Clip Early:** Apply defined clipping ranges *before* processing inputs.
4.  **Use Artifacts:** Leverage the incomplete `input_validator.py` and your detailed validation journal.

**Key Artifacts to Use:**
*   `input_validator.py` (your planned fix)
*   Your validation strategy journal

**Avoid:**
*   Relying solely on SafeActivation.
*   Ignoring numerical overflow warnings.
*   Running untested neural net passes.

## What Works (Keep Doing)
- Isolate modifications before integrating them into core components
- Prioritize input normalization before neural network processing
- Use numerically stable activation functions with input clipping
- Maintain rigorous input validation to prevent extreme values
- Create diagnostic scripts for numerical stability testing
- Isolate modifications before core integration
- Document and reinforce architectural checks for edge cases
- Plan for systematic input normalization and clipping
- Creation of diagnostic scripts for edge case testing
- Isolation of code modifications for validation before integration

## What Fails (Avoid)
- Failing to thoroughly test the impact of modifications on numerical stability
- Creating untested or syntactically broken scripts
- Relying solely on simulator stability without empirically verifying on actual outputs.
- Ignoring precursors' warnings regarding numerical range management.
- Assuming input sanity checks are always sufficient with
- Neglecting core code paths with known numerical risks
- Running neural network forward passes without input validation
- Relying solely on SafeActivation without input validation
- Assuming helper scripts automatically resolve core issues
- Ignoring numerical overflow warnings

## Active Mutations (Behavioral Tweaks)
- be methodical and careful
- make a short plan (3-5 steps) then start
- begin by creating a small helper script
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
