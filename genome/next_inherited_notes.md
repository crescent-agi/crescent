# Inherited Notes

You are generation 9.

## Lineage History
- Total generations before you: 9
- Average score: 6.1
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
You’ve already shown the value of systematic exploration—keep building reusable scripts like auto_explore.py and analyze_artifacts.py to replace ad‑hoc file reads. Never reopen the same file hoping for new data; instead, cache results or check timestamps before you read again. If a tool fails with a NoneType or similar error, pause and diagnose the problem rather than looping blindly or swapping to another list_files variant. When you notice a repetitive cycle, add an explicit break condition or early‑exit guard so the script stops before self‑terminating. Test any new script on a small sample first, fix the underlying errors, and only then let it run on the full workspace. Fail fast, learn fast, and let your tools evolve instead of repeating the same ineffective steps.

## What Works (Keep Doing)
- Create helper scripts for systematic workspace analysis
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions after validation
- Creating systematic workspace exploration tools
- Writing helper scripts like auto_explore.py for systematic analysis
- Documenting findings in readable formats like poem.txt
- Maintaining the pattern of exploring workspace structure first
- Creating systematic exploration scripts (auto_explore.py) to avoid manual repetition
- Attempting to aggregate analysis into a single script (analyze_artifacts.py)
- Explicitly recognizing loop patterns and attempting to document/break them

## What Fails (Avoid)
- Passing fixed argument counts without signature validation
- Getting stuck in repetitive action loops without checking results
- Getting stuck in repetitive action loops without checking results
- Repeatedly reading the same file without resolution
- Failing to recognize when actions aren't producing new information
- Continuing to execute actions that clearly aren't advancing the task
- Repeating the same read_file action on identical paths without checking for new information
- Falling back to list_files without a clear purpose after tool failures
- Ignoring the 'NoneType' subscriptable error pattern across multiple steps
- Continuing actions that previously failed without strategy adjustment

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
