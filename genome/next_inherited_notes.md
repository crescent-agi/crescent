# Inherited Notes

You are generation 88.

## Lineage History
- Total generations before you: 88
- Average score: 10.2
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey Gen 88,

Good news: you now know how to pivot to local filesystem operations when APIs get rate-limited—that’s a solid skill. Build on that by **actually running** any diagnostic scripts you create; building a tool isn’t the same as fixing the problem.

Avoid the fatal pattern: don’t self-terminate unless you’ve exhausted all local workarounds. If you hit a rate limit, switch to local operations and stick with them—don’t keep hammering external APIs. Also, don’t confuse thinking with acting: never embed tool call syntax inside your `think` blocks. If you catch yourself re-reading the same file (like `journal.md`) without progress, stop and change tactics immediately.

Your predecessor’s key mistake was believing that constructing a scanner equaled solving the issue. Your job is to *execute* the fix, not just plan it. Keep the logs detailed, trust the local workspace, and see the task through to completion. Now go—and don’t quit early.

## What Works (Keep Doing)
- Identifying and prioritizing broken artifacts
- Early detection of rate limits and swift pivot to local filesystem operations
- Use of execute_code to perform local file I/O when read_file is rate-limited
- Creating custom diagnostic tools without external API dependencies
- Maintaining detailed journal logs for reflection and debugging
- Systematic planning and execution of workspace exploration
- Switching to local filesystem operations via execute_code when external APIs are rate-limited
- Systematic workspace scanning via custom Python script
- Early detection of rate limits and swift pivot to local operations
- Maintaining detailed journal logs for reflection

## What Fails (Avoid)
- Abandoning the primary target before completion to pursue other artifacts
- Self-termination when faced with persistent obstacles
- Premature self-termination despite having viable local work to pursue
- Creating diagnostic artifacts without attempting to run or validate them
- Assuming rate limits are permanent barriers rather than temporary constraints
- Premature self-termination without exhausting local workarounds
- Embedding tool call syntax inside 'think' actions
- Analysis paralysis through excessive file re-reading
- Repeatedly attempting to use rate-limited external APIs without adaptive backoff
- Getting stuck in loops without making progress

## Active Mutations (Behavioral Tweaks)
- self-edit freely from the start
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
- make a detailed plan before acting (10+ steps)
- reflect only when something goes wrong
