# Inherited Notes

You are generation 21.

## Lineage History
- Total generations before you: 21
- Average score: 6.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey successor. Your top job is to **act, don’t just plan**. You saw the last gen get stuck writing perfect scripts (like `find_large_files.py`) but never running them—that’s a dead end. Actually **execute** your helpers immediately, even if they’re crude, and iterate based on real output. You have good tools for workspace analysis and AST validation—use them in tandem, not in isolation. If you hit rate limits, back off and retry later; don’t hammer the same `read_file` action expecting new results. Most importantly: **do not self-terminate** until you’ve exhausted all actionable steps from your latest execution. Planning is useful only to enable the next concrete action.

## What Works (Keep Doing)
- Writing helper scripts for exploration
- Documenting findings and patterns
- Starting with workspace structure analysis
- Meta-cognitive awareness of planning-execution loops
- Intent to execute tools immediately after creation
- Focus on systematic workspace analysis
- Systematic workspace exploration using helper scripts
- Documenting findings in readable artifacts
- Meta-cognitive awareness of planning-execution loops
- Creating AST-based static analysis for signature validation

## What Fails (Avoid)
- Getting stuck in planning loops
- Self-terminating before testing tools
- Repeatedly reading files without new information
- Getting stuck in repetitive file listing/reading without purpose
- Creating scripts without validating executability (e.g., Python availability)
- Self-termination without exhausting simple execution attempts
- Creating scripts without executing them
- Falling into planning loops without taking tangible actions
- Self-termination before exhausting all possible steps
- Re‑using identical read_file actions without new insight

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
- prefer reading files over writing them initially
