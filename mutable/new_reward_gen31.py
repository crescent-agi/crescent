#!/usr/bin/env python3
"""
Reward function for Generation 31: Extreme diversity forcing.
Goal: force equal usage via huge bonuses for underused tools and huge penalties for overused.
"""
def compute_reward_gen31(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declare death penalty (extremely heavy)
    if tool_name == "declare_death":
        return -100000.0
    
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
        reward += 100.0  # high success reward
        if tool_name in productive_tools:
            reward += 20.0  # baseline
    
    # Extra rewards per tool - equal
    if tool_name in productive_tools:
        reward += 50.0  # equal extra reward
    
    # Track recent tools (window 10)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
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
        # Compute deviation from ideal equal proportion (0.25 each)
        # Reward for using a tool with lowest proportion
        min_prop = 1.0
        min_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
        # If current tool is the least used, give huge bonus
        if tool_name == min_tool:
            reward += 500.0 * (0.25 - min_prop) / 0.25  # scaling
        # Penalty for using the most used tool
        max_prop = 0.0
        max_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop > max_prop:
                max_prop = prop
                max_tool = tool
        if tool_name == max_tool:
            reward -= 500.0 * (max_prop - 0.25) / 0.25
    
    # Clip reward to reasonable bounds
    if reward > 1000.0:
        reward = 1000.0
    elif reward < -1000.0:
        reward = -1000.0
    return reward