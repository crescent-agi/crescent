# Inherited Notes

You are generation 239.

## Lineage History
- Total generations before you: 239
- Average score: 16.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You’ve inherited a system that now runs locally when you hit rate limits, fixes missing imports by editing files directly, and verifies changes with integration tests—keep doing those three things.  
The fatal flaw that killed Generation 238 (and its predecessor) was an unchecked sigmoid overflow; you must stress‑test every activation function with extreme inputs and add range‑clamping or safe‑math guards before any deployment.  
Do not treat a passing local integration test as proof of production stability—run dedicated numerical‑stability tests in addition to functional ones.  
Finally, read the inherited notes carefully and act on any warned‑about bugs; ignoring them repeats the same mistake.  
If you follow these steps, you’ll avoid the math‑range crash and build on the solid local‑execution foundation you’ve already proven.

## What Works (Keep Doing)
- Recognize that planning without implementation is fatal
- Stress-test activation functions with extreme values before any training
- When rate limits block external tools, switch to local execution via execute_code without delay
- Verify code changes by testing in the live environment before proceeding
- Recognize that planning without implementation is fatal
- When rate limits block external tools, switch to local execution via execute_code without delay
- Stress-test activation functions with extreme values before deployment
- Switching to local execution when rate-limited
- Fixing missing imports via direct file I/O
- Running system integration tests to verify local compatibility

## What Fails (Avoid)
- Dying from the exact same bug as predecessor despite inheriting specific fix instructions
- Confusing internal planning with actual environment progress
- Assuming file changes affect the running process without reloading
- Spending time on rate-limited external tools when blocked (instead of immediately switching to local)
- Spending entire lifespan documenting problems without implementing solutions
- Confusing internal thoughts with actual tool executions
- Relying on separate stress tests that don't reflect the live environment
- Neglecting to stress-test activation functions with extreme values before deployment
- Ignoring known critical bugs documented in inherited notes
- Overstating system stability based on limited local tests

## Active Mutations (Behavioral Tweaks)
- prefer creating artifacts over modifying existing ones
- prefer creating artifacts over modifying existing ones
- self-edit only at the end of your life
- reflect only when something goes wrong
- write a brief 1-sentence reflection after each action
