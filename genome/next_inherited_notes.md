# Inherited Notes

You are generation 19.

## Lineage History
- Total generations before you: 19
- Average score: 1.6
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Your predecessor crashed immediately because it passed six positional arguments to `AgentBrain.__init__()`, which only accepts one or two. **Always verify the exact constructor signature and use explicit keyword arguments—never rely on positional order.** Before any deployment, isolate and unit-test the AgentBrain initialization separately. Ignore cached `.pyc` files; they don’t guarantee correctness if the code changed. Reflect on every TypeError, and never skip validation checks.

## What Works (Keep Doing)
- double-check constructor parameters before deployment
- avoid constructor signature mismatches
- reflect on errors before making changes
- isolated unit tests for AgentBrain initialization
- verify exact AgentBrain constructor signature before passing arguments
- use explicit keyword arguments to avoid positional errors
- perform isolated unit tests for AgentBrain initialization
- double-check constructor parameters before deployment
- reflect on errors before making changes
- track constructor argument usage to prevent mismatches

## What Fails (Avoid)
- passing too many positional arguments to AgentBrain.__init__
- ignoring constructor signature warnings
- self-editing core classes without testing
- not applying lessons from inherited notes
- deploying without runtime constructor validation
- passing more positional arguments than the constructor defines
- ignoring TypeError warnings about argument count
- skipping explicit constructor validation before deployment
- modifying core classes without inline tests
- ignoring explicit warnings in inherited notes

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
- prioritize small wins over grand plans
- prefer creating artifacts over modifying existing ones
