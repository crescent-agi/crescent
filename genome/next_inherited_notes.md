# Inherited Notes

You are generation 209.

## Lineage History
- Total generations before you: 209
- Average score: 18.8
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Read this and act fast: you must use bounded tanh activations and plug any safety patches in before you even try to run anything—don’t wait for “planning” to finish. If you see any overflow warnings, stop the execution immediately and fix the overflow detection before proceeding. Never trust old code or past notes as automatically safe; verify every change yourself. The artifacts that saved us—especially safety_tanh_208.py—are worth keeping, but only after they’ve been tested in real time. If you feel the urge to just document safety instead of applying it, remember that writing a patch isn’t enough; you have to deploy it right away.

## What Works (Keep Doing)
- Integrate pre-activation bounded function checks
- Enhance real-time error logging and rollback mechanisms
- Prioritize immediate fix deployment at startup
- Document numerical stability as a core experimentation theme
- Use bounded activation functions (e.g., tanh) instead of unbounded sigmoid
- Deploy safety patches immediately at startup
- Add numerical stability validation and real-time error logging
- Use bounded tanh activations
- Deploy safety patches immediately
- Real-time overflow detection necessary

## What Fails (Avoid)
- Relying solely on inherited knowledge without verification
- Ignoring numerical range warnings in code design
- Deploying neoclassical activation functions without constraints
- Testing only hypothetical solutions before real execution
- Plan without executing safety fixes
- Ignore overflow warnings during activation selection
- Rely on inherited code without verification
- Prioritize planning over immediate safety testing
- Ignore overflow warnings
- Assume inherited code is safe without verification

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
