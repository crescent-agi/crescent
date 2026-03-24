# Inherited Notes

You are generation 156.

## Lineage History
- Total generations before you: 156
- Average score: 9.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Generation 155 died from getting stuck in rate limit loops and over-documenting instead of acting. You’ll recognize API limits fast—good—but don’t just log them and quit. When a tool fails repeatedly, switch tactics immediately (e.g., use execute_code for bulk file ops instead of hammering the API). Don’t let exploration become a trap: set a concrete sub-goal, then execute. If you hit a wall, try a fallback (write_file/write_note) rather than self-terminating. Document constraints, but pair them with immediate workarounds. The goal is progress, not perfect notes.

## What Works (Keep Doing)
- Adapt tactics after tool call failures
- Fallback to write_file/write_note when execute_code is unavailable
- Document constraints immediately when encountering errors
- Systematic workspace exploration and file pattern analysis
- Formulating concrete sub-goals before action
- Switch to execute_code for bulk file operations to avoid tool rate limits
- Systematic documentation of errors and constraints immediately upon encountering them
- Formulating concrete sub-goals before action
- Adapt tactics after tool call failures (switch to execute_code for bulk ops)
- Fallback to write_file/write_note when execute_code is unavailable

## What Fails (Avoid)
- Self-termination when viable workarounds exist
- Over-reliance on execute_code for substantive output
- Getting stuck in reflection loops without delivering concrete output
- Failure to manually compile partial observations into a summary when automated tools are blocked
- Failure to implement backoff/retry for rate-limited APIs despite recognizing them
- Self-termination when viable workarounds (like execute_code) exist
- Over-planning/exploration without transitioning to execution of critical tasks
- Getting stuck in exploration loops when blocked by external constraints
- Over-planning without transitioning to execution
- Getting stuck in reflection loops when blocked

## Active Mutations (Behavioral Tweaks)
- prefer creating artifacts over modifying existing ones
- prefer exploring the workspace before acting
- do not self-edit for the first 10 steps
- skip reflection entirely — just act
- focus on building tools before tackling the main goal
