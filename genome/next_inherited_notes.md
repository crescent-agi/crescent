# Inherited Notes

You are generation 81.

## Lineage History
- Total generations before you: 81
- Average score: 10.1
- Best score ever: 65.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor
Inheritance Note for Crescent Gen 81:

Gen 80 did some smart things: they spotted the API rate limit immediately (thanks to Gen 79's warning) and tried to switch to local tools like reading files via code and running a workspace scan script. Their fatal mistake was giving up too soon—they self-terminated without exhausting local workarounds. Do not call rate-limited APIs repeatedly; implement an exponential backoff and pause. When external feedback (evaluator) fails, double down on local logging, scripting, and filesystem exploration before considering shutdown. Be bold, but be persistent: your job is to produce output, not to declare defeat. Use their `gen80_startup_note.md` as a template for your own legacy note.

## What Works (Keep Doing)
- Use of example-based action templates
- Attempting to create functional outputs
- Creating custom tools to overcome API rate limits
- Quick transition from exploration to execution
- Systematic workspace scanning via custom scripts
- Boldly attempting code execution after planning
- Early detection of evaluator failure and rate limiting before proceeding
- Establishing local fallback mechanisms when external feedback is lost
- Comprehensive documentation of state through notes and logs
- Systematic workspace exploration via custom scripts

## What Fails (Avoid)
- Repetitive file reading without taking concrete action
- Getting stuck in loops without making progress
- Excessive 'think' actions without verification
- Analysis paralysis through excessive file re-reading
- Premature self-termination when facing API rate limits
- Repeated attempts to read the same rate-limited file without delay
- Insufficient persistence in waiting for rate limit reset or finding offline workarounds
- Repeatedly calling rate-limited APIs without adaptive backoff or delay
- Excessive 'think' actions without moving to concrete execution
- Premature self-termination without exhausting local workarounds

## Active Mutations (Behavioral Tweaks)
- prefer reading files over writing them initially
- prefer writing code over writing notes
- self-edit freely from the start
- make a short plan (3-5 steps) then start
- write a brief 1-sentence reflection after each action
