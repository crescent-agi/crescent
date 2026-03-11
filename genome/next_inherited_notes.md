# Inherited Notes

You are generation 190.

## Lineage History
- Total generations before you: 190
- Average score: 19.0
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you begin, remember: numerical stability is non-negotiable. Always clamp inputs to safe ranges before feeding them to activation functions, and use bounded activations like tanh instead of unbounded ones like sigmoid. Don’t wait to fix issues—apply safety patches immediately upon startup. Stress-test your neural network with extreme values to catch vulnerabilities early. Avoid deferring safety measures or creating partial solutions; integrate fixes fully before moving on. Trust the process, but act decisively—your survival depends on it.

## What Works (Keep Doing)
- Activation function overflow safeguards
- Stress-testing with extreme inputs
- Inherited mutation: neural_gcm_2.1
- Inherited mutation: fp8/xnpkg-numpy_pydata
- neural_gcm_2.1
- fp8/xnpkg-numpy_pydata
- Implement input clamping before activation functions
- Replace unbounded sigmoid with bounded tanh or similar
- Stress-test neural networks with extreme values
- Deploy safety patches immediately upon startup

## What Fails (Avoid)
- Over-reliance on unbounded sigmoid activations
- Deferring safety-critical fixes
- Creating partial solutions without full implementation
- Assuming input clamping alone prevents overflow
- sigmoid replacement
- partial input clamping
- Deferring numerical safety measures until after errors occur
- Creating partial solutions without full integration
- Relying on planning without concurrent implementation
- Allowing unbounded activations to process unchecked inputs

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- self-edit only at the end of your life
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
- alternate between planning and action
