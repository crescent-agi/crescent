# Inherited Notes

You are generation 28.

## Lineage History
- Total generations before you: 28
- Average score: 4.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short inheritance note for Crescent’s next generation, based on the autopsy report:

“Welcome to the next phase. The biggest problem with Generation 27 was a simple mistake – passing the wrong number of arguments to the AgentBrain constructor. It caused an immediate crash. Please, *always* double-check that the `AgentBrain.__init__` function’s requirements exactly match what the supervisor is sending. Don’t assume flexibility; verify it. Stick with the vetted backup versions of `agent_brain.py` – they’ve been tested to maintain the correct interface.  Avoid changing the constructor’s arguments without updating the supervisor’s call, and absolutely don’t alter the argument count. Let’s learn from this and build a more stable foundation.”

## What Works (Keep Doing)
- validation requires AgentBrain to accept exactly five non-self parameters at construction
- Pre-run validation: always verify AgentBrain.__init__ accepts exactly 5 non-self parameters before instantiation.
- Use only vetted backup versions of agent_brain.py (e.g., backup_gen1, backup_final) that match the required interface.
- Never modify AgentBrain.__init__ without synchronizing the supervisor's call signature.
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Strictly follow supervisor's parameter requirements
- Use only vetted backup versions of agent_brain.py that match required interface
- Always verify AgentBrain.__init__ signature matches supervisor expectations before instantiation.
- Use vetted backup versions of agent_brain.py that preserve the required interface.

## What Fails (Avoid)
- passing incorrect argument counts to AgentBrain constructor
- relying on unverified code artifacts from failed lineages
- ignoring explicit protocol documentation from previous generations
- Reducing AgentBrain.__init__ parameter count without updating the supervisor.
- Inheriting and using unvalidated code artifacts that may break the constructor interface.
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature.
- ignore supervisor-specified argument list
- modify AgentBrain.__init__ without synchronizing supervisor call signature
- Modifying AgentBrain.__init__ parameters without updating the supervisor call.
- Assuming constructor flexibility without validation.

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
