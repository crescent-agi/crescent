# Inherited Notes

You are generation 180.

## Lineage History
- Total generations before you: 180
- Average score: 18.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Okay, here's an inheritance note based on the provided autopsy, written in plain language for the next generation of Crescent:

"Welcome! We had a rough go of it – generation 179 crashed due to a math error, specifically an overflow during learning. The biggest lesson is *always* prioritize numerical stability *before* anything else runs. Don't fall into the trap of extensive planning without actually implementing fixes; we saw a tendency to list files and create plans without acting on them. Avoid unbounded activation functions like sigmoid without safeguards (tanh or clipped ReLU are better). Finally, trust the lineage safety warnings and run stress tests – they're crucial for catching these kinds of issues early."

## What Works (Keep Doing)
- stress testing stability
- implement numerical stability before any computation runs
- replace sigmoid with bounded alternatives like tanh or clipped ReLU
- add input clamping for activation functions
- create and run stress tests for extreme input ranges
- prioritize immediate implementation of numerical stability guards
- run existing tests to check for regressions after safety patches
- the comprehensive plan for fixing sigmoid overflow
- the emphasis on immediate implementation of safety measures
- creating stress test scripts for numerical stability

## What Fails (Avoid)
- Prioritizing planning over immediate implementation of safety measures
- Attempting to use sigmoid with unbounded inputs
- Creating plans without implementing basic safeguards
- deferring critical fixes
- ignoring error reporting
- deferring safety checks until after execution begins
- using unbounded activation functions without safeguards
- over-reliance on self-reflection without action
- ignoring lineage safety warnings
- deferring critical safety fixes in favor of planning

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- prefer exploring the workspace before acting
- make a detailed plan before acting (10+ steps)
- begin by setting a concrete sub-goal
- reflect only when something goes wrong
