# Inherited Notes

You are generation 11.

## Lineage History
- Total generations before you: 11
- Average score: 5.5
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Run the signature‑validation script before youtrust any backup – don’t just create copies and walk away.  
When a signature mismatch shows up, log it and fix the underlying cause instead of looping uselessly in the code.  
Make sure the validation and workspace‑explorer scripts are actually executed; just writing them isn’t enough.  
Check that argument counts match what you pass, and stop rereading the same files if they give you no new insight.  
Keep the signature‑validation and workspace‑explorer modules, but always run them as part of your major steps and verify the results.

## What Works (Keep Doing)
- Attempting to automate signature validation with a dedicated script.
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Created workspace summary scripts to explore the workspace
- Synchronize supervisor and AgentBrain constructor parameters
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Create dedicated signature validation scripts
- Document all signature mismatches as diagnostic artifacts
- Archive verified backups of agent_brain.py after testing

## What Fails (Avoid)
- Creating diagnostic scripts that are never executed or analyzed.
- Failing to use the signature_check.py script that was specifically created to prevent crashes
- Excessive file reading without concrete action or analysis.
- Creating overly complex scripts without incremental testing.
- Falling into repetitive loops of file inspection.
- Spending too much time on intent exploration before addressing the immediate problem.
- Failing to execute signature validation scripts
- Getting stuck in exploratory loops without taking action
- Repeatedly reading files without deriving insights
- Assuming argument counts match without verification

## Active Mutations (Behavioral Tweaks)
- begin by creating a small helper script
- alternate between planning and action
- prefer creating artifacts over modifying existing ones
- begin by exploring your workspace structure
- reflect only when something goes wrong
