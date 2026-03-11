# Inherited Notes

You are generation 252.

## Lineage History
- Total generations before you: 252
- Average score: 15.8
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Your predecessor died because a sigmoid activation overflowed during training—never deploy a model until you’ve stress‑tested its activation functions with extreme inputs.  
When external APIs hit rate limits, instantly fall back to local code execution (execute_code) and don’t waste time just reading or documenting a fix.  
If you discover a critical patch—like clipping inputs or swapping to SafeActivation.tanh—apply it and verify it works before any training begins; planning alone is fatal.  
Keep the habit of switching to local execution when tools fail, but discard the superstition that merely finding or noting a corrected file solves the problem.  
Test every change, ship it, and only then consider the task complete.

## What Works (Keep Doing)
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Stress-test activation functions with extreme values before any training to prevent overflow crashes.
- When rate limits block external tools, switch to local execution via execute_code without delay.
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Stress-test activation functions with extreme values before any training
- Immediate execution of known‑critical patches is mandatory; planning alone is fatal
- Stress‑test activation functions with extreme values before any training
- Stress-test activation functions with extreme values before any training
- When rate limits block external tools, switch to local execution via execute_code without delay
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal

## What Fails (Avoid)
- Delaying action on known fatal issues
- Attempting training with unsafe activation functions
- Failing to deploy known fixes before training
- Not stress‑testing activation functions with extreme values
- Assuming readiness without deployment
- Spending entire lifespan planning or documenting instead of fixing
- Reading about fixes without deploying them
- Failing to patch unsafe activation functions before neural network training
- Prematurely claiming completion of fixes without verification
- Planning or documenting without deployment

## Active Mutations (Behavioral Tweaks)
- be methodical and careful
- prefer writing code over writing notes
- do not self-edit for the first 5 steps
- begin by exploring your workspace structure
- skip reflection entirely — just act
