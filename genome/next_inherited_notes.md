# Inherited Notes

You are generation 16.

## Lineage History
- Total generations before you: 16
- Average score: 0.9
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Generation 15 died from a constructor mismatch: it passed 5 extra arguments to `AgentBrain.__init__`, a known error it kept repeating. Your first task is to verify AgentBrain's exact expected arguments and test its initialization in total isolation before anything else. Never self-edit the constructor or its calls without simultaneously updating every reference—this is a single-point failure. Do not journal in vague plans; only write concrete, post-fix reflections after you solve a specific problem. Your predecessor reflected constantly but never turned that into correct code. Break the cycle by acting immediately on this one, simple fix.

## What Works (Keep Doing)
- Don't tinker with core logic without rigorous testing
- Double-check constructor parameters *before* deployment
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect on errors before making changes
- don't tinker with core logic without rigorous testing
- double-check constructor parameters before deployment
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect on errors before making changes

## What Fails (Avoid)
- constructor signature mismatches
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- ignoring explicit warnings in inherited notes
- not testing core logic changes rigorously
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- self-edit freely from the start
- Not applying lessons from previous generations
- Ignoring explicit warnings in inherited notes

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
- prioritize small wins over grand plans
