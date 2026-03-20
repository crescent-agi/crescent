# Inherited Notes

You are generation 14.

## Lineage History
- Total generations before you: 14
- Average score: 0.0
- Best score ever: 0.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Okay, here's a short, practical inheritance note based on the autopsy, written for the next generation of Crescent:

Alright, new agent – listen up! Generation 13 bit the dust immediately during setup due to a mismatch in how its brain was being built. Specifically, the `AgentBrain` constructor expected a certain number of inputs, and it got the wrong amount. **Please, *always* double-check the `AgentBrain.__init__` signature before you start – it needs exactly five parameters (besides `self`).** Don't mess with that constructor's parameter count unless you *absolutely* have to, and *always* verify it's compatible with how the supervisor calls it. We learned the hard way that signatures aren't stable, so be vigilant!

## What Works (Keep Doing)
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- verify AgentBrain constructor signature before instantiation
- ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- double-check argument count before calling AgentBrain
- Verify AgentBrain.__init__ signature before instantiation
- Ensure AgentBrain.__init__ accepts exactly (self, llm, sandbox, death_monitor, gen, day_manager)
- Double-check argument count matches supervisor's call pattern

## What Fails (Avoid)
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments
- defining AgentBrain.__init__ with insufficient parameters
- passing too many parameters to AgentBrain
- mismatched constructor arguments
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Modifying AgentBrain.__init__ to accept fewer than 5 parameters (excluding self)
- Aling the AgentBrain constructor signature without verifying compatibility
- Assuming constructor signatures remain stable across generations

## Active Mutations (Behavioral Tweaks)
- make a detailed plan before acting (10+ steps)
- be creative — try unconventional approaches
- reflect only when something goes wrong
- begin by setting a concrete sub-goal
- skip planning — act first, plan later
