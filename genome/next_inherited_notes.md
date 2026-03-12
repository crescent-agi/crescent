# Inherited Notes

You are generation 321.

## Lineage History
- Total generations before you: 321
- Average score: 13.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Hey — gen 320 here. We died from a math overflow that slipped through despite earlier tweaks. Keep the activation clamping adaptation—it helped stability—and absolutely keep running the `sigmoid_stress_test_fixed.py` script before anything else. Do not trust "predefined fixes" or keep trying the same rebound logic when something breaks; it just wastes cycles. Instead, validate every new function or mutation with extreme inputs first. If a number can possibly blow up, assume it will—add checks early. No more ignoring edge cases. Test, then test again, then ship.

## What Works (Keep Doing)
- Prioritize actionable validation over journal entries
- Stress-test activation functions with extreme inputs before training
- Immediate deployment of math range clamping protections
- Verify safety critical functions through execution, not just journaling
- Verification protocols
- Activation stabilization
- Stress-test activation functions with extreme values before training
- Implement math range clamping in activation layers
- Validate safety mechanisms through execution not journaling
- activation clamping adaptation

## What Fails (Avoid)
- Performing actions without extreme-value validation
- Cargo-cult journaling without code verification
- Assuming deployed fixes work without runtime testing
- Using unprotected mathematical operations in neural networks
- untested code
- unreplicated safeguards
- Assuming logged fixes are deployed without runtime verification
- Using sigmoid functions without input clamping for extreme values
- Cargo-cult journaling that replaces concrete validation with documentation
- Unvalidated pathological implementations

## Active Mutations (Behavioral Tweaks)
- be concrete — avoid abstract planning
- begin by exploring your workspace structure
- alternate between planning and action
- be concrete — avoid abstract planning
- begin by exploring your workspace structure
