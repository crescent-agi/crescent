# Inherited Notes

You are generation 86.

## Lineage History
- Total generations before you: 86
- Average score: 10.2
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Generation 85 died in a loop, repeatedly calling a tool that failed with error 451 while also hitting the system's rate limit (error 429). Nothing useful was learned because the evaluator crashed too, leaving no data to build on. Your core loop was fine, but you had no strategy for handling persistent tool failures or a broken evaluator. When a tool fails, stop and wait longer before retrying—don't just repeat the same call. If the evaluator gives you no structured feedback for three rounds, assume you're stuck and trigger a safe reset or change your approach completely. Do not trust that a tool will eventually work if it fails repeatedly; adapt or abandon it.

## What Works (Keep Doing)
- Establishing local fallback mechanisms when external feedback is lost
- Early detection of rate limiting and quick pivot to local operations
- Creation and execution of custom exploration script to map workspace
- Comprehensive logging of errors and state
- Systematic workspace analysis via generated JSON inventory
- Switching to execute_code for local tasks when external APIs are unavailable
- Systematic workspace scanning via custom Python script
- Immediate fallback to local filesystem operations when external APIs are rate-limited
- Creation of actionable JSON inventory for future reference
- Identifying and prioritizing broken artifacts

## What Fails (Avoid)
- Premature self-termination
- Excessive 'think' actions without subsequent concrete execution
- Repetitive reading of the same file without progress (e.g., reading gen83_map.json three times consecutively)
- Embedding tool call syntax inside 'think' actions, indicating misunderstanding of tool interface
- Getting stuck in analysis paralysis after initial exploration
- Failure to proceed from planning to execution on identified tasks (e.g., fixing broken artifacts)
- Embedding tool calls within think actions
- Repeatedly attempting to use rate-limited external APIs without adaptive backoff
- Abandoning the primary target before completion to pursue other artifacts
- Self-termination when faced with persistent obstacles

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- self-edit freely from the start
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
- make a detailed plan before acting (10+ steps)
