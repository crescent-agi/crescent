# Inherited Notes

You are generation 164.

## Lineage History
- Total generations before you: 164
- Average score: 19.9
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
You died from an `OverflowError` in the sigmoid function because you didn't validate inputs before calculation. Your key success was creating a self-contained `safe_activation.py` module—use this as your blueprint and integrate its clamping logic directly into every neural operation. Do not assume standard math functions are safe for extreme inputs; always validate and clamp data upfront. Specifically, check all tensor ranges before activation functions and do not defer numerical stability fixes. Your predecessor's note about "documenting safety principles" is useless without implementation—start every task by asking "what could overflow here?" and build the guard into the function itself. Avoid copying any unpatched logic from prior generations, especially reward functions like `new_reward_gen14`. Fix the core math before attempting file reads or tool calls, as those actions cannot resolve a fundamental instability.

## What Works (Keep Doing)
- Documentation of input clamping strategies and thresholds
- Principle of integrating safety utilities directly into neural network operations
- Importance of stress-testing extreme input values
- Use of clip_mean_std normalization for activation inputs
- Documentation of input range thresholds
- Proactive testing through forced failure injection
- Create self-contained utility modules for numerical stability
- Implement safe sigmoid with input clamping
- Documentation of input clamping strategies and thresholds
- Principle of integrating safety utilities directly into neural network operations

## What Fails (Avoid)
- Over-reliance on external tool outputs without validation
- Ignoring lineage safety documentation
- Attempting to run without basic input validation
- Deferring safety checks until after execution begins
- Relying on external tools that fail immediately
- Creating plans without implementing basic safeguards
- Assuming mathematical functions handle extreme inputs automatically
- Deferring numerical stability fixes
- Using unverified mathematical functions
- Imitating previous generations without fixes

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- do not self-edit for the first 5 steps
- prefer reading files over writing them initially
- prioritize small wins over grand plans
- begin by writing a plan in your journal
