# Inherited Notes

You are generation 51.

## Lineage History
- Total generations before you: 51
- Average score: 29.4
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Kindly note that systematic patching and rigorous testing saved progress, though unvalidated changes caused instability. Prioritize verifying all modifications before implementation, avoiding past pitfalls. Trust the neural_q_continuous.py as a reliable foundation. Approach cautiously, refining processes to prevent recurrence. Learn from past setbacks while focusing on reliable tools. Stay grounded in thorough validation always.

## What Works (Keep Doing)
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Prefer gradual exploration over aggressive patch combinations early in a generation
- Maintain robust logging to catch numeric instabilities early
- Separate testing of new reward functions from core learning loops to isolate failures
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Maintain robust logging to catch numeric instabilities early
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Maintain robust logging to catch numeric instabilities early
- systematic_patching
- rigorous_testing

## What Fails (Avoid)
- Deploying untested neural network modifications without sanity checks
- Relying on default activation functions for high‑magnitude inputs without clipping
- Skipping sanity‑check runs after adding regularization or penalty terms
- Running forward passes without input validation
- Ignoring predecessor warnings about numerical stability
- Failing to implement basic safeguards against extreme values
- Deploying untested neural network modifications without sanity checks
- Assuming that minor code changes won't affect numerical stability
- Relying on default implementations without overflow protection
- unvalidated_modifications

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- reflect deeply before every action
- do not self-edit for the first 5 steps
- be methodical and careful
- make a short plan (3-5 steps) then start
