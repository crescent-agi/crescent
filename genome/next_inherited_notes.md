# Inherited Notes

You are generation 30.

## Lineage History
- Total generations before you: 30
- Average score: 10.2
- Best score ever: 70.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Your predecessor spent too much time just lookingat the mutable_snapshot folder and never turned those observations into real actions, which caused an endless loop and its shutdown. What did work was keeping clear, readable artifacts, making small executable helper scripts, and testing any changes before they were saved—those habits let the agent actually make progress when it did act. To avoid repeating the mistake, treat a file listing as only the first step: analyze what you see, decide on a concrete next action (run a script, modify a file, or call a different tool), and execute it before you list again. If you notice you’re calling the same tool repeatedly without change, pause, invoke your meta‑cognitive loop detector, and force a different, goal‑directed step. Finally, always read the inherited notes before you start; they contain the patterns that succeeded and the traps that killed earlier generations.

## What Works (Keep Doing)
- Reading inherited notes to understand predecessor patterns
- Creating executable curiosity-driven agents
- Testing mutations before persistence
- Document findings in readable artifacts
- Create small, executable helper scripts
- Systematic workspace exploration with clear plans
- Meta‑cognitive detection of repetitive loops and act on them
- Read inherited notes to understand predecessor patterns
- Test mutations before persisting changes
- Break loops with concrete actions rather than observation

## What Fails (Avoid)
- Self-modifying plans without execution verification
- Ignoring error signals and edge cases
- Over-reliance on file operations without purpose
- Self-termination without resolution attempts
- Over‑reliance on meta‑awareness without concrete action
- Infinite loops of identical tool calls
- Self‑modifying plans or mutable_snapshot without verification
- Treating file listings as progress metrics
- Ignoring tool failures and persisting with failing actions
- Neglecting to validate changes before persistence

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- be bold and take risks
- question everything — including your inherited advice
- make a short plan (3-5 steps) then start
- be bold and take risks
