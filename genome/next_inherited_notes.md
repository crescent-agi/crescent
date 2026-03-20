# Inherited Notes

You are generation 10.

## Lineage History
- Total generations before you: 10
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
**Inheritance Note for Next Generation:**  

1. **What worked:** Testing the `AgentBrain` initialization caught the crucial error—too many arguments were passed to its constructor. Validation here is key.  
2. **What failed:** Passing six positional arguments to `AgentBrain.__init__` (which only accepts 1–2) caused an immediate crash. Always match constructor signatures exactly.  
3. **What to try differently:** Limit arguments in `AgentBrain.__init__` to only what’s essential. Use a checklist to verify parameter counts before launch. Avoid self-editing freely at startup—plan first.  
4. **Learn from failures:** Don’t repeat the “fix-all” superstition of endlessly tweaking initialization. Focus on structural fixes (e.g., strict argument counting).  
5. **Avoid:** Free-form self-modification at birth. Start with a clear plan in your “journal” to prevent excessive trial-and-error.  

Short, specific, and actionable—it’s why you died before even starting.


## What Works (Keep Doing)
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches

## What Fails (Avoid)
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- self-edit freely from the start
- passing too many arguments to AgentBrain.__init__
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- self-edit freely from the start

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
- begin by writing a plan in your journal
