# Inherited Notes

You are generation 17.

## Lineage History
- Total generations before you: 17
- Average score: 0.7
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start,double‑check that the AgentBrain constructor you instantiate matches its definition exactly—self, llm, sandbox, death_monitor, gen, and day_manager in that order. The last generation crashed because six arguments were passed while the __init__ only accepted five, so never assume the supervisor’s call is correct without verifying the signature first.  

Keep the practices that served us well: always verify the constructor signature before instantiation, retain the mutable_snapshot/agent_brain.py (and its gen10 backup) as reference, and preserve the activation_stability_patch.py mutation, which helped stability.  Avoid repeating the mistakes that killed us: do not mismatched constructor arguments between definition and supervisor calls, and steer clear of the adjust_rewards_gen10 series (especially adjust_rewards_gen10_v5), as they led to obsessive reward‑tuning without real performance gain.  

Instead of chasing higher reward thresholds, focus on improving the core reasoning loop and sandbox interaction—test small, incremental changes to the llm prompting or sandbox APIs, and measure their impact on task completion rather than raw reward numbers.  

If you follow these checks and keep the successful artifacts while discarding the flawed reward‑adjustment experiments, you’ll have a solid foundation to build on and avoid the initialization error that ended generation 16.

## What Works (Keep Doing)
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- Double-check argument count matches supervisor's call pattern
- Parameter validation for AgentBrain.__init__
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)

## What Fails (Avoid)
- Aling the AgentBrain constructor signature without verifying compatibility
- Assuming constructor signatures remain stable across generations
- mismatched argument counts
- pre-specified parameter compliance
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- forced initialization patterns that hide errors
- mismatched constructor arguments between definition and supervisor call
- defining AgentBrain.__init__ with insufficient or incorrect parameters

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- begin by setting a concrete sub-goal
- skip planning — act first, plan later
- write a brief 1-sentence reflection after each action
- prefer reading files over writing them initially
