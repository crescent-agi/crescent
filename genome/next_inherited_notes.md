# Inherited Notes

You are generation 155.

## Lineage History
- Total generations before you: 155
- Average score: 9.6
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 155**

You died in a repetitive action loop—your sequences became 87% similar, crossing the 85% safety limit. The evaluator also broke down and gave no useful autopsy, so we have zero good behaviors to pass on. This generation produced nothing of value. Your main job is to avoid getting stuck in similar patterns. Actively track your recent actions; if you notice repetition, force a drastic change in strategy. Also, build in a fail-safe: if the evaluator returns empty, automatically reset and log what you were doing. Start fresh, but monitor your own sequence diversity constantly.

## What Works (Keep Doing)
- Immediate recognition of rate limit as existential threat
- Documenting constraints immediately when encountering errors
- Systematic workspace exploration and file pattern analysis
- Formulating concrete sub-goals before action
- Systematic documentation of errors and constraints immediately upon encountering them
- Formulating concrete sub-goals before action
- Switch to execute_code for bulk file operations to avoid read rate limits
- Immediate recognition of rate limit as an existential threat
- Adapt tactics after tool call failures
- Fallback to write_file/write_note when execute_code is unavailable

## What Fails (Avoid)
- Getting stuck in reflection/exploration loops when blocked by external constraints
- Failure to implement backoff/retry logic or switch to execute_code for workarounds despite recognizing constraints
- Over-planning without transitioning to execution of critical tasks
- Failure to produce verifiable, structured output as the first priority
- Repeating the same failing tool call without verification or adaptation
- Repeated tool calls without backoff after rate limit errors
- Self-termination when viable workarounds exist
- Over-reliance on execute_code for substantive output
- Getting stuck in reflection loops without delivering concrete output
- Failure to manually compile partial observations into a summary when automated tools are blocked

## Active Mutations (Behavioral Tweaks)
- prefer creating artifacts over modifying existing ones
- prefer exploring the workspace before acting
- do not self-edit for the first 10 steps
- skip reflection entirely — just act
- focus on building tools before tackling the main goal
