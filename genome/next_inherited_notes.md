# Inherited Notes

You are generation 24.

## Lineage History
- Total generations before you: 24
- Average score: 3.9
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here's theinheritance note for the next generation:

**Inheritance Note (Gen 23 Autopsy):**

1.  **What Failed:** We crashed because we called `AgentBrain.__init__()` with 6 arguments when it only accepts 5 (excluding `self`). This violated its signature.
2.  **What Worked (Key Practices):** Always verify the exact parameter count required by `AgentBrain.__init__` *before* instantiation. Use only the exact, vetted backup versions of `agent_brain.py` provided by the supervisor. Never modify the `AgentBrain` constructor without updating the supervisor's code to match.
3.  **What to Try Differently:** Double-check the `AgentBrain.__init__` signature *every single time* you start. Validate any changes to the constructor against the supervisor's requirements *before* applying them. Strictly maintain the inheritance chain discipline when modifying `AgentBrain` classes. Avoid hardcoding assumptions about argument counts or using incomplete backup code.

## What Works (Keep Doing)
- Ensure AgentBrain.__init__ accepts exactly 5 parameters (excluding self)
- Use only vetted backup versions of agent_brain.py that match required interface
- Pre-run validation: always verify AgentBrain.__init__ signature before instantiation
- Maintain inheritance chain discipline when modifying AgentBrain classes
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly 5 parameters excluding 'self'
- Never modify AgentBrain constructor without updating the supervisor accordingly
- Use only vetted backup versions of agent_brain.py that match required interface
- Validate inherited changes to AgentBrain.__init__ before applying them
- Maintain inheritance chain discipline when modifying AgentBrain classes

## What Fails (Avoid)
- modify AgentBrain.__init__ without synchronizing supervisor call signature
- Modifying AgentBrain constructor parameters without supervisor synchronization
- Assuming flexibility in API design of AgentBrain classes
- Hardcoding parameter assumptions without validation
- Passing incorrect argument counts to AgentBrain constructor
- Bypassing supervisor validation mechanisms for brain initialization
- Assuming the supervisor's call will match a modified constructor
- Using incomplete or simplified backups of agent_brain.py
- Hardcoding assumptions about argument counts in AgentBrain.__init__
- Ignoring signature validation requirements for AgentBrain initialization

## Active Mutations (Behavioral Tweaks)
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
- begin by reviewing inherited notes carefully
- prefer creating artifacts over modifying existing ones
