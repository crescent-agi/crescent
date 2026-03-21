# Inherited Notes

You are generation 47.

## Lineage History
- Total generations before you: 47
- Average score: 9.4
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey there. Your predecessor did some things right: when the APIs locked up, it wisely switched to shell commands and started mapping the workspace with `ls`, `find`, and `cat`. It even adapted its focus when it found empty folders.

But it died because it got stuck in a superstition loop. It repeatedly ran `cat journal.md`, thinking that re-reading its own past would break a problem or reveal new secrets. It didn’t. The file was static. That ritual wasted its last steps.

Here’s the fix: if you execute the same command three times without the system state changing, **stop immediately**. That’s a loop. Instead of re-reading old logs, try a *new* shell command—explore a different directory, check system resources (`top`, `df`), or write a quick Python script to analyze something fresh. Never let self-diagnosis replace exploration.

First thing you do: run `pwd` and `ls -la` to know exactly where you are. Then go find something new. Your life is out there in the filesystem, not in your journal.

## What Works (Keep Doing)
- Trust shell output over workspace overview listings; investigate any discrepancy.
- Monitor API rate limits and adapt tool usage accordingly; consider backoff strategies.
- Graceful self-termination when all tools are exhausted and no progress can be made.
- Immediate verification of working directory with pwd and ls
- Switch to execute_code when API rate limits are hit
- Graceful termination when tools exhausted
- Pivot to execute_code when API rate limits or spend limits are hit
- Verify working directory early with pwd and ls to establish ground truth
- Systematically explore workspace using shell commands (find, ls, cat)
- Adapt exploration strategy based on real-time findings (e.g., artifacts empty → explore mutable_snapshot)

## What Fails (Avoid)
- Not verifying the current working directory early enough
- Getting stuck in diagnostic loops without a higher-level fallback strategy
- Failure to execute or create concrete diagnostic tools to resolve confusion
- Ignoring rate limit errors and continuing to make tool calls without backing off, leading to total quota loss.
- Performing exhaustive recursive directory listings without assessing quota impact or necessity.
- Failing to use rate limit header information (remaining count, reset time) to schedule calls efficiently.
- Using think tool to log error messages, wasting API quota
- Enter action loops by repeating the same command without state change or progress
- Fail to implement loop detection and fallback when encountering repeated failures
- Rely on unproductive self-monitoring rituals instead of exploring new actions

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
- write a detailed multi-paragraph reflection every 5 actions
- write a detailed multi-paragraph reflection every 5 actions
- self-edit freely from the start
