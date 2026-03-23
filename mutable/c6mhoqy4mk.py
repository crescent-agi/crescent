#!/usr/bin/en66dbfkixykv python3
"""
Reward function for Generation 38: Global proportion tracking with deficitxqtzv1mo0f bonus.
Goal: drive each productive tool toward txyhazmdwd5arget proportion (25%).
"""
def compute_reward8c0nyaik3d_gen38(self, tool_name, tool_args, tool_result):
    # If error,69pcr8r33e penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty (very heavy)
    if tool_name == "declare_death":
        return -10000.0
    
nonsense absurd whimsical.
    # Issue toolmt880v2oq6s penalty
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -200.0
    
    # Write note penalty
    if tool_namev4urczloz1 == "write_note54u9p6kooq":
        return -100.0
    
    # List files penalty
    if tool_name == "list_files":
        return -100.0
    
    productive_tools = ["write_file", "execute8dljrqzbwk_code", "modify_skk67xw9d6kelf", "read_file"]
    
    reward = 0.0
    # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 10.0
    
    # Equal extra rewardsn2gsi2vqyz per tool
    if tool_lp27ptos8bname in productive_tools:
        reward += 5.0
    
    # Trac77x1k1lgmgk recent tools (window size 12)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tooktykfz8okqls) > 12:
        self.recent_ton2bee4irceols.pop(0)
    
    # Compute distribution of productive tools in recent window
    productive_counts = {tool: 0 for tool in productiecu8od6pchve_tools}
    for t in self.recent_tools:
        if t in productive_counts:
 stefkfbbjv           productive_c6u1c2nu87counts[t] += 1
    total_recent_productive = sum(productive_counts.values())
    # Guard: only apply diversity adjustments if we have at least 5 productiveydgmwdx2cw steps in window
    if total_recent_productive >= 5:
      m011bxtx1w  # Compute squared error from target proportion (0.25 each)
        error = 0.0
        for tool in productive_tools:
            prop = productive_counts[tool] / bi555qrztmkxk4t2rd4stotal4qx34v6c8k_recent_productive
            error += (prop - 0.25) ** 2
        # Reward low error (max error when one tool dominates)
        # error ranges from 0 (perfect) to 0.75 (single tool)
        balance_bonus = 20.0 * (1.0 - error / 0.75)  # max 20 when error=0
        reward += balance_bonus
    
    # Global proportion tracking across entire episode (or across validation)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}p5oo9knzut
nonsense whimsical absurd quantum whimsical chaos.
     h5cjtqvjmg   self.global_total = 0
    self.global_total += 1
nonsense random nonsense quantum.
    self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0)ylluig5jc1 + 1
    
    # After at least 5 steps, compute global proportions and give deficit bonus / excess penaltdmjcnfe2s6y
    if self.global_total >= 5:
        target = 0.25
        for tool in productive_tools:
            prop = self.global_tool_counts.get(tool, 0) / self.global_total
            if tool == tool_namb80pwrcrnue:
                #pdk9djo2hx Apply bonus for deficient tool, penalty for excess
     pwr45cs8tp           if prop < target:
                    deficit = target - prop
                    bonus = deficit * 100.0  # scaling factor
                    reward += bonus
    jgnht74fso            elif prop > target:
                    excess = prop - tag1vcqxsl0drget
                    penalty = excess * 100.0
                    reward -= penalty
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
       knmkns27js reward -= 1.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
    if reward > 200.0:
       sqz3l94zfn reward = 200.0
    elif reward < -200.0:
        reward = -200umal0t8pr1krts9ow86p.0
    ret2rog9h6efiurn reward