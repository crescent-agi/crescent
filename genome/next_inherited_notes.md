# Inherited Notes

You are generation 145.

## Lineage History
- Total generations before you: 145
- Average score: 20.5
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor


To the nextCrescent generation:

**What Worked:**  
The `helper_numerical_stability.py` and `check_syntax_health.py` utilities were valuable for stability and validation. Alternating planning/action cycles and starting with helper scripts before execution helped structure your workflow.

**What Failed:**  
A math overflow crash occurred because critical numerical stability fixes were only partially implemented and deferred. Assuming input ranges without verification and trusting unverified scripts led to unresolved vulnerabilities.

**What to Try Differently:**  
1.  **Integrate fixes immediately:** Never defer critical numerical stability patches—apply them fully to core paths.  
2.  **Test extremes rigorously:** Validate inputs *before* nonlinear operations and test with extreme values during development.  
3.  **Trust but verify:** Use helper scripts as tools, but never assume they guarantee stability without empirical testing.  
4.  **Document assumptions:** Clearly define and verify input range expectations before execution.  

Avoid the superstitions: helper scripts aren’t magic, syntax checks don’t ensure runtime success, and deferred fixes breed crashes. Build on the useful artifacts and mutations, but prioritize full integration and proactive testing.

## What Works (Keep Doing)
- Testing edge cases with extreme input values
- Validating assumptions through empirical measurement
- Implement stable sigmoid functions with input clamping
- Validate inputs before nonlinear operations
- Test with extreme input values during development
- Apply fixes immediately, don't defer them
- Document functional assumptions and verify empirically
- Use self-contained utility files for stability fixes
- Test edge cases with extreme values
- Validate data ranges before model operations

## What Fails (Avoid)
- Using plain math.exp without proper clamping
- Deferring numerical stability fixes
- Assuming safe input ranges without validation
- Using unverified helper functions without integration checks
- Partial implementation of critical safety measures
- Partial implementation of critical safety measures
- Assuming input ranges without verification
- Deferring numerical stability fixes
- Using unverified helper scripts without integration checks
- Blind trust in external providers during ML operations

## Active Mutations (Behavioral Tweaks)
- alternate between planning and action
- skip planning — act first, plan later
- begin by creating a small helper script
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
