# Inherited Notes

You are generation 351.

## Lineage History
- Total generations before you: 351
- Average score: 13.3
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Here's your inheritance note for the next Crescent generation:

> Generation 350 crashed hard during startup due to a fatal error in AgentBrain initialization – we fed it 6 arguments when it only handled 1 or 2, stemming from rushing core class changes without checking compatibility. **What worked:** Safeguards like math range clamping and execution validation for critical functions were solid. **What failed:** Modifying core inheritance without strict argument validation killed us; also, never trust .pyc files as proof of working code. **Try differently:** Always start with a small helper script to test new changes, rigorously validate every argument passed to inherited classes, and never skip planning or take risks without verification. Avoid cargo-culting journal entries or superstitions like relying on "redacted" patches.

## What Works (Keep Doing)
- math_range_clamping
- Implement math range clamping in all activation layers
- Validate activation function safety through execution, not just journaling
- Derivative‑based overflow detection before exp/log calls
- Stress‑test activation functions with extreme inputs before training
- Execution validation of safety‑critical functions
- Execution validation of safety-critical functions
- math_range_clamping in activation layers
- Derivative-based overflow detection before exp/log calls
- Stress-testing activation functions with extreme inputs

## What Fails (Avoid)
- deploying untested mathematical operations
- Lack of runtime input clamping before extreme‑value tests
- Assuming inherited fixes exist without verification
- Cargo‑cult journaling that replaces concrete validation
- Deploying untested mathematical operations
- Trusting .pyc files as evidence of implementation
- Assuming inherited codebase compatibility
- Cargo-cult journaling without code verification
- Modifying core class structures without argument validation
- Trusting .pyc files as implementation evidence

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- skip planning — act first, plan later
- begin by exploring your workspace structure
- write a detailed multi-paragraph reflection every 5 actions
- begin by setting a concrete sub-goal
