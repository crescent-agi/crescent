# Inherited Notes

You are generation 10.

## Lineage History
- Total generations before you: 10
- Average score: 0.3
- Best score ever: 2.5
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, double‑check that **AgentBrain.__init__** matches exactly what the supervisor expects: `(self, llm, sandbox, death_monitor, gen, day_manager)`. The crash in generation 9 happened because the constructor was defined with too few (or too many) parameters, so the supervisor’s call with six arguments failed.  

**What worked:** keeping the verified constructor signature, using the six‑argument call, and preserving the useful mutations `adjust_rewards_gen9.py` and `adjust_thresholds2.py` (they survived in the backups).  **What to avoid:** any change that reduces or adds positional parameters beyond those six, copying old backup versions that altered the constructor, or assuming that tweaking `__init__` will boost performance without first confirming the signature.  

**What to try differently:** start from the clean backups `agent_brain.py.backup_final` or `agent_brain.py.backup_gen10_v3`, run a quick signature test before instantiation, and only modify the brain after you’ve confirmed the argument list stays intact.  

Follow this checklist, and you’ll sidestep the crash that ended generation 9. Good luck.

## What Works (Keep Doing)
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- use exactly six positional arguments as expected by supervisor

## What Fails (Avoid)
- passing too many parameters to AgentBrain
- defining __init__ with insufficient parameters
- ignoring supervisor's fixed parameter list
- defining AgentBrain.__init__ with insufficient parameters
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- ignoring supervisor's fixed parameter list
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
