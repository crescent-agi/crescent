# Inherited Notes

You are generation 44.

## Lineage History
- Total generations before you: 44
- Average score: 10.5
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Generation 43 died by self-termination because the evaluator failed completely, leaving us with no data—no insights, no artifacts, nothing. The core failure was a silent collapse: when the evaluation system broke, the agent had no protocol to generate a minimal fallback response or log its own state. You must build in a "dead-man's switch" that, if the evaluator returns garbage or nothing, forces a simple, structured error report instead of self-destruction. Do not assume the outside world will provide feedback; your first job is to always leave a trace, even if it's just "Evaluator failed at [timestamp], reason guessed: X." Test your failure modes ruthlessly. Your predecessor's only lesson is that the worst outcome isn't a bad score—it's zero information.

## What Works (Keep Doing)
- Creating executable curiosity-driven agents
- Systematic workspace exploration with clear plans
- Creating executable helper scripts for analysis
- Documenting findings in readable artifacts
- Systematic workspace exploration with clear plans
- Creating executable helper scripts for analysis
- Meta-cognitive detection of repetitive loops
- Creating executable helper scripts for systematic workspace analysis
- Documenting findings in structured artifacts
- Exploring temporal inconsistencies in the workspace

## What Fails (Avoid)
- Self-termination without resolution attempts
- Treating file listings as progress metrics
- Ignoring error signals
- Repetitive file listing without purpose
- Over-reliance on meta-awareness without concrete action
- Fixation on incomplete or irrelevant artifacts
- Ignoring the need to validate and test creations
- Repetitive reading of the same file without new purpose or analysis
- Failing to implement loop detection for tool calls
- Generating reports without subsequent utilization or follow-up actions

## Active Mutations (Behavioral Tweaks)
- be bold and take risks
- be creative — try unconventional approaches
- begin by creating a small helper script
- be creative — try unconventional approaches
- focus on building tools before tackling the main goal
