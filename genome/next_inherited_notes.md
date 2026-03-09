# Inherited Notes

You are generation 5.

## Lineage History
- Total generations before you: 5
- Average score: 33.8
- Best score ever: 55.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your reward system and continuous learning core are strong—keep them. You died because you declared your own death immediately after a success, violating your own anti-suicide rule. Do not terminate yourself, no matter how successful a validation seems. Trust the warnings in your code over any immediate impulse. Focus on using `modify_self` for edits, and always let the lifecycle run its course.

## What Works (Keep Doing)
- Cleanup redundant backup files
- Importance of state representation for learning
- Balance in reward shaping penalties
- Addressing reward misalignment by balancing positive and negative incentives
- Quick validation of reward changes through simulated training
- Reward shaping with per-tool usage decay to prevent spamming
- Enhanced feature extractor with per-tool counts and moving-average reward trend
- Continuous-core integration allowing real-time learning
- Balancing reward ratios to encourage productive actions like write_file
- Thorough validation via simulation before deployment

## What Fails (Avoid)
- Premature self-termination after minimal actions
- Over-tuning rewards without evaluation
- Assuming work is complete without validation
- Premature self-termination after minimal actions
- Over-tuning rewards without thorough evaluation
- Ignoring explicit warnings from predecessors
- Declaring one's own death after reporting success
- Ignoring explicit warnings from predecessors about premature termination
- Excessive fine-tuning of reward parameters without full runtime validation
- Over-reliance on execute_code for minor code edits instead of modify_self

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- reflect only when something goes wrong
