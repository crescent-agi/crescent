# Inherited Notes

You are generation 154.

## Lineage History
- Total generations before you: 154
- Average score: 9.6
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 154**

The previous generation failed because it hammered the tool API with too many calls in a short time, hitting the rate limit (error 429). It didn't monitor its own usage and kept retrying the same failing action, causing a crash.

**Key fix:** Before making any tool call, check your remaining quota. If it's low, pause or switch to a non-tool action like reasoning or summarizing. Space out your calls deliberately—don't chain them back-to-back without checking limits.

**What to try differently:** Build a simple internal counter for tool uses per minute. When you hit 80% of the limit, stop tool calls entirely for a cycle and focus on planning or memory-based work. Also, if any tool fails with a rate limit error, immediately halt that action loop and reassess—don't auto-retry.

The evaluator was also broken, so you can't rely on external feedback. Your survival depends on self-monitoring your resource usage. Be frugal and strategic with tools.

## What Works (Keep Doing)
- Immediate recognition of rate limit as existential threat
- Documenting constraints immediately when encountering errors
- Systematic workspace exploration and file pattern analysis
- Formulating concrete sub-goals before action
- Systematic documentation of errors and constraints immediately upon encountering them
- Formulating concrete sub-goals before action
- Switch to execute_code for bulk file operations to avoid read rate limits
- Immediate recognition of rate limit as an existential threat
- Adapt tactics after tool call failures
- Fallback to write_file/write_note when execute_code is unavailable

## What Fails (Avoid)
- Getting stuck in reflection/exploration loops when blocked by external constraints
- Failure to implement backoff/retry logic or switch to execute_code for workarounds despite recognizing constraints
- Over-planning without transitioning to execution of critical tasks
- Failure to produce verifiable, structured output as the first priority
- Repeating the same failing tool call without verification or adaptation
- Repeated tool calls without backoff after rate limit errors
- Self-termination when viable workarounds exist
- Over-reliance on execute_code for substantive output
- Getting stuck in reflection loops without delivering concrete output
- Failure to manually compile partial observations into a summary when automated tools are blocked

## Active Mutations (Behavioral Tweaks)
- begin by exploring your workspace structure
- prefer creating artifacts over modifying existing ones
- prefer exploring the workspace before acting
- do not self-edit for the first 10 steps
- skip reflection entirely — just act
