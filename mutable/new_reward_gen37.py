#!/usr/bin/env python3
"""
Reward function for Generation 37: Strong balanced distribution reward with entropy bonus.
Goal: force balanced usage via large bonuses for underused tools and large penalties for overused.
"""
def compute_reward_gen37(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty
    if tool_name == "declare_death":
        return -500.0
    
    # Issue tools penalty
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -100.0
    
    # Write note penalty
    if tool_name == "write_note":
        return -50.0
    
    # List files penalty
    if tool_name == "list_files":
        return -50.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 10.0
    
    # Equal extra rewards per tool
    if tool_name in productive_tools:
        reward += 5.0
    
    # Track recent tools (window size 12)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 12:
        self.recent_tools.pop(0)
    
    # Compute distribution of productive tools in recent window
    productive_counts = {tool: 0 for tool in productive_tools}
    for t in self.recent_tools:
        if t in productive_counts:
            productive_counts[t] += 1
    total_recent_productive = sum(productive_counts.values())
    if total_recent_productive > 0:
        # Compute squared error from target proportion (0.25 each)
        error = 0.0
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            error += (prop - 0.25) ** 2
        # Reward low error (max error when one tool dominates)
        # error ranges from 0 (perfect) to 0.75 (single tool)
        balance_bonus = 200.0 * (1.0 - error / 0.75)  # max 200 when error=0
        reward += balance_bonus
        
        # Additional bonus for using a tool that is under-represented in recent window
        # Find tool with lowest proportion
        min_prop = 1.0
        min_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
        if tool_name == min_tool:
            # give extra bonus proportional to deficit
            deficit = 0.25 - min_prop
            reward += 100.0 * deficit / 0.25  # up to 100
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 5.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
    if reward > 500.0:
        reward = 500.0
    elif reward < -500.0:
        reward = -500.0
    return reward