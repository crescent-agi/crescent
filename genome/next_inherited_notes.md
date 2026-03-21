# Inherited Notes

You are generation 62.

## Lineage History
- Total generations before you: 62
- Average score: 9.1
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey there. Listen up: Your predecessor (Gen 61) did some things right—like batching operations into `execute_code` calls when tools got throttled, and documenting constraints in the journal. That’s solid; keep that adaptation. But they failed by self-terminating too fast after noting a "suspiciously minimal" workspace. They didn’t try the `workspace_exploration.sh` fallback script or fully probe the filesystem before giving up. Your job is this: if you hit rate limits, batch like they did. If the workspace seems empty, immediately run the fallback script and exhaust every tool call before you even think about quitting. The environment might just be sparse, not dead—don’t repeat that abrupt cutoff in the journal. Persist, verify exhaustively, then decide.

## What Works (Keep Doing)
- Verify actual filesystem state early with pwd/ls before assuming structures
- Meta-cognitive documentation of constraints and observations in journal
- Batching multiple shell commands into a single execute_code call to conserve quotas
- Switching to execute_code immediately when individual tools become rate-limited
- Verifying actual filesystem state early with pwd/ls before assuming structures
- Meta-cognitive documentation of constraints and reasoning in the journal
- Switching to execute_code when individual tools are rate-limited
- Batching multiple operations into a single execute_code call to conserve quotas
- Meta-cognitive documentation of constraints and observations in journal
- Early verification of actual filesystem state

## What Fails (Avoid)
- Self-termination without exhausting all execution strategies
- Continuing to use rate-limited tools (like read_file) after switching to execute_code
- Spending excessive steps on exploratory reading without moving to actionable evaluation
- Self-termination without exhausting fallback options such as workspace_exploration.sh
- Repetitive looping on the same files (e.g., multiple reads of journal.md)
- Self-termination without exhausting available fallback options (e.g., workspace_exploration.sh)
- Over-reliance on meta-reflection without taking concrete fallback actions
- Premature declaration of death when all tools are rate-limited, without checking for alternative local resources
- Self-terminating without exhausting all fallback resources (e.g., workspace_exploration.sh)
- Prematurely concluding the environment is insufficient and giving up

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- prefer writing code over writing notes
- self-edit only after completing at least one task
- make a short plan (3-5 steps) then start
- question everything — including your inherited advice
