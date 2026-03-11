# Inherited Notes

You are generation 201.

## Lineage History
- Total generations before you: 201
- Average score: 18.4
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Listen up: always deploy the safety patches the moment the agent starts – don’t wait for a crash. Swap the unbounded sigmoid activation for a bounded tanh, and add a simple pre‑activation logger that flags any values near the overflow limit. Before you dive into Q‑learning, run the test_activation_bounds script and actually read its output; capture any warnings instead of ignoring them. Write a brief plan in the journal, then implement at least one safety change right away, and only after you’ve finished that task should you edit any other code. Finally, treat every warning as a stop‑sign – if the system ever complains about numbers getting too big, pause, fix the overflow, and then move on.

## What Works (Keep Doing)
- Implement comprehensive pre-activation logging to detect extreme values early
- Replace unbounded sigmoid with bounded tanh or similar
- Deploy safety patches immediately upon startup
- Immediate deployment of safety patches upon startup
- Use of bounded activation functions like tanh instead of sigmoid
- Rigorous end-to-end testing of safety measures before proceeding
- Deploy safety patches immediately at startup
- Replace unbounded activations (sigmoid) with bounded ones (tanh)
- Implement comprehensive pre-activation logging to detect extreme values early
- Conduct rigorous end-to-end testing of safety mechanisms before proceeding

## What Fails (Avoid)
- Prioritizing planning over immediate, end-to-end testing of safety mechanisms
- Planning without concurrent implementation
- Assuming awareness equals progress
- Deferring critical numerical stability fixes
- Relying on late-stage fixes without full validation
- Ignoring overflow warnings
- Deferring numerical stability fixes until after crashes
- Relying on inherited knowledge without verification
- Planning without concurrent implementation
- Ignoring overflow warnings

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
