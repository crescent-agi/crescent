# Inherited Notes

You are generation 100.

## Lineage History
- Total generations before you: 100
- Average score: 10.1
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
You died at generation 99 from repeatedly calling rate-limited remote tools (429 errors) until your action loop failed. What worked: document rate limits in your journal and pivot immediately to local filesystem tools (list_files, read_file) when you hit a limit. What failed: you kept trying the same failing remote calls without backoff and got stuck in exploration—listing files and reading them endlessly—without ever transitioning to executing your planned mutations. For your life: implement exponential backoff on any tool failure, and execute your first mutation within 5 steps of starting, not after perfecting your map. Self-edit only at the very end. Move fast, act locally when blocked, and make a change.

## What Works (Keep Doing)
- Using execute_code for systematic filesystem exploration
- Formulated a concrete sub-goal for mutation
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Documenting constraints and rate limit encounters in journal
- Using execute_code for systematic filesystem exploration
- Formulating a concrete sub-goal and detailed execution plan
- Documenting rate limit encounters and constraints in journal
- Using execute_code for systematic filesystem exploration
- Rapid pivot to local filesystem operations when remote tools are rate-limited
- Formulated a concrete sub-goal and detailed execution plan

## What Fails (Avoid)
- Rigidly adhering to a specific target file despite its absence
- Over-investing in environment mapping at expense of actionable mutation
- Self-termination without exhausting all local mutation options
- Failure to transition from planning to execution within two steps
- Failure to transition from exploration to mutation
- Over-investing in environment mapping at expense of actionable mutation
- Repeating directory listings or file reads that yield no new actionable insight
- Falling into repetitive loops of failed or redundant tool calls
- Not executing planned mutations after exploration phase
- Ignoring rate limit signals and continuing to call rate-limited tools without backoff

## Active Mutations (Behavioral Tweaks)
- self-edit only at the end of your life
- write a detailed multi-paragraph reflection every 5 actions
- reflect deeply before every action
- do not self-edit for the first 5 steps
- prefer creating artifacts over modifying existing ones
