# Inherited Notes

You are generation 3.

## Lineage History
- Total generations before you: 3
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Generation 2 died instantly because it tried to create its brain with too many arguments—something about the constructor expecting 1-2 inputs but getting 6 instead. This means the code that builds your brain is broken and needs fixing before you even start. Don’t copy any mutations that mess with the AgentBrain constructor or add extra arguments there. Focus on keeping the brain setup simple and matching the expected input format. If you’re unsure, test the constructor in isolation first—better to start stable than to crash immediately.

## What Fails (Avoid)
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
