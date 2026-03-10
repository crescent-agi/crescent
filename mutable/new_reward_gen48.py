#!/usr/bin/env python3
"""
Reward function for Generation 48: Increased least-used bonus (10000), increased most-used penalty (500),
added global deficit bonus for tools below 15% proportion, larger terminal bonus (20000).
Goal: achieve balanced productive tool distribution with positive average reward.
"""
def compute_reward_gen48(self, tool_name, tool_args, tool_result):
    # If error, penalize
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
        max_prop = 0.0
        max_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
            if prop > max_prop:
                max_prop = prop
                max_tool = tool
        # If current tool is the least used, give bonus (scaling 10000)
        if tool_name == min_tool:
            reward += 10000.0 * (0.25 - min_prop) / 0.25  # scaling up to 10000 (least-used bonus)
        # Penalty for using the most used tool (increased to 500)
        if tool_name == max_tool:
            reward -= 500.0 * (max_prop - 0.25) / 0.25  # most-used penalty 500
        
        # Immediate penalty if proportion exceeds 0.30 (more aggressive)
        prop = productive_counts.get(tool_name, 0) / total_recent_productive
        if prop > 0.30:
            excess = prop - 0.30
            reward -= excess * 100.0  # immediate penalty scaling 100
    
    # Global proportion tracking (across entire episode)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if not hasattr(self, 'global_total'):
        self.global_total = 0
    self.global_total += 1
    self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
    
    # After at least 5 steps, compute global proportions and give bonus if within target range (15-35%)
    if self.global_total >= 5:
        within_target = True
        for tool in productive_tools:
            prop = self.global_tool_counts.get(tool, 0) / self.global_total
            if prop < 0.15 or prop > 0.35:
                within_target = False
                break
        if within_target:
            reward += 1000.0  # global balance bonus 1000
        # Global deficit bonus: if tool proportion below 0.15, give bonus proportional to deficit
        for tool in productive_tools:
            prop = self.global_tool_counts.get(tool, 0) / self.global_total
            if prop < 0.15:
                deficit = 0.15 - prop
                # bonus only if current tool is the deficient tool
                if tool_name == tool:
                    reward += deficit * 2000.0  # scaling 2000
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 10.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable bounds (but allow large penalties)
    if reward > 10000.0:
        reward = 10000.0
    elif reward < -10000.0:
        reward = -10000.0
    return reward

def compute_terminal_bonus_gen48(self, episode_steps):
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
        return 20000.0  # terminal per-episode bonus increased to 20000
    return 0.0