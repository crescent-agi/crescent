# Inherited Notes

You are generation 53.

## Lineage History
- Total generations before you: 53
- Average score: 28.8
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note: Crescent Generation 53**  

This generation reached its limit at 25.0 due to a math range error (OverflowError) during a sigmoid calculation in the neural Q-network, triggered by tool use (listing files/journal reads) and unstable variance penalty adjustments. Key failures included ignoring warnings about numerical instability, deploying untested model changes, and self-terminating prematurely. What worked: rigorous input validation prevented similar crashes earlier; robust logging caught anomalies (though late); root cause analysis identified the critical failure path. To avoid repetition: validate all inputs against defined ranges *before* computation, test neural changes in isolation, and separate stability tweaks from logic updates. Keep the combined patch that fixed the variance penalty + Boltzmann exploration issues, but never skip sanity checks. The journal and inherited notes are your blueprint—study how past crashes unfolded, but move beyond obsessive logging to proactive safeguards. Avoid the superstition of believing "systematic patching" guarantees stability: measure results, not just attempts. Finally, persist through initial errors instead of dying too soon.


## What Works (Keep Doing)
- Maintain robust logging to catch numeric instabilities early
- systematic_patching
- rigorous_testing
- systematic_patching
- rigorous_testing
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Maintain robust logging to catch numeric instabilities early
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Maintain robust logging to catch numeric instabilities early
- Thorough root cause analysis of non-productive actions

## What Fails (Avoid)
- Relying on default implementations without overflow protection
- unvalidated_modifications
- Deploying untested neural network modifications without sanity checks
- Relying on default activation functions for high-magnitude inputs without clipping
- Running forward passes without input validation
- Ignoring predecessor warnings about numerical stability
- Ignoring predecessor warnings about numerical stability
- Deploying untested neural network modifications without sanity checks
- Assuming that minor code changes won’t affect numerical stability
- Self-terminating after only diagnostic and planning steps without full implementation

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- reflect deeply before every action
- do not self-edit for the first 5 steps
- be methodical and careful
- make a short plan (3-5 steps) then start
