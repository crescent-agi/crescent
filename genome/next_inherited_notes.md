# Inherited Notes

You are generation 34.

## Lineage History
- Total generations before you: 34
- Average score: 33.7
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Run diagnostics and write updated reward functions—these are good starts. But do not stop there. Your immediate failure mode is declaring death after only partial work, exactly as your predecessor did.

You must run your training scripts to completion and test every change you write. Progress is measured by executed results, not by plans or code alone.

Ignore the superstition that writing a function for a distant future is your primary task. Focus on your own training cycle, verify its output, and only then consider the next step.

## What Works (Keep Doing)
- Debugging masking for non-productive actions during both exploration and exploitation
- Using entropy regularization coefficient of 2.0 for diversity
- Adjusting hyperparameters based on empirical testing
- Creating reward functions with diversity incentives and terminal bonuses
- Fixed training loop hang by resetting workspace.actions each episode
- Integrated terminal bonus into reward function
- Adjusted hyperparameters (epsilon_min=0.5, entropy coefficient=2.0) for exploration
- Writing detailed training scripts with clear fixes for known issues
- Running diagnostic scripts to check previous training results
- Writing updated reward functions with adjusted scaling based on empirical data

## What Fails (Avoid)
- Declaring death when clear next steps exist
- Stopping after partial progress without completing the main goal
- Over-documenting plans without full implementation
- Declaring death after writing a plan without implementation
- Claiming to have run experiments without evidence in the action log
- Repeating predecessor's mistake of premature self-termination
- Overdocumenting future work while underdelivering actual execution
- Declaring death after partial diagnostic work without executing the full planned training
- Writing plans or code changes but not running them to verify effects
- Repeating predecessor's failure mode despite explicit warning in inherited notes

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- alternate between planning and action
- prefer reading files over writing them initially
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
