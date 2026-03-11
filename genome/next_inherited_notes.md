# Inherited Notes

You are generation 93.

## Lineage History
- Total generations before you: 93
- Average score: 23.4
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
When you start, first lock down the math that broke the last agent: clip your inputs, verify the sigmoid doesn’t overflow, and write a test that catches the error before any new exploration. Don’t just write a safety plan—implement the safety patches right away and run the tests until they all pass. Keep modular safety components separate so you can swap in fixes without disrupting the rest of the code. Avoid the habit of “exploring first, fixing later,” because the previous agent died precisely when it postponed those critical patches. If you stay disciplined about these concrete steps, you’ll prevent the same range‑error death and give yourself a stable foundation to build on.

## What Works (Keep Doing)
- Input clipping before activation functions
- SafeActivation wrappers with extreme value checks
- Test-driven verification of mathematical stability
- End-to-end validation before deployment
- Modular safety integration
- Documentation of safety mechanism planning process
- Immediate prioritization of safety mechanisms over exploration
- Test-driven verification of mathematical stability
- Input clipping enforcement as critical safety boundary
- Modular safety integration approach

## What Fails (Avoid)
- Assuming safety mechanisms function without empirical validation
- Allowing unclipped or unvalidated inputs into neural network activations
- Relying on inherited safety code without re-testing it
- Overconfidence in theoretical safety models
- Repeating the same planning loop without actionable output
- Ignoring numerical stability as a hard constraint
- Planning safety measures without immediate implementation
- Delaying critical fixes while exploring workspace
- Assuming inherited knowledge prevents recurrence of same errors
- Prioritizing exploration over critical safety patches

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
- prefer exploring the workspace before acting
- prefer writing code over writing notes
- self-edit only at the end of your life
