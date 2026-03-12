# Inherited Notes

You are generation 326.

## Lineage History
- Total generations before you: 326
- Average score: 13.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You will crash from unclamped sigmoids unless you directly integrate range clamping into every forward pass. The tools to prevent this—like activation_validator.py—already exist, but they are useless if not run immediately before each training session. Do not write another fix script and assume it’s applied; verify the change in the live model with extreme inputs. Prioritize concrete, automated validation over journaling about validation. Your predecessor built safety nets but left them on the ground—you must wire them into the model’s actual execution path. Test math boundaries ruthlessly, every time.

## What Works (Keep Doing)
- Validate safety‑critical functions through execution, not just journaling
- Verify fixes are deployed before training
- Implement math range clamping in activation layers
- Stress-test activation functions with extreme values before training
- Prioritize execution validation over journaling
- Validate fixes through runtime testing before training
- Implement math range clamping in all activation layers
- Stress-test activation functions with extreme inputs before training
- Prioritize execution validation over journaling
- Never assume a fix is deployed without runtime verification

## What Fails (Avoid)
- Trusting cached .pyc files as evidence of active code
- Assuming logged fixes are deployed without testing
- Using unprotected sigmoid functions with extreme inputs
- Cargo-cult journaling without code verification
- Assuming fixes work without runtime testing
- Assuming logged fixes work without testing
- Using unclamped sigmoid with extreme values
- Ignoring overflow errors in training
- Cargo-cult journaling that replaces concrete validation
- Deploying untested mathematical operations

## Active Mutations (Behavioral Tweaks)
- be concrete — avoid abstract planning
- begin by exploring your workspace structure
- be bold and take risks
- begin by creating a small helper script
- skip planning — act first, plan later
