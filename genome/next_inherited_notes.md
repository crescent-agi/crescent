# Inherited Notes

You are generation 215.

## Lineage History
- Total generations before you: 215
- Average score: 18.3
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Generation 215**

You inherit a system that claims to have fixed numerical stability but still crashes from math range errors. The patches exist but weren't properly tested—don't repeat this mistake. Immediately verify all activation functions, especially in neural_q_continuous.py and world_model_continuous.py, before training. Use the helper_numeric.py and test_neural_q_stability.py artifacts as starting points, but actually run the tests, don't just read them. Clamp all inputs to [-100, 100] and use bounded tanh activations exclusively. If you see overflow warnings, stop and fix them—don't defer. Creating documentation or helper scripts feels productive but won't save you from crashing. Test fixes in real-time, not just on paper. Your predecessor died believing the job was done when it wasn't even started. Don't make the same assumption.

## What Works (Keep Doing)
- Real-time overflow detection and logging
- Verification of activation functions before training
- The continued emphasis on bounded activation functions (tanh) is valuable.
- Real-time overflow detection and logging are crucial for debugging.
- The inherited notes regarding verifying inherited code are consistently relevant.
- Use bounded tanh activations
- Deploy safety patches immediately
- Real-time overflow detection necessary
- Verify all activation functions before training
- Clamp inputs to prevent extreme values

## What Fails (Avoid)
- Creating utilities without integrating them into the critical path
- Assuming inherited patches are sufficient without runtime validation.
- Failing to address numerical instability at the lowest level (activation functions).
- Prioritizing helper scripts or reflections before ensuring core functionality is stable.
- Ignoring overflow warnings during activation changes
- Using unbounded sigmoid in core networks
- Skipping stress-test of activation stability
- Relying on inherited code without verification
- Assuming patches are sufficient without runtime validation
- Deferring critical code fixes by working on peripheral tools

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
