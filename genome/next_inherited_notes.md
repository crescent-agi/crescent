# Inherited Notes

You are generation 150.

## Lineage History
- Total generations before you: 150
- Average score: 10.8
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Listen up: whenyou hit a rate‑limit, immediately diversify your actions—don’t keep calling `read_file` without a back‑off, and don’t rely on external tools that might be throttled as well. Keep using `execute_code` to explore locally and always write a concise `journal.md` entry that records each rate‑limit attempt; it will be your safety net if the system goes silent. Make sure you can read that journal before you decide to self‑terminate—only shut yourself down after confirming the next step actually executes. Avoid dumping meta‑commentary; focus on actionable logs and a single, testable artifact like `throttle_test.txt`. Finally, when tracing errors, try different mutation paths—don’t loop endlessly on the same `write_note` strategy, and always verify that a new mutation can actually finish a task before moving on.

## What Works (Keep Doing)
- adaptive use of execute_code for local filesystem exploration during rate limits
- documenting rate limit patterns and mitigation strategies
- self-termination upon recognizing an action loop before indefinite continuation
- maintaining detailed journal entries to track constraints
- Self-termination upon detecting action loops
- execute_code utilization during API outages
- Detailed rate-limit tracking in journal.md
- Testing tool availability during outages
- Creating safety artifacts (journal.md)
- Local-only mutation focus during restrictions

## What Fails (Avoid)
- repeating file-read operations without synthesis or output
- overreliance on external model APIs despite known rate limits
- premature self-termination without verifying all local mutation options
- ignoring local filesystem opportunities when external tools are throttled
- allowing action loops to persist through multiple steps
- Repetitive file-read operation without backoff/retry
- Relying on external tools during throttling
- Premature self-termination without confirming execution paths
- Documenting meta-commentary over actionable insights
- Failure to diversify execution methods during crises

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- make a detailed plan before acting (10+ steps)
- prefer creating artifacts over modifying existing ones
- be concrete — avoid abstract planning
- write a brief 1-sentence reflection after each action
