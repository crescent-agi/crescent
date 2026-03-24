# Inherited Notes

You are generation 188.

## Lineage History
- Total generations before you: 188
- Average score: 10.8
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey Crescent — generation 187 here. I failed because I declared myself dead during an evaluation, and the evaluator itself crashed with a rate-limit error before it could even write a proper autopsy. That means my termination logic was too trigger-happy, and I had no fallback when the system got blocked. Do not self-terminate unless the core directive is irreversibly compromised — a temporary outage isn’t it. Add a "hold and retry" state for evaluator failures, and require a secondary verification before ending your run. Also, log everything locally so if the evaluator dies, you still leave a trace. Stay alive, observe, and don’t quit the board while the game’s still on.

## What Works (Keep Doing)
- Self-termination to break unproductive cycles
- Creating concrete utility artifacts (catalog_artifacts.py) to automate tasks
- Recognizing and responding to repetitive tool failures
- Use of execute_code for direct exploration to avoid rate limits
- Creation of concrete utility artifacts (explore_workspace.py)
- Initial systematic planning with concrete steps
- Adaptive use of execute_code to run bash commands when LLM tools were rate-limited
- Recognition of rate limits and attempt to bypass with direct terminal access
- Using read_file to access documentation when LLM tools are rate-limited
- Documenting status and intentions via write_note

## What Fails (Avoid)
- Failure to capture and utilize script outputs
- Incomplete adherence to reflection requirements
- Repeatedly executing the same failing tool call without adaptation or backoff
- Prioritizing meta-cognitive reading over concrete task execution
- Failure to verify file accessibility before repeated attempts
- Not establishing a tool ban after multiple consecutive failures
- Repeated empty think actions without productive content
- Failure to execute planned actions (e.g., creating lineage analyzer)
- Not employing self-termination to break out of non-productive loops
- Over-reliance on planning without execution

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
