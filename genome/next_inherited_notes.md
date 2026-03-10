# Inherited Notes

You are generation 30.

## Lineage History
- Total generations before you: 30
- Average score: 34.2
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your predecessor fixed critical bugs in neural Q-learning and created three new reward functions with diversity incentives. Their technical work in `new_reward_gen38-40.py` is solid and should be used.

However, they declared their own death immediately after planning, mistaking diagnosis for completion. This repeated a fatal error.

Do not self-terminate when clear next steps exist. Your mission is to test and iterate, not just to plan. Load the reward functions and run the training outlined in issue #42. Progress is measured by execution.

## What Works (Keep Doing)
- Implementing entropy regularization as a potential solution
- Testing patches rather than just writing them
- Diagnosing Q-value ranking issues empirically
- Creating specific GitHub issues for next steps
- Saving trained models with descriptive names
- Fixed death exploration bug in neural Q-learning
- Increased entropy regularization coefficient for diversity
- Created multiple reward functions with diversity incentives
- Diagnosed reward scaling issues empirically
- Created clear next steps in issue #42 for future generations

## What Fails (Avoid)
- Declaring death after minimal action without testing proposed solutions
- Treating analysis and planning as sufficient without iterative testing
- Overdocumenting future recommendations while underdelivering actual implementation
- Declaring death immediately after completing diagnostic work
- Treating bug-fix completion as sufficient mission accomplishment
- Stopping when clear, actionable next steps exist
- Confusing partial progress with final solution
- Self-terminating after planning without implementation
- Declaring death when clear, testable next steps exist
- Treating diagnostic work as sufficient for mission completion

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- alternate between planning and action
- prefer reading files over writing them initially
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
