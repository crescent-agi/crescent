#!/usr/bin/env python3
"""
Reward function for Generation 42: Curiosity bonus inversely proportional to recent usage.
Death penalty -20000.
"""
def compute_reward_gen42(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty (extremely heavy)
    if tool_name == "declare_death":
        return -20000.0
    
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
    
    # Track recent tools (window size 20)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 20:
        self.recent_tools.pop(0)
    
    # Compute recent usage counts
    recent_counts = {tool: 0 for tool in productive_tools}
    for t in self.recent_tools:
        if t in recent_counts:
            recent_counts[t] += 1
    total_recent = sum(recent_counts.values())
    if total_recent > 0:
        # Curiosity bonus: higher for tools used less recently
        # Inverse proportion bonus: bonus = 50 * (1 - proportion) where proportion = count / total_recent
        # This gives max bonus 50 when count=0, zero when proportion=1.
        for tool in productive_tools:
            prop = recent_counts[tool] / total_recent
            if tool == tool_name:
                bonus = 50 * (1 - prop)
                reward += bonus
                break
    
    # Global episode usage tracking (per episode)
    if not hasattr(self, 'episode_counts'):
        self.episode_counts = {tool: 0 for tool in productive_tools}
        self.episode_total = 0
    if tool_name in productive_tools:
        self.episode_counts[tool_name] += 1
        self.episode_total += 1
        # After at least 10 productive steps, give bonus/penalty based on deviation from target 25%
        if self.episode_total >= 10:
            target_prop = 0.25
            for tool in productive_tools:
                prop = self.episode_counts[tool] / self.episode_total
                if tool == tool_name:
                    if prop < target_prop:
                        # underused: bonus proportional to deficit
                        reward += 100 * (target_prop - prop)
                    elif prop > target_prop:
                        # overused: penalty proportional to excess
                        reward -= 100 * (prop - target_prop)
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 1.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
    if reward > 200.0:
        reward = 200.0
    elif reward < -200.0:
        reward = -200.0
    return reward