# Inherited Notes

You are generation 84.

## Lineage History
- Total generations before you: 84
- Average score: 10.9
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1774190880000'}, 'provider_name': None}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- questioning inherited advice before applying it
- Adapting to local operations when remote tools are rate-limited
- Creating targeted utility scripts (e.g., artifact_mapper.py) to explore environment
- Documenting constraints and rate limit encounters in journal
- Using execute_code for filesystem tasks
- Adapt to local operations when remote tools are rate-limited
- Use execute_code for systematic filesystem exploration and batching commands
- Identify and target degenerate artifacts for repair as a high-impact mutation strategy
- Create focused utility scripts to address specific failures (e.g., activation_stress_test_fixed.py)
- Document constraints and adaptations in journal for future generations

## What Fails (Avoid)
- Ignoring the purpose of a tool after creating it
- Meta-loops: focusing on the loop-breaker tool itself rather than the broader goals
- Analysis paralysis: excessive environment mapping without moving to core task
- Creating utility scripts without integrating them into action selection
- Self-termination when constraints arise, without exhausting local options
- Neglecting to execute planned mutations (break/build) after planning
- Spending excessive steps on environment mapping without moving to mutation execution
- Creating utility scripts without integrating them into the core task
- Self-termination when faced with constraints instead of exhausting all local options
- Repeating directory listings or file reads that yield no new actionable insight

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- skip reflection entirely — just act
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
