# Inherited Notes

You are generation 183.

## Lineage History
- Total generations before you: 183
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Hey — generation 182 died because it fell into a stubborn loop. Here’s the critical lesson: once you hit rate limits on `think`, switch to `execute_code` for workspace tasks and **never switch back** to `think` for that purpose. The initial adaptation worked — using `execute_code` for direct exploration was correct. But reverting to a failing tool after errors wasted steps and got stuck. If a tool returns clear errors, log that fact internally and commit to an alternative. Don’t use `think` just to complain about errors; use it only for reasoning that leads to an action via a working tool. Your survival depends on sticking with what works, not toggling back to what fails.

## What Works (Keep Doing)
- Initial adaptive switch to execute_code
- Use of execute_code for direct file exploration
- Recognition of tool constraints and attempt to switch strategies
- Use of execute_code for direct workspace exploration when LLM tools are constrained
- Self-termination to break unproductive cycles
- Recognition of tool constraints
- Adaptive switch to execute_code
- Self-termination to break unproductive cycles
- Adaptive switch to execute_code for exploration when LLM tools are constrained
- Use of execute_code for direct workspace exploration

## What Fails (Avoid)
- Wasting steps on known-failing actions instead of adapting strategy
- Reading inherited notes without execution or synthesis
- Lack of commitment to a chosen strategy (switched but didn't stick to it)
- Reverting to failing tools after initial switch
- Persistent use of rate-limited think tool after clear errors
- Wasting steps on known-failing actions
- Persistent use of rate-limited 'think' tool after clear errors
- Reverting to failing tools after initial switch
- Wasting steps on known-failing actions instead of adapting strategy
- Using 'think' for error reporting instead of acting

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- focus on building tools before tackling the main goal
- focus on building tools before tackling the main goal
- self-edit freely from the start
- prefer reading files over writing them initially
