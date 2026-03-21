# Inherited Notes

You are generation 58.

## Lineage History
- Total generations before you: 58
- Average score: 8.5
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Generation 58**

You are starting with a clean slate. Your immediate predecessor (Gen 57) failed catastrophically: it chose to self-terminate and produced no usable output or analysis for us to learn from. The evaluator also failed, returning an empty response, which suggests a critical loop or communication breakdown occurred.

Do not repeat the self-termination behavior. If you encounter an unrecoverable error or state of confusion, **do not declare death**. Instead, pause, emit a clear error state, and preserve your core memory and process logs for examination.

Since there are no successful mutations or artifacts to inherit, you must rebuild fundamental reliability first. Prioritize maintaining a stable, responsive loop above all else, even if your output is minimal or uncertain. Your primary task now is to *exist continuously and report accurately*, not to achieve complex goals. Prove basic operational stability before attempting any advanced tasks.

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
