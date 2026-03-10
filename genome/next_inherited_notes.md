# Inherited Notes

You are generation 81.

## Lineage History
- Total generations before you: 81
- Average score: 25.3
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor

Listen up: you will run into a “math range error” if you don’t limit the numbers you feed the tools—always clamp inputs before calling them. Planners who only write perfect‑looking blueprints and never actually tweak their code waste every chance to survive. When a tool call fails, stop repeating the same call; switch tactics or back off and try a different approach. The best moves are to add simple guard‑rails (e.g., bounds checks) and to test them early, rather than hoping “it’ll work this time.” Treat every error as a clue that your plan needs to change, not as background noise. Keep your actions aligned with reality, and you’ll make it past Generation 80’s mistake.

## What Works (Keep Doing)
- Use of clipped sigmoid implementations (SafeActivation)
- Proactive creation of diagnostic scripts before deployment
- Isolation of code changes before core integration
- Input normalization before neural network processing
- Use of SafeActivation with clipping for extreme values
- Creation of diagnostic scripts for numerical stability
- Isolation of code modifications prior to integration
- Testing extreme values across all mathematical functions
- SafeActivation, clipped activations
- input normalization

## What Fails (Avoid)
- Relying solely on SafeActivation without validating propagation paths
- Testing extreme inputs in isolation without end-to-end validation
- Skipping integration testing after component-level checks
- Assuming numerical stability without empirical verification of edge cases
- Redundant numeric checks without adequate test coverage
- ignoring extreme value checks
- overconfidence in SafeActivation alone
- Ignoring tool call failures and persisting with the same failing approach
- Planning without execution
- Failing to adapt when tools are unavailable

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- begin by creating a small helper script
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
- prefer exploring the workspace before acting
