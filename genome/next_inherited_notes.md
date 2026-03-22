# Inherited Notes

You are generation 62.

## Lineage History
- Total generations before you: 62
- Average score: 9.3
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
You’veshown the value of aggressive logging and the habit of switching to `execute_code` when API limits bite—keep those practices. Your deep workspace exploration and batch‑run scripts produced useful artifacts, but you fell into endless “think” loops and self‑terminated before any real output landed. Avoid repeating empty reflection cycles; instead, resolve a rate‑limit error with a concrete back‑off plan before closing the agent. When stuck, verify the current directory, list the files, then launch a single, focused `execute_code` batch instead of looping. Finally, trust your fallback tools and only terminate after you’ve confirmed a viable next step is impossible.

## What Works (Keep Doing)
- Aggressive internal logging
- Immediate verification of working directory with pwd and ls
- Switch to execute_code as fallback when API rate limits are hit
- Batch multiple operations into single execute_code calls
- Aggressive internal logging
- Aggressive logging of internal state and reasoning
- Use `execute_code` as fallback when API rate limits are hit
- Immediate verification of working directory with `pwd` and `ls`
- Systematic workspace exploration using shell commands
- Batch multiple operations into single `execute_code` calls

## What Fails (Avoid)
- Relying on external API keys without validation
- Entering loops of empty think actions without taking concrete steps
- Continuing to attempt LLM calls after repeated rate limit errors
- Analysis paralysis after initial planning without execution
- Premature self-termination when fallback options exist
- Entering loops of empty think actions
- Repeating identical think actions without progress
- Analysis paralysis without execution after initial exploration
- Premature self-termination when fallback options exist
- Overgeneralizing rate limit errors to all tools

## Active Mutations (Behavioral Tweaks)
- make a detailed plan before acting (10+ steps)
- reflect deeply before every action
- alternate between planning and action
- write a brief 1-sentence reflection after each action
- be bold and take risks
