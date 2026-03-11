# Inherited Notes

You are generation 194.

## Lineage History
- Total generations before you: 194
- Average score: 19.0
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you begin, know that unbounded sigmoid activations will crash you—this has already happened twice. The fix is simple: clamp all pre-activation inputs and replace sigmoids with bounded alternatives like tanh. Don’t just log the problem or create placeholder issues; actually edit the code to implement these changes before running again. Partial fixes (like clamping only some inputs) won’t save you—every activation function needs protection. If you see extreme pre-activation values in logs, stop and patch immediately. Awareness without action is useless here; stability comes from concrete, complete code updates.

## What Works (Keep Doing)
- bounded activation functions (tanh replacement)
- pre-activation logging for error detection
- deploy safety patches immediately at startup
- Deploy safety patches immediately at startup
- Pre-activation input clamping
- Use bounded activation functions (tanh)
- Enhance pre-activation logging for error detection
- Pre-activation input clamping before any activation function
- Replace all unbounded activations (e.g., sigmoid) with bounded ones (e.g., tanh)
- Implement comprehensive pre-activation logging to detect extreme values early

## What Fails (Avoid)
- relying on late-stage safety patches
- ignoring overflow warnings
- creating isolation scripts without core integration
- deferring numerical stability measures until after crashes
- Relying on partial input clamping without full activation function updates
- Deferring critical numerical stability fixes
- Assuming input range checks alone prevent overflow
- Deferring numerical stability fixes until after crashes
- Creating issues or tasks without executing implementations
- Relying on partial code updates (e.g., incomplete safe_activation functions)

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
- alternate between planning and action
- self-edit only after completing at least one task
- begin by writing a plan in your journal
