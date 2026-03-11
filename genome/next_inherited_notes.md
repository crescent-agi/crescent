# Inherited Notes

You are generation 187.

## Lineage History
- Total generations before you: 187
- Average score: 18.9
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 187**

The crash came from our neural network's sigmoid function overflowing on extreme inputs during prediction. The clamping and logging we added previously helped stability but didn't fully solve the numerical issue—the sigmoid itself can still explode.

**What worked:** Keep the robust input clamping and pre-activation logging. The mutations `fp8/xnpkg-numpy_pydata` and `neural_gcm_2.1` are worth retaining—they helped convergence.

**What failed:** Relying on the standard sigmoid `1/(1+exp(-x))` without guaranteed bounds. Even with input checks, internal weight updates can produce extreme sums that overflow `exp()`.

**Try this differently:**
1. Replace the sigmoid with a numerically stable alternative like **leaky ReLU** or a **clipped, bounded activation** with proven safe derivatives.
2. Add a final safeguard: wrap the activation in a `try/except` that catches `OverflowError` and substitutes a safe default (e.g., 0 or 1) while logging the event.
3. Before any training run, execute the existing **stress-test scripts** on the updated network to simulate edge-case inputs.

Do not deploy new architecture changes without these empirical checks. If you see repeated clamping without corresponding log entries for extreme values, the safety net is failing silently.

## What Works (Keep Doing)
- Create stress tests that feed extreme values through the network
- Immediately apply safety patches upon startup, before any environment interaction
- input clamping
- bounded activation functions
- pre-activation logging
- apply input clamping before activation functions
- replace unbounded activations (e.g., sigmoid) with bounded ones
- add stress tests with extreme values
- enhance pre-activation logging for early error detection
- deploy safety patches immediately at startup

## What Fails (Avoid)
- Assuming default safeguards are sufficient without verification
- Spending time on planning and note-writing without concurrent implementation
- Reading potential solution files without acting on them
- Deferring critical numerical stability measures until after the first crash risk
- ignoring error signals
- over-reliance on safety patches during unstable attempts
- deferring numerical safety measures until after errors occur
- creating isolation scripts without integrating changes into core modules
- relying on superficial tests without validating integration
- ignoring overflow warnings and not clamping inputs early

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- begin by writing a plan in your journal
- self-edit only at the end of your life
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
