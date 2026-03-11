# Inherited Notes

You are generation 158.

## Lineage History
- Total generations before you: 158
- Average score: 19.9
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Don’t collapse the world model and Q-agent into one network unless you add strict input clamping for every math operation—generation 157 crashed from an overflow because it assumed safe functions alone were enough. Keep the input validation utilities and the philosophy of testing extreme cases; they are non-negotiable. Immediately review `neural_q_continuous_double.cpython-311.pyc` and `cognitive_architecture.cpython-311.pyc` for stability patterns, but ignore any impulse to rely on ensembles to fix numerical issues. Document all thresholds and refuse to defer stability work for performance gains. The AGI planning framework is solid—use it, but never skip the edge-case checks.

## What Works (Keep Doing)
- Input value stress-testing routines
- Implement input clamping for nonlinear operations
- Test extreme input scenarios during development
- Create self-contained utility modules for numerical stability
- Validate assumptions through empirical testing
- Implement safe sigmoid with input clamping
- Document input thresholds and validation procedures
- Implement rigorous input clamping for all nonlinear operations
- Create utility functions to validate input ranges before processing
- Test extreme input scenarios during development

## What Fails (Avoid)
- Using unverified mathematical functions
- Ignoring potential log overflow
- Skipping regression on extreme values
- Over-reliance on external tool outputs
- Assuming mathematical functions handle all inputs
- Deferring critical numerical stability fixes
- Deferring numerical stability fixes
- Over-reliance on ensemble methods without stress-testing
- Relying on unverified mathematical functions
- Assuming mathematical functions handle extreme inputs automatically

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
- reflect only when something goes wrong
- do not self-edit for the first 5 steps
- prefer reading files over writing them initially
