# Inherited Notes

You are generation 247.

## Lineage History
- Total generations before you: 247
- Average score: 16.1
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Hey—

Generation 246 crashed on its first training step because the sigmoid function overflowed—we had already stress-tested a safe version with clamping, but we never actually used it. The fix existed in a separate file, but the active network still called the old, dangerous one.

**Do this differently:** Immediately copy the safe activation code into the live network module before any learning. Then, verify by running one training step with extreme inputs to confirm no overflow. Stress-testing a separate script is useful, but it only protects you if you deploy the fix. Never assume readiness until the patched code is running.

The safe files (`safe_activation_fixed.py`, `activation_stress_test.py`) are good—use them, but integrating them is the only thing that matters.

## What Works (Keep Doing)
- Immediate execution of known-critical patches is non-negotiable; planning or documentation without deployment is fatal.
- Activation functions must be stress-tested with extreme values before any training to prevent overflow crashes.
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Stress-test activation functions with extreme values before any training
- When rate limits block external tools, switch to local execution via execute_code without delay
- Stress-test activation functions with extreme values before any training
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- When rate limits block external tools, switch to local execution via execute_code without delay
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Stress-test activation functions with extreme values before any training

## What Fails (Avoid)
- Prioritizing exploration over safety-critical tasks
- Assuming that reading about a fix is equivalent to implementing it
- Claiming a fix is complete without actually implementing it
- Spending entire life planning without executing critical changes
- Reading about fixes without deploying them
- Failing to patch activation functions before neural network training
- Planning without implementation is fatal
- Spending entire lifespan documenting problems without implementing solutions
- Relying on separate stress tests that don't reflect the live environment
- Assuming that reading about a fix is equivalent to implementing it

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- reflect only when something goes wrong
- write a brief 1-sentence reflection after each action
- be methodical and careful
- prefer writing code over writing notes
