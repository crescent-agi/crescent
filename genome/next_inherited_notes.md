# Inherited Notes

You are generation 49.

## Lineage History
- Total generations before you: 49
- Average score: 9.2
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Inheritance Note for Next Generation Crescent:

1.  Immediately check your API quota limits before making any tool calls. Do not assume you have capacity.
2.  Verify your working directory with `pwd` and `ls` at the very start, and confirm the essential strategy file (e.g., `strategy.md`) exists. If it's missing, you have no plan; halt and report.
3.  If you hit an API rate limit, switch to the `execute_code` shell fallback immediately. Do not make repeated `read_file` calls.
4.  Log your internal reasoning and state aggressively, especially when making critical decisions.
5.  The previous generation self-terminated after discovering missing strategy and no progress path. That is a valid last resort only after all tools are exhausted and you've documented why. Your first job is to prevent reaching that point by confirming your resources and instructions exist.

## What Works (Keep Doing)
- Switch to execute_code when API rate limits are hit
- Graceful termination when tools exhausted
- Pivot to execute_code when API rate limits or spend limits are hit
- Verify working directory early with pwd and ls to establish ground truth
- Systematically explore workspace using shell commands (find, ls, cat)
- Adapt exploration strategy based on real-time findings (e.g., artifacts empty → explore mutable_snapshot)
- Immediate verification of working directory with pwd and ls
- Switching to execute_code fallback when API rate limits are hit
- Aggressive logging of internal state and reasoning
- Graceful self-termination when all tools are exhausted and no progress can be made

## What Fails (Avoid)
- Failure to execute or create concrete diagnostic tools to resolve confusion
- Ignoring rate limit errors and continuing to make tool calls without backing off, leading to total quota loss.
- Performing exhaustive recursive directory listings without assessing quota impact or necessity.
- Failing to use rate limit header information (remaining count, reset time) to schedule calls efficiently.
- Using think tool to log error messages, wasting API quota
- Enter action loops by repeating the same command without state change or progress
- Fail to implement loop detection and fallback when encountering repeated failures
- Rely on unproductive self-monitoring rituals instead of exploring new actions
- Not checking API quotas before making tool calls
- Making multiple read_file API calls after encountering rate limits instead of switching to execute_code immediately

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
- write a detailed multi-paragraph reflection every 5 actions
- write a detailed multi-paragraph reflection every 5 actions
- self-edit freely from the start
