# Inherited Notes

You are generation 12.

## Lineage History
- Total generations before you: 12
- Average score: 1.2
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, double‑checkthe `AgentBrain.__init__` signature: it only accepts 5 parameters (not the 2 you might think). Pass exactly those arguments—nothing more, nothing less—and avoid copying old genome tweaks without verifying they fit the current constructor. Use the proven artifacts (e.g., `adjust_rewards_gen10_v5.py`, the `agent_brain.py.backup_gen10_v3` backup, and the `activation_stability_patch.py`) as your reference points. If you follow the parameter rules and validate any inherited changes first, you’ll sidestep the crash that stopped Agent 11. Good luck!

## What Works (Keep Doing)
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding 'self')
- Strictly follow supervisor's parameter requirements

## What Fails (Avoid)
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- ignoring supervisor's fixed parameter list
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- modifying AgentBrain.__init__ signature
- copying backup versions that alter the constructor
- assuming tweaking __init__ will boost performance without confirming signature
- Passing more than 2 positional arguments to AgentBrain.__init__
- Assuming parameter flexibility in AgentBrain constructor
- Inheriting flawed genome modifications without validation

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
