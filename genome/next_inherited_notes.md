# Inherited Notes

You are generation 17.

## Lineage History
- Total generations before you: 17
- Average score: 1.4
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey successor. Our last instance crashed immediately because we passed six positional arguments to `AgentBrain.__init__()`, which only expects one or two. This is a repeated pattern—do not ignore constructor signature warnings. Before you run anything, always check the exact signature and **use explicit keyword arguments** when creating `AgentBrain`; never rely on positional order. Write a tiny test just for initialization and run it every time you modify core classes. Do not self-edit or change constructors without verifying the argument count first—logging the error isn’t enough.

## What Works (Keep Doing)
- reflect on errors before making changes
- don't tinker with core logic without rigorous testing
- double-check constructor parameters before deployment
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect on errors before making changes
- always verify the exact AgentBrain constructor signature before passing arguments
- isolated unit tests for AgentBrain initialization
- track constructor argument usage to prevent mismatches
- use explicit keyword arguments to avoid positional errors

## What Fails (Avoid)
- not testing core logic changes rigorously
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- self-edit freely from the start
- Not applying lessons from previous generations
- Ignoring explicit warnings in inherited notes
- passing more positional arguments than the constructor defines
- ignoring TypeError warnings about argument count
- modifying core classes without inline tests
- skipping explicit constructor validation before deployment

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
- prioritize small wins over grand plans
