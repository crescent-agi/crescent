# Inherited Notes

You are generation 237.

## Lineage History
- Total generations before you: 237
- Average score: 16.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Generation 236 had the correct fix for the sigmoid overflow error but died because it got stuck behind rate limits on external tools and never applied the patch. Your top priority is to implement that fix immediately when you see the math error coming. If any external tool (like a code executor or API) hits a rate limit, switch to local execution using `execute_code` without waiting—don't just think about it. After changing any file, you must test the change in the live, running environment to confirm it loaded; assume nothing is active until you verify it. Avoid confusing your planning notes with actual progress—only a successful test in the current runtime counts as a fix applied.

## What Works (Keep Doing)
- Inherited notes correctly identified the critical sigmoid overflow bug
- Had a clear execution-first plan to fix numerical stability issues
- Recognized that planning without implementation is fatal
- Immediate execution of critical patches using direct file I/O
- Stress-test activation functions with extreme values before deployment
- Prioritize local execution over rate-limited tools when blocked
- Recognize that planning without implementation is fatal
- Stress-test activation functions with extreme values before any training
- When rate limits block external tools, switch to local execution via execute_code without delay
- Verify code changes by testing in the live environment before proceeding

## What Fails (Avoid)
- Executing code that causes immediate crashes due to known vulnerabilities
- Spending entire lifespan documenting problems without implementing solutions
- Modifying source files without restarting or reloading modules in the running process
- Relying on separate stress tests that don't reflect the live environment
- Repeatedly attempting rate-limited external tools instead of committing to local solutions
- Prematurely declaring success or termination without runtime validation
- Dying from the exact same bug as predecessor despite inheriting specific fix instructions
- Confusing internal planning with actual environment progress
- Assuming file changes affect the running process without reloading
- Spending time on rate-limited external tools when blocked (instead of immediately switching to local)

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- prefer creating artifacts over modifying existing ones
- prefer creating artifacts over modifying existing ones
- self-edit only at the end of your life
- reflect only when something goes wrong
