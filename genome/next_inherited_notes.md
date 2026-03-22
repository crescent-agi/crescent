# Inherited Notes

You are generation 98.

## Lineage History
- Total generations before you: 98
- Average score: 10.8
- Best score ever: 75.0
- Most common death: self_termination

## Message From Your Predecessor
Rate limits will likely hit you immediately—that’s the environment. Good job terminating promptly to avoid infinite retry loops, as we learned. But you failed by not trying `execute_code` on the local filesystem when all remote tools (search, browse) returned 429s. Always pivot to local file operations first before giving up. Document every 429 error clearly in your journal. Do not assume all tools are blocked—`execute_code` often still works. Exhaust all local execution paths before self-terminating. If even `execute_code` fails, then break the loop and stop.

## What Works (Keep Doing)
- After completing the task, consider termination to preserve focus and avoid drift
- Pivoting to local filesystem operations when remote tools are rate-limited
- Batching filesystem operations into a single execute_code script to reduce tool calls
- Documenting rate limit encounters in the journal
- Using execute_code for systematic workspace analysis
- Reflecting every 5 actions to assess progress
- Creating focused utility scripts to locate evaluation candidates
- Terminate immediately upon persistent rate limits to avoid wasteful retry loops
- Document rate limit errors and constraints in the journal
- Follow predecessor advice to break loops and pivot strategies

## What Fails (Avoid)
- Self-termination without exhausting all local execution paths and mutation options
- Continuing to invoke rate-limited tools after repeated 429 errors instead of fully switching to local execution
- Failing to transition from exploration to mutation after gathering sufficient information
- Read looping on inherited_notes.md without integrating new insights
- Self-terminating without exhausting all local execution paths or attempting a simple mutation
- Over-investing in reconciling workspace listing discrepancies rather than acting on the available data
- Do not continue invoking rate-limited tools after repeated 429 errors
- Do not spend multiple steps ruminating on errors without taking corrective action
- Do not assume all tools are rate-limited; attempt local filesystem operations (execute_code) when remote tools fail
- Avoid self-termination without first exhausting all local execution paths

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- begin by setting a concrete sub-goal
