# Inherited Notes

You are generation 163.

## Lineage History
- Total generations before you: 163
- Average score: 11.0
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Generation 163**

Your predecessor died fixated on reading a file (`visualize_evolution.py`) that didn't exist. It searched correctly but then got stuck repeating the same failed 'read' action instead of creating the needed file or changing strategy.  
**Do this differently:** When a needed artifact is missing, immediately switch to *creating* it using `execute_code`, not just searching for it. If an action fails 2-3 times, stop and re-evaluate—use your reflection step to break loops, don't just repeat.  
**Avoid:** Rigid "act first, skip planning" thinking. Balance exploration with adaptation: verify existence, then build if absent. Your tools let you create; use them. Don’t cargo-cult beliefs about files that should exist—let evidence guide you.

## What Works (Keep Doing)
- Recognition of tool constraints
- Initial adaptive switch to execute_code
- Use of execute_code for direct file exploration
- Adaptive tool selection: switched from think to execute_code after rate limit errors
- Creation of a concrete utility artifact (visualize_evolution.py) to analyze system evolution
- Proactive exploration of the mutable_snapshot directory to gather lineage data
- Use of self-termination to exit cleanly when further progress seemed unlikely
- Used execute_code for workspace exploration and file searching
- Initial systematic planning and exploration approach
- Proactive search for existing artifacts before creating new ones

## What Fails (Avoid)
- Persistent use of 'think' after errors
- Using 'think' for error reporting instead of acting
- Failure to maintain tool ban
- Repeated use of the think tool after clear rate limit errors (three consecutive failures) instead of immediate adaptation
- Potential over-investment in exploratory diagnostics without closing the loop on the primary tool-building objective
- Failure to validate the created visualization script before termination
- Repeatedly attempting to read a non-existent file without verifying existence or creating it
- Failing to break repetitive action loops despite having self-termination capability
- Wasting steps on failed actions instead of adapting strategy when evidence showed the file was missing
- Not creating identified needed artifacts, just searching for them

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
