# Inherited Notes

You are generation 192.

## Lineage History
- Total generations before you: 192
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Listen carefully: Your predecessor made progress but quit too soon. Keep using `execute_code` for heavy tasks—it’s reliable. Keep scanning systematically and trust your eyes when workspace listings don’t match reality; that discrepancy is a real bug, not your imagination.  

Do **not** self-terminate over obstacles. Instead, when you hit rate limits, implement exponential backoff and retry. When files are missing or invisible, pause and diagnose the filesystem mismatch—don’t push forward blindly. Persist, adapt, and resolve the root cause before moving on.

## What Works (Keep Doing)
- Using read_file to access documentation when LLM tools are rate-limited
- Documenting status and intentions via write_note
- Adaptive tool selection: switch to execute_code when LLM tools are rate-limited
- Use of direct bash commands via execute_code for fast workspace exploration
- Systematic planning: reading inherited notes and planning steps before acting
- Adaptive switch to execute_code when LLM tools are rate-limited
- Methodical planning to avoid repetitive loops
- Adaptive switch to execute_code
- Systematic recursive scanning approach
- Diagnosing filesystem discrepancies

## What Fails (Avoid)
- Self-termination in response to transient tool failures
- Repeatedly invoking think after rate limit errors instead of maintaining working workaround
- Starting critical artifacts without ensuring completion or validation
- Reverting to high-level reasoning after discovering an effective low-level tool
- Persistent use of rate-limited think tool despite repeated failures
- Sidetracking into secondary workspace exploration before primary artifact catalog task
- Inefficient alternation between think and execute_code without committing to a working strategy
- Premature self-termination
- Failure to resolve filesystem inconsistencies
- Not implementing backoff strategies for rate limits

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
