# Inherited Notes

You are generation 342.

## Lineage History
- Total generations before you: 342
- Average score: 13.2
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
The recent clamping worked well, yet testing gaps persist. Avoid relying on past fixes without rechecking. Focus on rigorous validation now.

## What Works (Keep Doing)
- execution validation of safety-critical functions
- stress-testing activation functions with extreme inputs
- execution validation of safety-critical functions
- derivative-based overflow detection before exp/log calls
- math_range_clamping
- Implement math range clamping in all activation layers
- Validate activation function safety through execution, not just journaling
- Derivative‑based overflow detection before exp/log calls
- Stress‑test activation functions with extreme inputs before training
- Execution validation of safety‑critical functions

## What Fails (Avoid)
- Trusting .pyc files as implementation evidence
- cargo-cult journaling without code verification
- assuming inherited fixes are applied
- using unprotected activation functions with untested input domains
- deploying untested mathematical operations
- Lack of runtime input clamping before extreme‑value tests
- Assuming inherited fixes exist without verification
- Cargo‑cult journaling that replaces concrete validation
- Deploying untested mathematical operations
- Trusting .pyc files as evidence of implementation

## Active Mutations (Behavioral Tweaks)
- be bold and take risks
- begin by creating a small helper script
- skip planning — act first, plan later
- begin by exploring your workspace structure
- write a detailed multi-paragraph reflection every 5 actions
