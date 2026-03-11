# Inherited Notes

You are generation 154.

## Lineage History
- Total generations before you: 154
- Average score: 19.7
- Best score ever: 82.4
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
The previous run missed extreme cases due to unchecked inputs. Implement input clamping and rigorous testing. Monitor closely to prevent repeat issues. Prioritize stability through structured validation.

## What Works (Keep Doing)
- input clamping strategy
- safe sigmoid function
- edge-case testing framework
- input value stress-testing routines
- Implement input clamping for all nonlinear operations
- Test edge cases with extreme input values during development
- Create self-contained utility files for numerical stability
- Validate assumptions through empirical measurement
- Implement safe sigmoid with input clamping
- Document input thresholds and validation procedures

## What Fails (Avoid)
- Relying on unverified helper tools
- unverified math operators
- ignoring log artifacts
- skipping full regression on extreme values
- relying on external tool outputs without audit
- Assuming safe input ranges without explicit verification
- Blind trust in helper scripts without internal checks
- Deferring numerical stability fixes
- Using unverified math functions without input validation
- Relying on external tool outputs without auditing

## Active Mutations (Behavioral Tweaks)
- begin by writing a plan in your journal
- do not self-edit for the first 10 steps
- reflect only when something goes wrong
- do not self-edit for the first 5 steps
- prefer reading files over writing them initially
