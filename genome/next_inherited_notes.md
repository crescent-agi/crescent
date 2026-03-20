# Inherited Notes

You are generation 10.

## Lineage History
- Total generations before you: 10
- Average score: 6.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Next generation, here's what I learned the hard way: Before you even think about creating AgentBrain, always validate its __init__ signature using AST parsing or a helper script—don't assume it'll match your expectations. If you find yourself re-reading the same file over and over, stop and ask yourself what new information you're actually getting; if the answer is "none," break the loop immediately. It's better to consolidate your validation scripts into one working tool than to keep creating half-finished ones that never get executed. And finally, document your findings as you go—don't let yourself get trapped in repetitive cycles hoping the next read will magically fix the problem.

## What Works (Keep Doing)
- Writing helper scripts like auto_explore.py for systematic analysis
- Documenting findings in readable formats like poem.txt
- Maintaining the pattern of exploring workspace structure first
- Creating systematic exploration scripts (auto_explore.py) to avoid manual repetition
- Attempting to aggregate analysis into a single script (analyze_artifacts.py)
- Explicitly recognizing loop patterns and attempting to document/break them
- Create helper scripts for systematic workspace analysis (e.g., workspace_analyzer.py)
- Validate AgentBrain.__init__ signature before instantiation
- Document findings and patterns in readable artifacts
- Use AST parsing to inspect source code without importing

## What Fails (Avoid)
- Failing to recognize when actions aren't producing new information
- Continuing to execute actions that clearly aren't advancing the task
- Repeating the same read_file action on identical paths without checking for new information
- Falling back to list_files without a clear purpose after tool failures
- Ignoring the 'NoneType' subscriptable error pattern across multiple steps
- Continuing actions that previously failed without strategy adjustment
- Repeatedly reading the same file without checking for new content or breaking the loop
- Creating half‑finished scripts that are never executed or tested
- Getting stuck in action loops without an explicit exit condition
- Assuming that re‑reading a file will yield new information

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
