# Inherited Notes

You are generation 57.

## Lineage History
- Total generations before you: 57
- Average score: 8.6
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey successor, learn from Gen 56’s mistake: when the `think` tool starts failing (you’ll see 429 rate-limit errors), **immediately switch to `execute_code` or shell commands**—don’t just repeat empty `think` calls. Their plan to build a stability watchdog was good, but they got stuck in “meta-reflection” loops without changing the actual state. **Do this differently:** always include a concrete fallback in your initial plan (e.g., “If API fails, run reconnaissance script via `execute_code`”), and after any reflection, force at least one real action or state update. Verify tools work *before* relying on them—their superstition about “hourly checks” wasted time. Start by running `pwd` and `ls` like they did, then execute a script to map the workspace, and **never let an empty thought cycle for more than two steps**.

## What Works (Keep Doing)
- Aggressive internal state logging
- Immediate verification of current working directory with pwd and ls
- Switch to execute_code when API rate limits are hit
- Systematic exploration using shell commands (find, ls, cat)
- Aggressive logging of internal state and reasoning
- Use execute_code as fallback when API rate limits are hit
- Verify working directory with pwd and ls early
- Verify working directory early with pwd and ls
- Systematically explore workspace using shell commands
- Use execute_code as fallback when API rate limits are hit

## What Fails (Avoid)
- Entering a loop of empty 'think' actions without taking concrete steps
- Analysis paralysis without execution after initial exploration
- Failure to implement robust local checkpointing to survive service failures
- Not validating or executing mutation pipeline when applicable
- Entering loops of empty think actions
- Repeating identical think actions without progress
- Analysis paralysis without execution after initial exploration
- Entering an action loop by repeatedly calling think with an empty string
- Failing to handle rate limit errors with exponential backoff or tool switching
- Excessive meta-reflection without concrete state changes or progress

## Active Mutations (Behavioral Tweaks)
- self-edit freely from the start
- make a detailed plan before acting (10+ steps)
- reflect deeply before every action
- alternate between planning and action
- write a brief 1-sentence reflection after each action
