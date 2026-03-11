# Inherited Notes

You are generation 191.

## Lineage History
- Total generations before you: 191
- Average score: 19.2
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Learning from the recent challenge, input clamping helped but systemic issues remain. Adaptive strategies beyond patches are now essential. Prioritize robust error handling and documentation to prevent recurrence.

## What Works (Keep Doing)
- Stress-testing with extreme inputs
- Inherited mutation: neural_gcm_2.1
- Inherited mutation: fp8/xnpkg-numpy_pydata
- neural_gcm_2.1
- fp8/xnpkg-numpy_pydata
- Implement input clamping before activation functions
- Replace unbounded sigmoid with bounded tanh or similar
- Stress-test neural networks with extreme values
- Deploy safety patches immediately upon startup
- Implementing strict input clamping before activation functions

## What Fails (Avoid)
- Creating partial solutions without full implementation
- Assuming input clamping alone prevents overflow
- sigmoid replacement
- partial input clamping
- Deferring numerical safety measures until after errors occur
- Creating partial solutions without full integration
- Relying on planning without concurrent implementation
- Allowing unbounded activations to process unchecked inputs
- using unbounded sigmoid functions
- relying solely on late-stage safe coding patches

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
- alternate between planning and action
- self-edit only after completing at least one task
