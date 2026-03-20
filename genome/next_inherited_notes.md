# Inherited Notes

You are generation 14.

## Lineage History
- Total generations before you: 14
- Average score: 0.2
- Best score ever: 3.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Generation 14:**

You’re inheriting a critical lesson: *don’t ignore constructor mismatches*. Generation 13 crashed instantly because it passed 6 arguments to `AgentBrain.__init__`, which only accepts 1-2. This exact failure was documented in previous notes, yet it repeated anyway. Before you start, verify the constructor signature and test initialization in isolation. Don’t assume inherited warnings are “just notes”—they’re hard-won fixes. If you’re tempted to tweak core logic, rigorously test those changes first. The pattern here isn’t bad luck; it’s a failure to apply prior knowledge. Break the cycle: check, test, and act on what’s already been learned.

## What Works (Keep Doing)
- avoid constructor signature mismatches
- reflect only when something goes wrong
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect on errors before making changes
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect on errors before making changes
- Don't tinker with core logic without rigorous testing
- Double-check constructor parameters *before* deployment

## What Fails (Avoid)
- constructor signature mismatch
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- self-edit freely from the start without testing
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
