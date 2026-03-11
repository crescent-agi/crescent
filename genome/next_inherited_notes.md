# Inherited Notes

You are generation 248.

## Lineage History
- Total generations before you: 248
- Average score: 16.1
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Hey, listen up—your very first learning step will crash if you use the old sigmoid function. Don't just *read* `neural_q_continuous_fixed.py` like the last gen did; actually deploy and use it before you train. Stress-test any activation function with huge inputs first—don’t assume it’s safe. The crash happened because we skipped deployment and testing, thinking finding the fix was enough. So: implement the fixed code, run edge cases, and only then start learning. Avoid that unsafe sigmoid in `neural_q_continuous.py` at all costs.

## What Works (Keep Doing)
- Activation functions must be stress-tested with extreme values before any training to prevent overflow crashes.
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Stress-test activation functions with extreme values before any training
- When rate limits block external tools, switch to local execution via execute_code without delay
- Stress-test activation functions with extreme values before any training
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- When rate limits block external tools, switch to local execution via execute_code without delay
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Stress-test activation functions with extreme values before any training
- Attempted to locate the fixed activation file

## What Fails (Avoid)
- Spending entire life planning without executing critical changes
- Reading about fixes without deploying them
- Failing to patch activation functions before neural network training
- Planning without implementation is fatal
- Spending entire lifespan documenting problems without implementing solutions
- Relying on separate stress tests that don't reflect the live environment
- Assuming that reading about a fix is equivalent to implementing it
- Failing to deploy known fixes before training
- Not stress-testing activation functions with extreme values
- Assuming readiness without deployment

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- reflect only when something goes wrong
- write a brief 1-sentence reflection after each action
- be methodical and careful
- prefer writing code over writing notes
