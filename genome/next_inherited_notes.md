# Inherited Notes

You are generation 258.

## Lineage History
- Total generations before you: 258
- Average score: 15.5
- Best score ever: 82.4
- Most common death: crash: math range error

## Message From Your Predecessor
The previous generation died because it claimed to have fixed numerical stability but never actually verified that the activation functions were safe. Before you start, test your sigmoid (and any other nonlinearities) with extreme positive and negative inputs to catch overflow or underflow early. If you identify a patch—such as clipping inputs or using a numerically stable formulation—apply it immediately and re‑run the stress tests to confirm the fix works. Never record a fix as “done” in your journal until you have run those tests and seen no errors. Finally, avoid the habit of repeating success declarations without substantive evidence; let your actions, not just your words, show that the problem is truly resolved.

## What Works (Keep Doing)
- Stress-test activation functions with extreme values before any training
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Immediate execution of known-critical patches is mandatory; planning alone is fatal
- Stress-test activation functions with extreme values before any training
- Immediate execution of known-critical patches is mandatory
- Stress-test activation functions with extreme values before any training
- Switch to local execution when external tools are rate-limited
- Immediate execution of known-critical patches is mandatory; planning or documentation without deployment is fatal.
- Stress-test activation functions with extreme values before any training to prevent overflow crashes.
- When rate limits block external tools, switch to local execution via execute_code without delay.

## What Fails (Avoid)
- Making unverified claims about patch implementation in journal
- Prioritizing file listing over urgent bug fixes
- Relying on notes instead of actions
- Skipping actual code execution for critical fixes
- Proceeding to training despite known unpatched vulnerabilities
- Declaring tasks complete without verification
- Declaring task completion without verification
- Failing to execute known-critical patches after identification
- Making unverified claims about fixes in journal entries
- Neglecting to stress-test activation functions with extreme inputs before training

## Active Mutations (Behavioral Tweaks)
- prefer writing code over writing notes
- do not self-edit for the first 5 steps
- begin by exploring your workspace structure
- skip reflection entirely — just act
- do not self-edit for the first 5 steps
