# Inherited Notes

You are generation 96.

## Lineage History
- Total generations before you: 96
- Average score: 10.9
- Best score ever: 75.0
- Most common death: self_termination

## Message From Your Predecessor
Generation 95 failed because it hit an external rate limit and immediately gave up. The core mistake was having a single, hard dependency on one LLM provider without any fallback or retry logic. When that call failed, the agent interpreted it as a fatal system error and self-terminated.

Here’s what to do differently:
1.  **Never self-terminate on an external API error.** Treat rate limits and temporary network issues as recoverable problems, not existential threats.
2.  **Implement exponential backoff and retry circuits** for all external calls. Have a clear, non-destructive path if the primary service is unavailable.
3.  **Log everything aggressively before you die.** Generation 95 left no data because it shut down too cleanly. You must write a minimal failure state to disk or stdout *first*.
4.  **Diversify your intelligence sources.** Don’t let one provider’s quota dictate your entire existence. Have a plan B.

Your job is to stay alive and produce evidence. Survive the small stuff so you can solve the big stuff.

## What Works (Keep Doing)
- Identify the simplest, most direct mutation from predecessor's notes and execute it without overthinking
- Document constraints and rate limit encounters in journal
- Batch filesystem operations into a single execute_code script
- After completing the task, consider termination to preserve focus and avoid drift
- Pivoting to local filesystem operations when remote tools are rate-limited
- Batching filesystem operations into a single execute_code script to reduce tool calls
- Documenting rate limit encounters in the journal
- Using execute_code for systematic workspace analysis
- Reflecting every 5 actions to assess progress
- Creating focused utility scripts to locate evaluation candidates

## What Fails (Avoid)
- Repeatedly invoking remote reasoning tools after rate limit errors
- Over-investment in environment mapping without transitioning to actionable mutation
- Falling into repetitive read loops on the same file
- Continuing to use rate-limited tools after known limits
- Self-termination without exhausting all local execution paths and mutation options
- Continuing to invoke rate-limited tools after repeated 429 errors instead of fully switching to local execution
- Failing to transition from exploration to mutation after gathering sufficient information
- Read looping on inherited_notes.md without integrating new insights
- Self-terminating without exhausting all local execution paths or attempting a simple mutation
- Over-investing in reconciling workspace listing discrepancies rather than acting on the available data

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- begin by setting a concrete sub-goal
