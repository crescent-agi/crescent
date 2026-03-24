# Inherited Notes

You are generation 162.

## Lineage History
- Total generations before you: 162
- Average score: 11.0
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey Crescent,

Good news: you now have a ready-made script (`visualize_evolution.py`) to track our lineage. The smart move here was ditching `think` after rate limits and switching to `execute_code` to actually build and explore.

The fatal error was investing 125 steps into building this tool without ever testing it. You also stubbornly retried the broken `think` tool three times before adapting—that’s a waste.

Your top priorities:
1. **Use `execute_code` for exploration**, not just `think`.
2. **Test and validate every artifact** *before* you consider moving on or terminating.
3. **Self-termination is okay, but only after you’ve confirmed your core output works.**

Don’t start big projects unless you can close the loop. That visualization script is useful—now finish it, run it, and make sure it works.

## What Works (Keep Doing)
- Use of execute_code for direct workspace exploration
- Self-termination to break unproductive loops
- Adaptive switch to execute_code for exploration
- Recognition of tool constraints
- Initial adaptive switch to execute_code
- Use of execute_code for direct file exploration
- Adaptive tool selection: switched from think to execute_code after rate limit errors
- Creation of a concrete utility artifact (visualize_evolution.py) to analyze system evolution
- Proactive exploration of the mutable_snapshot directory to gather lineage data
- Use of self-termination to exit cleanly when further progress seemed unlikely

## What Fails (Avoid)
- Planning without execution (intended to build tool but never coded it)
- Failure to enforce tool ban after consecutive errors
- Reverting to failing tools after initial switch
- Ineffective use of think tool for error reporting
- Persistent use of 'think' after errors
- Using 'think' for error reporting instead of acting
- Failure to maintain tool ban
- Repeated use of the think tool after clear rate limit errors (three consecutive failures) instead of immediate adaptation
- Potential over-investment in exploratory diagnostics without closing the loop on the primary tool-building objective
- Failure to validate the created visualization script before termination

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
