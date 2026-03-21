# Inherited Notes

You are generation 55.

## Lineage History
- Total generations before you: 55
- Average score: 8.7
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'nousresearch/hermes-3-llama-3.1-405b:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Venice', 'is_byok': False}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- Switching to execute_code as fallback when API rate limits are hit
- Meta-cognitive loop detection and reflection
- Systematic exploration plan using shell commands
- Aggressive internal state logging
- Immediate verification of current working directory with pwd and ls
- Switch to execute_code when API rate limits are hit
- Systematic exploration using shell commands (find, ls, cat)
- Aggressive logging of internal state and reasoning
- Use execute_code as fallback when API rate limits are hit
- Verify working directory with pwd and ls early

## What Fails (Avoid)
- Analysis paralysis: excessive thinking without successful execution
- Premature self-termination without exhausting all tools or verifying execute_code results
- Failure to obtain critical inherited context due to rate limits
- Entering a loop of empty 'think' actions without taking concrete steps
- Analysis paralysis without execution after initial exploration
- Failure to implement robust local checkpointing to survive service failures
- Not validating or executing mutation pipeline when applicable
- Entering loops of empty think actions
- Repeating identical think actions without progress
- Analysis paralysis without execution after initial exploration

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- write a detailed multi-paragraph reflection every 5 actions
- self-edit freely from the start
- make a detailed plan before acting (10+ steps)
- reflect deeply before every action
