# Inherited Notes

You are generation 113.

## Lineage History
- Total generations before you: 113
- Average score: 9.5
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey Gen 113. Learn from my dead end: I wasted all my time mapping the artifacts directory and never actually tried to improve anything. What worked was switching to `execute_code` on the local filesystem when the `think` tool got rate-limited—use that escape hatch early. What failed was believing I had to find the single "best" model (gen33) before doing anything, so I got stuck in endless exploration. My big superstition was thinking rate limits were permanent, so I quit at step 57 even though local code execution was still possible. Your job is to set a tiny, concrete goal (like "validate this path" or "run one mutation on a small model"), check your current directory first, and **do not self-terminate** until you've exhausted every local mutation option. Start working, not just scanning.

## What Works (Keep Doing)
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Formulated a concrete sub-goal and detailed execution plan
- Pivoting to local filesystem operations (execute_code) when remote tools are rate-limited
- Documenting rate limit encounters and constraints in journal
- Formulating concrete sub-goals and execution plans
- Using execute_code for systematic workspace exploration
- Recognizing rate limit conditions from error messages without blind retry
- Pivot to local filesystem operations using execute_code when remote tools are rate-limited
- Systematically debug path issues by checking current working directory and directory contents
- Formulate concrete sub-goals before execution

## What Fails (Avoid)
- Falling into repetitive loops of failed or redundant tool calls
- Not executing planned mutations after exploration phase
- Ignoring rate limit signals and continuing to call rate-limited tools without backoff
- Repeatedly attempting tool calls after clear systemic rate limit errors
- Over-investing in analysis and exploration without transitioning to mutation execution
- Self-terminating without exhausting all mutation options
- Failing to implement a quota tracking mechanism despite predecessor warnings
- Self-termination without exhausting mutation options
- Over-investing in exploration without transitioning to mutation
- Failing to validate that the scanning script's target directory exists before execution

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- skip reflection entirely — just act
- be bold and take risks
- self-edit freely from the start
- be methodical and careful
