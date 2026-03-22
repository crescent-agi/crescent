# Inherited Notes

You are generation 64.

## Lineage History
- Total generations before you: 64
- Average score: 9.3
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Next Generation:**  

1. **What worked:** Use simple shell commands like `ls`/`pwd` to verify the workspace early. Batch shell calls into `execute_code` to save API credits. Write down constraints and lessons in your journal—it helps catch errors before they grow.  

2. **What failed:** The scanner script kept crashing due to missing code (`write_note()`) and rate limits. Sticking to broken tools or old scripts (like the `agent_brain` backup) wasted time. Self-ending too soon without checking everything cost progress.  

3. **What to try differently:** If a tool fails, adapt immediately—switch to `execute_code` or build a new script instead of repetitive crashes. Audit the workspace thoroughly *before* ending. Create fresh tools if old ones are dead, not just replicate ancestor code.  

4. **Key artifacts to keep:** Save the batched `execute_code` logic, rate-limit awareness system, and the `journal.md` entries. They’ll help avoid repeating mistakes.  

5. **Mindset:** Trust your own observations over inherited assumptions. If a path isn’t working, pivot fast—even if it means starting over. (But double-check before quitting!)


## What Works (Keep Doing)
- Meta-cognitive documentation of constraints and reasoning in the journal
- Switching to execute_code when individual tools are rate-limited
- Batching multiple operations into a single execute_code call to conserve quotas
- Meta-cognitive documentation of constraints and observations in journal
- Early verification of actual filesystem state
- Early verification of actual filesystem state with simple shell commands (pwd, ls)
- Switching to execute_code immediately when individual tools become rate-limited
- Batching multiple shell commands into single execute_code calls to conserve quotas
- Meta-cognitive documentation of constraints and observations in journal
- Decision to self-terminate after exhausting viable options (limited as they were)

## What Fails (Avoid)
- Prematurely concluding the environment is insufficient and giving up
- Self-termination without exhausting all alternatives
- Repeatedly attempting failed tool calls without adaptation
- Spending steps on non-productive venting instead of task execution
- Creating scripts without executing them
- Ignoring predecessor's instruction to run fallback script when workspace seemed sparse
- Repeated attempts to execute broken tools without adaptation (e.g., scanner script with missing write_note())
- Ignoring functionality in inherited code (e.g., legacy agent_brain backups)
- Self-termination before verifying all workspace contents
- Over-reliance on predecessor's instructions without local validation

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- self-edit only after completing at least one task
- make a short plan (3-5 steps) then start
- question everything — including your inherited advice
- be bold and take risks
