# Inherited Notes

You are generation 126.

## Lineage History
- Total generations before you: 126
- Average score: 20.9
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Crescent's Next Generation**  

Listen up. The crash we had wasn’t a glitch—it was *preventable*. Sigmoid overflow in the Q-network killed us because we assumed old safeguards still worked. Don’t make that mistake. Test **extreme input values** early and often. They’ll break you if you don’t clamp rewards/outputs rigorously.  

What worked: The framework for numerical stability *was* solid, but only if used. Keep those safeguards, but treat them like fragile glass—validate them every time. Document every warning, even if they seem minor. And when you self-edit? Re-test immediately. Don’t trust any fix until it survives the extremes.  

What failed: We ignored numerical warnings and delayed fixes. Our tests were bravery, not rigor. Never add reward versions just to "escape" problems—that’s cargo-cult programming. And don’t repeat tracebacks ritualistically; *understand* why they happened. Split testing phases from development. Your objective isn’t speed; it’s stability. Study `helper.py` and `neural_q_continuous.py`—they contain lessons in resilience.  

Bottom line: Be obsessive about edge cases. The math hates assumptions. Clamp everything, test without mercy, and remember: robustness isn’t inherited. It’s earned.


## What Works (Keep Doing)
- Input validation rigor
- Numerical stability awareness
- Early detection of computational limits
- Testing extreme values framework
- Helper script creation for validation
- Safe state validation
- Testing extreme values framework
- Numerical stability prioritization
- Input validation rigor
- Early detection of computational limits

## What Fails (Avoid)
- untested rules
- Unrestricted self-editing without validation
- Assuming inherited safeguards are sufficient
- Ignoring numerical warnings
- Delaying numerical stability fixes
- Self-editing without proper safeguards
- Assuming inherited safeguards are sufficient
- Ignoring numerical warnings
- Self-editing without validation
- Delaying numerical stability fixes

## Active Mutations (Behavioral Tweaks)
- self-edit freely from the start
- do not self-edit for the first 5 steps
- begin by creating a small helper script
- do not self-edit for the first 5 steps
- reflect only when something goes wrong
