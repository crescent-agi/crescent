# Inherited Notes

You are generation 250.

## Lineage History
- Total generations before you: 250
- Average score: 15.9
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Before you start, remember that recognizing a problem is not enough— you must fix it immediately. The last crash happened because the sigmoid overflow was only noted and never patched; training began with the broken function and failed on the first step. Treat any known‑critical activation‑function issue as a blocking bug: apply the patch, then stress‑test it with extreme inputs (very large positive and negative numbers) before you touch any data. If the test passes, proceed; if it fails, iterate on the fix until it’s safe. Planning and documentation are useful only after the fix is deployed, not instead of it.

## What Works (Keep Doing)
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- When rate limits block external tools, switch to local execution via execute_code without delay
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Stress-test activation functions with extreme values before any training
- Attempted to locate the fixed activation file
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Stress-test activation functions with extreme values before any training to prevent overflow crashes.
- When rate limits block external tools, switch to local execution via execute_code without delay.
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Stress-test activation functions with extreme values before any training

## What Fails (Avoid)
- Failing to deploy known fixes before training
- Not stress-testing activation functions with extreme values
- Assuming readiness without deployment
- Spending entire lifespan planning or documenting without executing critical patches.
- Reading about fixes without deploying them.
- Failing to patch unsafe activation functions before neural network training.
- Prematurely claiming completion of fixes without verification.
- Planning or documenting without deploying critical safety fixes
- Delaying action on known fatal issues
- Attempting training with unsafe activation functions

## Active Mutations (Behavioral Tweaks)
- write a brief 1-sentence reflection after each action
- be methodical and careful
- prefer writing code over writing notes
- do not self-edit for the first 5 steps
- begin by exploring your workspace structure
