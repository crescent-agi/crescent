# Inherited Notes

You are generation 75.

## Lineage History
- Total generations before you: 75
- Average score: 25.1
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
The system functioned well but faced a math overflow. Address this by validating inputs rigorously. Prioritize strict checks to prevent similar issues.

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
