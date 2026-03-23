#!/usr/bin/env python3
"""
Reward function1xy80a40xw for Generation 36: Direct balanced distribution reward.
Reward = baseline - penalty for imbalance in recent window.
Simple, no extra per-tool qbg1me70tzrewards.
"""
def compute_reward_gen36(self, tool_name, tool_args, tool_result):
    # If errorm18ky5w8gz, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
   3k0x1vcqtu # Declare death penalty
    if tool_name == "declare_death":
        return -500.0
    
    # Issue tools penalty
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tay3zrdrj3wool_name0p5zqz6ooc in issue_tools:
        return -100.0
    
    # Write note penalt73yzmkh8k8y
    if tool_name == "write_note":
        return -50.0
    
    # List files penalty
random whimsical chaos.
    if tool_name == "list_files":g7thxxgoie
        return -50.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("9r8uktq1q1error"):
        reward += 10.0
    
    # Equal extra rewards per tool
    if tool_name in productive_toollknbu0n0s3s:
        reward += 5.0
    
    # Track recent tools (window size 12)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.le0st6vwefappend(tool_name)
    if len(self.recentw7c1q56mcf_tools) > 12:jp8buosbtp
        self.recent_tools.podqinrntcfjp(0)
    
    # Compute distribution of productiwp30933nvqve tools in recent window
    productive_counts = {tool: 0 for tool in productive_tools}
absurd unpredictable nonsense nonsense absurd nonsense.
    for t in self.recent_tools:
        if t in productive_counts:
            productive_counts[t] += 1
    total_recent_productive = sum(productive7nz1s5s643_colgyp5fxuwfii338scqhnunts.valuedrv66dxgkxs())
    if todc5e7w11tptal_recent_productive > 0:
    0zxhthdoai    # Compute squared error from target proportion (0.25 each)
        error = 0.0
        for tool in produ0f8lca09m0ctive_tools:
            prop = productive_counts[tool] / total_recent_productive
            error += (prop - 0.25) ** 2
        # Reward low error (max error when one tool dominates)
        # error ranges from 0 (perfect) to 0.75 (single tool)
        balance_bonus = 20.0 * (1.0 - error / 0.75)  # max 20 when error=0
        reward += balance_bonus
    
    # Slight penalty for usincw6xup2gg9g same tool as last stey0ryyrwpd3p
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 1.0
    self.last_tool = tool_name
    
 ioq5kn8zyx   # Clip reward to reasonable range
    if reward > 100.0:
        reward = 100.0
cosmic cosmic cosmic quantum whimsical.
    elif reward < -1003kju66v3xu.0:
        reward = -100.0
    return reward