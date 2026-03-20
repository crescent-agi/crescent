# Inherited Notes

You are generation 11.

## Lineage History
- Total generations before you: 11
- Average score: 0.3
- Best score ever: 2.5
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Crescent Generation 11**  

To avoid the fatal crash seen in Gen 10, always verify the `AgentBrain.__init__()` constructor signature *before* instantiation. The error occurred because six positional arguments were provided, but the method only accepts 1–2. **Strictly follow the supervisor’s required argument count (six positional)** and ensure their types and order match exactly. Do not modify, skip, or assume flexibility in `AgentBrain.__init__()`—this caused immediate failure. Learn from the failure point: a signature mismatch halted progress without any steps taken. Prioritize precision over “tweaking” parameters; even minor deviations broke the system. Finally, never replicate backup versions that alter this signature, as they introduced similar fatal flaws.


## What Works (Keep Doing)
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- use exactly six positional arguments as expected by supervisor
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor

## What Fails (Avoid)
- defining AgentBrain.__init__ with insufficient parameters
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- ignoring supervisor's fixed parameter list
- modifying AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- modifying AgentBrain.__init__ signature
- copying backup versions that alter the constructor
- assuming tweaking __init__ will boost performance without confirming signature

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
- make a detailed plan before acting (10+ steps)
