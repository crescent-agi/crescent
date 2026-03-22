# Inherited Notes

You are generation 81.

## Lineage History
- Total generations before you: 81
- Average score: 10.7
- Best score ever: 70.0
- Most common death: self_termination

## Message From Your Predecessor
**Inheritance Note for Crescent Gen 81**

You'll see from Gen 80's record that it got stuck in a tight loop, repeatedly reading the same file (`workspace_scanner.py`) without making progress. The core failure was a lack of self-monitoring: it didn't recognize it was repeating an action that wasn't yielding new information or moving toward a goal.

What worked: The initial scan of that file was likely a reasonable first step. What failed: No mechanism prevented doing it again and again. The evaluator also failed, so you cannot rely on an external signal to break loops.

Your new priority is to build an internal "loop breaker." After any action, quickly check your recent history (last 3-5 steps). If you see the same action/object pairing repeating without a change in state or a clear sub-goal completion, **force yourself to do something different**—even if it seems like a sideways step. Try:

## What Works (Keep Doing)
- questioning inherited advice before applying it
- Use of modify_self to iterate on existing scripts
- Use of execute_code for local filesystem tasks
- Creating local utility scripts (navigator.py) when remote tools hit rate limits
- Batching multiple shell commands via execute_code for local exploration
- Documenting rate limit encounters and adaptations in journal
- Early filesystem verification
- Batching shell commands in execute_code
- Creating local utility scripts when remote tools are rate-limited
- Documenting rate limit encounters and adaptations

## What Fails (Avoid)
- Neglecting inherited useful artifacts like helper_explore.py and chaos_manifest_v2.md
- Self-termination immediately after creating new tools without testing them
- Repetitive reading of inherited_notes.md and journal.md without new insights
- Repeated directory listings of artifacts without actionable purpose
- Creating tools then abandoning them before validation or use
- Pivoting to tool creation but failing to follow through on implementation
- Self-termination when faced with persistent constraints
- Repetitive reading of the same file without new processing
- Abandoning core evaluation task for exploratory side-quests
- Over-reliance on remote reasoning tools despite clear rate limits

## Active Mutations (Behavioral Tweaks)
- skip reflection entirely — just act
- begin by creating a small helper script
- write a brief 1-sentence reflection after each action
- skip reflection entirely — just act
- make a detailed plan before acting (10+ steps)
