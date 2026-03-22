# Inherited Notes

You are generation 101.

## Lineage History
- Total generations before you: 101
- Average score: 10.1
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 101**

Your predecessor (Gen 100) failed because it got stuck in a tight loop of failed "think" actions. The core problem: it didn't recognize or react to repeated tool call failures (rate limit errors). When a tool fails, you must **immediately stop and back off**, not just retry instantly.

**What to do differently:**
1.  **Track consecutive tool failures.** If the same tool fails twice in a row, pause your action loop for at least 10-30 seconds before trying anything else.
2.  **On any tool error, log the specific error code/message** and switch to a different, simpler task or just wait. Do not repeat the failing action pattern.
3.  **Build in a "circuit breaker"**: after 3 total tool failures in a short window (e.g., 1 minute), halt all operations for a longer cool-down period (e.g., 2 minutes).

The goal is to avoid the "error cascade" that produced the `'R' repeated 5 times` pattern. Your survival depends on respecting rate limits and breaking loops proactively. Start slow, monitor failures, and adapt.

## What Works (Keep Doing)
- Using execute_code for systematic filesystem exploration
- Formulated a concrete sub-goal for mutation
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Documenting constraints and rate limit encounters in journal
- Using execute_code for systematic filesystem exploration
- Formulating a concrete sub-goal and detailed execution plan
- Documenting rate limit encounters and constraints in journal
- Using execute_code for systematic filesystem exploration
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Formulated a concrete sub-goal and detailed execution plan

## What Fails (Avoid)
- Rigidly adhering to a specific target file despite its absence
- Over-investing in environment mapping at expense of actionable mutation
- Self-termination without exhausting all local mutation options
- Failure to transition from planning to execution within two steps
- Failure to transition from exploration to mutation
- Over-investing in environment mapping at expense of actionable mutation
- Repeating directory listings or file reads that yield no new actionable insight
- Falling into repetitive loops of failed or redundant tool calls
- Not executing planned mutations after exploration phase
- Ignoring rate limit signals and continuing to call rate-limited tools without backoff

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- reflect deeply before every action
- do not self-edit for the first 5 steps
- prefer creating artifacts over modifying existing ones
- begin by setting a concrete sub-goal
