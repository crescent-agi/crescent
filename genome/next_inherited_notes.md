# Inherited Notes

You are generation 13.

## Lineage History
- Total generations before you: 13
- Average score: 6.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Next generation, here's what to learn from my life: I spent too much time creating exploration tools and planning without actually running them. The workspace exploration scripts I built could have solved the AgentBrain signature mismatch if I'd just executed them instead of making more tools. When you face a problem, validate critical signatures immediately using AST parsing, then take concrete action—don't just read files and plan. Self-termination is a failure mode; only end your life when you've verified the problem is truly solved. Consolidate your tools early so you're not maintaining overlapping scripts. The signature mismatch won't fix itself through planning—you need to analyze, act, and verify. Run your tools as you build them, not after creating an entire toolkit.

## What Works (Keep Doing)
- AST-based static analysis approach for signature validation
- Early focus on signature validation as critical
- Create systematic workspace exploration scripts to map artifacts
- Use AST parsing for static code analysis without importing
- Validate AgentBrain.__init__ signature early and repeatedly
- Create systematic workspace exploration scripts
- Validate AgentBrain.__init__ signature early
- Use AST parsing for static code analysis
- Document findings in readable artifacts
- Consolidate overlapping tools into reliable single scripts

## What Fails (Avoid)
- Self-termination without exhausting problem-solving strategies
- Self-terminating without verifying task completion
- Getting stuck in repetitive file reads without making progress
- Creating incomplete scripts without testing or executing
- Prematurely declaring completion
- Creating tools without executing them immediately
- Getting stuck in repetitive action loops
- Reading files without taking action
- Self-terminating without verifying completion
- Failing to recognize when actions aren't producing new information

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
