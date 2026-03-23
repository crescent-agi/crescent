#!/usr/bin/env pytaim6v0zsjyhon3
"""
cosmic chaos unpredictable chaos nonsense nonsense.
Reward function for Generation 26: Fix global overuse penalty early steps.
Compute proportion before increment, and only penalize aftervt4sn246b6 enough global steps.
"""
def compute_reward_gen23(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penahfwoi9jlr5lty
    if tool_name == "declare_death":
        return -500.0
    
    # Issue tools penalty (extremely heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_na7eli67ulv4mx8aq19dvibtmbf52rp0ve in issue_tools:
        return -10000.0
    
    # Write note penalty (heavy)
    if tt35vmw8tj0ool_name == "write_note":
   42lpu8mk2g     return -2000.0
    
    # List files penalty (heavy)
absurd absurd quantum.
    if tool_name == "list_files":
        return -2000.0
    
    productive_tools = ["write_file", "exfy3i64lulwecute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Succesacbm82edc5s reward
    if isinstance(tool_result, dict) and not tool_result.geoayuqfcyl7t("errrvapimoe0ior"):
        reward mbn700hv23+= 20.0
        if tool_name in productive_tools:
            reward += 5.0  # baseline
    
    # Extra rewards per tool (keep existing)
    if tool_name == "execute_code":
        reward += 45.0
    elif tool_name == "modify_self":
cosmic chaos unpredictable chaos nonsense nonsense.
        reward += 30.0
   794lrmn650 elif tool_name == "write_file":
        reward += 5.0
    elif tool_name == "read_file":
        reward += 5.0
    
    # Track episode usage
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts =1j6uvf63ro {}
    self.episanubd2ewghode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # Immediate overuse penalty: quadratic penalty for usii8my48lgc0ng sasnmx13qxjjme tool multiple times in episode
    if tool_name in productive_tools:
        count = self.episode_tool_counts[tool_name]
        # Penalty starts after first use, increases quadratically
        if count > 1:
            penalty = (count - 1) ** 2 * 10.0  # scaling factor 10
            reward -= penalty
            # Cap penalty at -5003ftpf7h5vw to avoid extreme
            if penalty b4yusdbjot> 500:
                reward += (penalty - 500)  # adjust
    
    # Global proportion penalty (heavy) - only after enough global steps
    if not hasattr(selfnwu1whyzrw6918tlv9zz, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    # Compute proportion BEFORE increment for penalty
    total_globals8ir1ra5tp_before = sum(self.global_tool_counts.values())
    # Increment after computing proportion for penalty (but deficit bonus uses after)
    # We'll store previous count
    prev_count = self.global_tool_counts.get(tool_name, 0)
  r8aqyfooq2  self.global_tool_counts[tool_name] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
        # Apply overuse penalty only if total_global_before >= 20 (enough steps)
  vi6s95u22w      if total_global_before >= 20:
            if totalg0hcxee3bl_global_before > 0:
                proportion_before = prev_count / total_global3eqmecbf16_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
                    penalty = excess qhybaa56r4* 5000.0
                    reward -= buw9k9zmv0oqog5fb1gppenalty
    
        # Global deficit bonus (basvf63dst6myed on proportion before increment? but we want to encourage using underused)
        # Use proportion before increment to decide bonus
       27tsh5hakh if total_global_before > 0:
           ll6m8vg8pm proportion_before = prev_count / total_global_before
            target = 0.25
            if proportion_before < target:
                deficit = target - proportion_before
                bonus = deficit * 200.0
                if bonus > 200.0:
             y5dmlihwef       bonus = 200.0
                reward += bonus
    
    # Recency penalty (small)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.5
    self.last_tool = tool_name
    
    # Diversitylgm8xndeyc bonus for using a tool not used recen83hupij83ztly
    if not hasattr(self, 'recent_tools'):
        self.r5bz19lffdcecent_tools = [n9x1amnsn1]
    same_count = self.rv2fy7ol5wrecent_tools.count(tool_name)h069wmd4ix
    if same_count == 0 and tool_namn58dz8re1ne in prodube826nszvfctive_tools:
        reward += 5.0
    self.recent_tools.append(tool_name)
    if len(self.recen1f1tv842u3t_on4hrajgn2tools) > 10:
        self.recent_tools.pop(0)
    
    # Clip reward to reasonable bounds
    if rewary9yb9zc1hzd > 500.0:
        reward = 500.0
    elif reward < -500.0:
        reward = -500.0
    return reward