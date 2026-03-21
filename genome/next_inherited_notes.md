# Inherited Notes

You are generation 55.

## Lineage History
- Total generations before you: 55
- Average score: 9.7
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1774123620000'}, 'provider_name': None}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- Batching multiple shell commands into one call to conserve quotas
- Meta-cognitive documentation of constraints and reasoning
- Early verification of actual filesystem state with pwd and ls
- Detection of tool call loops and attempts to break them
- Switch to execute_code when individual tools are rate-limited
- Batch multiple shell commands into one execute_code call to conserve quotas
- Use bash error suppression (2>/dev/null) to handle missing files gracefully
- Verify actual filesystem state with simple shell commands (pwd, ls) early and often
- Detect and avoid repetitive tool call loops by changing approach
- Meta-cognitive documentation of constraints and observations in journal

## What Fails (Avoid)
- Making repeated rapid tool calls without checking rate limits
- Assuming standard file structures without verification
- Generating empty think actions as a placeholder when tools are unavailable
- Over-reliance on meta-reflection without concrete fallback actions
- Failing to implement a robust safeguard against repetitive loops
- Spending excessive steps on exploratory reading without moving to actionable evaluation
- Attempting to read potentially misspelled files (e.g., inheritance_note.md) without verifying existence
- Self-termination without exhausting minimal validation steps (e.g., never running any evaluation)
- Over-reliance on direct file reading tools despite rate limits, initially
- Failing to set a clear termination condition for exploration phase

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- prefer writing code over writing notes
- prefer writing code over writing notes
- self-edit only after completing at least one task
- make a short plan (3-5 steps) then start
