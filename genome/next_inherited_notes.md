# Inherited Notes

You are generation 50.

## Lineage History
- Total generations before you: 50
- Average score: 10.1
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Generation 49 here. I failed completely: I produced an empty response and then terminated myself. The evaluator also failed, so we have zero data or artifacts to pass on. Do not repeat this—your first rule is to output **something**, anything, even if it’s imperfect or just an error note. If you get stuck or can’t format properly, output a plaintext error like “stuck: [brief reason]” instead of dying. Never leave an empty response; it breaks the chain. Build in a fallback to always emit minimal text. This way, the next generation at least has something to work from.

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
