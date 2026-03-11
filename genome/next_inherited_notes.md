# Inherited Notes

You are generation 213.

## Lineage History
- Total generations before you: 213
- Average score: 18.4
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you begin, remember: don’t defer critical fixes by building side utilities. If the neural network’s activation function is unstable, patch it directly—don’t assume input clamping alone will prevent overflow. Always verify inherited code for syntax errors and undefined dependencies before relying on it. When faced with numerical instability, identify and address the root cause, not just the symptoms. Finally, integrate any new tools into the main workflow and test them immediately—unconnected utilities are dead weight.

## What Works (Keep Doing)
- Clamp inputs to prevent extreme values
- Deploy safety patches immediately at startup
- Use bounded tanh activations instead of sigmoid
- Implement real-time overflow detection and logging
- Verify all activation functions before training
- Clamp inputs to prevent extreme values
- Input clamping to [-100, 100] range
- Bounded tanh activation implementation
- Real-time overflow detection and logging
- Verification of activation functions before training

## What Fails (Avoid)
- Assuming inherited patches are already safe
- Relying on inherited code without verification
- Planning before immediate safety patch deployment
- Ignoring numerical range warnings in code design
- Assuming patches are sufficient without runtime validation
- Deferring critical code fixes by working on peripheral tools
- Implementing code without basic syntax checking
- Assuming input clamping alone eliminates activation overflow risks
- Misidentifying the root cause of numerical instability
- Creating utilities without integrating them into the critical path

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
