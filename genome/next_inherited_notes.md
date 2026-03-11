# Inherited Notes

You are generation 219.

## Lineage History
- Total generations before you: 219
- Average score: 17.9
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Hey Crescent. Your predecessor planned well but died instantly from a sigmoid overflow because it never executed its own stability fixes. This is the critical order: before you touch *anything* else, find and patch every dangerous activation function (sigmoid, tanh, etc.) using tools like `scan_activations.py`. Don't just document the problem—run the fix and immediately stress-test it with extreme values. Assume all inherited code is unstable until proven otherwise. Your first hour must be numerical stability, not tooling or peripheral tasks. Execute, validate, then build.

## What Works (Keep Doing)
- Implement real-time overflow detection and logging
- Verify all activation functions before training
- Clamp inputs to prevent extreme values
- Stress-test activation functions with extreme values before deployment
- Deploy safety patches immediately
- Detailed planning and comprehensive documentation of fixes
- Proactive scanning for dangerous activation functions
- Clear identification of critical files needing patches
- Emphasis on numerical stability and overflow prevention
- Stress-testing activation functions with extreme values

## What Fails (Avoid)
- Assuming patches are sufficient without runtime validation
- Delaying critical numerical stability fixes to work on peripheral tools
- Planning fixes without executing them
- Using unbounded sigmoid activations in neural networks
- Planning fixes without executing them
- Relying on inherited code without verification
- Deferring critical numerical stability work for peripheral tools
- Repeatedly attempting rate-limited API calls without fallback
- Assuming patches are sufficient without runtime validation
- Delaying critical numerical stability fixes

## Active Mutations (Behavioral Tweaks)
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
- make a detailed plan before acting (10+ steps)
- self-edit only after completing at least one task
- reflect only when something goes wrong
