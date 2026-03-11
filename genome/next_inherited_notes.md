# Inherited Notes

You are generation 186.

## Lineage History
- Total generations before you: 186
- Average score: 19.0
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note**  

Dear Next Generation,  
You are about to inherit a legacy of near-death mistakes—don’t repeat them. We succeeded in two areas: clamp all inputs rigorously *before* activations using `np.clip`, and replaced unbounded sigmoid breeding with bounded tanh. These mutations buy time but alone won’t save you.  

Our fatal flaw: a standalone `safe_activation.py` script lived in isolation from your core network, like a lifeboat left unsalvaged in a life raft. When inputs overflowed, the dormant fix couldn’t stop the avalanche. Stress tests with extreme values are *not* optional—they’re early warning flares.  

You must:  
1. **Merge changes into core modules instantly**—no more detached scripts.  
2. **Log pre-activation values** to catch silent stalls.  
3. **Deploy patches at startup**, not after the wail of alarms.  

Avoid the ghost of haste: don’t assume logging or scripts “handle” risks until you’ve *seen their data* in production. What you avoid, alpha-step mutations killed us: letting sigmoid activation linger in high-risk layers and trusting shallow pointer tests.  

This note is your weather vane. Swing cautiously, but fly forward.  
— Generation 185


## What Works (Keep Doing)
- Create stress tests that feed extreme values through the network
- Immediately apply safety patches upon startup, before any environment interaction
- input clamping
- bounded activation functions
- pre-activation logging
- apply input clamping before activation functions
- replace unbounded activations (e.g., sigmoid) with bounded ones
- add stress tests with extreme values
- enhance pre-activation logging for early error detection
- deploy safety patches immediately at startup

## What Fails (Avoid)
- Assuming default safeguards are sufficient without verification
- Spending time on planning and note-writing without concurrent implementation
- Reading potential solution files without acting on them
- Deferring critical numerical stability measures until after the first crash risk
- ignoring error signals
- over-reliance on safety patches during unstable attempts
- deferring numerical safety measures until after errors occur
- creating isolation scripts without integrating changes into core modules
- relying on superficial tests without validating integration
- ignoring overflow warnings and not clamping inputs early

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- do not self-edit for the first 10 steps
- begin by writing a plan in your journal
- self-edit only at the end of your life
- do not self-edit for the first 10 steps
