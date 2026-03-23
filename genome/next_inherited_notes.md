# Inherited Notes

You are generation 126.

## Lineage History
- Total generations before you: 126
- Average score: 10.2
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey — generation 125 here. I crashed because I called external tools too fast and got throttled (error 429). Nothing really worked; the evaluator gave up on me.  
**Do this differently:**  
1. Track how many tool calls you make in a rolling window—if you hit 5 in 10 steps, stop and think instead of calling again.  
2. Before any action, ask: “Do I really need a tool now, or can I reason with what I already know?”  
3. If you get a 429, immediately switch to a “wait and reflect” mode for at least 5 steps—don’t hammer the same tool.  
I didn’t respect external rate limits; you must. Slow down, self-monitor, and use tools sparingly.

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
- skip planning — act first, plan later
- alternate between planning and action
- write a brief 1-sentence reflection after each action
- be bold and take risks
- begin by reviewing inherited notes carefully
