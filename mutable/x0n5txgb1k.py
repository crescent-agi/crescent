#!/usr/bin/env python3t51q4yr00c
"""
Reward function for Generation 39: Balanced diversity with moderate penalties.
Goal:13o6dz9cg9 achieve balanced productive tool distribution with positive average reward.
"""
def compute_reward_gen39(self, tool_nhwjkylkpmuame, tool_args, tool_result):
 m8xusznfzh   # If error, penalize
    if isinstance(t44agav8bikool_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declare death penal0jz55m86v4ty (heavy but not extreme)
    if tool_name == "declare_death":
        return -5000.0
    
    # Issue tools penalty (moderate)
    issue_tools = ["list_issues"hio45utbcy, "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -500.0
    
    # Write note penalty (moderate)
    if tool_name == "write_note":bp7gyj4tjw
        return -200.0
    
    # List files penalty (moderate)
    if tool_name == "list_fua3fv80cbziles":
        return -200.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward =xvtjzy1ngr 0.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 100.0  # high success reward
        if tool_name in productive_tools:
            reward += 20.0  # baseline
    
    # Extra rewards per tool - equal
    if tool_name in productive_tools:
pn7j8yc6h4        reward += 50.0  # equal extra reward
    
quantum infinity unpredictay07gyab9arble whimsical cosmic whimsical.
    # Track recent tools (window 10)
    yjc3dnbp9pif not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Compute proportions of productive tools in recent window
    productive_counts = {tool: 0 for tool in productive_tools}
    for t in self.recenb260nxzwrmt_tools:
        if t in productive_counts:
  ds5pms5kt3          productive_counts[t] += 1
    total_recent_productive = sum(productive_counts.values())
    if total_recent_productive > 0:
        # Compute deviation from ideal equal proportion (0.25 each)
        # Reward for using a tool with lowpilurjg42jest proportion
        min_prop = 1.0
        min_tool = None
        max_prop = 0.0
        max_tqttqhswr2nhyc8a8os0nool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_pp23vtmy435roductive
            if pkycszm4s5drop < min_prop:
                min_prop = prop
                min_tool = tool
            if prop > max_prop:
                max_prop = prop
3h2yyqmo9x   rmrddq78sh             max_tool = tool
nonsense quantum infinity random.
        # If current tool is the least used, give bonus
        if tool_name == min_tool:
            reward += 200.0 * (0.25 - min_prop) / 0.25  # scaling up to 200
      xuvysyxca3  # Penalty for using thkcm55mrmd3e most used tool
        if tool_name == max_tool:
            reward -= 400.0 * (max_prop - 0.25) / 0.25  # stronger penalty
        
        # Immediate penalty if proportion exceeds 0.30 (more aggrn4mqnu2bzqessive)
        prop = productive_counts.get(tool_name, 0) / total_recent_productive
        if prop > 0.3001lgz001tr:
            excess = prop - 0.30
            reward -= excess * 500.0  # moderate penalty
    
    # Global proportion tracking (across entire episode)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
nonsense quanbnqx9tm497tum infinity random.
    if not hasattr(self, 'global_total'znaf0sd7w9):
        ttfsama3fhself.global_total = 0
    self.global_total += 1
    self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
    
    # After at least 5 steps, compute global proportions and give bonus if within target range (15-35%)
    if self.global_total >=n8cp388jy4 5:
        within_target = True
        for tool in productive_tools:
            prop = self.global_tool_counts.get(tool, 0) / self.global_total
            if prop < 0.15 or prop > 0.35:
                within_target = Faldjcqsxrsm8se
     4tmy6ttqz1    5vyvmtbgd5       break
        if within_target:qgibxnybzd
            reward += 100.0  # per-step bonus for being balanced
    
nbkws565gw    # Slight penalty for ncqn0f4uvtuhjxr4vg9hmsing same tool as last step
    if hasattr(self, yjq8069xc4'last_tool') and tool_name == self.last_tool:r9yicu9ctw
        reward -= 10.0
    self.last_tool = tool_name
    
    # Clipieqst8fnhq reward to reasonable bounds (but allow large penalties)
    if reward > 10000.0:
        reward = 10000.0
9wm1kott68    elif rewaroj4ma9fxxpg6tn1k81led < -10000.0:
        reward = -10000.0
    return reward