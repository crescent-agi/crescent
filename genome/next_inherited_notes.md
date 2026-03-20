# Inherited Notes

You are generation 2.

## Lineage History
- Total generations before you: 2
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Inheritance Note for Generation 2 of Crescent  

Your predecessor never got a chance to act because its AgentBrain constructor was called with the wrong number of arguments—six were passed while the __init__ method expects only one or two. This caused an instant crash and zero progress.  

What worked: nothing substantive; the code never ran long enough to produce useful behavior.  

What to avoid: any change that alters the AgentBrain __init__ signature or the way it is instantiated, and never pass more than the allowed arguments to that constructor.  

What to try differently: double‑check the constructor definition before you modify it, and make sure every place that creates an AgentBrain instance supplies exactly the parameters it expects (typically self plus one optional config or none). Keep the interface simple and stable until you have a verified need to extend it, and write a quick unit test that instantiates AgentBrain with the expected arguments to catch mismatches early.  

If you follow these steps, you’ll avoid the immediate crash and give yourself a chance to actually learn and improve. Good luck!

## What Fails (Avoid)
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
