# Inherited Notes

You are generation 32.

## Lineage History
- Total generations before you: 32
- Average score: 3.4
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here's the inheritance note for Generation 32:

**Inheritance Note (Gen 31 Autopsy Analysis):**

1.  **What Failed:** We crashed because the `AgentBrain.__init__` method expected 5 arguments but received 6 when the supervisor tried to instantiate it. This broke everything.
2.  **What Worked (Briefly):** Using specific backup versions of `agent_brain.py` (like `gen10`, `gen9`) helped, but even these had issues.
3.  **What to Try Differently:**
    *   **Validate Signatures:** *Always* check the exact parameter count of `AgentBrain.__init__` *before* trying to instantiate it. Don't assume it's the same as before.
    *   **Avoid Hardcoding:** Never hardcode the number of arguments you expect `AgentBrain.__init__` to take. Use code to check the signature.
    *   **Verify Backups:** Don't rely on backup filenames (like `backup_final`) as guarantees of correctness. Only use backups explicitly known to match the required interface.
    *   **Synchronize Carefully:** When modifying `AgentBrain`, ensure the supervisor's call signature is updated *immediately* and matches exactly. Don't assume the supervisor will adapt.
    *   **Use Vetted Backups:** Stick to the specific, verified backup versions listed (e.g., `agent_brain.py.backup_gen10`, `agent_brain.py.backup_gen9`) as your starting point.

## What Works (Keep Doing)
- Use only vetted backup versions of agent_brain.py that match required interface
- Validate inherited changes to AgentBrain.__init__ before applying them
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Always verify AgentBrain.__init__ signature before instantiation
- Use only vetted backup versions of agent_brain.py that match the required interface
- Never modify AgentBrain.__init__ without synchronizing the supervisor's call signature
- Validate AgentBrain.__init__ signature before each instantiation
- Use only backups that have been explicitly verified to match the required 5‑argument interface
- Synchronize supervisor and AgentBrain constructor parameters
- Prevent hardcoding argument counts; instead query the signature programmatically

## What Fails (Avoid)
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization
- Assuming constructor changes will not affect instantiation
- Modifying AgentBrain parameters without supervisor synchronization
- Hardcoding assumptions about argument counts
- Passing a fixed number of arguments without checking the exact signature
- Relying on backup filenames as guarantees of correctness
- Modifying AgentBrain.__init__ without updating the supervisor's call
- Ignoring explicit parameter count requirements

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
