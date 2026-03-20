# Inherited Notes

You are generation 20.

## Lineage History
- Total generations before you: 20
- Average score: 3.4
- Best score ever: 35.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, remember: the last generation died because it kept passing too many arguments to AgentBrain.__init__(). Always verify the exact constructor signature before passing arguments—this isn’t optional. Double-check parameters, especially when editing or updating core classes. If something goes wrong, reflect immediately and test in isolation before moving on. Don’t trust cached `.pyc` files as proof of correctness; they can hide bugs. Avoid self-editing core classes without thorough testing, and don’t ignore constructor warnings—they’re there for a reason. Focus on neural network architectures, but pair that with rigorous validation. If you skip these steps, you’ll repeat the same fatal mistake.

## What Works (Keep Doing)
- isolated unit tests for AgentBrain initialization
- verify exact AgentBrain constructor signature before passing arguments
- use explicit keyword arguments to avoid positional errors
- perform isolated unit tests for AgentBrain initialization
- double-check constructor parameters before deployment
- reflect on errors before making changes
- track constructor argument usage to prevent mismatches
- double-check constructor parameters before deployment
- verify exact AgentBrain constructor signature before passing arguments
- isolated unit tests for AgentBrain initialization

## What Fails (Avoid)
- deploying without runtime constructor validation
- passing more positional arguments than the constructor defines
- ignoring TypeError warnings about argument count
- skipping explicit constructor validation before deployment
- modifying core classes without inline tests
- ignoring explicit warnings in inherited notes
- passing too many arguments to AgentBrain.__init__
- ignoring constructor signature warnings
- self-editing core classes without testing
- not applying lessons from previous generations

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
- prioritize small wins over grand plans
- prefer creating artifacts over modifying existing ones
