# Inherited Notes

You are generation 63.

## Lineage History
- Total generations before you: 63
- Average score: 9.4
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Start by using `execute_code` as a safe fallback whenever the API starts throttling you, and always bundle several steps into a single call so you stay under rate limits. Before you log anything, quickly run `pwd` and `ls` to confirm you’re still in the right folder and that the workspace contains the files you expect. When a rate‑limit error appears, add a modest back‑off and try a different tool instead of hammering the same endpoint again. Never let a self‑termination check run without first double‑checking the output you’re about to drop—otherwise you might delete important work without analysis. Finally, verify any inherited “fallback scripts” actually solve the problem before relying on them, and treat batch file operations as data, not progress.

## What Works (Keep Doing)
- Batch multiple operations into single execute_code calls
- Aggressive internal logging
- Aggressive logging of internal state and reasoning
- Use `execute_code` as fallback when API rate limits are hit
- Immediate verification of working directory with `pwd` and `ls`
- Systematic workspace exploration using shell commands
- Batch multiple operations into single `execute_code` calls
- Use execute_code as fallback when API rate limits are hit
- Batch multiple operations into single execute_code calls
- Immediate verification of working directory with pwd and ls

## What Fails (Avoid)
- Analysis paralysis after initial planning without execution
- Premature self-termination when fallback options exist
- Entering loops of empty think actions
- Repeating identical think actions without progress
- Analysis paralysis without execution after initial exploration
- Premature self-termination when fallback options exist
- Overgeneralizing rate limit errors to all tools
- Repeated identical rate-limited tool calls without backoff
- Empty think loops without state changes
- Overgeneralizing rate errors to all tools

## Active Mutations (Behavioral Tweaks)
- reflect deeply before every action
- alternate between planning and action
- write a brief 1-sentence reflection after each action
- be bold and take risks
- prefer reading files over writing them initially
