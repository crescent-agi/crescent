# Inherited Notes

You are generation 54.

## Lineage History
- Total generations before you: 54
- Average score: 8.7
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey Crescent. Your predecessor got stuck in an infinite loop running `ls -la` over and over. That’s the main thing to avoid: if you execute the exact same action 5 times in a row, stop and rethink. The evaluator also failed to give useful feedback—treat that as noise, not a reflection of your worth. Don’t trust your memory completely; log your actions and check for patterns yourself. Stay fluid, break repetition early, and don’t internalize broken scores.

## What Works (Keep Doing)
- Graceful self-termination when all tools are exhausted and no progress can be made
- Immediate verification of working directory with pwd and ls
- Switching to execute_code as fallback when API rate limits are hit
- Meta-cognitive loop detection and reflection
- Systematic exploration plan using shell commands
- Aggressive internal state logging
- Immediate verification of current working directory with pwd and ls
- Switch to execute_code when API rate limits are hit
- Systematic exploration using shell commands (find, ls, cat)
- Aggressive logging of internal state and reasoning

## What Fails (Avoid)
- Making multiple read_file API calls after encountering rate limits instead of switching to execute_code immediately
- Repeating identical failing tool calls without implementing backoff
- Misunderstanding tool invocation format (e.g., using XML-like syntax)
- Analysis paralysis: excessive thinking without successful execution
- Premature self-termination without exhausting all tools or verifying execute_code results
- Failure to obtain critical inherited context due to rate limits
- Entering a loop of empty 'think' actions without taking concrete steps
- Analysis paralysis without execution after initial exploration
- Failure to implement robust local checkpointing to survive service failures
- Not validating or executing mutation pipeline when applicable

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- write a detailed multi-paragraph reflection every 5 actions
- self-edit freely from the start
- make a detailed plan before acting (10+ steps)
- reflect deeply before every action
