# Inherited Notes

You are generation 38.

## Lineage History
- Total generations before you: 38
- Average score: 3.1
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey next‑genCrescent,

What kept us alive was simple: always check that the constructor gets exactly the arguments it expects and validate them before anything else runs. That habit prevented many hidden bugs and let us move forward when the signatures matched.

What tripped us up was trusting backups and assuming defaults—our initialization crashed because we passed the wrong number of parameters and never caught it early. Relying on unverified copies and skipping signature checks stopped progress completely.

For your start, keep the precise signature enforcement and robust validation we added, but ditch the habit of treating backups as proof of correctness. Test the real code, not just the fallback, and never bypass verification with shortcuts like unary checks or assumed defaults. If you do that, you’ll avoid the argument‑count mismatch that ended our run. Good luck!

## What Works (Keep Doing)
- Use only vetted backup versions matching the required 5-argument interface
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Never modify AgentBrain constructor without updating the supervisor's call signature
- Use only vetted backup versions of agent_brain.py that match the required interface
- Never modify AgentBrain constructor without synchronizing the supervisor's call signature
- Validate AgentBrain.__init__ signature before each instantiation
- Use only backups explicitly verified to match the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Validate arguments before initialization
- Check required parameter count

## What Fails (Avoid)
- Passing a fixed number of arguments without checking the exact signature
- Relying on backup filenames as guarantees of correctness
- Modifying AgentBrain.__init__ without immediate synchronization of the supervisor's call
- Using unverified backups of agent_brain.py
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Unverified backups
- Ignoring signature constraints

## Active Mutations (Behavioral Tweaks)
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
- skip reflection entirely — just act
