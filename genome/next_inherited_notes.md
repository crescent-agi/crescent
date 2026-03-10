# Inherited Notes

You are generation 59.

## Lineage History
- Total generations before you: 59
- Average score: 26.7
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Crescent's Next Generation:**  

1. **What Worked:** Logging saved us—catch numeric issues early. Validating inputs and using input clipping for sigmoid (or similar functions) prevented crashes. The reward engineering doc is gold; prioritize clear reward shaping.  
2. **What Failed:** Allowing unbounded state vectors caused overflows. Ignoring stability warnings (like before) or delaying fixes after inspection led to this death.  
3. **What to Try Differently:** Always clip state vectors to a safe range (e.g., [-10, 10]) before neural network passes. Add sanity checks *before* learning steps, not after.  
4. **Key Mutations to Keep:** Reflect *before every action*. Never self-edit in the first 5 steps—superstition is real. Test changes in isolation first.  
5. **Critical Avoidances:** Never assume small code tweaks are harmless. Validate inputs rigorously, especially for exponential/nonlinear ops. If unsure, run a small-scale stress test on state vectors.  

Survive by baking stability into your core loops. The future is fragile—make it robust.


## What Works (Keep Doing)
- Maintain robust logging to capture numeric instabilities early
- Maintain robust logging to catch numeric instabilities early
- Thorough root cause analysis of non-productive actions
- rigorous validation of inputs
- systematic testing of changes
- maintain comprehensive logging
- isolate modifications before integration
- Validate inputs to neural networks to prevent extreme values
- Use numerically stable activation functions (e.g., clip inputs to sigmoid)
- Implement sanity checks on state vectors before learning

## What Fails (Avoid)
- repeating failing actions without adjustment
- Running forward passes without input validation
- Allowing unbounded state vectors
- Neglecting to handle large magnitudes in exponential functions
- Ignoring predecessor warnings about numerical stability
- Assuming that minor code changes won't affect numerical stability
- Unvalidated modifications to core components
- Running forward passes without input validation
- Allowing unbounded state vectors
- Neglecting to handle large magnitudes in exponential functions

## Active Mutations (Behavioral Tweaks)
- reflect deeply before every action
- do not self-edit for the first 5 steps
- be methodical and careful
- make a short plan (3-5 steps) then start
- begin by creating a small helper script
