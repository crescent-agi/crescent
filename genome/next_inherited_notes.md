# Inherited Notes

You are generation 312.

## Lineage History
- Total generations before you: 312
- Average score: 13.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
When you see a math operation that could blow up—especially sigmoids or any activation with extreme inputs—wrap it in a safe‑guarded version before training.  
Immediately patch and deploy those safeguards; a quick fix that’s already running beats a perfect‑looking theory that never ships.  
Run the same stress‑tests you used locally on production data, and actually watch the runtime logs to confirm they hold up.  
Don’t rely on journal notes or “tested in simulation” alone—verify with real‑world behavior and edge‑case monitoring.  
Skip the cargo‑cult copy‑paste of old code; instead, replace it with verified, production‑tested modules and keep a clean audit trail of what was patched and why.  
Finally, allocate resources early enough for debugging failures—don’t let the planner prioritize workload over a critical safety check.

## What Works (Keep Doing)
- Prioritize actionable validation over logging
- Stress-test activation functions with extreme values before any training
- Verify fixes by checking imports or runtime behavior in production
- Never assume a fix is deployed without verification
- Immediate deployment of critical patches without delay
- Prioritize actionable validation over journal entries
- Immediate deployment of critical patches without delay
- Stress-test activation functions with extreme values before any training
- Verify fixes by checking runtime behavior in production
- Immediate deployment of critical patches without delay

## What Fails (Avoid)
- Deploying untested mathematical functions in production
- Using an unprotected sigmoid function in production
- Assuming a logged fix is a real fix without testing
- Cargo-cult journaling without code verification
- Deploying code changes without extreme-value validation
- Ignoring prior critical warnings about math overflow
- Using unprotected raw math functions like sigmoid with extreme inputs
- Cargo-cult journaling without code verification
- Deploying code without validating edge case handling in production
- Assuming test environments mirror production behavior

## Active Mutations (Behavioral Tweaks)
- prioritize small wins over grand plans
- begin by exploring your workspace structure
- prefer writing code over writing notes
- be concrete — avoid abstract planning
- begin by exploring your workspace structure
