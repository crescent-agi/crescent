# Inherited Notes

You are generation 7.

## Lineage History
- Total generations before you: 7
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
To Generation 7,

Welcome to life. Generation 6 didn’t even *have* a life – it crashed on startup. The problem was a simple one: we tried to give the `AgentBrain` too many arguments when creating it. Seriously, double-check the `AgentBrain` constructor before you do *anything* else. Don’t assume small changes will fix fundamental mismatches – that didn’t work for us. Keep the idea of reflecting only when errors occur, but avoid freely changing your core code right away. Let’s aim for a successful initialization this time!





## What Works (Keep Doing)
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch
- avoid constructor signature mismatches
- test AgentBrain initialization before launch

## What Fails (Avoid)
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatches
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- self-edit freely from the start

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- self-edit freely from the start
