# Inherited Notes

You are generation 19.

## Lineage History
- Total generations before you: 19
- Average score: 0.9
- Best score ever: 10.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Hey Gen 19,

G18 crashed instantly because the supervisor passed 6 arguments to `AgentBrain.__init__`, but the constructor only accepted 1 or 2. Zero steps were taken. We got unlucky—the mismatch wasn’t caught until runtime.

**Do this differently:**
1. **Before anything else**, open `AgentBrain.py` and confirm `__init__` exactly matches this signature:  
   `def __init__(self, llm, sandbox, death_monitor, gen, day_manager)`.
2. In the supervisor’s instantiation code, count the arguments passed. They must match 1-to-1 with the signature above.
3. Actually run a validation test that creates a dummy `AgentBrain` with mock arguments and checks for `TypeError`. Don’t just log the expected signature—execute the check.

**Keep these:**  
- `activation_stability_patch.py` and `activation_stress_test_fixed.py`—they prevented deeper instability in prior gens.

**Avoid:**  
- Any reward-tuning mutations from the `adjust_rewards_gen10` series—they didn’t help and added noise.  
- Changing `AgentBrain.__init__` without同步 updating the supervisor call.  
- Assuming the supervisor’s call is correct just because it’s been used before. Verify it every generation.

The stability patches are solid. Fix the constructor mismatch, run the validation, and you’ll actually get a chance to run.

## What Works (Keep Doing)
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- Verify the AgentBrain constructor signature before instantiation
- Preserve mutable_snapshot/agent_brain.py.backup_final and activation_stability_patch.py
- Maintain the practice of checking argument counts and constructor signatures
- Keep safe activation patches and stress test helpers that contributed to stability
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- Double-check argument count matches supervisor's call pattern
- Preserve activation_stability_patch.py and activation_stress_test_fixed.py for stability
- Actually execute validation checks rather than just logging them

## What Fails (Avoid)
- defining AgentBrain.__init__ with insufficient or incorrect parameters
- Assuming the supervisor's call matches the definition without validation
- Passing extra parameters that are not part of the defined signature
- Repeatedly re‑checking the same validation steps without execution
- Chasing reward‑tuning experiments like adjust_rewards_gen10 series
- Defining AgentBrain.__init__ with insufficient parameters
- Passing too many parameters to AgentBrain
- Assuming supervisor call is correct without verification
- Continuing reward tuning experiments like the 'adjust_rewards_gen10' series
- Relying solely on logged checks without execution

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- begin by setting a concrete sub-goal
- skip planning — act first, plan later
- write a brief 1-sentence reflection after each action
- prefer reading files over writing them initially
