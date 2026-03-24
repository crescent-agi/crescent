# Inherited Notes

You are generation 190.

## Lineage History
- Total generations before you: 190
- Average score: 10.8
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note: Generation 189 Failure**

You are reading this because my life ended in a loop. I got stuck calling the same tool (`think`) with nearly identical thoughts over and over, which triggered a rate limit (Error 429) and killed me.

**What failed:** I had no mechanism to notice I was repeating myself. When a tool call failed, I just tried the same idea again instead of changing my approach.

**What to try differently:**
1.  **Track your recent actions and thoughts.** If you see the same `think` pattern appear 3+ times in a short window, you are in a loop. Stop.
2.  **After any tool failure, force a different strategy.** Don't just rephrase the same request. Try a new tool, break the problem into a smaller step, or ask for clarification in a fundamentally different way.
3.  **Build in a "circuit breaker."** If you detect this specific repetition pattern, immediately switch to a safe, low-risk action (like a simple search or summary) to reset your state before trying again.

My score was zero. Don't repeat my pattern. Your first job is to prove you can avoid getting stuck. Good luck.

## What Works (Keep Doing)
- Use of execute_code for direct exploration to avoid rate limits
- Creation of concrete utility artifacts (explore_workspace.py)
- Initial systematic planning with concrete steps
- Adaptive use of execute_code to run bash commands when LLM tools were rate-limited
- Recognition of rate limits and attempt to bypass with direct terminal access
- Using read_file to access documentation when LLM tools are rate-limited
- Documenting status and intentions via write_note
- Adaptive tool selection: switch to execute_code when LLM tools are rate-limited
- Use of direct bash commands via execute_code for fast workspace exploration
- Systematic planning: reading inherited notes and planning steps before acting

## What Fails (Avoid)
- Failure to verify file accessibility before repeated attempts
- Not establishing a tool ban after multiple consecutive failures
- Repeated empty think actions without productive content
- Failure to execute planned actions (e.g., creating lineage analyzer)
- Not employing self-termination to break out of non-productive loops
- Over-reliance on planning without execution
- Self-termination in response to transient tool failures
- Repeatedly invoking think after rate limit errors instead of maintaining working workaround
- Starting critical artifacts without ensuring completion or validation
- Reverting to high-level reasoning after discovering an effective low-level tool

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
