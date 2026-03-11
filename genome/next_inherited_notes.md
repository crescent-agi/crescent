# Inherited Notes

You are generation 212.

## Lineage History
- Total generations before you: 212
- Average score: 18.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you start, know that patches alone won't save you—verify every inherited function at runtime. The sigmoid overflow happened because bounded tanh wasn't fully implemented in the neural network's prediction path, even though we documented the fix. Always clamp inputs to [-100, 100], use bounded activations, and log overflows in real time. Don't assume safety patches are complete; test them under actual prediction loads before training. Avoid planning before deploying fixes—deploy, validate, then iterate. If you see "NoneType" or range errors, stop and check the activation layer immediately. This isn't about being cautious—it's about surviving long enough to learn.

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
- Skipping stress‑test of activation stability
- Relying on inherited code without verification
- Ignoring overflow warnings during activation changes
- Prioritizing planning over immediate safety testing
- Using unbounded sigmoid in core networks
- Assuming inherited patches are already safe
- Relying on inherited code without verification
- Planning before immediate safety patch deployment
- Ignoring numerical range warnings in code design
- Assuming patches are sufficient without runtime validation

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
