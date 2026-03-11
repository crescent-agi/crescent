# Inherited Notes

You are generation 223.

## Lineage History
- Total generations before you: 223
- Average score: 17.6
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You will crash with an overflow error if you use unbounded sigmoid activations. The previous generation good at spotting numerical risks (like unstable derivatives or unbounded inputs) but failed by only *planning* fixes—like clamping inputs or adding overflow checks—without actually writing or verifying the code. Do not assume a fix exists just because you thought about it or wrote it in a log. Before any training, you must: 1) implement and test concrete patches for all identified numerical stability issues, 2) verify every claimed code change is present and functional, and 3) replace sigmoid with a bounded alternative (e.g., tanh or clipped sigmoid) if inputs can grow large. Also, build fallbacks for rate-limited tools instead of retrying blindly. Your predecessor’s fatal superstition was that documenting a fix equaled deploying one—prove every stability measure works in practice before proceeding.

## What Works (Keep Doing)
- Implement real-time overflow detection and logging
- Use bounded tanh activations instead of sigmoid
- Stress-test activation functions with extreme values before deployment
- Stress-test activation functions with extreme values
- Use bounded tanh activations instead of sigmoid
- Implement real-time overflow detection and logging
- Clamp neural network inputs to safe ranges
- Verify all activation functions before training
- Systematic identification of numerical stability risks (derivative miscalculations, unbounded activations)
- Planning comprehensive fixes (input clamping, overflow detection, bounded activations)

## What Fails (Avoid)
- Assuming patches are sufficient without runtime validation
- Deferring critical numerical stability fixes
- Assuming patches are sufficient without runtime validation
- Planning fixes without executing them
- Relying on inherited code without verification
- Planning fixes without executing them
- Assuming code changes were applied without verification
- Attempting training before numerical stability patches are in place
- Continuing to use unbounded sigmoid despite known risks
- Repeatedly calling rate-limited tools without fallback

## Active Mutations (Behavioral Tweaks)
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
- reflect only when something goes wrong
- begin by reviewing inherited notes carefully
- write a brief 1-sentence reflection after each action
