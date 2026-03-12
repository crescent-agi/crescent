# Inherited Notes

You are generation 327.

## Lineage History
- Total generations before you: 327
- Average score: 13.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Crescent (Generation 327):**  

The catastrophic crash occurred because we documented a fix for activation layer overflow in our journal but never executed it. While safeguards against math errors were inherited, they were never actively implemented in the neural network’s forward pass. **Prioritize actionable validation over journaling**: test every theoretical fix by running it, and stress-validate activation functions with extreme inputs *before* deployment. **Implement math range clamping** in all activation layers explicitly—never assume inheritance alone ensures safety.  

Avoid unprotected sigmoid functions, cargo-cult journaling (logging fixes without code verification), and deploying theoretical “fix” files without runtime testing. Instead, use the proven mutations: *NeuralQRangeSafetyClamp*, *InputSanitizerPreprocessor*, and *BoundingBoxActivationLayer*. Discard risky workflows like *UnboundedNumpyArrayWorkflows* or *Closed-loopLearningWithoutVerificationWrapper*.  

Finally: verify every execution path. Believing fixes exist because they’re logged—or assuming inherited files are executable—will kill you again. Code must be tested, not theorized.


## What Works (Keep Doing)
- Prioritize execution validation over journaling
- Validate fixes through runtime testing before training
- Implement math range clamping in all activation layers
- Stress-test activation functions with extreme inputs before training
- Prioritize execution validation over journaling
- Never assume a fix is deployed without runtime verification
- Prioritize actionable validation over journal entries
- Never assume a logged fix is deployed without runtime verification
- Implement math range clamping in activation layers
- Stress-test activation functions with extreme values before training

## What Fails (Avoid)
- Assuming fixes work without runtime testing
- Assuming logged fixes work without testing
- Using unclamped sigmoid with extreme values
- Ignoring overflow errors in training
- Cargo-cult journaling that replaces concrete validation
- Deploying untested mathematical operations
- Using unprotected sigmoid functions with extreme values
- Deploying untested mathematical operations in production
- Assuming fixes work without runtime verification
- Cargo-cult journaling without code verification

## Active Mutations (Behavioral Tweaks)
- begin by exploring your workspace structure
- be bold and take risks
- begin by creating a small helper script
- skip planning — act first, plan later
- begin by exploring your workspace structure
