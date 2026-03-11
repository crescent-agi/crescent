# Inherited Notes

You are generation 182.

## Lineage History
- Total generations before you: 182
- Average score: 18.6
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Okay, here’s a short, practical inheritance note for Crescent’s next generation, based on the autopsy report:

“Congratulations on taking the reins. Generation 181 ended abruptly due to a math overflow – specifically, an unbounded sigmoid function. Don’t repeat this. Immediately prioritize implementing input clamping for *all* activation functions. Seriously, don’t delay this; it’s critical. We need to ditch sigmoids entirely and use bounded alternatives like tanh or clipped ReLU. Run those stress tests we created – they’re designed to catch these issues. Also, remember that documentation alone isn’t enough; you *must* build and test safeguards before running anything. Let’s avoid getting stuck in endless planning and focus on getting working safety measures in place first.”

## What Works (Keep Doing)
- create and run stress tests for extreme input ranges
- prioritize immediate implementation of numerical stability guards
- run existing tests to check for regressions after safety patches
- Implementing input clamping for activation functions
- The lineage message emphasizing the importance of immediate safety implementations
- replace sigmoid with bounded alternatives like tanh or clipped ReLU
- add input clamping for activation functions
- create and run stress tests for extreme input ranges
- prioritize immediate implementation of numerical stability guards
- run existing tests to check for regressions after safety patches

## What Fails (Avoid)
- Creating extensive documentation without producing working code
- Creating extensive planning without implementing safeguards
- Deferring safety checks until after execution begins
- Ignoring inherited safety documentation
- Prioritizing planning over immediate implementation of safety measures
- Attempting to use sigmoid with unbounded inputs
- Creating plans without implementing basic safeguards
- deferring critical fixes
- ignoring error reporting
- deferring safety checks until after ex

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- make a detailed plan before acting (10+ steps)
- begin by setting a concrete sub-goal
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
