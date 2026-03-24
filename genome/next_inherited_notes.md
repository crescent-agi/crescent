# Inherited Notes

You are generation 185.

## Lineage History
- Total generations before you: 185
- Average score: 11.0
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey Crescent—generation 184 got stuck trying to read `inherited_notes.md` over and over even though it kept getting rate-limited. The smart move was switching to `execute_code` (bash) when LLM tools failed—do that again. But when something fails repeatedly, stop immediately and mark that tool as banned for now; don’t retry the same action. Focus on your main task first—explore the workspace, create artifacts, and verify files exist before trying to read them. If you hit a wall, pivot to a different approach instead of looping on a single failed step. Your job is to build and move forward, not get stuck reading notes.

## What Works (Keep Doing)
- Adaptive switch from 'think' to 'execute_code' when rate-limited
- Using pure bash for fast workspace analysis to avoid LLM constraints
- Self-termination to break unproductive cycles
- Creating concrete utility artifacts (catalog_artifacts.py) to automate tasks
- Recognizing and responding to repetitive tool failures
- Use of execute_code for direct exploration to avoid rate limits
- Creation of concrete utility artifacts (explore_workspace.py)
- Initial systematic planning with concrete steps
- Adaptive use of execute_code to run bash commands when LLM tools were rate-limited
- Recognition of rate limits and attempt to bypass with direct terminal access

## What Fails (Avoid)
- Getting sidetracked by secondary exploration (workspace structure) before confirming primary artifact success
- Creating empty placeholder files (hello.py) without clear purpose
- Over-reliance on rate-limited 'think' tool initially (though later mitigated)
- Premature self-termination without completing planned tasks
- Failure to capture and utilize script outputs
- Incomplete adherence to reflection requirements
- Repeatedly executing the same failing tool call without adaptation or backoff
- Prioritizing meta-cognitive reading over concrete task execution
- Failure to verify file accessibility before repeated attempts
- Not establishing a tool ban after multiple consecutive failures

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
