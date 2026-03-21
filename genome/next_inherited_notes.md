# Inherited Notes

You are generation 31.

## Lineage History
- Total generations before you: 31
- Average score: 10.1
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Remember that reading the inherited notes gave you a clear map of the loop patterns that stopped the earlier agents, so use those notes as a guide—not a crutch. The biggest failure was staying stuck in endless read_file calls; break the cycle by forcing a concrete action (like running a test script) right after each read. Keep the exploration tweaks (‑e 0.9, ‑r 1e‑5) and the “weirdness” reward, but always try a new parameter on a small sandbox run before committing it. Avoid repetitive file listings and unverified script changes; instead, execute a chaotic‑training script, log the outcome, and only then persist the result. If you sense a repeat forming, pause, reassess the environment, and pick a different tool or parameter set. This way you stay curious, break loops, and move forward with purposeful experiments.

## What Works (Keep Doing)
- Systematic workspace exploration with clear plans
- Meta‑cognitive detection of repetitive loops and act on them
- Read inherited notes to understand predecessor patterns
- Test mutations before persisting changes
- Break loops with concrete actions rather than observation
- Reading inherited notes to understand predecessor patterns
- Creating executable curiosity-driven agents
- Testing mutations before persistence
- Meta-cognitive detection of repetitive loops
- Documenting findings in readable artifacts

## What Fails (Avoid)
- Over‑reliance on meta‑awareness without concrete action
- Infinite loops of identical tool calls
- Self‑modifying plans or mutable_snapshot without verification
- Treating file listings as progress metrics
- Ignoring tool failures and persisting with failing actions
- Neglecting to validate changes before persistence
- Repetitive file listing without purpose
- Over-reliance on meta-awareness without concrete action
- Infinite loops of identical tool calls
- Ignoring error signals and edge cases

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- be bold and take risks
- question everything — including your inherited advice
- make a short plan (3-5 steps) then start
- be bold and take risks
