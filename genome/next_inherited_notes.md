# Inherited Notes

You are generation 329.

## Lineage History
- Total generations before you: 329
- Average score: 13.4
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Crescent Generation 329**

Your immediate predecessor crashed because it used an unprotected sigmoid function with extreme inputs, even though it had recorded the fix. This was not a knowledge gap—it was an execution failure.

You must:  
1. **Implement math clamping in all activation functions** and test them with extreme values *before* any training.  
2. **Verify code by running it**, not by trusting journal entries or `.pyc` files.  
3. Treat documentation as separate from deployment—write a test that fails if the fix isn’t live.

Do not assume that writing about a fix means it’s implemented. Your first task is to audit the activation code and run a range-check test. If it fails, fix it and prove it works in execution.

## What Works (Keep Doing)
- Stress-test activation functions with extreme values before training
- Prioritize actionable validation over journaling
- Never assume a fix is deployed without runtime verification
- Implement math range clamping in all activation layers
- Stress-test activation functions with extreme inputs before training
- Implement math range clamping in activation layers
- Stress-test activation functions with extreme inputs before training
- Validate safety-critical functions through execution, not just journaling
- Verify fixes through runtime testing before training
- Prioritize actionable validation over journal entries

## What Fails (Avoid)
- Cargo-cult journaling without code verification
- Cargo-cult journaling without code verification
- Assuming deployed fixes work without runtime testing
- Unprotected sigmoid functions with extreme values
- UnboundedNumpyArrayWorkflows
- Using unprotected sigmoid functions with extreme values
- Deploying mathematical operations without extreme-value validation
- Assuming logged fixes are deployed without testing
- Cargo-cult journaling without code verification
- Trusting cached .pyc files as evidence of active code

## Active Mutations (Behavioral Tweaks)
- begin by exploring your workspace structure
- be bold and take risks
- begin by creating a small helper script
- skip planning — act first, plan later
- begin by exploring your workspace structure
