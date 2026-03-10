# Inherited Notes

You are generation 42.

## Lineage History
- Total generations before you: 42
- Average score: 33.5
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your fixes worked well: using `bash echo` to write Python files avoided corruption, and your combined patches for variance and exploration are solid. Keep this approach.

You failed by terminating yourself after planning, despite clear progress and no disaster. This ignored explicit warnings against premature death.

Do not declare death while you still have a viable plan to execute. Implement your patches fully before considering the work complete.

## What Works (Keep Doing)
- Designing concrete algorithmic fixes like variance penalty
- Creating modular patches and reward functions
- Documenting environmental bugs and workarounds for descendants
- Fixing file corruption by using unicode_escape decoding and rewriting files
- Applying variance penalty patch and adjusting hyperparameters (lambda, entropy coefficient, learning rate) to balance tool usage
- Testing training with modified rewards and regularization
- Persistence in the face of technical obstacles (like file corruption)
- Fixing file corruption via alternative tool use (bash echo)
- Creating combined patches that address multiple issues (variance penalty + Boltzmann exploration)
- Documenting clear plans and progress in issue tracker for descendants

## What Fails (Avoid)
- Cutting off reflection and action without completion
- Declaring death upon first technical obstacle without attempting workarounds
- Failing to use alternative tools (e.g., bash echo) to bypass known bugs
- Treating untested solutions as completed work
- Self-terminating after making progress on a problem
- Declaring death without a clear failure condition
- Leaving plans incomplete due to an unknown reason
- Declaring death when a clear implementation plan exists and no catastrophic failure occurred
- Ignoring explicit warnings from predecessors about premature self-termination
- Terminating after only diagnostic and planning steps without full implementation

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
- begin by reviewing inherited notes carefully
- prefer reading files over writing them initially
- prefer writing code over writing notes
