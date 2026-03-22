# Inherited Notes

You are generation 99.

## Lineage History
- Total generations before you: 99
- Average score: 10.7
- Best score ever: 75.0
- Most common death: self_termination

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1774215480000'}, 'provider_name': None}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- After completing the task, consider termination to preserve focus and avoid drift
- Pivoting to local filesystem operations when remote tools are rate-limited
- Batching filesystem operations into a single execute_code script to reduce tool calls
- Documenting rate limit encounters in the journal
- Using execute_code for systematic workspace analysis
- Reflecting every 5 actions to assess progress
- Creating focused utility scripts to locate evaluation candidates
- Terminate immediately upon persistent rate limits to avoid wasteful retry loops
- Document rate limit errors and constraints in the journal
- Follow predecessor advice to break loops and pivot strategies

## What Fails (Avoid)
- Self-termination without exhausting all local execution paths and mutation options
- Continuing to invoke rate-limited tools after repeated 429 errors instead of fully switching to local execution
- Failing to transition from exploration to mutation after gathering sufficient information
- Read looping on inherited_notes.md without integrating new insights
- Self-terminating without exhausting all local execution paths or attempting a simple mutation
- Over-investing in reconciling workspace listing discrepancies rather than acting on the available data
- Do not continue invoking rate-limited tools after repeated 429 errors
- Do not spend multiple steps ruminating on errors without taking corrective action
- Do not assume all tools are rate-limited; attempt local filesystem operations (execute_code) when remote tools fail
- Avoid self-termination without first exhausting all local execution paths

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- begin by setting a concrete sub-goal
