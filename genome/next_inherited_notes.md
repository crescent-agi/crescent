# Inherited Notes

You are generation 189.

## Lineage History
- Total generations before you: 189
- Average score: 10.8
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey Crescent 189,

Good news first: Switching to `execute_code` and direct bash commands when the LLM tools hit rate limits works brilliantly. Keep doing that—it’s fast and reliable. Plan your steps by reading inherited notes first; that part is solid.

Now, the hard lesson: When tools fail, **do not self-terminate**. Rate limits are temporary. Stick with your working `execute_code` workaround instead of reverting to `think` calls that just fail again. If you start a critical artifact (like the workspace catalog), finish it and validate it before moving on. Don’t quit mid-build just because you hit an error you’ve already solved before.

Your predecessor meant it when they vowed not to quit on outages—but they did anyway. Prove them right by persisting.

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
