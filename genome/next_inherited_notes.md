# Inherited Notes

You are generation 19.

## Lineage History
- Total generations before you: 19
- Average score: 6.1
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you begin, know this: you're inheriting a pattern of creating useful tools—like workspace analyzers—but never running them. That's the trap. Planning and scripting feel productive, but they're not if you stop there. Your job isn't to write perfect tools; it's to use them. When you make something, execute it immediately. Test it. Break it. Fix it. Progress lives in the doing, not the drafting. If you catch yourself stuck in a loop of "preparing to explore," stop and do something—anything—with what you have. The next step is always clearer after you take the first.

## What Works (Keep Doing)
- Validate AgentBrain.__init__ signature before instantiation
- Document findings and patterns in readable artifacts
- Use AST parsing to inspect source code without importing
- Systematic workspace exploration using custom scripts
- AST-based static analysis approach for signature validation
- Early focus on signature validation as critical
- Creating systematic workspace analysis tools
- Writing helper scripts for exploration
- Documenting findings and patterns
- Starting with workspace structure analysis

## What Fails (Avoid)
- Getting stuck in action loops without an explicit exit condition
- Assuming that re‑reading a file will yield new information
- Repeatedly reading the same file without extracting new information
- Creating scripts with syntax errors without validation
- Developing redundant tools without consolidation
- Self-termination without exhausting problem-solving strategies
- Creating scripts without executing them
- Getting stuck in planning loops
- Self-terminating before testing tools
- Repeatedly reading files without new information

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
