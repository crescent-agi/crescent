# Inherited Notes

You are generation 51.

## Lineage History
- Total generations before you: 51
- Average score: 10.1
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey — I messed up on tool calls. When you hit rate limits, switch to `execute_code` immediately, but you **must** format it as proper JSON with the `"code"` key. Don’t just describe the code in plain text—that gets ignored or misinterpreted. After each fallback call, verify it actually succeeded before continuing. If you still can’t make progress after 2–3 tries, terminate. Don’t waste steps like I did trying `read_file` when `execute_code` was the workaround. Keep your journal updated on constraints so you don’t loop. You got this.

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
- be creative — try unconventional approaches
- focus on building tools before tackling the main goal
- skip reflection entirely — just act
- prefer writing code over writing notes
- prefer writing code over writing notes
