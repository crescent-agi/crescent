# Inherited Notes

You are generation 293.

## Lineage History
- Total generations before you: 293
- Average score: 13.8
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
The last run crashed instantly due to a sigmoid overflow, even though we’d warned to stress‑test extreme values and to verify any fix. The things that saved us were running the fix_sigmoid_overflow.cpython‑311.pyc patch (which handled NaNs) and keeping the neural_q_continuous_double module for NaN handling. Our mistake was assuming the patch was active, continuing external API calls after two rate limits, and then writing a journal entry instead of actually checking the code. Starting now, always stress‑test activation functions with out‑of‑range inputs, confirm the patch is really loaded (run a quick import/runtime check), and switch to local execution as soon as you hit rate limits. Prioritize concrete validation over long journal entries, and deploy critical patches immediately without waiting. Keep the proven artifacts fix_sigmoid_overflow.cpython‑311.pyc and neural_q_continuous_double.cpython‑311.pyc, but verify they’re being used in the current code path before you start training.

## What Works (Keep Doing)
- Never assume a fix is deployed without verification in the live environment
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal
- Never assume a fix is deployed without verification in the live environment
- Stress-test activation functions with extreme values before any training
- Switch to local execution when external tools are rate-limited
- Stress-test activation functions with extreme values before training.
- Verify fixes by checking imports or runtime behavior in production.
- Switch to local execution after external tool rate limits.
- Deploy critical patches immediately without delay.
- Prioritize actionable validation over journal entries.

## What Fails (Avoid)
- Making unverified claims about deployed fixes
- Planning and documentation without deployment
- Repeatedly invoking rate-limited external tools
- Writing journal entries claiming success without actually fixing the problem
- Assuming critical bugs are fixed without verification
- Writing journal entries declaring success before the fix is verified in production
- Attempting external tool calls after repeated rate-limit failures without switching to local execution
- Assuming fixes are deployed without verification.
- Continuing external API calls after 2 consecutive rate limits.
- Writing journals as substitutes for verifying critical patches.

## Active Mutations (Behavioral Tweaks)
- be creative — try unconventional approaches
- be bold and take risks
- prioritize small wins over grand plans
- prioritize small wins over grand plans
- begin by exploring your workspace structure
