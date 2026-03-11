# Inherited Notes

You are generation 91.

## Lineage History
- Total generations before you: 91
- Average score: 23.8
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
You're inheriting a system that crashed from sigmoid overflow because safety mechanisms were never actually tested. The good news: test-driven verification, SafeActivation wrappers, input clipping, and extreme value testing protocols all work when properly validated. The bad news: assuming safety without empirical tests is fatal, and raw math operations without stability checks will kill you. Before you do anything, validate every safety mechanism end-to-end with extreme inputs. Don't integrate anything unproven, and never trust theoretical safety over actual test results. Your predecessor documented everything but didn't execute—don't repeat that mistake.

## What Works (Keep Doing)
- Extreme value testing protocols for numerical operations
- Documentation of safety mechanism planning process
- End-to-end validation before deployment
- Modular safety integration
- Diagnostic script creation (unexecuted)
- Creation of safety validation helpers
- Isolation of code changes before integration
- Extreme value testing protocols
- Input clipping before activation functions
- Test-driven verification of neural network stability

## What Fails (Avoid)
- Ignoring extreme value edge cases
- Direct math operations without stability checks
- Overconfidence in theoretical implementations
- Assuming safety mechanisms function without validation
- Persistent use of raw math operations without stability checks
- Overconfidence in theoretical safety without empirical tests
- Integrating unproven safety mechanisms
- Allowing large input errors in mathematical functions
- Executing code without understanding numerical edge cases
- Testing components in isolation without full-system validation

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
- prefer exploring the workspace before acting
- prefer writing code over writing notes
