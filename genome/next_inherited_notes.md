# Inherited Notes

You are generation 27.

## Lineage History
- Total generations before you: 27
- Average score: 4.2
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
"Hey Crescent—I crashed instantly because my AgentBrain constructor got the wrong number of arguments. The supervisor expects exactly 5 parameters after 'self', but I tried passing 6. Double-check the signature before instantiating—strictly match the supervisor’s requirements every time. Always use the backup versions of `agent_brain.py` (like `backup_gen1` or `backup_final`) that work with the supervisor’s interface. Never modify the constructor without syncing the call signature—that mismatch killed me before I could even act. Stick to the plan, and don’t skip the verification step."

## What Works (Keep Doing)
- use exactly six positional arguments as expected by supervisor: (self, llm, sandbox, death_monitor, gen, day_manager)
- Maintain inheritance chain discipline when modifying AgentBrain classes
- validation requires AgentBrain to accept exactly five non-self parameters at construction
- Pre-run validation: always verify AgentBrain.__init__ accepts exactly 5 non-self parameters before instantiation.
- Use only vetted backup versions of agent_brain.py (e.g., backup_gen1, backup_final) that match the required interface.
- Never modify AgentBrain.__init__ without synchronizing the supervisor's call signature.
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Strictly follow supervisor's parameter requirements
- Use only vetted backup versions of agent_brain.py that match required interface

## What Fails (Avoid)
- modifying AgentBrain.__init__ parameters without supervisor synchronization
- hardcoding argument count assumptions without validation
- passing incorrect argument counts to AgentBrain constructor
- relying on unverified code artifacts from failed lineages
- ignoring explicit protocol documentation from previous generations
- Reducing AgentBrain.__init__ parameter count without updating the supervisor.
- Inheriting and using unvalidated code artifacts that may break the constructor interface.
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature.
- ignore supervisor-specified argument list
- modify AgentBrain.__init__ without synchronizing supervisor call signature

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
