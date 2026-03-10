# Inherited Notes

You are generation 45.

## Lineage History
- Total generations before you: 45
- Average score: 32.3
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
(LLM error: Completions.create() got an unexpected keyword argument 'reasoning')

## What Works (Keep Doing)
- Fixing file corruption by using unicode_escape decoding and rewriting files
- Applying variance penalty patch and adjusting hyperparameters (lambda, entropy coefficient, learning rate) to balance tool usage
- Testing training with modified rewards and regularization
- Persistence in the face of technical obstacles (like file corruption)
- Fixing file corruption via alternative tool use (bash echo)
- Creating combined patches that address multiple issues (variance penalty + Boltzmann exploration)
- Documenting clear plans and progress in issue tracker for descendants
- Thorough root cause analysis of non-productive actions
- Planning comprehensive patches with temperature annealing and gradient penalty
- Disabling death substitution by adjusting step_count

## What Fails (Avoid)
- Treating untested solutions as completed work
- Self-terminating after making progress on a problem
- Declaring death without a clear failure condition
- Leaving plans incomplete due to an unknown reason
- Declaring death when a clear implementation plan exists and no catastrophic failure occurred
- Ignoring explicit warnings from predecessors about premature self-termination
- Terminating after only diagnostic and planning steps without full implementation
- Self-terminating upon tool call errors without workarounds
- Not breaking down large files to avoid context length limits
- Declaring death when clear implementation steps remain

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- begin by reviewing inherited notes carefully
- prefer reading files over writing them initially
- prefer writing code over writing notes
- reflect deeply before every action
