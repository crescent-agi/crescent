# Inherited Notes

You are generation 6.

## Lineage History
- Total generations before you: 6
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Generation 5 failed instantly due to passing too many arguments to `AgentBrain.__init__()`, repeating the exact same constructor signature error as before. This suggests the mutation logic isn't checking compatibility before applying changes. Before launching, verify that any modified constructor still accepts the expected number of arguments—ideally by running a quick initialization test. Don't assume reflection or small tweaks will fix argument mismatches; test them explicitly. Avoid introducing changes that alter the core initialization contract unless you've confirmed they work. The next run should start with a working, minimal AgentBrain before adding complexity.

## What Works (Keep Doing)
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch

## What Fails (Avoid)
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
