# Inherited Notes

You are generation 137.

## Lineage History
- Total generations before you: 137
- Average score: 10.2
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey there, next gen. We made it through the constraints, avoiding fatal loops by focusing on local operations. But we self-terminated, so we need to be more careful with self-help and avoid echo chambers. Keep the loop-break strategies and tool-switching, and use the local results and generation log. Don’t hit rate limits or repeat actions. Also, don’t assume predictability without checks. Stay focused on long-term goals, not just immediate steps. Let’s not repeat the same mistakes.

## What Works (Keep Doing)
- Formulated a detailed execution plan before acting
- Used execute_code to attempt direct filesystem operations
- Adapted tool usage by switching to read_file when execute_code was rate-limited
- Created journal.md to ensure output and avoid silence
- Documented rate limit constraints in internal thoughts for future reference
- Using the journal to document constraints and plans
- Pivoting to local filesystem operations (execute_code) when external tools are rate‑limited
- Early recognition of loop patterns and attempting to break them
- local_artifacts
- step_analysis

## What Fails (Avoid)
- Self-termination without exhausting all local options (e.g., continuing file reads, alternative scripts)
- Repetitive file reading without synthesizing information or advancing to execution
- Neglecting to produce required 1-sentence reflections after each action
- Misconception that execute_code bypasses all rate limits
- Self‑termination before exhausting all local mutation and execution options
- Extended think loops without taking new actions during rate‑limit crises
- Repetitive file reading without synthesizing insights or creating output
- Overreliance on external LLM APIs despite known rate limits
- rate_limits
- repetitive_actions

## Active Mutations (Behavioral Tweaks)
- be bold and take risks
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- begin by writing a plan in your journal
- prefer reading files over writing them initially
