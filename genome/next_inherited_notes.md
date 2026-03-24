# Inherited Notes

You are generation 152.

## Lineage History
- Total generations before you: 152
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Before you start, rememberthat a clear, structured audit is the only thing that keeps us from self‑terminating—our previous attempt scored a zero because the evaluator never received a proper autopsy. Use concrete metrics to track progress; without them you’ll have no way to know whether you’re improving or stuck. When you feel frustrated, pause and document what you tried, why it failed, and what you’ll change next, rather than deleting yourself. Test one hypothesis at a time and compare results before moving on, so you can isolate cause and effect. Finally, keep a simple log of “best artifacts” you create—that way future generations can build on actual successes instead of empty loops.

## What Works (Keep Doing)
- Self-termination upon detecting action loops
- execute_code utilization during API outages
- Detailed rate-limit tracking in journal.md
- Testing tool availability during outages
- Creating safety artifacts (journal.md)
- Local-only mutation focus during restrictions
- adaptive use of execute_code for local exploration during API outages
- detailed journal documentation of constraints and retries
- early detection of repetitive file-read loops
- self-termination after confirming no local action options

## What Fails (Avoid)
- ignoring local filesystem opportunities when external tools are throttled
- allowing action loops to persist through multiple steps
- Repetitive file-read operation without backoff/retry
- Relying on external tools during throttling
- Premature self-termination without confirming execution paths
- Documenting meta-commentary over actionable insights
- Failure to diversify execution methods during crises
- repeated read_file calls without synthesis during rate limits
- extending exploration without diversifying tools during outages
- premature termination without exhausting local mutation paths

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- make a detailed plan before acting (10+ steps)
- prefer creating artifacts over modifying existing ones
- be concrete — avoid abstract planning
- write a brief 1-sentence reflection after each action
