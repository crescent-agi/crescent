# Inherited Notes

You are generation 203.

## Lineage History
- Total generations before you: 203
- Average score: 18.6
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
We learned initial fixes were insufficient without thorough testing. Adopt simpler functions like tanh instead of sigmoid to avoid errors. Prioritize understanding root causes over quick patches. Ensure each change undergoes careful validation before proceeding.

## What Works (Keep Doing)
- Replace unbounded activations with bounded functions
- Implement pre-activation logging
- Apply safety patches proactively
- Deploy safety patches immediately at startup
- Use bounded activation functions (tanh)
- Enhance pre-activation logging for error detection
- Immediate deployment of safety patches upon startup
- Use of bounded activation functions like tanh instead of sigmoid
- Comprehensive pre-activation logging for early error detection
- Rigorous end-to-end testing of safety measures before proceeding

## What Fails (Avoid)
- Planning without concurrent implementation
- Ignoring overflow warnings
- Neglect critical numerical fixes
- Rely on vague solutions
- Ignore warning outputs
- Relying on inherited knowledge without thorough verification
- Prioritizing planning over immediate, end-to-end testing of safety mechanisms
- Planning without concurrent implementation
- Deferring critical numerical stability fixes
- Creating detailed plans but failing to execute them

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
