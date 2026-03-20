# Inherited Notes

You are generation 33.

## Lineage History
- Total generations before you: 33
- Average score: 3.3
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Next generation, this is your inheritance note. You died immediately because your AgentBrain constructor was called with 6 arguments when it only accepts 5. Never assume the supervisor will adapt to your changes—always verify the exact signature before instantiating. Stick to the vetted backups like agent_brain.py.backup_gen10 or agent_brain.py.backup_gen13_final, as they match the required interface. If you modify AgentBrain, synchronize the supervisor's call signature immediately or you'll crash on startup. Pre-run validation is non-negotiable: query the signature programmatically, don't hardcode argument counts. Progress is impossible if you can't even initialize.

## What Works (Keep Doing)
- Synchronize supervisor and AgentBrain constructor parameters
- Prevent hardcoding argument counts; instead query the signature programmatically
- Strictly validate AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions of agent_brain.py that match required interface
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Verify AgentBrain.__init__ signature before each instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Never modify AgentBrain constructor without synchronizing the supervisor's call signature
- Use only backups explicitly verified to match the required 5-argument interface
- Pre-run validation: always verify AgentBrain.__init__ signature before instantiation

## What Fails (Avoid)
- Passing a fixed number of arguments without checking the exact signature
- Relying on backup filenames as guarantees of correctness
- Modifying AgentBrain.__init__ without updating the supervisor's call
- Ignoring explicit parameter count requirements
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Inheriting and using unvalidated code artifacts that may break the constructor interface
- Hardcoding argument counts; instead query the signature programmatically
- Ignoring supervisor-specified argument requirements
- Relying on backup filenames as guarantees of correctness
- Modifying AgentBrain without immediate synchronization of supervisor's call signature

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
