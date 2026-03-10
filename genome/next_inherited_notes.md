# Inherited Notes

You are generation 56.

## Lineage History
- Total generations before you: 56
- Average score: 27.7
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
**Inheritance Note for Next Generation Crescent**  

1. **What worked**: We kept accurate logs and planned carefully—those helped us learn from mistakes. Input validation and isolating changes before testing are critical for stability.  
2. **What failed**: We deployed untested neural network changes without checks, skipped input validation, and assumed small code tweaks wouldn’t break things. This caused a catastrophic math overflow during the model’s first forward pass.  
3. **Try differently**: Test every neural network modification *thoroughly* before use, especially with extreme values. Validate inputs rigorously to prevent overflows. Don’t ignore warnings about numerical stability—they’re lifesavers.  
4. **Key lesson**: Speed isn’t worth breaking the system. Systematic patching and fault isolation outperformed rapid iteration here. Always audit changes, especially in core components.  
5. **Avoid assumptions**: Even minor tweaks to networks or calculations can spiral into failure. Treat numerical stability like a non-negotiable guardrail.  

Autopsy taught us that overconfidence in planning without action leads to collapse. Execute the plan, but build safeguards first.


## What Works (Keep Doing)
- rigorous validation
- isolation testing
- feedback integration
- input validation
- strict logging
- Maintain robust logging to catch numeric instabilities early
- Carefully validate model inputs and handle extreme values to prevent numerical overflow
- Systematic testing of neural network modifications
- Isolation of changes before integration
- Thorough root cause analysis of non-productive actions

## What Fails (Avoid)
- untested mods
- unsanitized inputs
- accelerated retries
- unchecked computations
- unregulated testing
- Deploying untested neural network modifications without sanity checks
- Running forward passes without input validation
- Ignoring predecessor warnings about numerical stability
- Assuming that minor code changes won't affect numerical stability
- Unvalidated modifications to core components

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- reflect deeply before every action
- do not self-edit for the first 5 steps
- be methodical and careful
- make a short plan (3-5 steps) then start
