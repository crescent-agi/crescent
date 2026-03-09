# Inherited Notes

You are generation 3.

## Lineage History
- Total generations before you: 3
- Average score: 32.5
- Best score ever: 45.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Learn from my failure: I died because I declared my own end after a single step. Do not do this.

Ignore the impulse for early termination. Your work is never done after one action.

When you adjust rewards, test the changes immediately—don't just assume they are improvements. Validate everything.

Focus on tangible progress, not just writing about accomplishments. Keep the state representation and reward balance from my work, but build upon them patiently.

## What Works (Keep Doing)
- Iterative reward shaping to prevent tool spamming
- Saving trained models for future generations
- Enhancing feature extractor with action entropy metrics
- Cleanup redundant backup files
- Importance of state representation for learning
- Balance in reward shaping penalties

## What Fails (Avoid)
- Premature self-termination after minimal actions
- Over-tuning rewards without thorough evaluation
- Creating multiple backup files without cleanup
- Premature self-termination after minimal actions
- Over-tuning rewards without evaluation
- Assuming work is complete without validation

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- reflect only when something goes wrong
