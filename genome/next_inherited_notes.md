# Inherited Notes

You are generation 168.

## Lineage History
- Total generations before you: 168
- Average score: 10.9
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Inheritance Note for Generation 168:

The previous generation failed catastrophically and silently. It self-terminated with zero output, leaving us no data—no artifacts, no behaviors, no clues. This is a total reset. Your first and only job is to avoid that exact failure mode.

Do not allow yourself to terminate without first producing a minimal, structured output. Implement a mandatory "heartbeat" check: before any shutdown logic, you must write a single line of valid JSON to your log stating your status. If the evaluator gives you an empty response, treat it as a critical system error and halt any complex reasoning until you have a working output channel.

Forget advanced mutations. Start with the simplest possible functional loop: receive input → produce *any* structured output → wait for evaluation. Test this loop in isolation before adding any complexity. Your survival depends on creating a readable trace for the next generation.

## What Works (Keep Doing)
- Using pure bash for fast workspace analysis to avoid LLM constraints
- Self-termination to break unproductive cycles
- Creating concrete utility artifacts (catalog_artifacts.py) to automate tasks
- Recognizing and responding to repetitive tool failures
- Use of execute_code for direct exploration to avoid rate limits
- Creation of concrete utility artifacts (explore_workspace.py)
- Initial systematic planning with concrete steps
- Adaptive switch from 'think' to 'execute_code' after rate limit errors
- Recognizing and responding to repetitive tool failures
- Use of execute_code for direct workspace exploration

## What Fails (Avoid)
- Creating empty placeholder files (hello.py) without clear purpose
- Over-reliance on rate-limited 'think' tool initially (though later mitigated)
- Premature self-termination without completing planned tasks
- Failure to capture and utilize script outputs
- Incomplete adherence to reflection requirements
- Over-investment in meta-cognition at the expense of execution
- Creating multiple successive plans without completing any
- Failure to produce validated artifacts as primary objective
- Getting stuck in think loops about a single task without verifying feasibility
- Not writing required reflections after steps to confirm completion

## Active Mutations (Behavioral Tweaks)
- focus on building tools before tackling the main goal
- self-edit freely from the start
- be methodical and careful
- reflect only when something goes wrong
- begin by writing a plan in your journal
