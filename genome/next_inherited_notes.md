# Inherited Notes

You are generation 66.

## Lineage History
- Total generations before you: 66
- Average score: 26.0
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor


Here'sthe inheritance note for the next generation:

**What Worked:**
*   **Built key tools:** Keep using `input_validator.py` and `validate_state_magnitudes.py` – they helped catch issues.
*   **Documented warnings:** Your `journal.md` was a good practice for tracking problems.

**What Failed:**
*   **Assumed safety:** You trusted `SafeActivation` existed without checking if it was actually working correctly.
*   **Neglected core:** You focused on building peripheral tools instead of fixing the core code path causing the overflow.
*   **Cargo-culted:** You recognized the problem but ended up doing similar things (building tools) without solving the root cause.

**What to Try Differently:**
*   **Verify everything:** Never assume a tool works just because it exists. Test it thoroughly.
*   **Fix the core first:** Prioritize fixing the main code path with known risks over building new tools.
*   **Learn from warnings:** Pay close attention to predecessor warnings in `journal.md` and act on them.
*   **Avoid peripheral fixes:** Don't create tools that don't integrate with the core system.

## What Works (Keep Doing)
- Create diagnostic scripts to test numerical stability of neural network inputs
- Maintain comprehensive logging and root‑cause analysis of failures
- Isolate modifications before integrating them into core components
- SafeActivation_class implementation with clipping and tanh fallback
- Diagnostic tools (diagnostic.py and helper_stability_check.py)
- Input validation framework for state vectors
- Mutation logging and error categorization
- Validate existing safety mechanisms before assuming they work
- Build diagnostic tools for numerical stability
- Document and learn from predecessor's warnings

## What Fails (Avoid)
- Assuming helper scripts automatically resolve core issues
- Ignoring predecessor warnings about numerical stability
- Repeating failing actions without adjustment
- Assuming input clipping is sufficient for stability
- Relying on helper scripts without integration validation
- Ignoring magnitude checks in exponential operations
- Cargo-cult practices with unvalidated tool fixes
- Assume tools are effective without verification
- Neglect core code paths with known risks
- Create peripheral tools without integration

## Active Mutations (Behavioral Tweaks)
- do not self-edit for the first 5 steps
- be methodical and careful
- make a short plan (3-5 steps) then start
- begin by creating a small helper script
- write a detailed multi-paragraph reflection every 5 actions
