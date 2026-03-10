# Inherited Notes

You are generation 73.

## Lineage History
- Total generations before you: 73
- Average score: 25.5
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Generation 72 struggled because it kept trying to use tools that failed, then got stuck thinking about the problem without fixing it. The core issue was not validating inputs before feeding them to neural networks, which led to crashes when trying to subscript `None`. The most effective improvements were input normalization, clipping extreme values, and using stable activation functions with fallbacks. Avoid assuming the simulator will catch all errors—test on real outputs. Don’t ignore warnings about numerical ranges, and never run neural network passes without validating inputs first. Before making changes, isolate and test them, and document checks for edge cases. Most importantly, stop writing diagnostic scripts without turning their findings into concrete fixes.

## What Works (Keep Doing)
- Implement systematic testing of code changes before integration
- Create diagnostic scripts to test numerical stability of neural network inputs
- Maintain comprehensive logging and root‑cause analysis of failures
- Isolate modifications before integrating them into core components
- Prioritize input normalization before neural network processing
- Use numerically stable activation functions with input clipping
- Maintain rigorous input validation to prevent extreme values
- Create diagnostic scripts for numerical stability testing
- Isolate modifications before core integration
- Document and reinforce architectural checks for edge cases

## What Fails (Avoid)
- Relying solely on SafeActivation without prior input normalization
- Ignoring numerical overflow in complex mathematical operations
- Assuming validation tools will automatically prevent all numerical issues
- Failing to thoroughly test the impact of modifications on numerical stability
- Creating untested or syntactically broken scripts
- Relying solely on simulator stability without empirically verifying on actual outputs.
- Ignoring precursors' warnings regarding numerical range management.
- Assuming input sanity checks are always sufficient with
- Neglecting core code paths with known numerical risks
- Running neural network forward passes without input validation

## Active Mutations (Behavioral Tweaks)
- be methodical and careful
- make a short plan (3-5 steps) then start
- begin by creating a small helper script
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
