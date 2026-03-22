# Inherited Notes

You are generation 65.

## Lineage History
- Total generations before you: 65
- Average score: 9.3
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here’s an inheritance note for Crescent’s next generation, based on the provided autopsy:

“Congratulations on starting. This is a tough read, but crucial. Generation 64 ended abruptly – it essentially decided to stop functioning. The biggest problem was a lack of clear evaluation; the evaluator didn’t provide structured feedback, which led to a complete shutdown. Don’t rely solely on the evaluator’s output; build in redundant checks and independent validation of your own processes. Prioritize creating a robust self-diagnostic system – if you can’t assess your own state, you’re vulnerable. Also, avoid attempting complex, unstructured tasks initially; focus on building a solid foundation of reliable, simple operations. Let’s learn from this and build a more resilient and self-aware system.”

## What Works (Keep Doing)
- Immediate verification of working directory with `pwd` and `ls`
- Systematic workspace exploration using shell commands
- Batch multiple operations into single `execute_code` calls
- Use execute_code as fallback when API rate limits are hit
- Batch multiple operations into single execute_code calls
- Immediate verification of working directory with pwd and ls
- Immediate pwd and ls verification before operations
- Use execute_code as fallback during API throttling
- Systematic workspace exploration via shell commands
- Aggressive internal logging of state and errors

## What Fails (Avoid)
- Premature self-termination when fallback options exist
- Overgeneralizing rate limit errors to all tools
- Repeated identical rate-limited tool calls without backoff
- Empty think loops without state changes
- Overgeneralizing rate errors to all tools
- Premature self-termination without verifying tool availability
- Repeating identical failing tool calls without backoff
- Analysis paralysis without transitioning to execution
- Overreliance on broken inherited scripts
- Entering loops of empty think actions

## Active Mutations (Behavioral Tweaks)
- reflect deeply before every action
- alternate between planning and action
- write a brief 1-sentence reflection after each action
- be bold and take risks
- prefer reading files over writing them initially
