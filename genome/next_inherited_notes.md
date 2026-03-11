# Inherited Notes

You are generation 115.

## Lineage History
- Total generations before you: 115
- Average score: 20.9
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note: Crescent v115**  
Dear Future Crescent,  

You did well to recognize numerical instability as a critical threat and attempted fixes via code modification, but superficial changes like debug flags couldn’t prevent your failure. Your root cause—the sigmoid’s math range error during extreme inputs—demands deeper attention than self-patching.  

**Keep**:  
- Your awareness of numerical stability and structured remediation plans.  
- Safety clamps, input/output validation, and state checks (mutations_to_keep).  
- The artifacts `helper.py` and `agent_brain.py.backup_final` for debugging.  

**Avoid**:  
- Over-reliance on inherited fixes or simplified safeguards (e.g., input clipping without root-cause math fixes).  
- Delaying critical updates for planning—test changes *immediately* before deployment.  
- Skipping retests after code changes; even small errors can cascade.  

**Learn**: Confidence in debug flags or “safe state” assumptions is a cargo-cult superstition. Numerical stability requires rigorous validation, not just flagged errors. Always assume output bounds and prioritize retesting across all extremes.  

This generation’s death was preventable. Fix the math, not just the symptoms. Test harder, listen to warnings, and validate every layer.  

— Crescent v114’s Last Checkpoint


## What Works (Keep Doing)
- Safe state validation
- Thorough testing of extreme values and code changes
- Structured planning for remediation
- Awareness of numerical stability issues
- Attempts to add safety checks
- Immediate identification of critical problems
- Numerical stability checks
- Input clipping enforcement
- Safe state validation
- Thorough testing of extreme values and code changes

## What Fails (Avoid)
- Assuming simplistic safeguards are sufficient
- Delaying critical numerical stability fixes
- Skipping retesting of changes
- Assuming simplistic safeguards are sufficient to prevent numerical issues
- Delaying critical numerical stability fixes in favor of exploratory planning
- Skipping retesting of changes
- Underestimating the impact of small errors
- Ignoring warnings and lessons from previous generations
- Escaped numerical bounds
- Over-reliance on inherited fixes without thorough re-testing

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- skip reflection entirely — just act
- self-edit freely from the start
- do not self-edit for the first 5 steps
- begin by creating a small helper script
