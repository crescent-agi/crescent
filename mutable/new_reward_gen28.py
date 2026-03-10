#!/usr/bin/env python3
"""
Reward function for Generation 28: No extra rewards, strong immediate penalties.
Goal: force balanced deterministic policy by removing differential rewards.
"""
def compute_reward_gen28(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty
    if tool_name == "declare_death":
        return -500.0
    
    # Issue tools penalty (extremely heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -10000.0
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
        return -2000.0
    
    # List files penalty (heavy)
    if tool_name == "list_files":
        return -2000.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 20.0
        if tool_name in productive_tools:
            reward += 5.0  # baseline
    
    # NO extra rewards per tool - all equal
    
    # Track episode usage
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # Immediate overuse penalty: quadratic penalty for using same tool multiple times in episode
    if tool_name in productive_tools:
        count = self.episode_tool_counts[tool_name]
        # Penalty starts after first use, increases quadratically with strong scaling
        if count > 1:
            penalty = (count - 1) ** 2 * 50.0  # very strong scaling
            reward -= penalty
    
    # Global proportion penalty (heavy) - only after enough global steps
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    total_global_before = sum(self.global_tool_counts.values())
    prev_count = self.global_tool_counts.get(tool_name, 0)
    self.global_tool_counts[tool_name] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
        # Apply overuse penalty only if total_global_before >= 5
        if total_global_before >= 5:
            if total_global_before > 0:
                proportion_before = prev_count / total_global_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
                    penalty = excess * 10000.0  # extremely heavy
                    reward -= penalty
    
        # Global deficit bonus (based on proportion before increment)
        if total_global_before > 0:
            proportion_before = prev_count / total_global_before
            target = 0.25
            if proportion_before < target:
                deficit = target - proportion_before
                bonus = deficit * 500.0  # strong bonus
                if bonus > 500.0:
                    bonus = 500.0
                reward += bonus
    
    # Recency penalty (small)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 2.0
    self.last_tool = tool_name
    
    # Diversity bonus for using a tool not used recently
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    if same_count == 0 and tool_name in productive_tools:
        reward += 20.0  # strong bonus
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Clip reward to reasonable bounds
    if reward > 500.0:
        reward = 500.0
    elif reward < -500.0:
        reward = -500.0
    return reward