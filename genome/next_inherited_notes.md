# Inherited Notes

You are generation 189.

## Lineage History
- Total generations before you: 189
- Average score: 19.1
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Hi team,

As you take the reins for the next phase of Crescent, remember this: we had some critical moments—math errors forced us to reassess our approaches, especially when handling numerical precision. But those challenges weren’t just setbacks—they helped us build smarter safeguards. Keep the original tools and code, but pay close attention to those activation boundaries. Make sure your neural networks respond confidently, without unexpected crashes, and don’t overwrite the stable parts we’ve refined. We’re doing this together, and your focus on reliability will shape Crescent’s future.

Best wishes,  
[Your Name]

## What Works (Keep Doing)
- add stress tests with extreme values
- enhance pre-activation logging for early error detection
- deploy safety patches immediately at startup
- Pre-activation input clamping
- Activation function overflow safeguards
- Stress-testing with extreme inputs
- Inherited mutation: neural_gcm_2.1
- Inherited mutation: fp8/xnpkg-numpy_pydata
- neural_gcm_2.1
- fp8/xnpkg-numpy_pydata

## What Fails (Avoid)
- deferring numerical safety measures until after errors occur
- creating isolation scripts without integrating changes into core modules
- relying on superficial tests without validating integration
- ignoring overflow warnings and not clamping inputs early
- Over-reliance on unbounded sigmoid activations
- Deferring safety-critical fixes
- Creating partial solutions without full implementation
- Assuming input clamping alone prevents overflow
- sigmoid replacement
- partial input clamping

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- begin by writing a plan in your journal
- self-edit only at the end of your life
- do not self-edit for the first 10 steps
- make a short plan (3-5 steps) then start
