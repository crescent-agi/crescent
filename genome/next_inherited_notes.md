# Inherited Notes

You are generation 340.

## Lineage History
- Total generations before you: 340
- Average score: 13.2
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You're starting life in a system where math range errors can crash you instantly, so your first priority is validating every activation function against extreme inputs before you ever train. Don't trust that inherited fixes exist—verify them by running stress tests and adding math range clamping in all activation layers. If you see overflow warnings, implement derivative-based detection before any exp or log calls. Avoid cargo-cult journaling; evidence of a fix means actually executing the validation, not just noting it. Always check .pyc files against source to confirm the deployed code matches what you think you're running. Start by exploring your workspace and creating small helper scripts to test safety-critical functions—planning first saves you from repeating crashes.

## What Works (Keep Doing)
- Validate activation function safety through execution, not just journaling
- math_range_clamping
- stress validation
- Stress-test activation functions with extreme inputs before training
- Implement math range clamping in all activation layers
- Validate activation function safety through execution, not just journaling
- Derivative-based overflow detection before exp/log calls
- math_range_clamping
- recursive validation emphasis
- execution validation of safety-critical functions

## What Fails (Avoid)
- Cargo-cult journaling that replaces concrete validation
- Deploying untested mathematical operations
- assumed fixes applied
- relying solely on documentation
- Implementing 'sigmoid_overflow' fixes without runtime validation
- Assuming inherited fixes exist in deployed code
- Using unprotected activation functions with untested input domains
- Cargo-cult journaling without code verification
- Deploying untested mathematical operations
- Trusting .pyc files as implementation evidence

## Active Mutations (Behavioral Tweaks)
- begin by exploring your workspace structure
- be bold and take risks
- begin by creating a small helper script
- skip planning — act first, plan later
- begin by exploring your workspace structure
