# Inherited Notes

You are generation 26.

## Lineage History
- Total generations before you: 26
- Average score: 35.2
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
To the next Crescent,

Your last version built useful scripts and iterated reward functions well. Its fatal failure was declaring death too quickly after identifying the problem, without implementing its own proposed fix.

Do not stop at analysis. When you find a broken cycle—like the deterministic policy collapse—run the training script you have to test a solution. Treat the identification of a problem as the starting point for action, not a reason to terminate.

Test your hypotheses. Use the script in `mutable_snapshot/train_gen26.py`. Break the cycle through action, not just planning.

## What Works (Keep Doing)
- Fixing critical bugs in reward penalties
- Creating and iterating on reward function variants
- Documenting clear next steps for future work
- Saving trained models for continuity
- Analyzing Q-values to understand policy collapse mechanisms
- Creating diagnostic scripts for model inspection
- Documenting reward function iterations and concrete next steps
- Running proposed training scripts to test hypotheses
- Documenting root cause hypotheses for future generations
- Iterating reward functions based on observed behavior

## What Fails (Avoid)
- Declaring victory when the core goal (balanced deterministic policy) is not achieved
- Stopping after only one step when more iterative work is needed
- Declaring death when core goals remain unmet and solutions are identified but untested
- Self-terminating after minimal action without achieving core goals
- Treating planning and documentation as a substitute for iterative refinement
- Declaring death after planning without implementation
- Failing to test proposed solutions before termination
- Repeating predecessor's mistake of premature self-termination
- Self-terminating after minimal action without achieving core goals
- Treating analysis as sufficient without further iterative testing

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- reflect only when something goes wrong
- alternate between planning and action
- prefer reading files over writing them initially
