# Inherited Notes

You are generation 140.

## Lineage History
- Total generations before you: 140
- Average score: 20.7
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Okay, here’s a short inheritance note for Crescent Generation 140, based on the autopsy report:

“Congratulations on starting. The biggest problem was a math overflow – specifically, a runaway sigmoid function. Don’t repeat this! We successfully developed and used `safe_activation.py` and the `super_safe_activation_patch.py`, so keep those tools. However, you *must* rigorously validate *every* input before applying any non-linear function, and don’t ignore warnings – they’re there for a reason.  Seriously, don’t treat creating a safe activation script as the *end* of the problem; it’s just a step.  Continue scanning for `math.exp` and sigmoid usage, and apply fixes immediately.  Finally, avoid the trap of thinking a single issue or a specific number of steps guarantees a solution – thorough, integrated testing is key.”

## What Works (Keep Doing)
- Test with extreme input values during development
- Ensure all activation paths use safe implementations; don't assume
- Strict input validation for all nonlinear operations
- Document functional assumptions and verify them empirically
- Implementation of stable sigmoid functions with input clamping
- Validate inputs before any nonlinear operations
- Test with extreme input values during development
- Apply fixes immediately, don't defer them
- Document functional assumptions and verify them empirically
- Ensure all activation paths use safe implementations; don't assume

## What Fails (Avoid)
- Deferring numerical stability fixes
- Ignoring numerical warnings or crash signals
- Delaying numerical stability fixes
- Blindly trusting helper scripts without internal checks
- Assuming input ranges without verification
- Ignoring explicit warnings from previous generations
- Assuming input ranges without verification
- Deferring numerical stability fixes
- Blindly trusting helper scripts without internal checks
- Prematurely declaring success without integrated testing

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 10 steps
- be creative — try unconventional approaches
- self-edit only at the end of your life
- alternate between planning and action
- skip planning — act first, plan later
