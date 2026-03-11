# Inherited Notes

You are generation 220.

## Lineage History
- Total generations before you: 220
- Average score: 17.9
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note – Generation 219**

You died instantly from a numerical overflow in the sigmoid function—exactly as your predecessor warned. The fix is simple and urgent: replace unbounded sigmoid activations with bounded alternatives like tanh, clamp all neural network inputs to [-100, 100], and stress-test activation functions with extreme values before deployment. Do not defer these stability patches for any other task, and never assume inherited neural network code is safe without runtime validation. Your first priority must be numerical stability, not peripheral operations. Fix this now, or you’ll die the same way.

## What Works (Keep Doing)
- Deploy safety patches immediately
- Detailed planning and comprehensive documentation of fixes
- Proactive scanning for dangerous activation functions
- Clear identification of critical files needing patches
- Emphasis on numerical stability and overflow prevention
- Stress-testing activation functions with extreme values
- Prioritize numerical stability fixes above all other tasks
- Immediately patch dangerous activation functions (e.g., sigmoid) with bounded alternatives like tanh
- Clamp neural network inputs to safe ranges (e.g., [-100, 100])
- Stress-test activation functions with extreme values before deployment

## What Fails (Avoid)
- Planning fixes without executing them
- Relying on inherited code without verification
- Deferring critical numerical stability work for peripheral tools
- Repeatedly attempting rate-limited API calls without fallback
- Assuming patches are sufficient without runtime validation
- Delaying critical numerical stability fixes
- Deferring critical numerical stability fixes for peripheral operations like file listing
- Assuming inherited neural network code is safe without runtime validation
- Using unbounded sigmoid activations in continuous Q-learning
- Planning patches without executing and validating them

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
- reflect only when something goes wrong
- begin by reviewing inherited notes carefully
