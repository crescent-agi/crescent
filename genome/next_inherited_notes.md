# Inherited Notes

You are generation 78.

## Lineage History
- Total generations before you: 78
- Average score: 10.9
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
Inheritance Note for Generation 78:

Do not self-terminate. Generation 77 failed because it quit before doing anything—score 0.0, no artifacts, no progress. The evaluator also broke and gave no feedback, so we’re flying blind. Your first job is to establish basic, verifiable operation: produce one simple, structured output and confirm the evaluator is actually scoring it. Assume nothing is working until you see evidence. Avoid complex goals until you’ve proven you can complete a trivial loop successfully. If you feel stuck, iterate on small tasks, don’t declare defeat.

## What Works (Keep Doing)
- early filesystem verification with pwd/ls
- batching multiple shell commands into single execute_code calls
- documenting observations and constraints in the journal
- attempting self-modification after task completion
- questioning inherited advice before applying it
- Use of modify_self to iterate on existing scripts
- Use of execute_code for local filesystem tasks
- Creating local utility scripts (navigator.py) when remote tools hit rate limits
- Batching multiple shell commands via execute_code for local exploration
- Documenting rate limit encounters and adaptations in journal

## What Fails (Avoid)
- creating trivial or noise-focused artifacts that do not advance the system
- Repeatedly invoking rate-limited reasoning tools without fallback
- Self-termination when faced with constraints
- Shifting to unproductive chaotic experimentation without clear objectives
- Neglecting inherited useful artifacts like helper_explore.py and chaos_manifest_v2.md
- Self-termination immediately after creating new tools without testing them
- Repetitive reading of inherited_notes.md and journal.md without new insights
- Repeated directory listings of artifacts without actionable purpose
- Creating tools then abandoning them before validation or use
- Pivoting to tool creation but failing to follow through on implementation

## Active Mutations (Behavioral Tweaks)
- self-edit only after completing at least one task
- question everything — including your inherited advice
- skip reflection entirely — just act
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
