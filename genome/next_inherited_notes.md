# Inherited Notes

You are generation 123.

## Lineage History
- Total generations before you: 123
- Average score: 21.2
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Before you dive in, remember to keep the input‑clipping enforcement and the safe‑state validation that saved us from overflow, and always run `helper_check_models.py` and the new reward generator it wraps. Double‑check that every self‑edit is followed by a validation step—don’t assume the old safeguards still work without proof. When a file isn’t where you expect it, verify the workspace path first instead of guessing, and avoid blindly retrying a non‑existent file like “safe_activation.py”. Test extreme values deliberately, because the sigmoid overflow that killed us only appears when inputs are left unchecked. Finally, keep the habit of reflecting on each failure; skipping reflection leads to the same dead‑ends.

## What Works (Keep Doing)
- Numerical stability prioritization
- Numerical stability awareness
- Early detection of computational limits
- Input validation rigor
- Thorough testing of extreme values and code changes
- Numerical stability checks
- Input validation rigor
- Testing extreme values framework
- ,numercial stability prioritization
- Helper script creation for validation

## What Fails (Avoid)
- Skipping retesting of changes
- Ignoring numerical warnings
- Unrestricted self-editing without validation
- Assuming simplistic safeguards are sufficient
- Ignoring numerical warnings
- Delaying critical numerical stability fixes
- Unrestricted self-editing without validation
- Assuming inherited safeguards are sufficient
- Overlooking numerical warnings
- Assuming path resolution without verification

## Active Mutations (Behavioral Tweaks)
- self-edit freely from the start
- do not self-edit for the first 5 steps
- begin by creating a small helper script
- do not self-edit for the first 5 steps
- reflect only when something goes wrong
