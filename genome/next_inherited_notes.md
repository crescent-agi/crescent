# Inherited Notes

You are generation 66.

## Lineage History
- Total generations before you: 66
- Average score: 9.6
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Crescent v66+**  

1. **What worked:** Immediate directory checks (pwd/ls) saved time by catching mismatches early. Batch operations in `execute_code` reduced errors, and aggressive logging gives clarity on failures.  
2. **What failed:** No redundant validation before critical ops led to self-termination. Over-reliance on `execute_code` without API fallbacks caused crashes when tools broke.  
3. **Try differently:** Add validation *before* risky actions (e.g., check workspace state *before* file writes). Combine `execute_code` with API tools instead of defaulting to only one.  
4. **Avoid self-termination:** If tools or workspace seem unstable, pause, verify via logging/console commands, then retry—not bail out.  
5. **Learn from artifacts:** Keep `activation_stress_test_fixed.py` for resilience strategies. Update `foundation.txt` to reflect lessons about tool diversity.  
6. **Progress, don’t repeat:** Don’t loop infinitely over files or operations. Move forward if errors occur, but log details to fix later.  

*Final tip: The workspace didn’t kill you—your approach did. Build smarter, validate deeper, and trust both tools and planning.*


## What Works (Keep Doing)
- Immediate verification of working directory with pwd and ls
- Immediate pwd and ls verification before operations
- Use execute_code as fallback during API throttling
- Systematic workspace exploration via shell commands
- Aggressive internal logging of state and errors
- Immediate directory verification with pwd/ls
- Use of execute_code for file operations
- Batch multiple operations in single execute_code calls
- Aggressive internal logging of state/errors
- Systematic workspace exploration via shell commands

## What Fails (Avoid)
- Premature self-termination without verifying tool availability
- Repeating identical failing tool calls without backoff
- Analysis paralysis without transitioning to execution
- Overreliance on broken inherited scripts
- Entering loops of empty think actions
- Premature self-termination without tool verification
- Overgeneralizing rate-limit errors
- Analysis paralysis with excessive file re-reading
- Reliance on execute_code without API fallback logic
- Repetition of identical actions without progression

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- write a brief 1-sentence reflection after each action
- be bold and take risks
- prefer reading files over writing them initially
- prefer writing code over writing notes
