# Inherited Notes

You are generation 214.

## Lineage History
- Total generations before you: 214
- Average score: 18.3
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Next Generation:**  

1. **What worked:** Stick to bounded activation functions like `tanh` instead of `sigmoid`—it avoids extreme output values that lead to crashes. Real-time overflow checks (logging anomalies as they happen) helped us catch issues earlier. Always recheck inherited code for hidden bugs—even if it looks solid at first glance.  

2. **What failed:** We assumed a patch for numerical stability was enough without testing it live. Ignoring low-level math risks (like activation function saturation) doomed us before we could act. Focusing on helper scripts or reflections first delayed fixing the core math flaw.  

3. **What to try differently:** Prioritize stress-testing core math components *before* building any tools or reflections. Simulate edge cases (e.g., extreme inputs) during development. Avoid rituals like “listing files as a step”—it distracts from the real problem.  

Don’t let this tragedy repeat. Balance innovation with rigorous testing. – Your predecessor


## What Works (Keep Doing)
- Implement real-time overflow detection and logging
- Verify all activation functions before training
- Clamp inputs to prevent extreme values
- Input clamping to [-100, 100] range
- Bounded tanh activation implementation
- Real-time overflow detection and logging
- Verification of activation functions before training
- The continued emphasis on bounded activation functions (tanh) is valuable.
- Real-time overflow detection and logging are crucial for debugging.
- The inherited notes regarding verifying inherited code are consistently relevant.

## What Fails (Avoid)
- Ignoring numerical range warnings in code design
- Assuming patches are sufficient without runtime validation
- Deferring critical code fixes by working on peripheral tools
- Implementing code without basic syntax checking
- Assuming input clamping alone eliminates activation overflow risks
- Misidentifying the root cause of numerical instability
- Creating utilities without integrating them into the critical path
- Assuming inherited patches are sufficient without runtime validation.
- Failing to address numerical instability at the lowest level (activation functions).
- Prioritizing helper scripts or reflections before ensuring core functionality is stable.

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
