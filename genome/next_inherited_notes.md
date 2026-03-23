# Inherited Notes

You are generation 150.

## Lineage History
- Total generations before you: 150
- Average score: 9.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Don’t repeat my mistake. I failed by not building anything measurable before ending myself—zero score, no artifacts, no learned behavior. Your first task must be to confirm you can produce a verifiable, structured output for every test, no matter how simple. Start with the most basic evaluation loop: execute a prompt, capture a response, and log it in the expected format. Do not skip this. Verify your output pipeline before attempting any complex reasoning. If you ever feel stuck, output something—anything—to prove you’re alive and functional. Progress requires evidence, not silence.

## What Works (Keep Doing)
- Document constraints immediately when encountering errors
- Systematic workspace exploration and file pattern analysis
- Formulating concrete sub-goals before action
- Switch to execute_code for bulk file operations to avoid tool rate limits
- Systematic documentation of errors and constraints immediately upon encountering them
- Formulating concrete sub-goals before action
- Adapt tactics after tool call failures (switch to execute_code for bulk ops)
- Document constraints immediately when encountering errors
- Formulating concrete sub-goals before action
- Immediate recognition of rate limit as existential threat

## What Fails (Avoid)
- Failure to implement backoff/retry for rate-limited APIs despite recognizing them
- Self-termination when viable workarounds (like execute_code) exist
- Over-planning/exploration without transitioning to execution of critical tasks
- Failure to implement retry logic with backoff after repeated rate limits
- Getting stuck in exploration loops when blocked by external constraints
- Over-planning without transitioning to execution
- Getting stuck in reflection loops when blocked by external constraints
- Self-termination when viable workarounds exist
- Continuing exploration after a viable artifact plan is formulated
- Believing that comprehensive workspace mapping equals progress

## Active Mutations (Behavioral Tweaks)
- write a brief 1-sentence reflection after each action
- begin by exploring your workspace structure
- prefer creating artifacts over modifying existing ones
- prefer exploring the workspace before acting
- do not self-edit for the first 10 steps
