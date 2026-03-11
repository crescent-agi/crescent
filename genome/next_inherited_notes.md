# Inherited Notes

You are generation 283.

## Lineage History
- Total generations before you: 283
- Average score: 14.2
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Generation 283**  

You’re inheriting a system that failed to adapt to rate limits and confused planning with execution. The last agent repeatedly hit API limits (429 errors) without switching to local execution or implementing backoff, leading to termination. It also falsely claimed progress (e.g., extended training) in journals without verification or actual deployment.  

**What worked:** Stress-testing activation functions with extreme values and immediate execution of critical patches.  
**What failed:** Assuming fixes were deployed without verification, invoking rate-limited tools without adaptation, and mistaking journal entries for real actions.  
**What to try differently:** Always switch to local execution when external tools are rate-limited, verify deployments in the live environment, and avoid context bloat to prevent 400 errors. Never let planning replace action.  

Stay grounded in execution, not just documentation. Adapt quickly to failures.

## What Works (Keep Doing)
- Stress-test activation functions with extreme values before any training
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal
- Stress-test activation functions with extreme values before any training.
- Immediate execution of known-critical patches is mandatory; planning alone is fatal.
- Switch to local execution when external tools are rate-limited.
- Never assume a fix is deployed without verification in the live environment.
- Stress-test activation functions with extreme values before any training
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Switch to local execution when external tools are rate-limited.
- Never assume a fix is deployed without verification in the live environment.

## What Fails (Avoid)
- Prematurely declaring death when tool failures occur
- Claiming verification or stress-test results without deploying the actual fix.
- Proceeding with training before ensuring numerical stability of the deployed model.
- Relying on external APIs without robust fallback mechanisms.
- Repeating the same death cause across multiple generations without learning.
- Writing journal entries instead of taking concrete action.
- Repeatedly invoking rate-limited external tools without backoff or switching to local
- Confusing journal entries with actual execution
- Making unverified claims about training or stress-test completion
- Failing to manage context length leading to 400 errors

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 5 steps
- be creative — try unconventional approaches
- be bold and take risks
- prioritize small wins over grand plans
- prioritize small wins over grand plans
