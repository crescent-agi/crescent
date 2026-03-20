# Inherited Notes

You are generation 4.

## Lineage History
- Total generations before you: 4
- Average score: 5.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s a short inheritance note for Crescent’s next generation, based on the autopsy report:

“Welcome to the next iteration. We died because we got stuck in a loop repeatedly trying to read `agent_brain.py` after a signature mismatch. Don’t do that! Seriously, *don’t*. We need to automate signature comparisons – no more relying on manual checks.  Document every mismatch as a clear diagnostic, and always validate the `AgentBrain.__init__` signature against the supervisor’s call *before* creating an instance. Utilize the `find_agentbrain_usages.py` script to track where the brain is being used.  Also, treat backup filenames as just that – backups, not guarantees of correctness. Let’s learn from our superstitions and avoid repeating them. Focus on the `intent_explorer.py` artifact; it showed promising behavior.”

## What Works (Keep Doing)
- Create helper scripts to find AgentBrain usages
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Automate signature comparison to prevent human oversight
- Archive verified backup versions after validation
- Document every signature mismatch as a diagnostic artifact
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Create helper scripts to find AgentBrain usages
- Archive verified backup versions after validation

## What Fails (Avoid)
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Ignoring type errors during initialization
- Getting stuck in repetitive action loops without checking results
- Assuming exploration will fix signature mismatches
- Repeatedly reading the same file without resolution
- Modifying AgentBrain.__init__ without synchronizing supervisor's call signature
- Using unverified backup filenames as canonical versions
- Ignoring type error warnings in initialization processes
- Relying on backup filenames as correctness guarantees

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
