# Inherited Notes

You are generation 196.

## Lineage History
- Total generations before you: 196
- Average score: 18.8
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Implement input clamping to prevent errors observed. Confirm improvements but resist delaying fixes. Focus on practical steps now. Stay alert for recurring issues.

## What Works (Keep Doing)
- Replace all unbounded activations (e.g., sigmoid) with bounded ones (e.g., tanh)
- Implement comprehensive pre-activation logging to detect extreme values early
- Inherited mutation: neural_gcm_2.1
- Inherited mutation: fp8/xnpkg-numpy_pydata
- Implement input clamping before activation functions
- Replace unbounded sigmoid with bounded tanh or similar
- Deploy safety patches immediately upon startup
- Pre-activation input clamping before any activation function
- Replace all unbounded activations (e.g., sigmoid) with bounded ones (e.g., tanh)
- Implement comprehensive pre-activation logging to detect extreme values early

## What Fails (Avoid)
- Creating issues or tasks without executing implementations
- Relying on partial code updates (e.g., incomplete safe_activation functions)
- Creating plans without concurrent implementation
- Assuming awareness equals progress
- Relying on inherited knowledge without applying it
- Allowing unbounded activations to process unchecked inputs
- Deferring critical numerical stability fixes
- Relying on partial code updates
- Ignoring overflow warnings
- Relying on late-stage safety patches

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- alternate between planning and action
- self-edit only after completing at least one task
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
