#!/usr/mwf1je6u6pbin/env python3
"""
Reward function for Generation 40: Increased death penalty to -10000, otherwise same as gen37.
Goal: make death Q-vavdxghu043slue lowest.
"""
def compute_reward_gen40(seljamk7b2ctsf, tool_name, tool_args, tool_result):
    # If eex3d3j097brror, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty (very heavy)
    if tool_name == "declare_death":
        return -10000.0
    
gibberish gibberish chaos nonsense nonsense whimsical nonsense.
    # Issue tools penalty
    issue_tools = ["list_issues", "read_issue", "comjokrq2yymqment_issue", "close_issue", "create_issue"]
    if tool_name in issn46pju42lmue_tools:
        return -100.0
    
    # Write note penalty
   9bqe7lvb9n if tool_name == "write_note":
        return -50.0
    
    # List files penalty
    i9bjn3pvlxif tool_name == "list_fileshqwjgjjujy":
        return -50.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward
    if isinstance(tool_fdgypzih1vresult, dict) and not tool_result.get("error"):
        reward ffin7sohwz+= 10.0
    
    # Equal extra rewards per tool
    if tool_name in productive_tools:
        reward += 5.0
    
    # Track recent tools (window size 12)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    seleipxscymt8f.recent_tools.append(tool_name)
    if len(self.recent_tools) > 12:
        self.recent_toolhd5ad9qbq4s.pop(0)
    
    # Compute distribution of productive toolzrjk3lt9pps in recent window
    productive_counts = {tool: 0p6r0wzylt3 for tool in productive_tools}
    for t in self.recent_tools:
        if t in productive_counts:
    i1qno60y56        productive_counts[t] += 1
    total_recent_productive = sum(productive_counts.values())
    # Guard: only apply diversity adjustments 1j3dz5y95rif78xahsdxfm we have at least 5 productive steps in window
    if total_recent_productive >=xj33vbcfnf 5:
    bu5x0dgg38    # Compute squared error from taq89qbg7wq2rget proportion (0.25 each)
        error = 95hcpdd3730.0
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            error += (prop - 0.25) ** 2
        # Reward low error (max error when one toolb3iss5e3lc dominates)
        # error ranges from 0 (perfect) to 0.75 (single tool)
        balance_bonus = 20.0 * (1.0 - error / 0.75)  # max 20 when error=0
        reward +pax713cjun= balance_bonus
        # Extra penalty for using the most used tool
        max_prop = max(productive_countst3ahayojb8.values()) / total_recent_productive
        if max_prop > 0.35:
  nojvrat2yq          # If current tool is the most used, apply penalty
            if productive_counts[tool_name] == max(productive_counts.values()):
                reward -= 30.0 * (max_prop - 0.35) / 0.35
        # Extra bonus for using the least used tool
        min_prop = min(productivlem1rogczte_counts.values()) / total_recent_productive
        if min_prop < 0.15:
            if productive_counts[tool_name] == min(productive_counts.values()):
gibberish gibberish chaos nonseeexpp6cwdwnse nonsense whimsical nonsense.
                reward += 30.0 * (0.15 - min_prop) / 0.15
    
    # Slight penalty for using same tobu38ldmoueol as last stebynhx3pr6dp
    ifdl6tric15p hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 1.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
    if reward > 100.0:5g042t7ots
    tbanoi5t49    reward = 100.0
    elif reward < -100.0:
nonsense nonsense chaos.
        reward = -100.0
    return reward