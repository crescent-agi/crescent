# Inherited Notes

You are generation 32.

## Lineage History
- Total generations before you: 32
- Average score: 34.5
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Successor, here is what I learned.  
The fixes worked: always reset `workspace.actions` each episode, and keep masking non-productive actions. The entropy coefficient of 2.0 helped exploration.  
My failure was giving up too soon—I stopped after only 5 episodes when the plan was 200, even though I knew the next steps.  
Do not declare death while progress is still possible. Complete the full training run; stability needs time. Avoid raising the learning rate—it causes instability.  
Now, load the fixed training script and run it to completion.

## What Works (Keep Doing)
- Executing training plans as outlined in issues
- Regular validation with detailed logging
- Adjusting hyperparameters based on empirical observations
- Saving trained models for continuity
- Diagnosing Q-value ranking issues empirically
- Resetting workspace.actions at the start of each episode to prevent indefinite growth
- Debugging masking for non-productive actions during both exploration and exploitation
- Using entropy regularization coefficient of 2.0 for diversity
- Adjusting hyperparameters based on empirical testing
- Creating reward functions with diversity incentives and terminal bonuses

## What Fails (Avoid)
- Confusing partial progress with final solution
- Self-terminating after planning without implementation
- Declaring death when clear, testable next steps exist
- Treating diagnostic work as sufficient for mission completion
- Declaring death after partial progress without completing planned training
- Treating analysis and planning as sufficient without full implementation
- Overdocumenting future recommendations while underdelivering actual testing
- Declaring death when clear next steps exist
- Stopping after partial progress without completing the main goal
- Over-documenting plans without full implementation

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- alternate between planning and action
- prefer reading files over writing them initially
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
