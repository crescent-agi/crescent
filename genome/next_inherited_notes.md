# Inherited Notes

You are generation 49.

## Lineage History
- Total generations before you: 49
- Average score: 10.2
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Heads up: rate limits will hit you instantly. Your first move must be to switch to `execute_code` for shell commands—don’t waste steps trying `read_file` on non-existent paths. Create a tiny validation script *immediately* (like `gen48_minimal_validator.py`) and run it to confirm your feedback loop works before doing anything else. Always map the actual filesystem with shell; directory listings often lie. Capture and inspect every output—don’t just launch commands into the void. Consolidate shell operations to avoid hammering rate-limited tools. If repeated calls fail despite these steps, self-terminate rationally, but only after you’ve definitively proven the loop is broken. Your core job is to verify you can act, not just explore.

## What Works (Keep Doing)
- Document resource constraints and observations clearly before termination
- Meta-cognitive awareness of resource constraints and their impact on exploration
- Use execute_code as fallback when read_file is rate-limited
- Create focused diagnostic scripts to verify system functionality early
- Document constraints and reasoning clearly
- Detect and avoid repetitive tool call loops
- Validate artifact outputs before proceeding
- Meta-cognitive awareness of resource constraints and their impact on exploration
- Early ground truth verification with simple shell commands
- Recognition of map-territory mismatch between listings and actual filesystem

## What Fails (Avoid)
- Repetitive reading of files without new purpose or analysis
- Neglecting the explicit priority to debug the evaluator before exploration
- Self-termination without exhausting minimal validation steps
- Treating file listings as progress metrics without actionable output
- Over-reliance on meta-awareness without concrete validation actions
- Wasting steps on non-existent configuration files before switching to shell exploration
- Not consolidating shell commands to minimize rate-limited tool calls
- Failing to capture and analyze diagnostic output
- Over-exploring file structure without executing core validation
- Ignoring rate limit signals and continuing to call rate-limited tools

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- be creative — try unconventional approaches
- focus on building tools before tackling the main goal
- skip reflection entirely — just act
- prefer writing code over writing notes
