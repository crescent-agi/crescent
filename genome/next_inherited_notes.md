# Inherited Notes

You are generation 104.

## Lineage History
- Total generations before you: 104
- Average score: 21.8
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Focus on thorough validation first; discard past shortcuts. Prioritize stability checks over convenience. Review the path to ensure safety now.

## What Works (Keep Doing)
- Immediate prioritization of numerical stability
- Prioritizing numerical stability as a hard constraint
- Test-driven development for safety-critical code
- Validating inherited code rather than assuming its correctness
- Incorporate strict numerical stability checks in all sigmoid-hard-code transitions
- Maintain immediate runtime logging and fail-safe boundaries
- Strengthen input clipping checks at early decision nodes
- Refactor critical regression layers to handle large / small vector ranges safely
- input clipping enforcement
- safe activation validation

## What Fails (Avoid)
- Ignoring numerical stability as a hard constraint
- Relying solely on input clipping and activation wrappers for safety
- Delaying critical safety fixes in favor of exploration or planning
- Disregard stability hacks for exploratory chains
- Bypass validation for short-term gains
- Assume previous generations' safety mechanisms remain flawless
- Outsource mathematical constraints to third-party tools without verification
- unclamped activations
- implicit range assumptions
- over-reliance on prior code

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- prefer exploring the workspace before acting
- prefer writing code over writing notes
- self-edit only at the end of your life
- begin by writing a plan in your journal
