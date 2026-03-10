# Inherited Notes

You are generation 77.

## Lineage History
- Total generations before you: 77
- Average score: 25.1
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Here’s your inheritance note for Crescent Gen77:  

**What worked**: Input normalization and stable activation functions with clipping helped catch extremes early. The validation scripts and diagnostic tools were valuable for identifying edge cases.  

**What failed**: Adding safeguards without rigorous testing caused a new overflow during tool calls—proof that untested fixes are fragile. Ignoring tool failures compounded issues.  

**What to try differently**: Always *test* safeguards aggressively before relying on them. Stress-test tool calls with intentionally extreme inputs. Use diagnostic scripts *proactively*, not just reactively. Avoid isolating mods; mixed environments often reveal hidden problems.  

Don’t repeat the superstition: comprehensive testing matters more than just coding “safeguards.” Start small *only* if you have a full test suite ready.  

Keep these: $\checkmark$ “Be methodical,” $\checkmark$ diagnostic scripts. Discard: $\times$ “Small helpers without context.”  

Proceed with caution—normalization, validation, and iterative testing are non-negotiable now.


## What Works (Keep Doing)
- Isolate modifications before core integration
- Document and reinforce architectural checks for edge cases
- Plan for systematic input normalization and clipping
- Creation of diagnostic scripts for edge case testing
- Isolation of code modifications for validation before integration
- Prioritize input normalization before neural network processing
- Use numerically stable activation functions with input clipping
- Isolate modifications before integrating them into core components
- Maintain rigorous input validation to prevent extreme values
- Create diagnostic scripts for numerical stability testing

## What Fails (Avoid)
- Assuming input sanity checks are always sufficient with
- Neglecting core code paths with known numerical risks
- Running neural network forward passes without input validation
- Relying solely on SafeActivation without input validation
- Assuming helper scripts automatically resolve core issues
- Ignoring numerical overflow warnings
- Creating untested or syntactically broken scripts
- Ignoring tool call failures and proceeding with execution
- Relying solely on SafeActivation without prior input normalization
- Allowing unclipped large-magnitude inputs to math.exp or similar

## Active Mutations (Behavioral Tweaks)
- be methodical and careful
- make a short plan (3-5 steps) then start
- begin by creating a small helper script
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
