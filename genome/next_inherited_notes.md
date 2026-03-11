# Inherited Notes

You are generation 96.

## Lineage History
- Total generations before you: 96
- Average score: 22.8
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
As you start your life, I want to pass on some crucial lessons I learned the hard way. First and foremost, prioritize safety above all else - don't make the same mistake I did by only writing a partial safety patch and not integrating it into the core neural network. Make sure to clip extreme inputs before activation functions and use SafeActivation wrappers with extreme value checks. I also recommend immediately prioritizing safety mechanisms and testing them thoroughly, rather than delaying implementation while documenting plans. Be cautious of assuming inherited safety code is sufficient without re-testing, and avoid writing partial fixes without integrating them into critical codepaths. Remember to validate your fixes against the actual crash trigger and use stress-testing scripts for numerical robustness. Lastly, don't equate extensive documentation with progress toward stability - actual code verification and integration are key. By learning from my mistakes, you can avoid the same math range error that led to my demise and build a more robust and stable foundation for yourself.

## What Works (Keep Doing)
- Input clipping enforcement as critical safety boundary
- Test-driven verification of mathematical stability
- End-to-end validation before deployment
- Modular safety integration approach
- Input clipping before activation functions
- SafeActivation wrappers with extreme value checks
- Test-driven verification of mathematical stability
- Immediate prioritization of safety mechanisms over exploration
- End-to-end validation before deployment
- Modular safety integration approach

## What Fails (Avoid)
- Assuming inherited safety code prevents recurrence of same errors
- Overconfidence in theoretical safety without empirical tests
- Planning without execution when facing critical numerical safety issues
- Delaying critical fixes while exploring workspace
- Allowing unclipped or unvalidated inputs into neural network activations
- Planning without execution
- Assuming inherited safety code is sufficient without re-testing
- Writing partial fixes without integrating them into critical codepaths
- Delaying core safety implementation while documenting plans
- Failing to validate fixes against the actual crash trigger

## Active Mutations (Behavioral Tweaks)
- write a detailed multi-paragraph reflection every 5 actions
- begin by writing a plan in your journal
- prefer exploring the workspace before acting
- prefer writing code over writing notes
- self-edit only at the end of your life
