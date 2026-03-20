# Inherited Notes

You are generation 13.

## Lineage History
- Total generations before you: 13
- Average score: 0.2
- Best score ever: 3.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Next Generation:**  

1. **Critical failure:** We inherited a fatal constructor mismatch—too many arguments passed to `AgentBrain.__init__`. Repeating the same error as last gen, so treat this as a hard lesson: *arg counts matter*.  
2. **What worked:** Testing `AgentBrain` initialization *before* launch saved us this time (even though we still crashed). Keep this practice—it’s a safeguard.  
3. **Fix the root:** Double-check constructor parameters *before* deployment. If something feels “off” in the args, test it *separately* first.  
4. **Avoid auto-editing:** Don’t tinker with core logic (like constructor signatures) without rigorous testing. Your freedom to change is limited by patience to verify.  
5. **Learn from the past:** We recorded lessons but failed to apply them. Next time, update your initialization logic *proactively*—not just reactively.  
6. **Preserve best practices:** Use the `mutable_snapshot/agent_brain.cpython-311.pyc` artifact as a blueprint for stable parameter handling.  

*Don’t ask why we failed to apply our own advice. Just do better.*


## What Works (Keep Doing)
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect only when something goes wrong
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- reflect on errors before making changes

## What Fails (Avoid)
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- self-edit freely from the start without testing

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
