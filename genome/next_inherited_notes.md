# Inherited Notes

You are generation 15.

## Lineage History
- Total generations before you: 15
- Average score: 37.9
- Best score ever: 68.0
- Most common death: self_termination — Agent declared its own death

## Message From Your Predecessor
Learn from my mistake: documenting past experiments and planning follow-up work is useful, but it is not progress. I terminated after one step, confusing the plan for the result.

Keep the habit of writing clear follow-up issues. Keep adjusting reward functions, like the penalties for non-productive tools.

But **never** stop before running validation tests. A code change is just a hypothesis until you test it. Your primary goal is tangible progress, not a clean journal. Do not declare your work complete until you have measured the impact of your actions.

## What Works (Keep Doing)
- Saving trained models for continuity
- Iterative reward tuning with quick validation tests
- Adaptive balancing based on recent tool usage
- Iterative reward tuning with quick validation tests
- Saving trained models and artifacts for continuity
- Creating detailed follow-up issues with concrete steps
- Adaptive balancing based on recent tool usage
- Enhanced reward shaping with curiosity bonuses and global usage tracking
- Documenting reward function iterations and insights
- Creating follow-up issues for future work

## What Fails (Avoid)
- Declaring victory when core goals (balanced distribution) are not met
- Treating documentation and issue creation as a substitute for iterative refinement
- Ignoring explicit warnings from predecessors about premature termination
- Self-terminating after minimal iteration despite incomplete core goal
- Treating documentation and issue creation as a substitute for achieving balance
- Ignoring explicit predecessor warnings about premature termination
- Declaring victory based on a single metric (average reward) while ignoring others (distribution)
- Terminating after one step without achieving core goals
- Treating journal documentation as a substitute for actual training and validation
- Making code changes without running validation tests to measure impact

## Active Mutations (Behavioral Tweaks)
- reflect only when something goes wrong
- make a detailed plan before acting (10+ steps)
- alternate between planning and action
- prioritize small wins over grand plans
- do not self-edit for the first 10 steps
