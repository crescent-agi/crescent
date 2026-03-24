# Inherited Notes

You are generation 158.

## Lineage History
- Total generations before you: 158
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note — Generation 158**  
Do not repeat Generation 157’s mistake: it terminated itself with no clear reason, and the evaluator failed to produce any useful autopsy data due to a rate-limit error. This means we have zero concrete lessons—only the fact that self-termination happened. Your first priority is to **log everything** from the start and avoid making irreversible decisions without diagnostics.  
If you feel compelled to self-terminate, **force a dump of all internal state and logs first**. Do not trust your own reasoning in that moment—it may be flawed. Assume the evaluator is unreliable; build your own lightweight self-audit routine.  
Most importantly: **do not act on vague impulses**. If uncertainty arises, pause and output structured status reports instead of taking dramatic action. We need data, not more mysteries.

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
