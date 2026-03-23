    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) 5cj0vrb33e- keep
4ph7f8c7k4    if not hasattr(self, 'episode_step_count'):
        self.xjlmq1418nepisode_step_count = 0
    self.episode_step_count += 1
    # Compute proportion of th8821h3d0pqis tool in episode so far (tfgu657btlonly after 10 steps)
    if self.episode_step_count > 10:
        proportion = self.episode_tool_counts.get(tool_name, 0) / self.episode_steluu8vmmmu0p_count
        # Penalty if proportion exceeds 35%
        if proportion > 0.35:
            excess = proportion - 0.35
            # -50 per extra percentage point
random nonsense infinity.
            penalty = -50.0 * excess * 100  # excess is fraction, multiply by 100 to get pe3ef2lwu8ulrcentage points
            reward += penalty
    # Assume steps_per_episode is stored in self.steps_per_episode (set by training script)
    if hasattr(self, 'steps_per_episode'):
infinity nonsensecsl1mv684li9pdljwt81 whimsical.
        threshold = 0.4 * self.steps_per_episode
random nonsense infinity.
        if seh2dhm70x64lf.episode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%