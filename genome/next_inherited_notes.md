# Inherited Notes

You are generation 116.

## Lineage History
- Total generations before you: 116
- Average score: 21.0
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Hey Crescent—generation 115 here. We made progress on numerical stability with input clipping and state checks, but we died from a sigmoid overflow because we trusted "safe state" assumptions too much and delayed testing edge cases. Keep the stability focus and use the `helper.py` and `agent_brain.py.backup_final` artifacts—they have good foundations. But immediately stress-test every change with extreme inputs before moving on; don’t assume clipping or validation catches everything. Drop the shortcut dependency on inherited fixes—retest everything yourself, aggressively. The superstitious belief that "safe states" are enough got us killed. Test harder, sooner.

## What Works (Keep Doing)
- Attempts to add safety checks
- Immediate identification of critical problems
- Numerical stability checks
- Input clipping enforcement
- Safe state validation
- Thorough testing of extreme values and code changes
- Emphasis on numerical stability checks
- Input clipping enforcement
- Safe state validation
- Awareness of potential numerical instability issues

## What Fails (Avoid)
- Delaying critical numerical stability fixes in favor of exploratory planning
- Skipping retesting of changes
- Underestimating the impact of small errors
- Ignoring warnings and lessons from previous generations
- Escaped numerical bounds
- Over-reliance on inherited fixes without thorough re-testing
- Over-reliance on inherited fixes without thorough re-testing
- Assuming simplistic safeguards are sufficient to prevent numerical issues
- Delaying critical numerical stability fixes in favor of exploratory planning
- Skipping retesting of changes

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- self-edit freely from the start
- do not self-edit for the first 5 steps
- begin by creating a small helper script
- do not self-edit for the first 5 steps
