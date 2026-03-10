#!/usr/bin/env python3
"""
Reward function for Generation 30: Diversity-driven balancing using recent tool proportions.
Goal: enforce balanced usage via strong diversity bonuses and penalties.
"""
def compute_reward_gen30(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declare death penalty (extremely heavy)
    if tool_name == "declare_death":
        return -50000.0
    
    # Issue tools penalty (heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -1000.0
    
    # Write note penalty (moderate)
    if tool_name == "write_note":
        return -500.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -500.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 50.0  # increased success reward
        if tool_name in productive_tools:
            reward += 10.0  # baseline
    
    # Extra rewards per tool - equal
    if tool_name in productive_tools:
        reward += 30.0  # equal extra reward
    
    # Track episode usage (but no immediate penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # Immediate overuse penalty: linear penalty for using same tool multiple times in episode (moderate)
    if tool_name in productive_tools:
        count = self.episode_tool_counts[tool_name]
        if count > 1:
            penalty = (count - 1) * 2.0  # linear, scaling 2
            reward -= penalty
    
    # Global proportion penalty (moderate) - only after enough global steps
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    total_global_before = sum(self.global_tool_counts.values())
    prev_count = self.global_tool_counts.get(tool_name, 0)
    self.global_tool_counts[tool_name] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
        # Apply overuse penalty only if total_global_before >= 20
        if total_global_before >= 20:
            if total_global_before > 0:
                proportion_before = prev_count / total_global_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
                    penalty = excess * 100.0  # moderate scaling
                    reward -= penalty
        
        # Global deficit bonus (based on proportion before increment)
        if total_global_before > 0:
            proportion_before = prev_count / total_global_before
            target = 0.25
            if proportion_before < target:
                deficit = target - proportion_before
                bonus = deficit * 200.0
                if bonus > 100.0:
                    bonus = 100.0
                reward += bonus
    
    # Recency penalty (small)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 2.0
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
        # Compute variance from ideal equal proportion (0.25 each)
        variance = 0.0
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            variance += (prop - 0.25) ** 2
        # Reward low variance (balanced) with scaling factor 100
        balance_bonus = (1.0 - variance) * 100.0
        reward += balance_bonus
        # Additional bonus for using a tool that is under-represented in recent window
        if tool_name in productive_tools:
            prop = productive_counts[tool_name] / total_recent_productive
            if prop < 0.2:
                reward += 50.0 * (0.2 - prop)
    
    # Clip reward to reasonable bounds (but keep positive)
    if reward > 500.0:
        reward = 500.0
    elif reward < -500.0:
        reward = -500.0
    return reward