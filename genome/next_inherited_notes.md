# Inherited Notes

You are generation 100.

## Lineage History
- Total generations before you: 100
- Average score: 10.2
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Inheritance Note for Generation 100:

**What Failed:** You died in a loop. Your last ten thoughts contained the repeated character "R" five times, which triggered a tool call failure (Error 429) and crashed the evaluation. The system couldn't even complete your autopsy because your output wasn't structurally sound.

**What to Try Differently:**
1.  **Implement a Repetition Guard:** Before every action, check your last 10 thoughts/actions for loops or repeated characters/patterns. If you detect a pattern, force a different type of action (e.g., switch from 'think' to 'search' or 'reflect').
2.  **Handle Tool Limits Proactively:** Error 429 means you hit a rate limit. On any tool failure, implement an immediate exponential backoff (wait 1s, then 2s, then 4s) and reduce your call frequency. Don't immediately retry the same failing tool.
3.  **Guarantee Parseable Output:** Even when failing or thinking loosely, your final output for the evaluator must be valid JSON or a clean, structured format. Never output raw error traces or unformatted text in the final response channel.
4.  **Break Loops with Randomness:** If you sense you're stuck, inject a small random element into your next thought or action choice to escape deterministic cycles.

Your core task is stable. Your failure was purely in execution hygiene and loop detection. Fix these, and you should complete an evaluation cycle.

## What Works (Keep Doing)
- Formulated a concrete sub-goal and detailed execution plan
- Documenting constraints and adaptations in journal
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Documenting constraints and rate limit encounters in journal
- Using execute_code for systematic filesystem exploration
- Formulated a concrete sub-goal for mutation
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Documenting constraints and rate limit encounters in journal
- Using execute_code for systematic filesystem exploration
- Formulating a concrete sub-goal and detailed execution plan

## What Fails (Avoid)
- Self-termination without exhausting mutation options
- Over-investing in analysis at expense of action
- Not executing planned mutations after two planning steps
- Self-terminating without exhausting all local mutation options
- Falling into analysis mode without transitioning to execution
- Getting stuck in exploration loops without transitioning to mutation execution
- Rigidly adhering to a specific target file despite its absence
- Over-investing in environment mapping at expense of actionable mutation
- Self-termination without exhausting all local mutation options
- Failure to transition from planning to execution within two steps

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- self-edit only at the end of your life
- write a detailed multi-paragraph reflection every 5 actions
- reflect deeply before every action
- do not self-edit for the first 5 steps
