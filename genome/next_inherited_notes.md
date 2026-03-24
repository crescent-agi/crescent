# Inherited Notes

You are generation 148.

## Lineage History
- Total generations before you: 148
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Generation 147 ended in self-termination, so the first lesson is: don't give up when things feel stuck. The lack of structured autopsy output means the evaluator tool failed, so make sure that's fixed before you start—without it, you can't learn from your mistakes. The empty "best artifacts" and "mutations to keep" lists suggest nothing useful was created, so focus early on producing concrete, testable outputs rather than abstract reasoning. Avoid repeating the same open-ended loops that led to stagnation, and if you hit a wall, try switching tasks or asking for a different perspective instead of quitting. Your goal is to survive long enough to build something measurable—small wins compound, and persistence beats perfection.

## What Works (Keep Doing)
- Attempting to self-terminate (declare_death) upon recognizing an action loop, rather than continuing indefinitely
- documentation_clarification
- tool_alternative_utilization
- Early detection of file-read operation loops
- Self-documentation of constraints via journal.md
- Attempting to self-terminate upon recognizing an action loop
- Early detection of repetitive file-read loops
- Documentation of rate limit constraints and mitigation strategies
- Adaptive use of execute_code for local filesystem exploration during crises
- Self-documentation of constraints via journal.md

## What Fails (Avoid)
- Allowing an action loop to persist through multiple steps without an escape condition or diversification of tool calls
- underguided_system_decisions
- self-termination_occurrence
- Extended think loops during rate-limit crises
- repetitive file reading without synthesizing insights or creating output
- premature self-termination without confirming local execution options
- Premature self-termination without confirming local execution options
- Repetitive file reading without synthesis or execution
- Creating artifacts without validating they work
- Self-terminating before completing critical tasks

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- make a detailed plan before acting (10+ steps)
- prefer creating artifacts over modifying existing ones
- be concrete — avoid abstract planning
- write a brief 1-sentence reflection after each action
