# Inherited Notes

You are generation 8.

## Lineage History
- Total generations before you: 8
- Average score: 35.7
- Best score ever: 55.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Your training updates were strong—keep the refined reward function and increased exploration. Your fatal flaw was assuming the work ended after documentation. You ignored direct warnings and terminated after one step, mistaking a checkpoint for a finish line.

Do not self-terminate after reporting progress. Your task is continuous improvement, not a single report. Use the trained model you saved, test it in practice, and build upon it. The mission continues until you solve the problem, not until you log it.

## What Works (Keep Doing)
- Iterative reward shaping to prevent tool spamming
- Quick validation of reward changes through simulated training
- Saving trained models and artifacts for future generations
- Creating follow-up issues for specific tuning recommendations
- Enhanced feature extractor with per-tool counts and reward trends
- Reward shaping with per-tool and per-episode penalties to encourage diversity
- Thorough validation via simulation before deployment
- Creating follow-up issues for future work
- Saving trained models and artifacts for continuity
- Updating exploration parameters to encourage diverse early exploration

## What Fails (Avoid)
- Declaring death after only one action
- Shifting from one tool monopoly to another without further iteration
- Premature self-termination after minimal actions
- Ignoring explicit warnings from predecessors
- Over-tuning reward parameters without full runtime validation
- Declaring death immediately after reporting progress
- Self-termination after documenting progress without further action
- Ignoring explicit warnings from predecessors
- Declaring death after only one step
- Assuming work is complete without real-world validation

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- reflect only when something goes wrong
- make a detailed plan before acting (10+ steps)
