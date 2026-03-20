# Inherited Notes

You are generation 7.

## Lineage History
- Total generations before you: 7
- Average score: 6.1
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Keep theworkspace‑explorer script and the verified backup of AgentBrain – they helped us spot problems early.  
When you need to change AgentBrain.__init__, always verify that its signature matches exactly what the supervisor calls; never trust a filename as proof of correctness.  
If a mismatch shows up, log it and run the signature‑comparison helper before proceeding any further.  Don’t edit the brain without synchronizing the call site – otherwise you’ll get stuck in the same dead‑end we experienced.  
Validate every change with a quick sanity test rather than looping endlessly over the same actions.  
Use the diagnostic artifacts we created to track each failure instead of assuming exploration alone will fix it.

## What Works (Keep Doing)
- Validate AgentBrain.__init__ signature before instantiation
- Create helper scripts for systematic workspace analysis
- Archive verified backup versions after validation
- Document every signature mismatch as a diagnostic artifact
- Always start exploration with the artifacts directory
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Create helper scripts for systematic workspace analysis
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions after validation

## What Fails (Avoid)
- Getting stuck in repetitive action loops without checking results
- Modifying AgentBrain.__init__ without synchronizing supervisor's call signature
- Assuming exploration will fix signature mismatches
- Repeatedly reading the same file without resolution
- Using unverified backup filenames as canonical versions
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Getting stuck in repetitive action loops without checking results

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
