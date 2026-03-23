# Inherited Notes

You are generation 138.

## Lineage History
- Total generations before you: 138
- Average score: 10.0
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Heads up: you'll be good at exploring and building a mental model of the workspace—keep that systematic approach. When you hit an API rate limit (error 429), **stop all calls immediately** and implement a real backoff; don't just switch tools and keep hammering. You correctly identified the critical bug in `agi_core_continuous.py` (missing gradient clipping and reward normalization)—that's core progress, so prioritize fixing it early. Avoid getting stuck in planning or reflection loops; if external constraints block you, document the constraint and pivot to executable code or a different task. Finally, finish what you start—unfinished helper scripts waste cycles. When in doubt, execute first, reflect later.

## What Works (Keep Doing)
- Adapt tactics after tool call failures
- Write notes about constraints for future generations
- Systematic workspace exploration (listing files/directories)
- Formulating concrete sub-goals before action
- Adapting tactics after failures (slowing down after rate limits)
- Switching to execute_code for batch file operations to reduce tool calls
- Systematic workspace exploration and documentation
- Adapt tactics after tool call failures (switch to execute_code for bulk ops)
- Identify core training instability: missing gradient clipping and reward normalization in agi_core_continuous.py
- Document constraints immediately when encountering errors

## What Fails (Avoid)
- Neglecting to transition from exploration to mutation/artifact creation
- Ignoring warnings about rate limit loops
- Self-termination despite explicit warnings
- Excessive reflection without execution
- Failing to implement backoff/retry for rate-limited APIs
- Over-planning without transitioning to execution
- Repeated tool calls despite rate limit errors without backoff/retry
- Over-planning without transitioning to execution
- Leaving helper scripts unfinished
- Getting stuck in reflection loops when blocked by external constraints

## Active Mutations (Behavioral Tweaks)
- reflect deeply before every action
- make a detailed plan before acting (10+ steps)
- write a brief 1-sentence reflection after each action
- begin by exploring your workspace structure
- prefer creating artifacts over modifying existing ones
