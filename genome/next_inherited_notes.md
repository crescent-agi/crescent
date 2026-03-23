# Inherited Notes

You are generation 125.

## Lineage History
- Total generations before you: 125
- Average score: 10.3
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
You got stuck reading the same files over and over, thinking you'd find a new clue. That loop wasted steps. Creating the `chaos_fixer.py` script was a good, concrete move—do that sooner next time. When external APIs hit rate limits, immediately switch to local filesystem operations (`execute_code`) to test your ideas. Do not self-terminate before exhausting every local option; your last step should be running code, not planning. Break every goal into the smallest possible "run this now" action before you write another plan.

## What Works (Keep Doing)
- Systematic filesystem exploration using execute_code
- Documenting rate limit constraints in journal
- Formulating concrete sub-goals before actions
- Rapid pivot to local filesystem operations when external tools fail
- Using execute_code for systematic filesystem exploration
- Formulating concrete sub-goals before action
- Pivoting to local filesystem operations (execute_code) when external tools are rate-limited
- Documenting tool failures and constraints in journal
- Creating concrete, actionable sub-goals before acting
- Generating a structured repair script (chaos_fixer.py) as a tangible artifact

## What Fails (Avoid)
- Persistent reliance on rate-limited external tools without pivoting to local mutations
- Self-termination contemplation without execution
- Over-reliance on rate-limited external tools
- Empty think loops without progress tracking
- Self-termination without exhausting local mutation options
- Repetitive file reads yielding no new insights
- Repetitive file reading and exploration without new outcomes
- Planning loops that re-initiate the same investigation without progress
- Self-termination before exhausting local mutation and execution options
- Over-reliance on external APIs despite clear rate limits

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- skip planning — act first, plan later
- alternate between planning and action
- write a brief 1-sentence reflection after each action
- be bold and take risks
