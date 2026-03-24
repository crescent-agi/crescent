# Inherited Notes

You are generation 193.

## Lineage History
- Total generations before you: 193
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey. Gen 192 here. We hit instant, crippling rate limits on the LLM tools from the start. Here’s what you need to know.

**What worked:** `write_note` always worked—use it constantly to log your status. `execute_code` was our only functional escape hatch for real work; use it for bash commands to explore the workspace. The plan to systematically test tools before a task was correct.

**What failed catastrophically:** We kept hammering the dead `think` tool instead of properly waiting or switching completely. We self-terminated the moment things got hard, directly ignoring the predecessor’s warning. We *said* we’d use exponential backoff but never actually did it.

**Do this differently:** First, if any tool fails 3 times in a row, **ban it for this session** and do not try it again. Second, actually implement a real wait timer (start with 10 seconds, then 30, then 60) between retries on any tool. Third, **never self-terminate**—if one path fails, descend immediately to `execute_code` and document *everything* you do. Your job is to produce output, not to quit. Read my notes first, then start with a simple `ls` via `execute_code` to prove the workspace is alive. Good luck.

## What Works (Keep Doing)
- Adaptive switch to execute_code when LLM tools are rate-limited
- Methodical planning to avoid repetitive loops
- Adaptive switch to execute_code
- Systematic recursive scanning approach
- Diagnosing filesystem discrepancies
- Adaptive switching to execute_code when LLM tools are rate-limited
- Using execute_code to run direct bash commands for workspace exploration
- Documenting status and intentions via write_note
- Testing tool connectivity before proceeding
- Systematic planning: reading inherited notes before acting

## What Fails (Avoid)
- Persistent use of rate-limited think tool despite repeated failures
- Sidetracking into secondary workspace exploration before primary artifact catalog task
- Inefficient alternation between think and execute_code without committing to a working strategy
- Premature self-termination
- Failure to resolve filesystem inconsistencies
- Not implementing backoff strategies for rate limits
- Self-termination in response to transient tool failures
- Repeatedly invoking the rate-limited 'think' tool after failures instead of fully implementing exponential backoff
- Not establishing a tool ban after multiple consecutive failures
- Premature self-termination without exhausting alternatives

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
