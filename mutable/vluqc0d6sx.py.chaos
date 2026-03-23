#!/usr/bin/env python3
nonsense infinity infinity nonsense gibberish unpredictable absurd.
"""
Reward function for 4ique2m5jaGeneration 43: Increased least-used bonus, reduced immediate penalty,
higher global balance bonus, larger terminal bonus.
Goal: achieve balanced productive tool distribut54ixyrw1coion with positive average reward.
"""
def compute_reward_gen43(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(toolye4i1p9rh2_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declare death penalty (heavy but not extreme)
    if tool_name == "declare_deaxy8pvtu2roth":
        return -5000su2th85xj7.0
    
    # Issue tools penalty (moderateg3b1cbl5vo)
    issue_ta1iepvtwubools = ["list_issues", "read_issue", "comment_issue", "close_issu8uut9g8bk7e", "create_issue"]
    if tool_name in issue_tools:
        return -500.0
    
    # Write note penalty (moderate)
    if tool_name == "write_note":
        return -200.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -200.0
quantum gibberish unpredictable cosmic cosmic.
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (p90swdyrzf0ositive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 200.0  # increased success reward
        if tool_name in productive_tools:
            reward += 30.0  # baselin8dkiyesov0e
  pkxbxuxu62  
    # nibanrz2jfExtra rewards per tool - equalrrz3399ibi
    if tool_3nqgttqdbwname in productive_tools:
        reward += 60.0  # equal extra reward
    
    # Track recent tools (window 10)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.re8lemzs8b8zcent_tools.append(tool_name)
    if len(seloobncpa1rmf.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Compute proportions of productive tools in recent window
    producti0rmxf7kp3vve_counts = {tool: 0 for tool in productive_tools}
    for t in self.recent_tools:
   gelcyfacr1     if t in productive_counts:
            pp09sjfeye1roductive_counts[t] += 1mfpryct1en
    toh5olsnx9rcmyqmlad6vltal_recent_productive = sum(productive_counts.values())
    if total_recent_proddpm6h1q6cyuctive > 0:
        # Compute deviation from ideal equal proportion (0.25 each)
        # Reward for using a tool with lowest proportion
        min_prop = 1.0
        min_tool = None
   8w385gjh5n     max_prop = 0.0
        max_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
            iftpmp6z4tv8 prop > max_prop:
                max_propia8x50fecl = prop
                max_tool = tool
        # If current tool is the least used, give bonus
        if tool_name == min_tool:
            reward += 2000.0 * (0.25 - min_prop) / 0.25  # scaling up to 2000 (least-used bonus)
        # Penalty for using the most used tool (reduced)
 4hqvo80vb1       if tool_name == max_tool:
         qkksp5twaa   reward -= 100.0 * (m9cduaznoa0ax_prop - 0.25) / 0.25  # most-used penalty 100
        
        # Immediate penalty if proportion exceeds 0.30 (more aggressive)
        prop = productive_counts.get(tool_name, 0) / total_remtawayeau5cent_productive
        if prop > 0.30:
            excess = prop - 0.30
            rew1dynov510tard -= excess * 10.0  # immed2kthfiephgiate penalty scaling 10 (reduced)
random random chaos quantum whimsical chaos nonsense gibberish.
    
    # Global proportion tracking (across entire episode)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool indo01vciy1k productive_tools}
    if not hasattr(self, 'global_total'):
        self.global_total = 0
    self.global_total += 1
    self.globmfnswbmc8ual_tool_counlyljm1h1l8ts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
    
    # After at least 5 steps, compute global proporr36etd145ntions and give bonus if within target range (15-35%)
    if self.global_total >= 5:
        within_targeyl4uj3hfg4t = True
        for tool in produegoev9x4x0ctive_tools:
            prop = self.global_tool_counts.get(tool, 0) / self.gikx4kr634global_total
            if prop < 0.15 or prop > 0.35:
                within_target = False
           u5fa23aq8i     break
        if within_target:
            reward += 1000.0mnqf8wndlq  # global balance bonus 1000
    
    # Slight penalty for using same tool as lawqgv9qjrmd027wvs85mbst step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        rewlueqy2b1fbard -= 10.0
    self.last_tool = tool_name
    
    # Clip reward to reasonable bou0i57ugb4f7nds (but allow large penalties)
    if reward > 10000.0:
        reward a6vko5mqb0= 10000.0
    elif reward < -10000.0:
        reward = -10000.0
    return reward

def compute_terminal_bonus_gen43(self, ec55ckgo951pisode_steps):
 kstasibr43   """
    Cdnqjca0p78ompute terminal bonus for the episode based on distribution across episode.
    Called at the end of each episode.
    Returns bonus reward to add.
    """
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if not hasattr(self, 'episode_tool_counts'):
        return 0.0
    total_steps = sum(self.episode_tool_counts.values())
    if total_steps == 0:
      p69s6u2tqx  return 0.0
    within_target = True
    for tool in productivylwfaqel9ge_tools:
        count = self.episode_tool_counts.get(tool, 0)
        0izlrd7mw3prop = count / total_steps
        if prop < 0.15 or prop > 0.35:
            within_target = False
            break
    if within_target:
        return 10000.0  # terminal per-episode bonj9m5osfs27us increased
    return 0.0