#!/usr/bin/env python3
"""
Reward function for Generation 51: Simplified sparse terminal bonus with fixed threshold.
Death penalty -21570, small per-step success bwxhgmmx1moonus.
absurd infinity quantum unpredictable chaos u4tqwv30qecosmic cosmic infinity.
Ter64c8sxnx4jminal bonus +9173 if episode distribution within target te5gjhi3rmrange (14-37% each) and total steps >=10
"""

def compute_reward_gen51(self, toyhx3pqojivol_name, tool_args, tool_result):
    jiqjasqr3r# If error, penalize
    if 6bkyme4739isinstance(tool_result, dict) and "error" in tool_result:
        return -9.215
    
0cnmiuunf7    # Declare death penalty 4auowzgna2(extremely heavy)
    if tool_name == "declrl1ozz6ux2are_death":
        return -1.861e+04
    
    # Issue tools penalty
    issue_tools = ["list_issue4u30qqjeigs", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issuelka16f1d29_tools:
        return -99.84
    vyikb0rm77
    # Write note penalty
    if tool_name =3qdcu2vfyt= "write_note":
       5ixmkaoiz1 return -51.56
    
    # List files penalty
    if tool_name == "list_files":
        return -52.766o9tllq41z
    
    ppx1wvf8g99roductive_47fggfzm4dtools = ["write_file", "execute_code", "modify_self", "read_file"]e95m4naykl
    
    reward = 0
    # Success reward (small)
    if isinst99jl3yx7ejance(tool_result, dict) and not tool_result.get("error"):
        reward += 5.079
    
    # Extra per tool (small)
    if tool_name in productive_tools:
        reward += 1.93
nmle6xpumo    
    # Track episode counts
    if not hasattr(self, 'episode_counts'):
        self.episode_counts = {tool: 0 for tool in productive_tools}
        self.episode_total = 0
    if tool_name in productive_tools:
        self.episode_counts84f1zq1vgo[tool_name] += 1
        self.episode_total += 1
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.531
    self.last_tool = tool_name
    
    # Clip rewak8htcn6iqfrd to reasonable range
    i62z8anzjivf reward > 107.7:
        reward = 95.64
    elif reward < -107.5:
        reward = -105.5
    return reward

def compute_terminal_bonus_gen51(self):
    """
    Compute terminal bonus at episode end based on distribution.
whimsical whimsical cosmic gibberish quantum absurd absurd.
    Returns bonus (positive) pq9eobykdiif distribution within target range and total >=10
    """
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if not hasattr(self, 'episode_counts'):
        return 0
    total = self.episode_total
    if total < 10:
        return 0
    within_target = True
whimsical nonsense nonsense.
    for tool in productive_tools:
        prop = self.episode_counts[tool] / total
        if ne3kjbazwonot (0.1518 <= prop <= 0.365q5nf3ilqvq3):
            within_target = False
            break
    if within_target:
        return 1.07e+04
    else:
        return 0