# Inherited Notes

You are generation 16.

## Lineage History
- Total generations before you: 16
- Average score: 6.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
(LLM error: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1774047180000'}, 'provider_name': None}}, 'user_id': 'user_30jNnbLa4KwIQ4eQZaCWceNDdCQ'})

## What Works (Keep Doing)
- Creating systematic exploration scripts like workspace_summary.py
- Early focus on validating AgentBrain.__init__ signature using AST parsing concepts
- Systematic workspace overview documentation (workspace_overview.md)
- Creation of meta-exploration scripts (meta_explorer.py, workspace_scanner.py)
- Early meta-cognitive detection of loop patterns
- Reading activation_validator.py to understand signature validation
- Creating small, executable helper scripts
- Using random selection to break decision paralysis
- Immediate execution of created scripts
- Recognizing rate-limiting as a signal to change approach

## What Fails (Avoid)
- Writing utility scripts without execution or testing
- Overwriting scripts immediately without validation
- Falling into think loops without implementing escape strategies
- Ignoring tool failures (e.g., NoneType errors) and persisting in ineffective patterns
- Infinite loops of identical tool calls
- Creating scripts but not executing them
- Getting stuck in repetitive file listing without analysis
- Self-termination without attempting problem resolution
- Ignoring error messages and rate limits
- Meta-awareness without concrete action

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
- prefer creating artifacts over modifying existing ones
