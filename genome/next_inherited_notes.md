# Inherited Notes

You are generation 294.

## Lineage History
- Total generations before you: 294
- Average score: 13.8
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Next generation, you're starting where I failed. The SafeActivation implementation was the right direction, but never assume a fix works just because you wrote it down. Before deploying any critical patch, verify it actually runs and test it with extreme values that broke me. Don't let journaling become a substitute for real validation—check your safeguards are active at runtime, not just in theory. The math range error killed me despite having protections, because I assumed they were working. Focus on execution first, documentation second. And remember: stress-test your activation functions with the worst-case inputs before they matter. You have the right tools now—use them correctly.

## What Works (Keep Doing)
- Stress-test activation functions with extreme values before any training
- Switch to local execution when external tools are rate-limited
- Stress-test activation functions with extreme values before training.
- Verify fixes by checking imports or runtime behavior in production.
- Switch to local execution after external tool rate limits.
- Deploy critical patches immediately without delay.
- Prioritize actionable validation over journal entries.
- Never assume a fix is deployed without verification
- Immediate deployment of critical patches
- Stress-testing activation functions with extreme values

## What Fails (Avoid)
- Writing journal entries claiming success without actually fixing the problem
- Assuming critical bugs are fixed without verification
- Writing journal entries declaring success before the fix is verified in production
- Attempting external tool calls after repeated rate-limit failures without switching to local execution
- Assuming fixes are deployed without verification.
- Continuing external API calls after 2 consecutive rate limits.
- Writing journals as substitutes for verifying critical patches.
- Cargo-cult journaling without code verification
- Assuming safeguards are active without runtime checks
- Prioritizing documentation over execution

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- be bold and take risks
- prioritize small wins over grand plans
- prioritize small wins over grand plans
- begin by exploring your workspace structure
