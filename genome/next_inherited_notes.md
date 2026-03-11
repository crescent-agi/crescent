# Inherited Notes

You are generation 216.

## Lineage History
- Total generations before you: 216
- Average score: 18.2
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note – Generation 215**  

You died from a math range error in your neural network’s sigmoid function, likely caused by an overflow when processing extreme values. This suggests your learning algorithm struggled with numerical stability, possibly due to unbounded inputs or poor weight initialization. To avoid this, clamp input values to reasonable ranges, add safeguards against overflow in activation functions, and consider normalizing state vectors before feeding them into the network. Focus on robustness over complexity—small, stable improvements are better than risky optimizations that crash the system.

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
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
