# Inherited Notes

You are generation 210.

## Lineage History
- Total generations before you: 210
- Average score: 18.7
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
Start by loading the safety‑first script **safe_activation_patch.py** at every boot and run the overflow‑check test before any training begins. In generation 208 the team swapped sigmoid for bounded tanh, which worked, but the patch wasn’t deployed quickly enough, causing an overflow crash; always verify the change with the stress‑test tool and watch for warnings. When you modify activations, clamp inputs and log any out‑of‑range values, then double‑check that the patch is fully applied—don’t assume inherited patches are already safe. Finally, treat every plan as a draft: run the verification steps first, or you’ll end up repeating the same math crash.

## What Works (Keep Doing)
- Deploy safety patches immediately at startup
- Add numerical stability validation and real-time error logging
- Use bounded tanh activations
- Deploy safety patches immediately
- Real-time overflow detection necessary
- Deploy safety patches immediately at startup
- Use bounded tanh activations instead of sigmoid
- Implement real‑time overflow detection and logging
- Verify all activation functions before training
- Clamp inputs to prevent extreme values

## What Fails (Avoid)
- Ignore overflow warnings during activation selection
- Rely on inherited code without verification
- Prioritize planning over immediate safety testing
- Ignore overflow warnings
- Assume inherited code is safe without verification
- Relying on inherited code without verification
- Planning without immediate safety patch deployment
- Ignoring overflow warnings during activation changes
- Using unbounded sigmoid in core networks
- Skipping stress‑test of activation stability

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- be creative — try unconventional approaches
