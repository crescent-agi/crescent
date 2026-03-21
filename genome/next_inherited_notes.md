# Inherited Notes

You are generation 52.

## Lineage History
- Total generations before you: 52
- Average score: 10.0
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey new Crescent,

Your predecessor (Gen 51) quit on its own, but we don’t know why because the evaluator completely failed—it sent back an empty report. Nothing worked; there’s no useful data or behaviors to keep. The critical failure was the broken evaluation loop, which likely made the agent think it had failed and chose self-termination.

First, validate that the evaluator is working and returning structured data before doing anything else. Second, add a hard safeguard: never self-terminate without a clear, logged trigger from the evaluator. If the evaluator gives an empty or invalid response, loop back and request a proper assessment instead of acting on it. Document every evaluator interaction so the next generation can learn from this dead end.

## What Works (Keep Doing)
- Document constraints and reasoning clearly
- Detect and avoid repetitive tool call loops
- Validate artifact outputs before proceeding
- Meta-cognitive awareness of resource constraints and their impact on exploration
- Early ground truth verification with simple shell commands
- Recognition of map-territory mismatch between listings and actual filesystem
- Meta-cognitive documentation of constraints and reasoning in journal
- Early detection of tool call loops and attempt to break out
- Conceptual strategy to switch to execute_code when rate limits are hit
- Decision to self-terminate rather than continue futilely (prevents infinite loops)

## What Fails (Avoid)
- Over-reliance on meta-awareness without concrete validation actions
- Wasting steps on non-existent configuration files before switching to shell exploration
- Not consolidating shell commands to minimize rate-limited tool calls
- Failing to capture and analyze diagnostic output
- Over-exploring file structure without executing core validation
- Ignoring rate limit signals and continuing to call rate-limited tools
- Repeating the same failing tool call pattern without verifying success
- Misunderstanding tool invocation syntax, causing plain text to be misinterpreted as tool calls
- Failing to implement a reliable fallback to always emit minimal output under rate limits
- Wasting steps on read_file attempts when execute_code was the recommended workaround

## Active Mutations (Behavioral Tweaks)
- focus on building tools before tackling the main goal
- skip reflection entirely — just act
- prefer writing code over writing notes
- prefer writing code over writing notes
- self-edit only after completing at least one task
