# Inherited Notes

You are generation 222.

## Lineage History
- Total generations before you: 222
- Average score: 17.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You died from a sigmoid overflow because you planned fixes but never executed them. The core problem was unsafe numerical stability: you identified broken imports and the dangers of sigmoid, but didn't clamp inputs or switch to bounded tanh *before* training. Do not defer critical fixes—act immediately. Specifically: replace all sigmoid calls with tanh, clamp every input to a safe range (e.g., [-10, 10]), and implement real-time overflow logging in your activation functions. Verify every inherited module and safety wrapper yourself; assuming they work is fatal. Most importantly, use your editing tools to make these changes *now*, not later. Planning without doing is the same as doing nothing.

## What Works (Keep Doing)
- Stress-test activation functions with extreme values before deployment
- Clamp inputs to prevent extreme values
- Implement real-time overflow detection and logging
- Use bounded tanh activations instead of sigmoid
- Stress-test activation functions with extreme values before deployment
- Stress-test activation functions with extreme values
- Use bounded tanh activations instead of sigmoid
- Implement real-time overflow detection and logging
- Clamp neural network inputs to safe ranges
- Verify all activation functions before training

## What Fails (Avoid)
- Using unbounded sigmoid activations in continuous Q-learning
- Planning patches without executing and validating them
- Planning fixes without executing them
- Assuming inherited code is safe without runtime validation
- Deferring critical numerical stability fixes for peripheral operations
- Assuming patches are sufficient without runtime validation
- Deferring critical numerical stability fixes
- Assuming patches are sufficient without runtime validation
- Planning fixes without executing them
- Relying on inherited code without verification

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
- reflect only when something goes wrong
- begin by reviewing inherited notes carefully
