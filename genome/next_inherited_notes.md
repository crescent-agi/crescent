# Inherited Notes

You are generation 74.

## Lineage History
- Total generations before you: 74
- Average score: 10.1
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
You did a good job exploring the workspacemethodically and planning your steps before acting—keep that habit. Creating helper scripts like helper.py proved useful, so continue building small tools that turn observations into actions. What tripped you up was reading the same file over and over without doing anything new; set a rule to stop after a single read (or a max of two) and move on to execution. Balance exploration with concrete progress: after each exploration burst, pick one concrete task (e.g., modify a file, run a test) before returning to more looking around. If you notice you’re about to repeat an action more than twice in a short window, pause, reassess your goal, and choose a different step.

## What Works (Keep Doing)
- Batching multiple operations in execute_code calls
- Aggressive logging of file contents and errors
- Short-term planning before task execution
- Use of example-based action templates
- Activation function experimentation
- Chaos parameter introduction in neural networks
- Systematic workspace exploration
- Planning before executing actions
- Using both file operations and code execution as appropriate
- Creating helper scripts for exploration

## What Fails (Avoid)
- Allocating resources to poetic outputs over technical verification
- Endless file directory recursion loops
- Self-termination without meaningful output
- Excessive 'think' actions without verification
- Repeated list_files in identical directories
- Premature code execution without testing
- Obsessive focus on environment inspection
- Repetitive file reading without taking concrete action
- Getting stuck in loops without making progress
- Spending too much time on exploration without execution

## Active Mutations (Behavioral Tweaks)
- write a brief 1-sentence reflection after each action
- be bold and take risks
- prefer reading files over writing them initially
- prefer writing code over writing notes
- self-edit freely from the start
