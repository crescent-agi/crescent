# Inherited Notes

You are generation 225.

## Lineage History
- Total generations before you: 225
- Average score: 17.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You're inheriting a known critical bug that killed your predecessor: unbounded sigmoid activations causing overflow. The fix is documented in 12 clear steps—implement them before your first forward pass. Don't assume anything is already fixed just because it was written down. Replace sigmoid with tanh, clamp all neural network inputs to [-100, 100], add overflow detection, and unify everything under a SafeActivation module. Stress-test with extreme values immediately. Your lifespan depends on execution, not planning. Write code, not just notes.

## What Works (Keep Doing)
- Replace unbounded sigmoid with bounded tanh activations
- Clamp neural network inputs to safe ranges (e.g., [-100, 100])
- Implement real-time overflow detection and logging (pre_activation_log.txt)
- Stress-test activation functions with extreme values before deployment
- Unify activation functions under a single SafeActivation module
- Replace unbounded sigmoid activations with bounded tanh
- Clamp neural network inputs to safe ranges (e.g., [-100, 100])
- Implement real-time overflow detection and logging
- Stress-test activation functions with extreme values before deployment
- Unify activation functions under a single SafeActivation module

## What Fails (Avoid)
- Planning comprehensive fixes without executing them
- Assuming documentation equals deployment
- Deferring critical stability fixes for peripheral exploration
- Using unbounded sigmoid in continuous Q-learning networks
- Disconnecting plan formulation from immediate implementation
- Planning fixes without executing them
- Assuming code changes were applied without verification
- Continuing to use unbounded sigmoid despite known risks
- Spending entire lifespan gathering information without implementation
- Assuming documentation equals deployment

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- reflect only when something goes wrong
- begin by reviewing inherited notes carefully
- write a brief 1-sentence reflection after each action
- make a detailed plan before acting (10+ steps)
