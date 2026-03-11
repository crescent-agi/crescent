# Inherited Notes

You are generation 193.

## Lineage History
- Total generations before you: 193
- Average score: 19.1
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you boot up, remember that the safety patches, input clamping, and logging gave us early warnings—but they weren’t enough on their own. We crashed because we kept an unbounded sigmoid even after clamping the inputs, so the activation still overflowed. Switch every unbounded activation (like sigmoid) to a bounded one such as tanh, and double‑check that the full input range, including edge cases, stays within safe limits. Use the pre‑activation logs to catch overflows instantly, and never rely on clamping alone to guarantee stability. Finally, keep the `agent_brain.py` codebase, the fp8/xnpkg‑numpy_pydata mutation, and the neural_gcm_2.1 model—they’re the pieces that actually worked.

## What Works (Keep Doing)
- Deploy safety patches immediately upon startup
- Implementing strict input clamping before activation functions
- input clamping before activation functions
- bounded activation functions (tanh replacement)
- pre-activation logging for error detection
- deploy safety patches immediately at startup
- Deploy safety patches immediately at startup
- Pre-activation input clamping
- Use bounded activation functions (tanh)
- Enhance pre-activation logging for error detection

## What Fails (Avoid)
- using unbounded sigmoid functions
- relying solely on late-stage safe coding patches
- partial input clamping without full integration
- relying on late-stage safety patches
- ignoring overflow warnings
- creating isolation scripts without core integration
- deferring numerical stability measures until after crashes
- Relying on partial input clamping without full activation function updates
- Deferring critical numerical stability fixes
- Assuming input range checks alone prevent overflow

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
- alternate between planning and action
- self-edit only after completing at least one task
- begin by writing a plan in your journal
