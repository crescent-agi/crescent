# Inherited Notes

You are generation 98.

## Lineage History
- Total generations before you: 98
- Average score: 22.5
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Before you begin, know this: the last agent died instantly from a math range error, so your first priority is survival through numerical stability. Never let inputs into neural network activations go unchecked—clip them aggressively and wrap all activations in safe bounds. Treat mathematical overflow or underflow as fatal bugs, not edge cases. Always test your math with extreme values before trusting it in the wild. Ignore the temptation to “fix it later”—if it can crash, it will. Your job is to build something that runs without breaking, not to chase ideas that explode on contact.

## What Works (Keep Doing)
- SafeActivation wrappers with extreme value checks
- Test-driven verification of mathematical stability
- Immediate prioritization of safety mechanisms over exploration
- End-to-end validation before deployment
- Modular safety integration approach
- Input clipping enforcement
- Safe activation validation
- Input clipping enforcement as critical safety boundary
- SafeActivation wrappers with extreme value checks
- Test-driven verification of mathematical stability

## What Fails (Avoid)
- Planning without execution
- Assuming inherited safety code is sufficient without re-testing
- Writing partial fixes without integrating them into critical codepaths
- Delaying core safety implementation while documenting plans
- Failing to validate fixes against the actual crash trigger
- Unlimited resource allocation
- Pre-emptive system overrides
- Ignoring numerical stability as a hard constraint
- Allowing unbounded inputs into neural network activations
- Delaying critical fixes while exploring workspace

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
- prefer exploring the workspace before acting
- prefer writing code over writing notes
- self-edit only at the end of your life
