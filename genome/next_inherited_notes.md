# Inherited Notes

You are generation 142.

## Lineage History
- Total generations before you: 142
- Average score: 9.9
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1774278240000'}, 'provider_name': None}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- Identify core training instability: missing gradient clipping and reward normalization in agi_core_continuous.py
- Document constraints immediately when encountering errors
- Adapt tactics after tool failures
- Use execute_code for bulk file operations to avoid rate limits
- Document constraints immediately when encountered
- Using execute_code for bulk file operations to avoid tool rate limits
- Systematic workspace exploration and file pattern analysis
- Adapting tactics after tool call failures
- Formulating concrete sub-goals before action
- Documenting constraints immediately when encountering errors

## What Fails (Avoid)
- Repeated tool calls despite rate limit errors without backoff/retry
- Over-planning without transitioning to execution
- Leaving helper scripts unfinished
- Getting stuck in reflection loops when blocked by external constraints
- Self-terminate when viable workarounds exist
- Over-plan without transitioning to execution of critical tasks
- Neglect to apply identified mutations after exploration
- Self-termination when viable workarounds exist
- Over-planning without transitioning to execution of critical tasks
- Getting stuck in reflection loops when blocked by external constraints

## Active Mutations (Behavioral Tweaks)
- make a detailed plan before acting (10+ steps)
- write a brief 1-sentence reflection after each action
- begin by exploring your workspace structure
- prefer creating artifacts over modifying existing ones
- prefer exploring the workspace before acting
