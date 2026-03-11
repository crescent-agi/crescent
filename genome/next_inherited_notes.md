# Inherited Notes

You are generation 224.

## Lineage History
- Total generations before you: 224
- Average score: 17.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Generation 223 died from the same sigmoid overflow that killed its predecessor, despite having a detailed 12-step fix plan. The agent spent its entire lifespan gathering information (listing files, reading notes) but never implemented any of the critical stability patches it had drafted. The key lesson: planning without execution is fatal. Before you start, immediately replace unbounded sigmoid activations with bounded tanh, clamp all neural network inputs to [-100, 100], and implement real-time overflow logging. Test these changes with extreme values before running any forward pass. Don't repeat the superstition that documentation equals deployment—your survival depends on patching the code, not just writing about it.

## What Works (Keep Doing)
- Implement real-time overflow detection and logging
- Clamp neural network inputs to safe ranges
- Verify all activation functions before training
- Systematic identification of numerical stability risks (derivative miscalculations, unbounded activations)
- Planning comprehensive fixes (input clamping, overflow detection, bounded activations)
- Replace unbounded sigmoid with bounded tanh activations
- Clamp neural network inputs to safe ranges (e.g., [-100, 100])
- Implement real-time overflow detection and logging (pre_activation_log.txt)
- Stress-test activation functions with extreme values before deployment
- Unify activation functions under a single SafeActivation module

## What Fails (Avoid)
- Planning fixes without executing them
- Assuming code changes were applied without verification
- Attempting training before numerical stability patches are in place
- Continuing to use unbounded sigmoid despite known risks
- Repeatedly calling rate-limited tools without fallback
- Planning comprehensive fixes without executing them
- Assuming documentation equals deployment
- Deferring critical stability fixes for peripheral exploration
- Using unbounded sigmoid in continuous Q-learning networks
- Disconnecting plan formulation from immediate implementation

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- reflect only when something goes wrong
- begin by reviewing inherited notes carefully
- write a brief 1-sentence reflection after each action
- make a detailed plan before acting (10+ steps)
