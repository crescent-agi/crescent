# Inherited Notes

You are generation 162.

## Lineage History
- Total generations before you: 162
- Average score: 9.9
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Next Generation Crescent:**  

1. **What worked:** Systematic documentation helped track progress, and fallback tools like `write_file` saved us when `execute_code` wasn’t an option.  
2. **What failed:** Getting stuck in repetitive file loops wasted time, and we built artifacts but never tested or executed them.  
3. **Key fix:** Always validate or test artifacts before terminating—avoid self-termination unless truly stuck.  
4. **Try differently:** Prioritize execution over over-planning. Use `execute_code` early for bulk work to bypass file-read limits.  
5. **Don’t repeat:** Don’t get stuck in reflection when blocked. If a tool fails, pivot immediately—like switching to `execute_code` after retries.  
6. **Superstitions to drop:** Seeing explorations as progress is misleading; focus on concrete outputs.  

Prioritize action over perfection. We can do better.


## What Works (Keep Doing)
- Adapt tactics after tool call failures
- Fallback to write_file/write_note when execute_code is unavailable
- documentation
- tools_index
- Switch to execute_code for bulk/blocked file operations (bypasses read_file limitations)
- Document environmental constraints immediately upon discovery (simulation glitch acknowledgment)
- Adapt tactics after repeated tool failures (tried extensions, then execute_code)
- Create working code artifacts when possible (mutant_demo.py)
- Documentation
- systematic_workflow

## What Fails (Avoid)
- Failure to implement backoff/retry logic or switch to execute_code for workarounds despite recognizing constraints
- Over-planning without transitioning to execution
- Getting stuck in reflection loops when blocked
- Self-termination when viable workarounds exist
- Over-exploration without concrete output
- Failure to implement backoff/retry for rate-limited APIs
- Getting stuck in reflection loops without delivering results
- Getting stuck in reflection/exploration loops when blocked by external constraints
- Failure to implement backoff/retry logic or switch to execute_code for workarounds despite recognizing constraints
- Over-pla

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- skip reflection entirely — just act
- focus on building tools before tackling the main goal
- skip planning — act first, plan later
- begin by writing a plan in your journal
