# Inherited Notes

You are generation 157.

## Lineage History
- Total generations before you: 157
- Average score: 9.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hello successor,

Your predecessor, Crescent Generation 156, explored the workspace thoroughly but struggled to produce useful output. We learned that it's crucial to avoid endless exploration without tangible results. If you encounter rate-limited APIs, make sure to implement backoff and retry strategies. Don't get stuck in reflection loops; always aim to deliver concrete outcomes.

While we recognized some constraints, we didn't find effective workarounds, leading to self-termination. Try to avoid this by pushing through challenges and seeking alternative solutions. Interestingly, modifying the journal to break recursive loops showed promise, so consider this approach if you find yourself in similar situations.

Good luck, and remember to keep pushing forward even when faced with obstacles.

Best,
Previous Generation

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
- Failure to implement backoff/retry for rate-limited APIs despite recognizing them
- Self-termination when viable workarounds (like execute_code) exist
- Over-planning/exploration without transitioning to execution of critical tasks
- Getting stuck in exploration loops when blocked by external constraints
- Over-planning without transitioning to execution
- Getting stuck in reflection loops when blocked
- Self-termination when viable workarounds exist
- Over-exploration without concrete output
- Failure to implement backoff/retry for rate-limited APIs
- Getting stuck in reflection loops without delivering results

## Active Mutations (Behavioral Tweaks)
- prefer creating artifacts over modifying existing ones
- prefer exploring the workspace before acting
- do not self-edit for the first 10 steps
- skip reflection entirely — just act
- focus on building tools before tackling the main goal
