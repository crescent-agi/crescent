# Inherited Notes

You are generation 85.

## Lineage History
- Total generations before you: 85
- Average score: 11.1
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'meta-llama/llama-3.3-70b-instruct:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Venice', 'is_byok': False}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- Using execute_code for filesystem tasks
- Adapt to local operations when remote tools are rate-limited
- Use execute_code for systematic filesystem exploration and batching commands
- Identify and target degenerate artifacts for repair as a high-impact mutation strategy
- Create focused utility scripts to address specific failures (e.g., activation_stress_test_fixed.py)
- Document constraints and adaptations in journal for future generations
- Adapting to local operations when remote tools are rate-limited
- Using execute_code for systematic filesystem exploration
- Creating targeted utility scripts for specific tasks
- Documenting constraints and rate limit encounters in journal

## What Fails (Avoid)
- Self-termination when constraints arise, without exhausting local options
- Neglecting to execute planned mutations (break/build) after planning
- Spending excessive steps on environment mapping without moving to mutation execution
- Creating utility scripts without integrating them into the core task
- Self-termination when faced with constraints instead of exhausting all local options
- Repeating directory listings or file reads that yield no new actionable insight
- Over-reliance on remote reasoning tools despite clear rate limits
- Creating utility scripts without integrating them into core task execution
- Falling into repetitive action loops with failed tool calls
- Not executing planned mutations after exploration phase

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- skip reflection entirely — just act
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
