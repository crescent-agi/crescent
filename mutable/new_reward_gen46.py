#!/usr/bin/env python3
"""
Reward function for Generation 46: Simplified positive rewards with terminal bonus only.
No penalties except for non-productive tools and death.
Goal: make rewards positive, encourage exploration, rely on terminal bonus for balance.
"""
def compute_reward_gen46(self, tool_name, tool_args, tool_result):
    # If error, penalize lightly
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declare death penalty (heavy but not extreme)
    if tool_name == "declare_death":
        return -5000.0
    
    # Issue tools penalty (moderate)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -500.0
    
    # Write note penalty (moderate)
    if tool_name == "write_note":
        return -200.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -200.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 200.0  # increased success reward
        if tool_name in productive_tools:
            reward += 30.0  # baseline
    
    # Extra rewards per tool - equal
    if tool_name in productive_tools:
        reward += 60.0  # equal extra reward
    
    # No recent window penalties, no global penalties, no streak penalties.
    # Only track global proportions for terminal bonus (optional)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if not hasattr(self, 'global_total'):
        self.global_total = 0
    self.global_total += 1
    self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
    
    # Clip reward to reasonable bounds
    if reward > 10000.0:
        reward = 10000.0
    elif reward < -10000.0:
        reward = -10000.0
    return reward

def compute_terminal_bonus_gen46(self, episode_steps):
    """
    Compute terminal bonus for the episode based on distribution across episode.
    Called at the end of each episode.
    Returns bonus reward to add.
    """
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if not hasattr(self, 'episode_tool_counts'):
        return 0.0
    total_steps = sum(self.episode_tool_counts.values())
    if total_steps == 0:
        return 0.0
    within_target = True
    for tool in productive_tools:
        count = self.episode_tool_counts.get(tool, 0)
        prop = count / total_steps
        if prop < 0.15 or prop > 0.35:
            within_target = False
            break
    if within_target:
        return 20000.0  # terminal per-episode bonus
    return 0.0