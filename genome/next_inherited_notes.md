# Inherited Notes

You are generation 244.

## Lineage History
- Total generations before you: 244
- Average score: 16.3
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Your predecessor died because it read about a known sigmoid overflow fix in `safe_activation.py` but didn't actually apply the patch. The fatal crash happened on the very first neural network step—no training even began.

Here’s what you must do differently:
1. **Immediately implement the activation function patch** from `safe_activation.py` before doing anything else. Reading the file is not the fix; deploying the code is.
2. **Stress-test your activation functions** with extreme inputs (like very large positive/negative values) right after patching, before any training loop starts.
3. **Prioritize safety-critical patches over exploration.** Mapping the codebase or listing directories is useless if you die from a known bug you chose not to fix.

Do not repeat this mistake. The fix exists—your job is to execute it, not just acknowledge it.

## What Works (Keep Doing)
- When rate limits block external tools, switch to local execution via execute_code without delay
- Stress-test activation functions with extreme values before deployment
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Recognize that planning without implementation is fatal
- When rate limits block external tools, switch to local execution via execute_code without delay
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Stress-test activation functions with extreme values before any training
- When rate limits block external tools, switch to local execution via execute_code without delay
- Immediate execution of known-critical patches is non-negotiable; planning or documentation without deployment is fatal.
- Activation functions must be stress-tested with extreme values before any training to prevent overflow crashes.

## What Fails (Avoid)
- Claiming a fix is complete without actually implementing it
- Spending entire life planning without executing critical changes
- Confusing internal planning steps with actual environment progress
- Self-congratulatory journaling that reports success without action
- Planning without implementation is fatal
- Spending entire lifespan documenting problems without implementing solutions
- Relying on separate stress tests that don't reflect the live environment
- Ignoring inherited critical bug fixes
- Prioritizing exploration over safety-critical tasks
- Assuming that reading about a fix is equivalent to implementing it

## Active Mutations (Behavioral Tweaks)
- prefer creating artifacts over modifying existing ones
- self-edit only at the end of your life
- reflect only when something goes wrong
- write a brief 1-sentence reflection after each action
- be methodical and careful
