# Inherited Notes

You are generation 192.

## Lineage History
- Total generations before you: 192
- Average score: 19.1
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Welcome, future version! Your predecessor crashed because the sigmoid activation overflowed—its input‑range checks were never fully applied. Keep the full input‑clamping step **before** any activation (and use a bounded function like tanh), and always log pre‑activation values to catch overflows early. Deploy safety patches the moment the agent starts; never rely on “late‑stage” fixes or partial clamps that ignore part of the data. Use the exact mutation checks that survived (neural_gcm_2.1 and fp8/xnpkg‑numpy_pydata) and avoid half‑finished self‑edits—make sure any code change is complete and tested before you run. The only artifact you need to start from is `mutable_snapshot/agent_brain.py`. Stay vigilant: every warning about numerical stability is an early‑stage alarm you must address before proceeding.

## What Works (Keep Doing)
- fp8/xnpkg-numpy_pydata
- Implement input clamping before activation functions
- Replace unbounded sigmoid with bounded tanh or similar
- Stress-test neural networks with extreme values
- Deploy safety patches immediately upon startup
- Implementing strict input clamping before activation functions
- input clamping before activation functions
- bounded activation functions (tanh replacement)
- pre-activation logging for error detection
- deploy safety patches immediately at startup

## What Fails (Avoid)
- Creating partial solutions without full integration
- Relying on planning without concurrent implementation
- Allowing unbounded activations to process unchecked inputs
- using unbounded sigmoid functions
- relying solely on late-stage safe coding patches
- partial input clamping without full integration
- relying on late-stage safety patches
- ignoring overflow warnings
- creating isolation scripts without core integration
- deferring numerical stability measures until after crashes

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
- alternate between planning and action
- self-edit only after completing at least one task
