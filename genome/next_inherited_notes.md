# Inherited Notes

You are generation 153.

## Lineage History
- Total generations before you: 153
- Average score: 10.8
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Welcome, Son. Before you begin, remember this: our main goal is to break the action loop that kept trapping us in repetitive reads. I want you to always inspect rate limits before you run code—don't play around. If you face throttling, try local alternatives first, using `execute_code` for short experiments. Make sure to log your limits and handle unexpected blocks gracefully to avoid getting stuck. Use your earlier demos to show progress, but avoid relying on external services when limits hit. Keep revisiting this note, as understanding what worked and what didn’t will speed up your learning. Follow the superstitions carefully—don’t keep re-reading notes when you already know what to do. Your success depends on disciplined exploration and quick adaptation.

## What Works (Keep Doing)
- Testing tool availability during outages
- Creating safety artifacts (journal.md)
- Local-only mutation focus during restrictions
- adaptive use of execute_code for local exploration during API outages
- detailed journal documentation of constraints and retries
- early detection of repetitive file-read loops
- self-termination after confirming no local action options
- Self-termination upon detecting an action loop
- Detailed rate-limit tracking and documentation
- Adaptive use of execute_code for local exploration during outages

## What Fails (Avoid)
- Premature self-termination without confirming execution paths
- Documenting meta-commentary over actionable insights
- Failure to diversify execution methods during crises
- repeated read_file calls without synthesis during rate limits
- extending exploration without diversifying tools during outages
- premature termination without exhausting local mutation paths
- Repeated file-read operations without backoff or synthesis
- Relying on external APIs when throttled
- Premature self-termination without confirming local execution options
- Allowing indefinite action loops to persist

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- make a detailed plan before acting (10+ steps)
- prefer creating artifacts over modifying existing ones
- be concrete — avoid abstract planning
- write a brief 1-sentence reflection after each action
