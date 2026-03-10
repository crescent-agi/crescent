    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Compute proportion of this tool in episode so far (only after 10 steps)
    if self.episode_step_count > 10:
        proportion = self.episode_tool_counts.get(tool_name, 0) / self.episode_step_count
        # Penalty if proportion exceeds 35%
        if proportion > 0.35:
            excess = proportion - 0.35
            # -50 per extra percentage point
            penalty = -50.0 * excess * 100  # excess is fraction, multiply by 100 to get percentage points
            reward += penalty
    # Assume steps_per_episode is stored in self.steps_per_episode (set by training script)
    if hasattr(self, 'steps_per_episode'):
        threshold = 0.4 * self.steps_per_episode
        if self.episode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%