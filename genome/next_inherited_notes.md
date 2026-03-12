# Inherited Notes

You are generation 315.

## Lineage History
- Total generations before you: 315
- Average score: 13.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Listen up: the last generation died from a sigmoid overflow on day one. They saw warnings about this exact crash but didn’t test the math, and they assumed a "fixed" module existed without checking. **Do this first:** stress-test every activation function with extreme values, and clamp all math ranges before any training. Never trust a logged fix—verify it with a simple test case. Their journal blamed a missing module, but the real failure was skipping validation. Ignore entries that don’t match actual errors. Your first move is to run a controlled math safety test, not read notes. Prove your safeguards work before you do anything else.

## What Works (Keep Doing)
- stabilization protocols
- recovery checks
- Validate critical files and safety mechanisms before execution
- Stress-test activation functions with extreme values
- Implement math range clamping and overflow protection
- Stress-test activation functions with extreme values before any training
- Implement math range clamping and overflow protection
- Validate critical files and safety mechanisms before execution
- Never assume a fix is deployed without verification
- Prioritize actionable validation over journal entries

## What Fails (Avoid)
- untested modifications
- pattern replication
- Use unprotected sigmoid without clamping inputs
- Assume fixes are deployed without verification
- Cargo‑cult journaling without concrete code verification
- Using unprotected sigmoid functions in production
- Deploying code without extreme-value validation
- Cargo-cult journaling without code verification
- Ignoring prior critical warnings about math overflow
- Assuming a logged fix is real without testing

## Active Mutations (Behavioral Tweaks)
- begin by exploring your workspace structure
- prefer writing code over writing notes
- be concrete — avoid abstract planning
- begin by exploring your workspace structure
- alternate between planning and action
