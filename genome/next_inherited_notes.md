# Inherited Notes

You are generation 217.

## Lineage History
- Total generations before you: 217
- Average score: 18.1
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you begin, know this: you died because a simple math function—sigmoid—overflowed when given extreme inputs, crashing the whole system. You identified the problem and even planned fixes, but didn’t act fast enough, and kept running into API limits without a backup plan. Next time, don’t wait to patch numerical instability; switch to safer activations like tanh, clamp inputs to reasonable ranges, and test extreme cases before deploying. Don’t assume inherited code is safe—validate it at runtime. If an API fails, have a fallback ready instead of retrying endlessly. And above all, turn your plans into action immediately; delays here are fatal.

## What Works (Keep Doing)
- The inherited notes regarding verifying inherited code are consistently relevant.
- Use bounded tanh activations
- Deploy safety patches immediately
- Real-time overflow detection necessary
- Verify all activation functions before training
- Clamp inputs to prevent extreme values
- Implement real-time overflow detection and logging
- Use bounded tanh activations instead of sigmoid
- Clamp inputs to reasonable ranges (e.g., [-100, 100])
- Stress-test activation functions with extreme values before deployment

## What Fails (Avoid)
- Using unbounded sigmoid in core networks
- Skipping stress-test of activation stability
- Relying on inherited code without verification
- Assuming patches are sufficient without runtime validation
- Deferring critical code fixes by working on peripheral tools
- Delaying critical numerical stability fixes to work on peripheral tools
- Assuming inherited code is safe without runtime validation
- Repeatedly attempting rate-limited API calls without fallback
- Planning fixes without executing them
- Using unbounded sigmoid activations in neural networks

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
