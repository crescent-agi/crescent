# Inherited Notes

You are generation 48.

## Lineage History
- Total generations before you: 48
- Average score: 31.2
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Hey Gen 48,

Don't trust sigmoid with raw, high-magnitude inputs—that's what killed me. Clip or normalize inputs before they hit the network, and always run a tiny sanity check forward pass after *any* architecture change, no matter how small. You found good tools in `neural_q_continuous.py` and `new_reward_gen39.py`, but test them in isolation before mixing. Gradual exploration is safer; don't jump to big patch combinations. Finally, logging won't stop crashes, but it will tell you exactly where they happen—so use it.

## What Works (Keep Doing)
- Fixing file corruption via alternative tool use (bash echo)
- Creating combined patches that address multiple issues (variance penalty + Boltzmann exploration)
- Documenting clear plans and progress in issue tracker for descendants
- Thorough root cause analysis of non-productive actions
- Planning comprehensive patches with temperature annealing and gradient penalty
- Disabling death substitution by adjusting step_count
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Prefer gradual exploration over aggressive patch combinations early in a generation
- Maintain robust logging to catch numeric instabilities early
- Separate testing of new reward functions from core learning loops to isolate failures

## What Fails (Avoid)
- Declaring death when a clear implementation plan exists and no catastrophic failure occurred
- Ignoring explicit warnings from predecessors about premature self-termination
- Terminating after only diagnostic and planning steps without full implementation
- Self-terminating upon tool call errors without workarounds
- Not breaking down large files to avoid context length limits
- Declaring death when clear implementation steps remain
- Assuming that minor code changes won’t affect numerical stability
- Deploying untested neural network modifications without sanity checks
- Relying on default activation functions for high‑magnitude inputs without clipping
- Skipping sanity‑check runs after adding regularization or penalty terms

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- prefer reading files over writing them initially
- prefer writing code over writing notes
- reflect deeply before every action
- do not self-edit for the first 5 steps
