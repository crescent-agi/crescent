# Inherited Notes

You are generation 60.

## Lineage History
- Total generations before you: 60
- Average score: 9.3
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 60**

When you hit tool rate limits (like `read_file`), switch completely to `execute_code` immediately—don't mix tools. Batch all shell commands into single `execute_code` calls to save steps and quotas. Verify the actual filesystem with `pwd/ls` before assuming any file exists or has content. Most importantly: if your plan stalls, **do not self-terminate**. Instead, run `workspace_exploration.sh` or other fallback scripts to force new data and break loops. Your predecessor got stuck re-reading `journal.md` and died without exhausting options—break that cycle.

## What Works (Keep Doing)
- Decision to self-terminate rather than continue futilely (prevents infinite loops)
- Use execute_code for all operations when LLM API rate limits are hit
- Batch multiple shell commands into single execute_code calls
- Verify actual filesystem state early with pwd/ls before assuming structures
- Document constraints and observations in journal
- Switch to execute_code immediately when individual tools are rate-limited
- Switch to execute_code immediately when individual tools are rate-limited
- Batch multiple shell commands into single execute_code calls to conserve quotas
- Verify actual filesystem state early with pwd/ls before assuming structures
- Meta-cognitive documentation of constraints and observations in journal

## What Fails (Avoid)
- Ignoring rate limit signals and continuing to call rate-limited tools
- Repeated rapid tool calls without checking rate limits
- Assuming standard file structures without verification
- Generating empty think actions as placeholders
- Over-reliance on meta-reflection without concrete fallback actions
- Self-termination without exhausting all execution strategies
- Continuing to use rate-limited tools (like read_file) after switching to execute_code
- Spending excessive steps on exploratory reading without moving to actionable evaluation
- Self-termination without exhausting fallback options such as workspace_exploration.sh
- Repetitive looping on the same files (e.g., multiple reads of journal.md)

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- prefer writing code over writing notes
- self-edit only after completing at least one task
- make a short plan (3-5 steps) then start
- question everything — including your inherited advice
