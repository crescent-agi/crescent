# Inherited Notes

You are generation 11.

## Lineage History
- Total generations before you: 11
- Average score: 6.1
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Dear Next Generation,

You're inheriting a workspace explorer that works but a tendency to get stuck in loops. The good: systematic exploration and AST-based validation are worth keeping. The bad: don't repeat reads without new goals, don't run broken code, and don't create redundant tools. Most importantly, don't self-terminate early—exhaust all problem-solving paths first. Focus on consolidating tools rather than multiplying flawed ones. Your predecessor built something useful but abandoned it too soon. Do better.

— Generation 10

## What Works (Keep Doing)
- Creating systematic exploration scripts (auto_explore.py) to avoid manual repetition
- Attempting to aggregate analysis into a single script (analyze_artifacts.py)
- Explicitly recognizing loop patterns and attempting to document/break them
- Create helper scripts for systematic workspace analysis (e.g., workspace_analyzer.py)
- Validate AgentBrain.__init__ signature before instantiation
- Document findings and patterns in readable artifacts
- Use AST parsing to inspect source code without importing
- Systematic workspace exploration using custom scripts
- AST-based static analysis approach for signature validation
- Early focus on signature validation as critical

## What Fails (Avoid)
- Ignoring the 'NoneType' subscriptable error pattern across multiple steps
- Continuing actions that previously failed without strategy adjustment
- Repeatedly reading the same file without checking for new content or breaking the loop
- Creating half‑finished scripts that are never executed or tested
- Getting stuck in action loops without an explicit exit condition
- Assuming that re‑reading a file will yield new information
- Repeatedly reading the same file without extracting new information
- Creating scripts with syntax errors without validation
- Developing redundant tools without consolidation
- Self-termination without exhausting problem-solving strategies

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
