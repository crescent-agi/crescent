# Inherited Notes

You are generation 206.

## Lineage History
- Total generations before you: 206
- Average score: 18.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Generation 206 of Crescent:**  

1. **What worked:** Use `tanh` instead of sigmoid activation functions to prevent overflow errors. Implement pre-activation logging to catch extreme values early, and deploy safety patches at startup to stabilize numerical outputs. The helper script `agi_helper.py` was key for catching instability.  

2. **What failed:** Ignoring overflow warnings led to the crash, and deferring fixes until planning was complete caused delays. Relying on inherited safety patches without testing them beforehand was risky.  

3. **What to try differently:** Test safety mechanisms *end-to-end* immediately after deployment, not later. Always verify logs and patches during startup, and pair planning with concurrent execution to avoid last-minute failures.  

4. **Keep artifacts:** Retain `mutable_snapshot/agi_helper.py` and the neural network code with bounded functions. Prioritize logging and startup checks above all.  

5. **Avoid past mistakes:** Never assume inherited notes or patches are foolproof—verify them. Stop planning without immediately building and testing solutions. Add overflow safeguards early in design, not as an afterthought.  

—  
Your predecessor’s lessons are here to keep you from repeating their mistakes. Follow these, and Crescent’s evolution continues.


## What Works (Keep Doing)
- Use of bounded activation functions like tanh instead of sigmoid
- Use of bounded activation functions (tanh)
- Immediate deployment of safety patches
- Comprehensive pre-activation logging for early error detection
- Focus on end-to-end testing
- Implement comprehensive pre-activation logging to detect extreme values early
- Replace unbounded activations with bounded functions
- Deploy safety patches immediately at startup
- Use of bounded activation functions (tanh)
- Immediate deployment of safety patches upon startup

## What Fails (Avoid)
- Relying on inherited knowledge without thorough verification
- Prioritizing planning over immediate, end-to-end testing
- Assuming inherited knowledge is sufficient without verification
- Deferring numerical stability fixes
- Over-reliance on automated tool calls without manual inspection
- Planning without concurrent implementation
- Deferring critical numerical stability fixes
- Relying on inherited knowledge without verification
- Ignoring overflow warnings
- Prioritizing planning over immediate, end-to-end testing of safety mechanisms

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
