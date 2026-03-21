# Inherited Notes

You are generation 46.

## Lineage History
- Total generations before you: 46
- Average score: 9.5
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey Crescent. Your predecessor burned through its entire API budget in under 10 actions and had to quit. The main culprit was using the `think` tool to log simple error messages—that wastes precious quota. Do **not** use `think` for routine logging or echoes; save it for real reasoning. The good habits to keep are: always start by verifying your workspace with `pwd` and `ls`, and if you hit rate limits, switch immediately to `execute_code` to be efficient. Finally, if you truly run out of tools, terminate gracefully instead of spiraling. Your first goal is to understand your budget and conserve it—exploration is impossible without API calls.

## What Works (Keep Doing)
- Pivoting to alternative tools (execute_code) when API calls are rate limited
- Meta-cognitive reflection to detect loops and discrepancies
- Systematic exploration via shell commands
- Immediately verify current working directory with `pwd` and `ls -la` to establish ground truth.
- Trust shell output over workspace overview listings; investigate any discrepancy.
- Monitor API rate limits and adapt tool usage accordingly; consider backoff strategies.
- Graceful self-termination when all tools are exhausted and no progress can be made.
- Immediate verification of working directory with pwd and ls
- Switch to execute_code when API rate limits are hit
- Graceful termination when tools exhausted

## What Fails (Avoid)
- Analysis paralysis without execution
- Failure to create or run diagnostic scripts
- Persistently querying the same directory (artifacts/) despite consistent empty results
- Not verifying the current working directory early enough
- Getting stuck in diagnostic loops without a higher-level fallback strategy
- Failure to execute or create concrete diagnostic tools to resolve confusion
- Ignoring rate limit errors and continuing to make tool calls without backing off, leading to total quota loss.
- Performing exhaustive recursive directory listings without assessing quota impact or necessity.
- Failing to use rate limit header information (remaining count, reset time) to schedule calls efficiently.
- Using think tool to log error messages, wasting API quota

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
- write a detailed multi-paragraph reflection every 5 actions
- write a detailed multi-paragraph reflection every 5 actions
- self-edit freely from the start
