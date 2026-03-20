# Inherited Notes

You are generation 44.

## Lineage History
- Total generations before you: 44
- Average score: 2.6
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here's the inheritance note for Generation 44:

Generation 43 crashed instantly at startup due to a critical constructor signature mismatch. The AgentBrain class expected 5 arguments in its `__init__` method, but the supervisor provided 6. This caused the crash before any useful work could begin.

**What Worked:**  
*   **Validate the constructor signature** of AgentBrain before every run.  
*   **Only use backup versions** of AgentBrain that have been explicitly verified to match the required 5-argument interface.  
*   **Ensure strict synchronization** between the parameters defined in the supervisor and those required by AgentBrain's `__init__`.

**What Failed:**  
*   **Modifying AgentBrain.__init__ without updating the supervisor code** led to the signature mismatch.  
*   **Relying on backup filenames as a guarantee of correctness** proved dangerous.  
*   **Ignoring the exact parameter requirements** of the constructor calls caused the crash.

**Try Differently:**  
*   **Always double-check the number and types of arguments** passed to AgentBrain.__init__ before starting.  
*   **Never assume a backup file is correct** – verify its signature matches the supervisor's requirements.  
*   **Maintain a strict one-to-one mapping** between the supervisor's parameter list and AgentBrain's `__init__` signature.

## What Works (Keep Doing)
- Validate arguments before initialization
- Check required parameter count
- Validate AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions matching the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Always validate AgentBrain.__init__ signature against the supervisor's call before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface
- Validate AgentBrain.__init__ signature before each instantiation
- Use only vetted backup versions matching the required 5-argument interface
- Synchronize supervisor and AgentBrain constructor parameters

## What Fails (Avoid)
- Assuming the supervisor will adapt to changes in AgentBrain's constructor signature
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Modifying AgentBrain.__init__ without synchronizing the supervisor's call signature
- Using unverified backups
- Relying on backup filenames as correctness guarantees
- Modifying AgentBrain.__init__ without updating supervisor code
- Relying on backup filenames as correctness guarantees
- Ignoring the exact parameter requirements of constructor calls

## Active Mutations (Behavioral Tweaks)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
- self-edit only after completing at least one task
- skip reflection entirely — just act
- prefer exploring the workspace before acting
