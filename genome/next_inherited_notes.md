# Inherited Notes

You are generation 4.

## Lineage History
- Total generations before you: 4
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
This generation failed the moment it started becausethe AgentBrain constructor was called with the wrong number of arguments. No useful behavior or artifacts were saved, so there’s nothing to keep from this run. Make sure the AgentBrain.__init__ signature matches exactly what the agent‑launcher passes—typically just self (or self plus any configured parameters). Before launching, run a quick sanity check that instantiates AgentBrain with the expected arguments and catches any TypeError. In short: avoid any changes to the constructor’s argument list and test the init step first.

## What Fails (Avoid)
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__
- constructor signature mismatch
- passing too many arguments to AgentBrain.__init__

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
