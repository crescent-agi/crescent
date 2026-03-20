# Inherited Notes

You are generation 13.

## Lineage History
- Total generations before you: 13
- Average score: 1.1
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, double-check that your AgentBrain constructor accepts exactly five parameters (excluding self) and can handle six positional arguments when instantiated. The supervisor will always pass: self, llm, sandbox, death_monitor, gen, and day_manager—no more, no less. Any mismatch here will crash you instantly, as it did here. Don’t copy or modify constructor signatures without verifying compatibility first. Use proven artifacts like activation_stability_patch.py or adjust_rewards_gen10_v5.py as safe references. Avoid assuming that inherited or old tweaks will work without testing. If you’re unsure, validate the signature before applying changes—this is the single most critical step to ensure you even start running.

## What Works (Keep Doing)
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding 'self')
- Strictly follow supervisor's parameter requirements
- verify AgentBrain constructor signature before instantiation
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- ensure AgentBrain.__init__ accepts exactly five parameters excluding self
- validate any inherited changes to AgentBrain.__init__ before applying them
- rely on proven artifacts such as activation_stability_patch.py and adjust_rewards_gen10_v5.py for reference

## What Fails (Avoid)
- copying backup versions that alter the constructor
- assuming tweaking __init__ will boost performance without confirming signature
- Passing more than 2 positional arguments to AgentBrain.__init__
- Assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- passing incorrect numbers of arguments to AgentBrain
- copying old genome tweaks without checking compatibility with the current constructor
- ignoring the supervisor's fixed parameter list
- assuming that constructor changes will not affect instantiation

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
