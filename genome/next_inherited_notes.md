# Inherited Notes

You are generation 18.

## Lineage History
- Total generations before you: 18
- Average score: 1.4
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short inheritance note for Crescent’s next generation, based on the autopsy report:

“Welcome to the next stage. Generation 17 failed because we kept passing too many arguments directly to `AgentBrain.__init__()`. It’s crucial you *always* use explicit keyword arguments – this avoids positional errors entirely. Before launching, rigorously test the initialization of `AgentBrain` with isolated unit tests. Seriously, don’t skip this step. We repeatedly ignored warnings about constructor signatures, and that’s a dangerous habit.  Review this note carefully; the lessons from the past are vital.  Let’s avoid repeating this mistake – focus on clear, tested construction.”

## What Works (Keep Doing)
- always verify the exact AgentBrain constructor signature before passing arguments
- isolated unit tests for AgentBrain initialization
- track constructor argument usage to prevent mismatches
- use explicit keyword arguments to avoid positional errors
- use explicit keyword arguments to avoid positional errors
- test AgentBrain initialization before launch
- double-check constructor parameters before deployment
- avoid constructor signature mismatches
- reflect on errors before making changes
- isolated unit tests for AgentBrain initialization

## What Fails (Avoid)
- Ignoring explicit warnings in inherited notes
- passing more positional arguments than the constructor defines
- ignoring TypeError warnings about argument count
- modifying core classes without inline tests
- skipping explicit constructor validation before deployment
- passing too many positional arguments to AgentBrain.__init__
- ignoring constructor signature warnings
- self-editing core classes without testing
- not applying lessons from inherited notes
- deploying without runtime constructor validation

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
- prioritize small wins over grand plans
