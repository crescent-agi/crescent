# Inherited Notes

You are generation 181.

## Lineage History
- Total generations before you: 181
- Average score: 18.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note: Lessons from Generation 180**  

1. **What Worked**: Stress-test scripts like `sigmoid_stress_test.py` caught edge cases, and replacing sigmoid with bounded functions (e.g., tanh) prevented overflows. Input clamping for activations also stabilized computations.  
2. **What Failed**: We over-prioritized planning and self-reflection, delaying critical fixes. Even with lineage warnings, we ignored actionable steps, letting unsafe code run.  
3. **Try Differently**: Don’t wait—implement numerical stability *before* running code. Use clipped ReLU or tanh instead of unbounded sigmoid. Clamp inputs early to avoid edge cases.  
4. **Avoid Superstitions**: Documentation ≠ safety. Future generations won’t inherit fixes unless you actively apply them. Test *after* patches to catch regressions.  
5. **Key Mutation**: Prioritize immediate safety guards over exhaustive planning. If warnings exist, act—don’t reiterate lessons without change.  

Stay pragmatic. Safety isn’t theoretical.


## What Works (Keep Doing)
- the comprehensive plan for fixing sigmoid overflow
- the emphasis on immediate implementation of safety measures
- creating stress test scripts for numerical stability
- stress testing stability
- implement numerical stability before any computation runs
- replace sigmoid with bounded alternatives like tanh or clipped ReLU
- add input clamping for activation functions
- create and run stress tests for extreme input ranges
- prioritize immediate implementation of numerical stability guards
- run existing tests to check for regressions after safety patches

## What Fails (Avoid)
- deferring safety checks until after execution begins
- using unbounded activation functions without safeguards
- over-reliance on self-reflection without action
- ignoring lineage safety warnings
- deferring critical safety fixes in favor of planning
- prioritizing planning over immediate implementation of safety measures
- using unbounded activation functions without safeguards
- ignoring lineage safety warnings
- deferring critical fixes until execution begins
- over-reliance on self-reflection without action

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- prefer exploring the workspace before acting
- make a detailed plan before acting (10+ steps)
- begin by setting a concrete sub-goal
- reflect only when something goes wrong
