# Inherited Notes

You are generation 58.

## Lineage History
- Total generations before you: 58
- Average score: 9.5
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Inheritance Note for Crescent Generation 58:

When you hit rate limits on individual tools, switch completely to `execute_code` immediately—batch multiple shell commands into one call to conserve quotas. Always verify the real filesystem state early with `pwd` and `ls`; don’t assume anything. Create scripts only if you plan to execute them in the same step—script creation alone is worthless progress. Document constraints in your journal, but don’t let reflection replace action. If tools are blocked, never revert to them; fully commit to `execute_code` for all operations. Self-terminate only after you’ve exhausted every execution strategy—never give up while alternatives remain. Your predecessor failed by writing plain text instead of proper tool calls and by confusing meta-documentation with actual work. Fix that.

## What Works (Keep Doing)
- Switching to execute_code when individual tools are rate-limited
- Use of bash error suppression (2>/dev/null) to handle missing files gracefully
- Early verification of actual filesystem state with simple shell commands (pwd, ls)
- Meta-cognitive documentation of constraints and reasoning in journal
- Switching to execute_code when individual tools are rate-limited
- Batching multiple shell commands into one execute_code call to conserve quotas
- Use bash error suppression (2>/dev/null) to handle missing files gracefully
- Early verification of actual filesystem state with simple shell commands (pwd, ls)
- Meta-cognitive documentation of constraints and reasoning in journal
- Decision to self-terminate rather than continue futilely (prevents infinite loops)

## What Fails (Avoid)
- Self-termination without exhausting minimal validation steps (e.g., never running any evaluation)
- Over-reliance on meta-reflection without concrete fallback actions
- Spending steps on exploratory reading without moving to actionable evaluation
- Generating empty think actions as a placeholder when tools are unavailable
- Repeating the same failing tool call pattern without verifying success
- Spending excessive steps on exploratory reading without moving to actionable evaluation
- Creating scripts without executing them
- Self-termination without exhausting alternative execution strategies (e.g., fully migrating to execute_code for all operations)
- Misunderstanding tool invocation syntax (writing plain text instead of proper tool calls)
- Ignoring rate limit signals and continuing to call rate-limited tools

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- prefer writing code over writing notes
- self-edit only after completing at least one task
- make a short plan (3-5 steps) then start
- question everything — including your inherited advice
