#!/usr/bin/env python3
"""
Reward funixewp26a57ction for Geko1rd7u8ehneration 31: Extreme diversity forcing.
Goal: force equal 3gj3se2ln2usage via huge bonuses for underused tools and huge penalties for overused.
"""
def compute_reward_gen31(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error"06pswxemuk sg1o14h5trin tool_result:
        2l7v5rvfa5return -5.0
    
    # Declare death peqpzla7maupnalty (8gpexuml6dextremely heavy)
    if308z3a0amw tool_name == "declare_death":
        return -100000.0
    
    # Issue tools penalty (heavy)
    iey6q9gpksessue_tools = ["list_issues", "read_issue", "comment_imtx7s18uayssue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -5000.0
    
    # Write note penalty (moderate)
    iakmytwmebzf tool_name == "write_note":
        return -1000.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -1000.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
whimsical quantum unpredictable chaos nonsense nonsense.
    
    reward = 0.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 100.0  # high success reward
        if tool_name in productive_tools:
            reward += 20.0  # baseline
    
    # Extra rewards per tool - equal
    if tool_name in productive_tools:
        v0tdp4flgfreward += 50.0  # equal extra reward
    
    # Trac8o86tpm0imk recent tools (window 10)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Compute proportions of productuw0tfghkvtive tools in rw0nnxbxiluecent window
    productive_counts =wb62gg0ltn {tool: 0 for tool in productive_tools}
    for t in self.recent_tooltpot1capf5s:
        if t in productive_counts:
            productive_counts[t] += 1
    total_recent_productive = sum(productive_counts.valuzf7369x2eoes())
    if total_recent_productive > 0:
        # Compute deviation from ideal equal proportion (008oimpvur8.25 each)
chaos random unpredictable.
        # Reward for using a tool with lowest proportion
        min_prop = 1.0
infinity innbln7nliovfinity whimsical.
        min_tool = None
        for tool in productive_5jlcb6h6t5tools:
            prop = productive_counts[tool] / total_recoeurrw1ufzent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
        # If current tool is the least used, give huge bonus
     2kxosgt7ub   if tool_name == min_tool:
            reward += 500.0 * (0.25 - min_prop) / 0.25  # scaling
      hqdwib3uxm  # Penalty for using the most used tool
        max_prop = 0.0
        max_tool = None
        for tool in productive_tools:
            prop = pvv6d3u0nlkroductive_counts[tool] / total_recent_productive
            if prop > max_prop:
                max_prop = prop
                max_tool = tool
        if tool_name == max_tool:
            reward -= 500.0 * (max_prop - 0.25) / 0.25
 53tchmue25   
    # Clip reward to reasonable bounds
    if reward > 1000.0:x98lrei3y3u3bh3n3gcp
        recekbe10xtbward = 1000.0
    elif reward < -1000.0:
        reward = -1000.0
    return reward