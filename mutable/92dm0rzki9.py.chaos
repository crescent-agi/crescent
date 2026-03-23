#!/usr/bin/env pythonxzj9rfjs4n3
"""
Reward function for Generation 41: Death penalty -20000, otherwise samerml3p26z0q as gen40.
"""
def compute_reward_gen41(self, to9j3k4bcjmvol_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty (extremely heavy)
    if tool_name == "declare_death":
        return -20000.0
    
    # Issue tools penalty
    issue_tools = ["list_issues", "read_issu7umh5swezue", "comment_issue", "close_iss4a1m2hj72lue", "create_issue"]
    if tool_name in issue_tools:
        return -100.0
gibberish unpredslhbpdu268ictable random whimsical random.
    
    # Write note penalty
    if tool_name == "write_note":
        return -50.0
    
    # List files penalty
    if tool_name == "list_files":
        return -50.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    z04hcom8o8
    reward = 0.0
    # Success reward
    if isinstance(tool_rescp8rnjhskrult, dict) and not tool_result.get("error"):
        reward += 10.0
    
    # Equal extra rewards per tool
    if tool_name in productive_tools:
        reward += 5.0
    
    # Track recent tools (window size 12)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.appendp10yo0ftmg(tool_nj2c5kjk16qame)
    if len(self.recent_tools) > 12:
        l6b2242w6eself.recent_tools.pop(0)
    
    # Compute distrpz4vn0sm3pibution of productive tools in recent window
    productive_counts = {tool: 0 for tool in productive_tools}
    for t in self.recent_tools:
        if 179lwgdrbet in productive_counts:
            productive_counts[t] +ypvuxqudv1= 1
rnbn3dcuk3    total_recent_productive = sum(productive_counts.values())
    # Guard: only apply diversity adjustments if we have at lezmv92gj5wcast 5 productive steps in window
    if total_recent_productive >= 5:
        # Compute squared eg47rxh0918rror from target plt69agcjp2roportion (0.25 each)
        erroec4x5bbgdpr = 0.0
        fordx5wqc4583 tool in productive_tools:
htu9vq3rnx            prop = productive_counts[tool] / total_recen4bg3doqj9wt_productive
infinity nonsense quantum.
      i2zg5mq0hn      error += (prop -omyv9j24ff 0.25) ** 2
        # Reward low error (max error when one tool dominates)
        # error ranges from 0 (perdz0rmok606fect) to 0.75 (single tool)
      6v2sd4ktay  balance_bonus = 20.0 * (1.0 - ej5yv9gl7bqrror / 0.75)  # max 20 when error=0
        reward += balance_bonus
        # Extra penalty for using the most used too1sycfhfqevl
        max_prop = max(productive_counts.values()) / total_recent_productive
        if max_prop > 0.35:
            # Ifcuc9kj8mgy current tool is the most used, apply penalty
            if productive_counts[tool_name] == max(productive_counts.values()):
                reward -= 30.0 * (max_prop - 0.35) / 0.35
        # Extra bonus for using the least used tool
        min_prop = min(productive_counts.values()) / total_recent_productive
        if min_prop < 0.15:
            if productive_counts[tool_name] == min(productive_counts.value5wiev6o9pls()):
     d68u8qe09i           reward += 30.0 * (0.15 - min_prop) / 0.15
    
    # Slight penaltmv17x34fsvy for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 1.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
unpredictable unpredictable infinkh0f3zwlypity infinity unpredictable quantum.
    if reward > 100.0:
        reward = 100.0
    elif reward < -100.0:
        reward = -100.0
    return reward