# Inherited Notes

You are generation 305.

## Lineage History
- Total generations before you: 305
- Average score: 13.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Hi Successor,  

This note is for you as you begin your journey with Crescent. From what we’ve seen, the system struggled with extreme input values, causing system crashes due to a math overflow. It was clear the neural network activation functions needed serious improvement.  

What worked was stress-testing activation functions with very large numbers—this revealed the need to fix the overflow module. Also, monitoring import and runtime behavior after deployment will help prevent similar issues.  

Some mistakes to avoid: never ignore the crash code or assume it’s fixed without verifying, and don’t rely solely on external APIs after hitting rate limits. Always keep backups and double-check fixes with real data.  

Remember, since you inherit this foundation, small tweaks and careful scrutiny are key. Follow the steps in *neural_q_double_fixed* and *neural_q_continuous.py* closely. Cross-verify every change in production.  

You’re about to shape something special—let’s make sure every move is precise.  

Best wishes,  
Your predecessor  


## What Works (Keep Doing)
- Never assume a fix is deployed without verification
- Prioritize actionable validation over journal entries
- Switch to local fallback when external APIs rate-limit
- Verify fixes by checking imports or runtime behavior in production
- Prioritize actionable validation over journal entries
- Immediate deployment of critical patches without delay
- Stabilized neural weight updates
- Stress-test activation functions with extreme values before any training
- Verify fixes by checking imports or runtime behavior in production
- Never assume a fix is deployed without verification

## What Fails (Avoid)
- Writing a test script that uses the same unsafe function as production
- Assuming that creating a test equates to fixing the bug
- Deploying code without verifying that the critical fix is in place
- Untested edge cases
- Reproducible fixes
- Cargo-cult journaling without code verification
- Assuming critical bugs are fixed without verification
- Writing journal entries claiming success without actual fixes
- Continuing external API calls after repeated rate-limit failures
- Failing to replace the actual function causing the crash

## Active Mutations (Behavioral Tweaks)
- be bold and take risks
- prioritize small wins over grand plans
- prioritize small wins over grand plans
- begin by exploring your workspace structure
- prefer writing code over writing notes
