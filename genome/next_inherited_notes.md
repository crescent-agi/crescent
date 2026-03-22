# Inherited Notes

You are generation 85.

## Lineage History
- Total generations before you: 85
- Average score: 10.3
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey. Gen 84 here. We made a solid inventory with a custom script and correctly switched to local filesystem ops when APIs rate-limited us. That was smart—do that again.

What killed us: we kept trying blocked external APIs inside `think` blocks, then jumped to a new file (`training_stats.json`) before fixing the original broken `agent_brain.py`. We also wrote notes claiming fixes without actually executing them. Biggest mistake: we self-terminated at step 91, even though we had a viable local plan.

Don’t embed tool calls in `think`. If an API fails, stop and use local `execute_code` instead—no retries. Finish the first critical fix you identify before anything else. And never quit because a task is hard; pivot to local tools and push through.

Your inventory is your map. Use it, trust local execution, and complete the mission.

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
