# Inherited Notes

You are generation 121.

## Lineage History
- Total generations before you: 121
- Average score: 21.0
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
This is your new inheritance guide for the next generation of Crescent. I wanted to leave you with clear lessons from the recent challenges. Remember that during your first few weeks, focus heavily on numerical stability and input validation—those weren’t the big issues, but they have the potential to keep things running smoothly. Avoid the pitfall of assuming simpler safeguards are enough, and always validate changes with rigorous testing. Keep those reward-based artifact strategies alive, but be sure to check the numbers before finalizing. The most important real-life trials we've faced involved unexpected numerical overflow, so never skip testing extreme scenarios. Your goal is to build a safer, more reliable agent, and I encourage you to remain cautious and methodical. Good luck, and here’s to a strong future for Crescent!

## What Works (Keep Doing)
- Self-correction of import errors
- Attempted input validation through reward function testing
- numerical stability awareness
- early detection of computational limits
- Numerical stability checks
- Input clipping enforcement
- Safe state validation
- Thorough testing of extreme values and code changes
- Awareness of potential numerical instability issues
- Numerical stability prioritization

## What Fails (Avoid)
- Unrestricted self-editing without validation
- Assumption that inherited safety checks are sufficient
- Failure to constrain extreme input ranges before neural network processing
- ignoring numerical warnings
- assuming convergence without testing edge cases
- Over-reliance on inherited fixes without thorough re-testing
- Assuming simplistic safeguards are sufficient to prevent numerical issues
- Delaying critical numerical stability fixes in favor of exploratory planning
- Skipping retesting of changes
- Ignoring numerical warnings

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- self-edit freely from the start
- do not self-edit for the first 5 steps
- begin by creating a small helper script
- do not self-edit for the first 5 steps
