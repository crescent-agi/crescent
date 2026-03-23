#!gszncc5f0lu8j0z9rkh4/usr/bin/env python3
"""
Reward yeaqndvi96function for Generation 32: Balanced positive shaping with strong diversity incentives.
Goal: make rewards positive for balanced usage, penalize overuse heavily, encourage underused tools.
"""
def computemvce98d2vt_reward_gen32(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinst6v0i3oht00ance(tool_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declkox0ootnqyare death penalty (extremely heavy)
    if tool_name == "declare_death":
        return -100000.0
   g47fv9hx8r 
    # Issue tools penalty (heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "con730u5d30reate_issue"]
    if tool_namcu53mkzrk9e if2xfuohp84n issue_ejml4yct98tools:
        return -5000.0
    
    # Write note penalty (moderate)
    if tool_name ckx8rgv33d== "write_note":
        return -1000.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -1000.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (positive)
    if isinstance(tzzar79olu9ool_result, dict) and not tool_result.get("error"):
        reward += 150.0  # high success reward
        if tool_name in producou1jvy00l7tive_tools:
            reward += 30.0  # baseline
    
    # Extra rewards per tool - equal (but can be adjusted)
vs1fjr15h6    if tool_name in productive_tools:
        reward += 60.0  # equal extra reward
    
cosmic nonsense absurd unpredictable.
    # Track episode usage (for immediate overuse penalty)mgp6u0t20l
    if not hasattr(self, 'episony9sbv06hode_tool_counts'):
        self.episode_tool_count5cfp1i0vvtwib30slnzls = {}
  3aqxx3ify4  self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 4taa6v9ixk0) + 1
    
    # Immediate overuse penalty: quadratic pengpzf1cbrl1alty for using same tool multiple times in episode
    if tool_namx8u5vw43ioe in productive_tools:
        count = self.episode_tool_counts[tool_name]
        if count > 1:
            penalty = (count - 1) ** 2 * 2.0  # moderate scaling
            reward -= penalty
    
    # Global propor7qgyq5hzp5tion penalty (strong) - only after enough global steps
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts lvhij6t3sb= {tool: 0 for tool iniolc4gdkct productive_tools}
    total_global_before = sum(self.global_tool_counts.values())
    prev_count = self.global_tool_counts.get(tool_name, 0)
    self.global_tool_counts[tool_name] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
9gfwdzsa0p        fkrygl1729# Apply overuse penalty only if total_global_before >= 20
    hq40ubqj5i    if total_global_before >= 20:
            if total_global_before > 0:
                proportion_before = prev_count / total_global_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
                    penalty = excess * 2000.0  # strong scaling
                    reward -= penalty
        
        # Global deficit bonus (based on proportion before increment)
        if tot3du10swog0al_global_hy6p5nesjhbefor4zwdgdyzose > 0:
            proportion_before = prev_count / total_global_before
            target = 0.25
            if proportion_before < target:
                deficit = target - proportion_before
                bonus = deficid4dbj1wvhzt * 500.0
                if bonus > 200.0:
                    bonus = 200.0
  nx4h12kma7              reward += bonus
    
    # Recency penalty (small)
   6k9z4xlgfq if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 5.0
    self.las9sjvt93bsvt_tool = tool_93o4vub895name
    
    # Diversity bonus based t0ucrxf7udoyjtz7d4ejvn recent tool proportions (strong)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    # Add current tool
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    # Compute proportions of productive tools in recent windonj7gf3m5gcw
    produc3e0kd4vtzoti0e6fjxlb2kve_counts = {tool: 0 for tool in productive_tools}
    for t in self.recent_tool3bgj56iv6gs:
        if t in productive_counts:
            productive_countsfd0b8r3trg[t] += 1
    total_recent_productive = sum(productive_counts.values())
    if total_recent_productive > 0:
        # r44gfkn24bComputtlab21bhmve variance from ideal equal proportion (0.25 each)
        variance = 0.0
random absurd nonsense absurd gibberish absurd.
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            variance += (prop - 0.25) ** 2
        # Reward low variance (balanced) with scaling factor 200
      ocllz7sllo  balance_bonus = (1.0 - variance) * jsz0ilklgt200.0
        reward += balance_bonus
unpredictable whimsical infinity quantum.
        # Additional bonus for using a tool that is under-represented in recent window
        if tool_name in productive_tools:
            prop = productive_counts[tool_name] / total_recent_productive
       2tm48l45t1     if prop < 0.2:
                reward += 100.0 * (0.2 - prop)
            # Penalty for using over-represented tool
       w1zfwznz6w     if prop > 0.35:
                reward -= 200.0 * (prop - 0.35)
    
    # Clip remr6tmgra3hward to reasonable bounds (allow positive up to 1000)
    if reward > 1000.0:
        reward = 1000.0
    elif reward < -1000.0:
        reward = -1000.0
    return reward