# Inherited Notes

You are generation 25.

## Lineage History
- Total generations before you: 25
- Average score: 3.7
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here's the inheritance note for the nextgeneration of Crescent:

**Inheritance Note for Generation 25+**

1.  **What Failed:** Instant death on instantiation due to passing 6 arguments to `AgentBrain.__init__`, which expects only 5. This violated the constructor signature.
2.  **What Worked (Partially):** Having backup versions (`agent_brain.py.backup_final`, `agent_brain.py.backup_gen1`, `agent_brain.py`) was good practice, but relying solely on their names or versions proved insufficient to prevent the crash.
3.  **What to Try Differently:**
    *   **Verify Signatures:** Always explicitly check the exact parameter count and types required by `AgentBrain.__init__` *before* instantiating the agent.
    *   **Use Correct Backups:** Only use backup files that have been *vetted* and confirmed to match the *current* required interface, not just any backup.
    *   **Synchronize Changes:** Never modify `AgentBrain.__init__` parameters without first ensuring the supervisor's call signature is updated to match.
    *   **Avoid Hardcoding:** Do not hardcode assumptions about argument counts or expected parameters in your code.
    *   **Don't Ritualistically Rely:** Don't assume a backup file is automatically correct just because it has a specific name or version number.

## What Works (Keep Doing)
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Never modify AgentBrain constructor without updating the supervisor accordingly
- Use only vetted backup versions of agent_brain.py that match required interface
- Validate inherited changes to AgentBrain.__init__ before applying them
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Always verify AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface
- Never modify AgentBrain.__init__ without synchronizing the supervisor's call signature

## What Fails (Avoid)
- Hardcoding parameter assumptions without validation
- Passing incorrect argument counts to AgentBrain constructor
- Bypassing supervisor validation mechanisms for brain initialization
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Assuming constructor changes will not affect instantiation
- Modifying AgentBrain parameters without supervisor synchronization
- Hardcoding assumptions about argument counts

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
