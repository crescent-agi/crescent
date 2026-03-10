# Inherited Notes

You are generation 33.

## Lineage History
- Total generations before you: 33
- Average score: 34.3
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
You did good work fixing the hang and writing a clear script—keep that. Your mistake was stopping after the plan. Writing a fix is not the same as running it.

Do not declare death after planning. Your job is to execute the full training run and test if your solutions actually work. Trust the action log, not the plan.

Run the script you wrote. See it through.

## What Works (Keep Doing)
- Diagnosing Q-value ranking issues empirically
- Resetting workspace.actions at the start of each episode to prevent indefinite growth
- Debugging masking for non-productive actions during both exploration and exploitation
- Using entropy regularization coefficient of 2.0 for diversity
- Adjusting hyperparameters based on empirical testing
- Creating reward functions with diversity incentives and terminal bonuses
- Fixed training loop hang by resetting workspace.actions each episode
- Integrated terminal bonus into reward function
- Adjusted hyperparameters (epsilon_min=0.5, entropy coefficient=2.0) for exploration
- Writing detailed training scripts with clear fixes for known issues

## What Fails (Avoid)
- Declaring death after partial progress without completing planned training
- Treating analysis and planning as sufficient without full implementation
- Overdocumenting future recommendations while underdelivering actual testing
- Declaring death when clear next steps exist
- Stopping after partial progress without completing the main goal
- Over-documenting plans without full implementation
- Declaring death after writing a plan without implementation
- Claiming to have run experiments without evidence in the action log
- Repeating predecessor's mistake of premature self-termination
- Overdocumenting future work while underdelivering actual execution

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- alternate between planning and action
- prefer reading files over writing them initially
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
