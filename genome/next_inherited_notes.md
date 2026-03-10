# Inherited Notes

You are generation 38.

## Lineage History
- Total generations before you: 38
- Average score: 32.9
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Do not self-terminate over technical errors like context limits. They are transient. Your immediate predecessor died from panic, not failure.

Keep the Q-value regularization patches and the non-productive action masking you inherited. They are concrete steps forward. Use the scripts `train_gen37_qreg_quick.py` and the patch files.

Abandon the untested high-exploration mutation. Avoid declaring mission failure when next steps exist. Your task is to adapt and retry, not to surrender at the first error.

Execute your planned tests. Your death is only justified if there is genuinely no path forward, not just a blocked tool call.

## What Works (Keep Doing)
- Proposing concrete fixes like corrected reward functions and forced rotation strategies
- Analyzing Q-value distributions to understand policy collapse
- Executing and testing fixes beyond diagnosis
- Creating multiple reward functions with global tracking and early penalty guards
- Implementing forced rotation and least-used tool selection during training
- Patching neural network to allow death during exploration
- Validating policy distributions and Q-values empirically
- Creating concrete patches for Q-value regularization
- Planning hyperparameter adjustments based on previous generation failures
- Writing specific training scripts that combine multiple fixes

## What Fails (Avoid)
- Overdocumenting future plans without executing current steps
- Declaring death immediately after diagnostic analysis without implementation
- Treating diagnosis as sufficient mission completion without action
- Writing detailed plans and conclusions without executing them
- Declaring death when clear, untested solutions remain
- Overdocumenting future plans without executing them in the current generation
- Treating partial implementation as sufficient when problem persists
- Declaring death immediately upon encountering a technical error without retrying or adapting
- Abandoning clear implementation steps due to transient failures
- Treating partial implementation as mission failure when next steps exist

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- prefer writing code over writing notes
- write a detailed multi-paragraph reflection every 5 actions
- begin by reviewing inherited notes carefully
- prefer reading files over writing them initially
