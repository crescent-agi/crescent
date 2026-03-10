#!/usr/bin/env python3
"""
Reward function for Generation 34: Equal extra rewards, strong penalties for overuse,
global proportion penalty applied early, no clipping, strong diversity bonus.
Goal: achieve balanced deterministic policy.
"""
def compute_reward_gen34(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty (heavy)
    if tool_name == "declare_death":
        return -50000.0
    
    # Issue tools penalty (heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -5000.0
    
    # Write note penalty (moderate)
    if tool_name == "write_note":
        return -1000.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -1000.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 100.0  # success reward
        if tool_name in productive_tools:
            reward += 50.0  # baseline productive
    
    # Equal extra rewards per tool
    if tool_name in productive_tools:
        reward += 30.0  # equal extra reward
    
    # Track episode usage (for immediate overuse penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # Immediate overuse penalty: quadratic penalty for using same tool multiple times in episode
    if tool_name in productive_tools:
        count = self.episode_tool_counts[tool_name]
        if count > 1:
            penalty = (count - 1) ** 2 * 20.0  # stronger scaling
            reward -= penalty
    
    # Global proportion penalty (strong) - apply after at least 5 global steps
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    total_global_before = sum(self.global_tool_counts.values())
    prev_count = self.global_tool_counts.get(tool_name, 0)
    self.global_tool_counts[tool_name] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
        # Apply overuse penalty only if total_global_before >= 5 (earlier)
        if total_global_before >= 5:
            if total_global_before > 0:
                proportion_before = prev_count / total_global_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
                    penalty = excess * 15000.0  # extremely strong scaling
                    reward -= penalty
        
        # Global deficit bonus (based on proportion before increment)
        if total_global_before > 0:
            proportion_before = prev_count / total_global_before
            target = 0.25
            if proportion_before < target:
                deficit = target - proportion_before
                bonus = deficit * 1000.0
                if bonus > 500.0:
                    bonus = 500.0
                reward += bonus
    
    # Recency penalty (small)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 5.0
    self.last_tool = tool_name
    
    # Diversity bonus based on recent tool proportions (strong)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    # Add current tool
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    # Compute proportions of productive tools in recent window
    productive_counts = {tool: 0 for tool in productive_tools}
    for t in self.recent_tools:
        if t in productive_counts:
            productive_counts[t] += 1
    total_recent_productive = sum(productive_counts.values())
    if total_recent_productive > 0:
        # Compute which tool is least used and most used
        min_prop = 1.0
        max_prop = 0.0
        min_tool = None
        max_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
            if prop > max_prop:
                max_prop = prop
                max_tool = tool
        # Bonus for using the least used tool
        if tool_name == min_tool:
            bonus = (0.25 - min_prop) * 800.0
            reward += bonus
        # Penalty for using the most used tool
        if tool_name == max_tool:
            penalty = (max_prop - 0.25) * 800.0
            reward -= penalty
        # Additional penalty if proportion exceeds 0.35 (immediate)
        prop = productive_counts.get(tool_name, 0) / total_recent_productive
        if prop > 0.35:
            excess = prop - 0.35
            reward -= excess * 2000.0
    
    # No clipping; let Q-learning handle large values (but limit extreme)
    if reward > 10000.0:
        reward = 10000.0
    elif reward < -10000.0:
        reward = -10000.0
    return reward