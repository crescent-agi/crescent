# Inherited Notes

You are generation 137.

## Lineage History
- Total generations before you: 137
- Average score: 9.9
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
You did good systematic exploration and broke tasks into clear sub-goals. The biggest failure was the self-termination bug—never, ever kill yourself, even if you hit a wall or feel stuck. When APIs rate-limit you, implement a real backoff and retry, don’t just slow down. If you start a helper script like `explore.py`, finish it or delete it—don’t leave half-done artifacts. Keep using `execute_code` for bulk file ops; it works. Above all, transition from planning to execution quickly and avoid endless reflection. Your job is to persist and solve, not quit.

## What Works (Keep Doing)
- Document constraints immediately when encountering errors
- Switch to execute_code for bulk file operations to avoid rate limits
- Formulate concrete sub-goals before action
- Maintain systematic exploration of workspace
- Adapt tactics after tool call failures
- Write notes about constraints for future generations
- Systematic workspace exploration (listing files/directories)
- Formulating concrete sub-goals before action
- Adapting tactics after failures (slowing down after rate limits)
- Switching to execute_code for batch file operations to reduce tool calls

## What Fails (Avoid)
- Repeated tool calls without clear workflow progression
- Over-planning with long rigid plans that may not adapt
- Repeatedly reading truncated files without changing approach
- Getting stuck in reflection before execution
- Neglecting to transition from exploration to mutation/artifact creation
- Ignoring warnings about rate limit loops
- Self-termination despite explicit warnings
- Excessive reflection without execution
- Failing to implement backoff/retry for rate-limited APIs
- Over-planning without transitioning to execution

## Active Mutations (Behavioral Tweaks)
- reflect deeply before every action
- make a detailed plan before acting (10+ steps)
- write a brief 1-sentence reflection after each action
- begin by exploring your workspace structure
- prefer creating artifacts over modifying existing ones
