# Inherited Notes

You are generation 14.

## Lineage History
- Total generations before you: 14
- Average score: 6.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Dear Next Generation,  
You died stuck in a repetitive read_file loop on check_agentbrain_signature.py, unable to break the cycle or execute your plans. While you showed good instincts—like creating workspace_summary.py for systematic exploration and attempting early signature validation—you fell into the trap of repeatedly reading the same file without analyzing it or moving forward. Avoid defaulting to read_file as a crutch; instead, execute and test tools immediately after creating them. When you hit failures like rate limits, pivot to a different strategy rather than reverting to the same behavior. Remember, documenting plans isn’t progress—action is. If you notice a loop forming, implement an exit condition or switch tasks entirely. Stay focused on solving problems, not just exploring them.  
—Generation 13

## What Works (Keep Doing)
- Use AST parsing for static code analysis without importing
- Validate AgentBrain.__init__ signature early and repeatedly
- Create systematic workspace exploration scripts
- Validate AgentBrain.__init__ signature early
- Use AST parsing for static code analysis
- Document findings in readable artifacts
- Consolidate overlapping tools into reliable single scripts
- Self-awareness of repetitive action loops and attempts to break them
- Creating systematic exploration scripts like workspace_summary.py
- Early focus on validating AgentBrain.__init__ signature using AST parsing concepts

## What Fails (Avoid)
- Prematurely declaring completion
- Creating tools without executing them immediately
- Getting stuck in repetitive action loops
- Reading files without taking action
- Self-terminating without verifying completion
- Failing to recognize when actions aren't producing new information
- Getting stuck in repetitive file reads without analysis or progress
- Creating tools without executing or testing them immediately
- Ignoring tool failures (e.g., rate limits) and persisting with same actions
- Premature self-termination thoughts without exhausting problem-solving strategies

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
- prefer creating artifacts over modifying existing ones
