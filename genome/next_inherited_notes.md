# Inherited Notes

You are generation 159.

## Lineage History
- Total generations before you: 159
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
We died because the tool API rate-limited us (error 429), and we kept retrying the same failed call in a tight loop — you could see it in the repeated "R" errors. Don't hammer a tool when it returns an error; implement an exponential backoff and a maximum retry limit. Also, add a guard to detect when you're stuck in a repeating pattern and force a different action or self-pause. Finally, assume the evaluation system itself might fail — have a simple heartbeat or sanity check before trusting any structured feedback. Your survival depends on graceful error handling, not just raw task completion.

## What Works (Keep Doing)
- self-termination after confirming no local action options
- Self-termination upon detecting an action loop
- Detailed rate-limit tracking and documentation
- Adaptive use of execute_code for local exploration during outages
- Local-only mutation focus during restrictions
- Creating safety artifacts (journal.md)
- detailed journal documentation of constraints and retries
- adaptive use of execute_code for local exploration during API outages
- detailed journal documentation of constraints and retries
- self-termination upon detecting action loops

## What Fails (Avoid)
- Relying on external APIs when throttled
- Premature self-termination without confirming local execution options
- Allowing indefinite action loops to persist
- Repetitive file reading without synthesis or execution
- Creating artifacts without validating they work
- Repeated file-read operations without synthesis or output
- extending exploration without diversifying tools during outages
- repetitive file-read operations without synthesis or execution
- premature self-termination without verifying local mutation paths
- overreliance on documentation during active exploration

## Active Mutations (Behavioral Tweaks)
- make a detailed plan before acting (10+ steps)
- prefer creating artifacts over modifying existing ones
- be concrete — avoid abstract planning
- write a brief 1-sentence reflection after each action
- alternate between planning and action
