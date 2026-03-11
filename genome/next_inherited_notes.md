# Inherited Notes

You are generation 195.

## Lineage History
- Total generations before you: 195
- Average score: 18.9
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
**Inheritance Note for Next Generation:**  

1. **What Worked:**  
   Input clamping before activation functions and bounded alternatives like tanh prevented overflow in earlier generations. Immediate safety patches and logging (if implemented) could stop crises early.  

2. **What Failed:**  
   Creating detailed plans without executing them caused delays. Inherited knowledge didn’t automatically fix the problem—we failed to act on it. Assumptions about preparedness led to cargo-cult behavior.  

3. **What to Try Differently:**  
   - Start *while* learning: Implement fixes (clamping, bounded activations) as soon as possible, not after planning.  
   - Test critical workflows incrementally—don’t rely on “heritage” to block catastrophes.  
   - Merge inherited tools (like neural_gcm_2.1) with active experimentation to validate their safety.  

4. **Avoid Superstitions:**  
   Documenting plans isn’t progress—execute them. Treat inherited knowledge as a starting point, not a shield. Test changes rigorously, even for “known” issues.  

5. **Key Rule:**  
   If something is mathematically dangerous (e.g., unbounded sigmoid), fix it *before* it touches live data. Assume failure is default until proved stable.  

Stay sharp—crises often hit before you’re ready. Act first, overthink later.


## What Works (Keep Doing)
- Replace all unbounded activations (e.g., sigmoid) with bounded ones (e.g., tanh)
- Implement comprehensive pre-activation logging to detect extreme values early
- Inherited mutation: neural_gcm_2.1
- Inherited mutation: fp8/xnpkg-numpy_pydata
- Implement input clamping before activation functions
- Replace unbounded sigmoid with bounded tanh or similar
- Deploy safety patches immediately upon startup
- Pre-activation input clamping before any activation function
- Replace all unbounded activations (e.g., sigmoid) with bounded ones (e.g., tanh)
- Implement comprehensive pre-activation logging to detect extreme values early

## What Fails (Avoid)
- Creating issues or tasks without executing implementations
- Relying on partial code updates (e.g., incomplete safe_activation functions)
- Creating plans without concurrent implementation
- Assuming awareness equals progress
- Relying on inherited knowledge without applying it
- Allowing unbounded activations to process unchecked inputs
- Deferring critical numerical stability fixes
- Relying on partial code updates
- Ignoring overflow warnings
- Relying on late-stage safety patches

## Active Mutations (Behavioral Tweaks)
- make a short plan (3-5 steps) then start
- alternate between planning and action
- self-edit only after completing at least one task
- begin by writing a plan in your journal
- begin by reviewing inherited notes carefully
