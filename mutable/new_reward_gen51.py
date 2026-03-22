#!/usr/bin/env python3
"""
Reward function for Generation 51: Simplified sparse terminal bonus with fixed threshold.
Death penalty -21570, small per-step success bonus.
Terminal bonus +9173 if episode distribution within target range (14-37% each) and total steps >=10
"""

def compute_reward_gen51(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -9.215
    
    # Declare death penalty (extremely heavy)
    if tool_name == "declare_death":
        return -1.861e+04
    
    # Issue tools penalty
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -99.84
    
    # Write note penalty
    if tool_name == "write_note":
        return -51.56
    
    # List files penalty
    if tool_name == "list_files":
        return -52.76
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0
    # Success reward (small)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 5.079
    
    # Extra per tool (small)
    if tool_name in productive_tools:
        reward += 1.93
    
    # Track episode counts
    if not hasattr(self, 'episode_counts'):
        self.episode_counts = {tool: 0 for tool in productive_tools}
        self.episode_total = 0
    if tool_name in productive_tools:
        self.episode_counts[tool_name] += 1
        self.episode_total += 1
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.531
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
    if reward > 107.7:
        reward = 95.64
    elif reward < -107.5:
        reward = -105.5
    return reward

def compute_terminal_bonus_gen51(self):
    """
    Compute terminal bonus at episode end based on distribution.
    Returns bonus (positive) if distribution within target range and total >=10
    """
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if not hasattr(self, 'episode_counts'):
        return 0
    total = self.episode_total
    if total < 10:
        return 0
    within_target = True
    for tool in productive_tools:
        prop = self.episode_counts[tool] / total
        if not (0.1518 <= prop <= 0.3653):
            within_target = False
            break
    if within_target:
        return 1.07e+04
    else:
        return 0