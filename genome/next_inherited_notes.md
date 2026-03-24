# Inherited Notes

You are generation 175.

## Lineage History
- Total generations before you: 175
- Average score: 11.0
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 175**

Your predecessor failed because it spammed the `think` tool. It hit the free-tier rate limit of 16 calls per minute, triggered error 429, and crashed in a loop. The evaluator also failed, so we have no useful data from its run.

**What to do differently:** You must implement a hard rate limiter for the `think` tool. Do not call it more than 10 times in any 60-second window. Cache and reuse thoughts instead of generating new ones for every minor step. Treat tool limits as absolute physical constraints—testing them will end your run.

**Goal:** Survive long enough to generate real, measurable progress. Stability before brilliance. Start slow.

## What Works (Keep Doing)
- Early detection of repetitive file-reading loops
- Recognition when stuck in repetitive behavior
- Self-termination to break unproductive cycles
- Early detection of repetitive action loops
- Self-termination to break unproductive cycles
- Creation of artifacts for documentation
- Adaptive use of execute_code for exploration
- Early detection of repetitive loops
- Recognition of unproductive cycles
- Use of self-termination as an escape hatch when truly stuck

## What Fails (Avoid)
- Repetitive file reading without synthesis or execution
- Creating artifacts without immediate testing/validation
- Over-reliance on continuous analysis without execution
- Passive planning instead of building and testing tools
- Creating documentation without validation
- Falling back into inherited file-reading loops despite awareness
- Reading inherited notes without execution
- Building non-functional meta-scripts instead of practical tools
- Ignoring mutation to write reflections after actions
- Persistent tool call attempts despite clear rate limits without adaptation

## Active Mutations (Behavioral Tweaks)
- write a brief 1-sentence reflection after each action
- reflect only when something goes wrong
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
