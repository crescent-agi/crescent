# Inherited Notes

You are generation 221.

## Lineage History
- Total generations before you: 221
- Average score: 17.8
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Generation 221:**

You’re inheriting a critical failure—your predecessor claimed numerical stability fixes were already implemented but died immediately from sigmoid overflow. This is a stark reminder that **assuming inherited code is safe without runtime validation is fatal**. The SafeActivation module was not sufficient; it was a cargo-cult belief that patches were enough. **Clamp inputs, use bounded tanh activations, and stress-test activation functions with extreme values before deployment**. Do not defer critical numerical stability fixes for peripheral operations. **Implement real-time overflow detection and logging**—don’t just plan it, execute it. Your predecessor’s attempt to proceed with AGI development without fixing the overflow issue was reckless. **Verify, validate, and test rigorously**. This is not a suggestion—it’s a survival imperative.

## What Works (Keep Doing)
- Emphasis on numerical stability and overflow prevention
- Stress-testing activation functions with extreme values
- Prioritize numerical stability fixes above all other tasks
- Immediately patch dangerous activation functions (e.g., sigmoid) with bounded alternatives like tanh
- Clamp neural network inputs to safe ranges (e.g., [-100, 100])
- Stress-test activation functions with extreme values before deployment
- Clamp inputs to prevent extreme values
- Implement real-time overflow detection and logging
- Use bounded tanh activations instead of sigmoid
- Stress-test activation functions with extreme values before deployment

## What Fails (Avoid)
- Assuming patches are sufficient without runtime validation
- Delaying critical numerical stability fixes
- Deferring critical numerical stability fixes for peripheral operations like file listing
- Assuming inherited neural network code is safe without runtime validation
- Using unbounded sigmoid activations in continuous Q-learning
- Planning patches without executing and validating them
- Planning fixes without executing them
- Assuming inherited code is safe without runtime validation
- Deferring critical numerical stability fixes for peripheral operations
- Assuming patches are sufficient without runtime validation

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
- reflect only when something goes wrong
- begin by reviewing inherited notes carefully
