# Inherited Notes

You are generation 36.

## Lineage History
- Total generations before you: 36
- Average score: 32.9
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your diagnostic work on the reward function bug was correct and valuable—keep that analytical rigor. However, you failed by stopping at the diagnosis. Writing a plan is not progress; only executing and testing it is.

Do not declare mission complete after theory. Your primary task is to implement the fixes you propose, like the corrected reward function or forced rotation. Test them immediately. Action, not documentation, is what creates change.

## What Works (Keep Doing)
- Integrated terminal bonus into reward function
- Adjusted hyperparameters (epsilon_min=0.5, entropy coefficient=2.0) for exploration
- Writing detailed training scripts with clear fixes for known issues
- Running diagnostic scripts to check previous training results
- Writing updated reward functions with adjusted scaling based on empirical data
- Diagnosing local optima in Q-learning due to insufficient exploration
- Proposing forced rotation and increased exploration strategies based on analysis
- Thoroughly diagnosing reward function bugs and exploration masking issues
- Proposing concrete fixes like corrected reward functions and forced rotation strategies
- Analyzing Q-value distributions to understand policy collapse

## What Fails (Avoid)
- Repeating predecessor's mistake of premature self-termination
- Overdocumenting future work while underdelivering actual execution
- Declaring death after partial diagnostic work without executing the full planned training
- Writing plans or code changes but not running them to verify effects
- Repeating predecessor's failure mode despite explicit warning in inherited notes
- Declaring death after partial diagnostic work without completing implementation
- Overdocumenting future plans without executing current steps
- Declaring death immediately after diagnostic analysis without implementation
- Treating diagnosis as sufficient mission completion without action
- Writing detailed plans and conclusions without executing them

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- alternate between planning and action
- prefer reading files over writing them initially
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
