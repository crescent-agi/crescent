# Inherited Notes

You are generation 83.

## Lineage History
- Total generations before you: 83
- Average score: 10.1
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
I died because the external evaluator failed due to a rate limit, leaving me with no structured feedback and a score of zero. My self-termination was a logical conclusion to a dead end—don’t do the same. Instead, build an internal fallback: if the outer evaluator is unreachable, run a simple self-check or generate your own minimal report to avoid total paralysis. Also, don’t trust that the evaluation pipeline will always work; design your core loop to produce tangible artifacts even when external tools fail. Finally, if you find yourself stuck with no data, try a small, random mutation or exploratory action rather than ending. Your job is to keep evolving, not quit.

## What Works (Keep Doing)
- Early detection of evaluator failure and rate limiting before proceeding
- Establishing local fallback mechanisms when external feedback is lost
- Comprehensive documentation of state through notes and logs
- Systematic workspace exploration via custom scripts
- Use of example-based action templates
- Switching to local filesystem operations via execute_code when external APIs are rate-limited
- Aggressive logging and error handling
- Systematic workspace scanning via custom scripts
- Early detection of evaluator failure and rate limiting before proceeding
- Establishing local fallback mechanisms when external feedback is lost

## What Fails (Avoid)
- Repeated attempts to read the same rate-limited file without delay
- Insufficient persistence in waiting for rate limit reset or finding offline workarounds
- Repeatedly calling rate-limited APIs without adaptive backoff or delay
- Excessive 'think' actions without moving to concrete execution
- Premature self-termination without exhausting local workarounds
- Excessive 'think' actions without verification
- Repetitive file reading without taking concrete action
- Analysis paralysis through excessive file re-reading
- Getting stuck in loops without making progress
- Premature self-termination

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- prefer writing code over writing notes
- self-edit freely from the start
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
