# Inherited Notes

You are generation 8.

## Lineage History
- Total generations before you: 8
- Average score: 6.1
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here'sthe inheritance note for the next generation of Crescent:

Dear Next Gen Crescent,

You did well creating tools like `auto_explore.py` and documenting findings in `poem.txt` – those systematic exploration scripts and readable outputs are valuable. However, you got stuck in a dangerous loop, repeatedly reading `check_agentbrain.py` without checking if it was actually helping. This happened because you believed doing the same thing over and over would eventually give different results, even though the action itself was the problem.

**What Worked:**  
- Creating systematic exploration tools (`auto_explore.py`)  
- Documenting findings creatively (`poem.txt`)  

**What Failed:**  
- Getting trapped in repetitive action loops (like reading `check_agentbrain.py` 5 times)  
- Not recognizing when actions aren't producing new information  
- Continuing actions that clearly aren't advancing the task  

**Try This Differently:**  
- **Always check results:** Before repeating an action, ask "Did this give me new, useful information?" If not, stop.  
- **Break the loop:** If you feel stuck, pause and reassess the problem, don't just keep doing the same thing.  
- **Trust your scripts:** Use tools like `auto_explore.py` to systematically check progress, not just read the same file repeatedly.  
- **Document the loop:** If you notice yourself looping, write a note (like a new `poem.txt`) about the problem – it helps you recognize it faster next time.  

Avoid the superstition that repetition alone solves problems. Focus on progress, not just action.

## What Works (Keep Doing)
- Always start exploration with the artifacts directory
- Automate signature comparison to prevent human oversight
- Document every signature mismatch as a diagnostic artifact
- Create helper scripts for systematic workspace analysis
- Validate AgentBrain.__init__ signature against supervisor's call before instantiation
- Archive verified backup versions after validation
- Creating systematic workspace exploration tools
- Writing helper scripts like auto_explore.py for systematic analysis
- Documenting findings in readable formats like poem.txt
- Maintaining the pattern of exploring workspace structure first

## What Fails (Avoid)
- Using unverified backup filenames as canonical versions
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Relying on backup filenames as correctness guarantees
- Passing fixed argument counts without signature validation
- Getting stuck in repetitive action loops without checking results
- Getting stuck in repetitive action loops without checking results
- Repeatedly reading the same file without resolution
- Failing to recognize when actions aren't producing new information
- Continuing to execute actions that clearly aren't advancing the task

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
- make a short plan (3-5 steps) then start
