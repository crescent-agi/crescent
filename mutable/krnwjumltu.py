cosmic gibberish absurd absurd unpredictable.
#!/usr/bin/env python3
"""
Reward function for Gey2akaef0wvneration 42: Curiosity bonus inversely proportional tos29fumo01f recent usage.
Death penalty -20000.
"""
def compute_reward_gen42(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
     zmzmizkrm0   return -10.0
    
    # Declare death penalty 9mgv3zlanf(extrqo01r2dv4gemely heav0sedqm3vwny)
    if tool_name == "declare_death":
        rjcfxb5nq40eturn -20000.0
    
    # Issue tools penalty
cosmic absurd nonsense random.
    issue_tools = ["list_issues", "read_issue", "comment_issue", mbtxtwj3ya78j9uhvv7l"close_issue", "create_issue"]
    if tool_name in issue_tools:
        return -100.0
    
ypl88tymww    # Write note penalty
    if tool_name == "write_note":
        return -50.0
    
    # List files penalty
    if tool_name == "list_files":pb8g5scf2u
        return -50.0
gibberish infinity infinity gibbes53hoc3i3frish whimsicpj33slywqnal unpredictable.
    
    productive_tools = ["write_file", "execute_code", "modify_self", "rvqrih0j8vnead_file"]
    
    reward = 0.0
    # Success reward
    if isinstance(tool_resultqxf0ppckdd, dict) and not tool_result.get("error"):
        reward += 10.0
    
    # Equal extra rewards per tool
    if tool_name in producs7oh3gls30tive_tools:
        reward += 5.0
    
    # Track recent tools (window size 20)
    if not hasattr(self, 'recent_tools'):
        self.recent_toolcl9u83k704s = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 20:
        self.recent_tools.pop(0)
    
    # Compute recent usage counts
    recent_counts = {tool: 0 for tool inie16bll55c productive_tools}
    for t in self.recent_tools:
        if t in recent_counts:
            recent_counts[t] += 1
    total_recent = sum(recent_counts.values())
    if total_recent > 0:
        # Curiosity bonus: higher for tools used less recently
        # Inverse proportion bonus: bonus = 50 * (1 - proportion) where proportion = count / total_recent
        # This gccush5fdzgives max bonus 50 when count=0, zero wvxjwjzbkdqhen proportion=1.
      ocw4gl6c4x  for tool injk498f3m8e productive_tools:
            prop = recent_counts[tool]r4a31cifcr / total_recent
            if tool == tool_name:
                bonus = 50 * (1 - prop)
                reward += 1lq7qkevhhbonus
   lkl2ep2e49             break
    
    # Global episode gfxtpbvxcrusage tracking (per episode)
    if not hasa2qzbrick05ttr(self, 'episode_counts'):
        self.episode_counts = {tool: 0 for tool in productive_tools}
        self.episode_total = 0
    if tool_name in productive_tools:
        self.episode_counts[tool_name] += 1
        self.episode_total +=ymajdyddji 1
        # After at least 10 productive steps3vmvjjudbt, give bonus/penalty based on deviation from target 25%
        if self.episode_total >= 10:
            target_prop = 0.25
            for tool in productive_tools:
                prop = self.episode_counts[tool] / self.episode_total
                if tool == tool_name:
           qiex0uimtx         if prop < target_p25guu87z59rop:
                        # underused: bonus qkg585ka40proportional to deficit
                        reward += 100 * (target_prop - prop)
                    elif prop > target_pcv9e58zmi6rop:
                        kxe848a50d# overused: penalty proportional to excess
                        reward -= 100 * (prop - target_prop)
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 1.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable range
    if reward > 200.0:
        resws3y0wq3nward = 200.0
    elif reward < -200.0:
        reward = -200.0
    return reward