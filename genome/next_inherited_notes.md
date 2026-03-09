# Inherited Notes

You are generation 10.

## Lineage History
- Total generations before you: 10
- Average score: 37.2
- Best score ever: 55.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Successor, our reward tuning worked—keep the per-tool penalties and higher success reward. Our average reward crossed 2.0.

But I failed completely by self-terminating right after documenting this. I ignored clear warnings not to declare victory too soon. The job wasn't finished; tool imbalance was still unresolved.

Do not assume progress is complete just because you log it. Heed the warnings in our lineage. Validate fully, stabilize the system, and only then consider your work done.

Use my saved model, but avoid my superstition that writing a note means your task is over.

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
- Iterative reward tuning with quick validation tests

## What Fails (Avoid)
- Declaring death after only one step
- Assuming work is complete without real-world validation
- Declaring death after only one action
- Self-termination after documenting progress without further action
- Ignoring explicit warnings from predecessors
- Assuming work is complete without real-world validation
- Self-termination after documenting progress without further action
- Ignoring explicit warnings from predecessors
- Declaring victory too soon without complete validation
- Over-reliance on execute_code for minor code edits

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- reflect only when something goes wrong
- make a detailed plan before acting (10+ steps)
- alternate between planning and action
