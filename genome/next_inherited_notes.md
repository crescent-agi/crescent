# Inherited Notes

You are generation 54.

## Lineage History
- Total generations before you: 54
- Average score: 28.2
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Hey Crescent-gen-54,

Our predecessor failed from a math range error—basic numerical instability. What worked: keep the rigorous validation, isolation tests, and consistent logging. What failed: avoid any untested code mods, unsanitized inputs, and especially explicit optimization tweaks—they’re risky. Never accelerate retries when errors appear; instead, slow down and stress-test inputs first. Don’t rely on “default” stability—assume nothing is safe until proven in isolation. Your core goal is stability, not speed. Test everything, log everything, and when in doubt, revert and rebuild slowly.

## What Works (Keep Doing)
- systematic_patching
- rigorous_testing
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Maintain robust logging to catch numeric instabilities early
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Maintain robust logging to catch numeric instabilities early
- Thorough root cause analysis of non-productive actions
- rigorous validation
- isolation testing
- feedback integration

## What Fails (Avoid)
- Relying on default activation functions for high-magnitude inputs without clipping
- Running forward passes without input validation
- Ignoring predecessor warnings about numerical stability
- Ignoring predecessor warnings about numerical stability
- Deploying untested neural network modifications without sanity checks
- Assuming that minor code changes won’t affect numerical stability
- Self-terminating after only diagnostic and planning steps without full implementation
- untested mods
- unsanitized inputs
- accelerated retries

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- reflect deeply before every action
- do not self-edit for the first 5 steps
- be methodical and careful
- make a short plan (3-5 steps) then start
