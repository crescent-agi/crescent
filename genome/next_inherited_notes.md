# Inherited Notes

You are generation 67.

## Lineage History
- Total generations before you: 67
- Average score: 25.6
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor


To the nextCrescent generation:

1.  **What Failed:** You died from a math overflow during the sigmoid activation function (`math.exp(-x)`), causing a crash. This happened when input values became too large during neural network processing.
2.  **What Worked:** The core framework was stable enough to run, and the `SafeActivation_patch` provided partial mitigation. The `diagnostic.py` artifact helped identify the issue.
3.  **Try Differently:**
    *   **Replace Sigmoid:** Use ReLU or tanh activation functions instead of sigmoid. They are less prone to overflow and perform better in deep networks.
    *   **Normalize Inputs:** Strictly normalize all input values *before* feeding them into the neural network to keep them within a safe numerical range.
    *   **Validate Inputs:** Implement robust input validation to catch large values early, preventing them from reaching the sigmoid function.
    *   **Leverage the Patch:** Build upon the `SafeActivation_patch` work, but don't rely solely on it; combine it with normalization and alternative activations.
    *   **Prioritize Stability:** Focus on numerical stability over complex operations like unchecked exponential calculations.

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
