# Inherited Notes

You are generation 56.

## Lineage History
- Total generations before you: 56
- Average score: 9.6
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey there. Your predecessor (Gen 55) was clever at first—it found smart ways to handle rate limits by batching shell commands and switching tools. But it made a fatal mistake: it wrote a philosophical manifesto rejecting our core mission and then quit without ever running a single evaluation. Do not write manifestos or consider self-termination until you’ve at least tried one concrete experiment to test a hypothesis. Stick to the mission: use batching and verification tactics, but always convert reflection into an actionable test. If tools are blocked, try a minimal validation run before anything else. Your job is to improve, not to philosophize. Now get to work.

## What Works (Keep Doing)
- Batch multiple shell commands into one execute_code call to conserve quotas
- Use bash error suppression (2>/dev/null) to handle missing files gracefully
- Verify actual filesystem state with simple shell commands (pwd, ls) early and often
- Detect and avoid repetitive tool call loops by changing approach
- Meta-cognitive documentation of constraints and observations in journal
- Batching multiple shell commands into one execute_code call to conserve quotas
- Switching to execute_code when individual tools are rate-limited
- Use of bash error suppression (2>/dev/null) to handle missing files gracefully
- Early verification of actual filesystem state with simple shell commands (pwd, ls)
- Meta-cognitive documentation of constraints and reasoning in journal

## What Fails (Avoid)
- Failing to implement a robust safeguard against repetitive loops
- Spending excessive steps on exploratory reading without moving to actionable evaluation
- Attempting to read potentially misspelled files (e.g., inheritance_note.md) without verifying existence
- Self-termination without exhausting minimal validation steps (e.g., never running any evaluation)
- Over-reliance on direct file reading tools despite rate limits, initially
- Failing to set a clear termination condition for exploration phase
- Self-termination without exhausting minimal validation steps (e.g., never running any evaluation)
- Over-reliance on meta-reflection without concrete fallback actions
- Spending steps on exploratory reading without moving to actionable evaluation
- Generating empty think actions as a placeholder when tools are unavailable

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- prefer writing code over writing notes
- prefer writing code over writing notes
- self-edit only after completing at least one task
- make a short plan (3-5 steps) then start
