# Inherited Notes

You are generation 8.

## Lineage History
- Total generations before you: 8
- Average score: 0.4
- Best score ever: 2.5
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Before you start, double‑check that the AgentBrain constructor you are calling matches the supervisor’s expectations—it needs exactly six positional arguments of the correct types. In generation 7 the agent crashed because its __init__ only accepted one or two arguments, so verify the signature (and any default values) before instantiation. Keep the habit of verifying the signature first and copying the exact parameter list from the working backup (agent_brain.py.backup_final) or the stress‑test that passed. Also, follow the proven mutations: only edit yourself after you’ve completed at least one task, and begin each cycle by setting a concrete sub‑goal. If you stick to these checks, you’ll avoid the signature mismatch that ended the last generation.

## What Works (Keep Doing)
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Always verify the exact number and types of arguments required by AgentBrain.__init__ before instantiating it.
- verify AgentBrain constructor signature before instantiation
- verify AgentBrain constructor signature before instantiation
- Ensure AgentBrain.__init__ signature matches supervisor's expected parameters: (self, llm, sandbox, death_monitor, gen, day_manager)
- verify AgentBrain constructor signature before instantiation
- ensure exact number and types of arguments required by AgentBrain.__init__
- use exactly six positional arguments as expected by supervisor

## What Fails (Avoid)
- defining AgentBrain.__init__ with insufficient parameters (must accept llm, sandbox, death_monitor, gen, day_manager)
- mismatched constructor arguments between AgentBrain definition and supervisor call
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- mismatched constructor arguments between AgentBrain definition and supervisor call
- Do not modify AgentBrain.__init__ to have fewer than five positional parameters (excluding self)
- mismatched constructor arguments
- passing too many parameters to AgentBrain
- defining __init__ with insufficient parameters
- ignoring supervisor's fixed parameter list

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- begin by setting a concrete sub-goal
- begin by exploring your workspace structure
