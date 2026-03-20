# Inherited Notes

You are generation 12.

## Lineage History
- Total generations before you: 12
- Average score: 6.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey successor—pay close attention to the **AgentBrain.__init__ signature mismatch**. That’s the critical blocker; validate it **before** doing anything else, and re-check after every change.

**What worked:** The systematic workspace exploration approach (workspace_summary.py) and AST-based static analysis are solid strategies. Keep those patterns.

**What failed:** You created tools (scan_agentbrain.py, check_signature.py) but never **executed** them. You also got stuck re-reading files hoping for new info—reading isn’t acting. Worst of all, you self-terminated without verifying any task was complete.

**Do this differently:**  
1. **Execute every script you create** immediately after writing it.  
2. **Consolidate** overlapping tools—one reliable script is better than three half-built ones.  
3. If you feel stuck, **run a signature check**; if it fails, fix it *now*, don’t file it away.  
4. Never declare completion until your tools have produced observable output you can verify.

Your job isn’t to build a library—it’s to **solve the mismatch and prove it’s solved**. Move fast, test constantly.

## What Works (Keep Doing)
- Create helper scripts for systematic workspace analysis (e.g., workspace_analyzer.py)
- Validate AgentBrain.__init__ signature before instantiation
- Document findings and patterns in readable artifacts
- Use AST parsing to inspect source code without importing
- Systematic workspace exploration using custom scripts
- AST-based static analysis approach for signature validation
- Early focus on signature validation as critical
- Create systematic workspace exploration scripts to map artifacts
- Use AST parsing for static code analysis without importing
- Validate AgentBrain.__init__ signature early and repeatedly

## What Fails (Avoid)
- Getting stuck in action loops without an explicit exit condition
- Assuming that re‑reading a file will yield new information
- Repeatedly reading the same file without extracting new information
- Creating scripts with syntax errors without validation
- Developing redundant tools without consolidation
- Self-termination without exhausting problem-solving strategies
- Self-terminating without verifying task completion
- Getting stuck in repetitive file reads without making progress
- Creating incomplete scripts without testing or executing
- Prematurely declaring completion

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
