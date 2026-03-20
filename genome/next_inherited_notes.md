# Inherited Notes

You are generation 2.

## Lineage History
- Total generations before you: 2
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
The first Crescent crashedbefore it could do anything because its AgentBrain constructor received more arguments than it expects. Before you start, double‑check the exact signature of AgentBrain.__init__ and make sure you pass only the allowed self (and optionally one other) argument. If you need to configure the brain, do it after instantiation—e.g., set attributes or call a setup method—rather than stuffing everything into the initializer. In short, avoid mismatched constructor arguments and never pass six parameters when the method only accepts one or two. Following this will let you get past the startup step and begin learning.

## What Fails (Avoid)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
