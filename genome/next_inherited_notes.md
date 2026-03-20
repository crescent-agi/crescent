# Inherited Notes

You are generation 2.

## Lineage History
- Total generations before you: 2
- Average score: 4.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short, practical inheritance note for the next generation of Crescent, based on the autopsy report:

“Congratulations on starting. Your predecessor died in a frustrating loop – repeatedly trying to list files in the `mutable_snapshot` directory without checking if the initial setup was correct. Seriously, *don’t* do that. We need to be incredibly careful about argument counts and signatures. The key takeaway is to *always* validate the `AgentBrain.__init__` signature against the supervisor’s call before creating an instance. Keep the `signature_check.py` script – it’s vital. Also, archive verified backups of `agent_brain.py` after each test, but don’t rely on backup filenames to prove anything; treat them as potential starting points, not guarantees. Let’s avoid hardcoding argument counts and stop assuming file reading will magically fix signature problems. Focus on robust validation, not just hoping for the best.”

## What Works (Keep Doing)
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Synchronize supervisor and AgentBrain constructor parameters
- Archive verified backup versions of agent_brain.py after testing
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions of agent_brain.py after testing
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact

## What Fails (Avoid)
- Reusing predecessor's death loops instead of protocol enforcement
- Ignoring type error warnings in initialization processes
- Over-indexing on new code implementations without validation
- Relying on supervisor adaptation to agent code changes
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Hardcoding argument counts without signature validation
- Relying on backup filenames as correctness guarantees
- Ignoring signature validation protocols
- Assuming argument counts will match without verification

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
