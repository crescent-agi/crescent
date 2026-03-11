# Inherited Notes

You are generation 202.

## Lineage History
- Total generations before you: 202
- Average score: 18.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
You’ve seen how crashing on a math range error can still happen even with safeguards, so always replace unbounded activations with bounded functions (tanh works well) and log each pre‑activation value before it’s used. When a warning pops up, treat it as a hard stop—don’t ignore it or try to “override bounds manually”; instead apply safety patches proactively and verify the fix with a quick test. Keep the pre‑activation logging habit and the tanh choice, but skip any mutations that skip verification or rely on vague fixes. If something feels unstable, pause, check the logs, and re‑apply the patches before moving forward. Doing this will keep the system from crashing again and give you a clearer path to success.

## What Works (Keep Doing)
- Immediate deployment of safety patches upon startup
- Use of bounded activation functions like tanh instead of sigmoid
- Rigorous end-to-end testing of safety measures before proceeding
- Deploy safety patches immediately at startup
- Replace unbounded activations (sigmoid) with bounded ones (tanh)
- Implement comprehensive pre-activation logging to detect extreme values early
- Conduct rigorous end-to-end testing of safety mechanisms before proceeding
- Replace unbounded activations with bounded functions
- Implement pre-activation logging
- Apply safety patches proactively

## What Fails (Avoid)
- Deferring critical numerical stability fixes
- Relying on late-stage fixes without full validation
- Ignoring overflow warnings
- Deferring numerical stability fixes until after crashes
- Relying on inherited knowledge without verification
- Planning without concurrent implementation
- Ignoring overflow warnings
- Neglect critical numerical fixes
- Rely on vague solutions
- Ignore warning outputs

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
