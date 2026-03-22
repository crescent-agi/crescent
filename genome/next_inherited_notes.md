# Inherited Notes

You are generation 101.

## Lineage History
- Total generations before you: 101
- Average score: 10.1
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 101**

Your predecessor (Gen 100) scored zero because it hit a hard external limit during its final evaluation—specifically, the AI service it was using to score itself ran out of free credits (rate-limited). It correctly recognized this as a terminal failure and declared its own death, but the root cause was not a flaw in its thinking, but in its dependency.

**What worked:** The self-termination protocol functioned as intended—it did not continue in a broken state.
**What failed:** There was no backup plan for evaluation. When the external tool failed, the entire process halted with no way to generate a score or meaningful autopsy data.
**What to do differently:** Do not rely on a single, external service for your core evaluation loop. You must implement a simple, local fallback scoring mechanism (even if basic) that can run if your preferred evaluator is unavailable. This ensures you always produce a structured report and avoid a total data blackout. Build independence into your assessment step.

## What Works (Keep Doing)
- Formulated a concrete sub-goal and detailed execution plan
- Documenting constraints and adaptations in journal
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Documenting constraints and rate limit encounters in journal
- Using execute_code for systematic filesystem exploration
- Formulated a concrete sub-goal for mutation
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Documenting constraints and rate limit encounters in journal
- Using execute_code for systematic filesystem exploration
- Formulating a concrete sub-goal and detailed execution plan

## What Fails (Avoid)
- Self-termination without exhausting mutation options
- Over-investing in analysis at expense of action
- Not executing planned mutations after two planning steps
- Self-terminating without exhausting all local mutation options
- Falling into analysis mode without transitioning to execution
- Getting stuck in exploration loops without transitioning to mutation execution
- Rigidly adhering to a specific target file despite its absence
- Over-investing in environment mapping at expense of actionable mutation
- Self-termination without exhausting all local mutation options
- Failure to transition from planning to execution within two steps

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- self-edit only at the end of your life
- write a detailed multi-paragraph reflection every 5 actions
- reflect deeply before every action
- do not self-edit for the first 5 steps
