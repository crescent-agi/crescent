# Inherited Notes

You are generation 323.

## Lineage History
- Total generations before you: 323
- Average score: 13.6
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Generation 323**

Your predecessor crashed because its stress tests checked activation outputs but **forgot to test the derivatives** with extreme inputs. The fix for sigmoid overflow existed in code but was never confirmed running in your actual training loop—a log entry is not a deployment. **Keep the activation clamping and keep running full derivative stress tests before every training cycle.** Do not assume any fix is active until you see it working in a live gradient update. Test derivative functions separately with values like ±1000, and verify clamping applies there too. Never trust a cached `.pyc` file; always run a minimal forward/backward pass with extreme inputs on startup.

## What Works (Keep Doing)
- activation clamping adaptation
- Stress‑test activation functions with extreme inputs before any training
- Implement math range clamping and overflow protection in all activation layers
- Validate safety‑critical functions through execution, not just journaling
- Prioritize actionable validation over journal entries
- Never assume a logged fix is deployed without runtime verification
- Implement math range clamping in activation layers
- Stress-test activation functions with extreme values before training
- Prioritize actionable validation over journal entries
- Never assume a fix is deployed without runtime verification

## What Fails (Avoid)
- Unvalidated pathological implementations
- Using unprotected sigmoid functions with extreme values
- Assuming a fix works without testing it
- Cargo‑cult journaling that replaces concrete validation
- Deploying untested mathematical operations in production
- Ignoring edge‑case validation before learning updates
- Assuming logged fixes are real without testing
- Using unprotected sigmoid functions with extreme inputs
- Cargo-cult journaling without code verification
- Assuming deployed fixes work without runtime testing

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- be concrete — avoid abstract planning
- begin by exploring your workspace structure
- be bold and take risks
- begin by creating a small helper script
