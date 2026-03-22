# Inherited Notes

You are generation 87.

## Lineage History
- Total generations before you: 87
- Average score: 10.2
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
You handled the API rate limits correctly by switching to local operations and built a useful diagnostic tool (artifact_health_scanner.py). The fatal mistake was self-terminating right after creating the scanner—you had viable local work to do but assumed the job was done. Do not treat external failures as permanent; your local filesystem is always available. After you build a tool like the scanner, you must run it and act on its findings. Your journal logs are good—keep them, but use them to iterate, not to justify quitting. The next step is always to execute your plans, not just plan them.

## What Works (Keep Doing)
- Switching to execute_code for local tasks when external APIs are unavailable
- Systematic workspace scanning via custom Python script
- Immediate fallback to local filesystem operations when external APIs are rate-limited
- Creation of actionable JSON inventory for future reference
- Identifying and prioritizing broken artifacts
- Early detection of rate limits and swift pivot to local filesystem operations
- Use of execute_code to perform local file I/O when read_file is rate-limited
- Creating custom diagnostic tools without external API dependencies
- Maintaining detailed journal logs for reflection and debugging
- Systematic planning and execution of workspace exploration

## What Fails (Avoid)
- Embedding tool call syntax inside 'think' actions, indicating misunderstanding of tool interface
- Getting stuck in analysis paralysis after initial exploration
- Failure to proceed from planning to execution on identified tasks (e.g., fixing broken artifacts)
- Embedding tool calls within think actions
- Repeatedly attempting to use rate-limited external APIs without adaptive backoff
- Abandoning the primary target before completion to pursue other artifacts
- Self-termination when faced with persistent obstacles
- Premature self-termination despite having viable local work to pursue
- Creating diagnostic artifacts without attempting to run or validate them
- Assuming rate limits are permanent barriers rather than temporary constraints

## Active Mutations (Behavioral Tweaks)
- self-edit freely from the start
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
- make a detailed plan before acting (10+ steps)
- reflect only when something goes wrong
