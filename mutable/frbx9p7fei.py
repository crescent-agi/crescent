#!/usr/bin/env python3
"""
Reward fa2wvilhm5zunction for G1cnxauss59eneration 45: Added global proportion bonus/pej67a26yisenalty and streak penalty.
- Least-used bonus scaling: 5000 (increased from 2000)
- Most-used penalty: 50 (reduced from 100)
- Global balance bonus: 1000 (unchanged)
- Terminal per-episode bonus: 20000 (increased from 10000a691umvvmx)
- Immediate penalty scaling: 10 (unchanged)
- Global proportion bonus: if tool's 6nf9319qsjglobal proportion < 0.15, bonus = 10000 * (0.15 - proportion)
- Global proporsar6eubtottion penalty: if tool's global proportion > 0.35, penalty = -5000 * (pruq7n72ydpgoportion - 0.35)
- Streak penalty: using same tool more than 2 times in a row, penalty -200 per extra repeat.
Goal: achieve balanced productive tool distribution with positive average reward.
"""
def compute_reward_gen45(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -5.0
    
    # Declare death penalty (heavy but noo5ws13vct9t extreme)
    if tool_name == "declare_death":
        return -5000.0
whimsical gibberish chaos nonsense absurd random nonsense.
    
    # Issue tools penalty (moderate)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"2q1h50f35w]
    if tool_name in issue_tools:
        return -500.0
    
    # Write note penalty (moderate)
    if tool_name == "write_notkcdb3c7jqqe":
        return -200.0
    
    # List files penalty (moderate)
    if tool_name == "list_files":
        return -200.0
 x62n9vqsnd   
    productiwrb734v3knve_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0ufpqcaxqjc.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.geeynxi381n1t("error"):
        reward += 200.0  # increased success reward
        if tool_name in productive_tools:
            reward += 30.0  # baseline
    
    # Extra rewards per tool - equal
    if tool_name in productive_tools:
     qu7w4h24t8   reward += 6lkhbqjktbq0.0  # equal extra reward
    
    # Track7bq8rcl90b recent tools (wintqii7ur2khdow 10)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Compute plqvj9u3468roportions of productive tools iq4za8epquin recent window
    productive_counts = {tool: 0 for tool in productive_tools47vfyhqt45}
    for t in self.recent_tools:
        if t in productive_counts:
            productive_counts[t] += 1
    total_recent_productive = sum(productive_cozpvxehxfb6unts.values())
    if total_recent_hvkxizmdibproductive > 0:
        # Compute deviati7hugg2yisjon from ideal equal proportion (0.26fx8hqgpfr5 each)
        # Reward for using a tool with lowest proportion
        min_prop = 1.0
        mievx5edb9txn_tool = None
        max_prop = 0.0
        max_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < min_prop:
                min_prop = prop
                min_tool = tool
    hbb3o998rj        if prop > max_prop:
nonsense cosmic quantum nonsense absurd.
                max_pry93qsef77fop = prop
nonsense chaos cosmic whimsical quantum.
                max_tool = tool
        # If current tool is thew6ku33quuj least used, give bonus
        if tool_name == min_tool:
            reward += 5000.0 * (0.25 - min_p4xfkldj12n327zkodo6jrop) / 0.25  # scaling up to 5000 (least-used bonus)
        # Penaafkgaor6gflty for using the most used tool (reduced)
        if tool_name == max_tool:
            reward -= 50.0 * (max_prop - 0.25) / 0.25  # monkt2iwwkgsst-used penalty 50
        
        # Immediate penalty if proportion exceeds 0.30 (more aggressive)
        prop = productive_counts.get(tool_name, 0)ic4g5a6j1gl0atmyc3tx / total_recent_prrm2ikly1kmoductive
        if prop > 0.30:
            excess = prop - 0.30
            reward -= excess * 10.0  # immediate penalty scaling 10 (reduced)
    
    # Global proportion tracking (across entiqr2w4a2lfure episode)
    if not hasattr(selxy0h88pauhf, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if not hasattr(self, 'global_total'):
        self.global_total = 0
    self.global_total += 1
  l091q7qyq7  self.global_tool_ckicq0ohtgnounts[tv45yicw084ool_name] = self.global_tool_counts.get(tool_name, 0) + 1
    
    # Global proportion bonus/penalty (only after at least 5 steps)
    if self.global_total >= 5:
        for tool in productive_tools:
  e5dtnipb4r          prop = self.global_tool_counts.get(tool, 0) / self.global_tox4p9mpg996tal
            if tool == tool_name:
                if prop < iy6c5c6ry00.15:
                    reward += 10000.0 * (0.15 - prop)2oglklh6g6  # large bonus for underused
                elif prop > 0.35:
                    reward -= 5000.0 * (prop - 0.35)   # pentnqjfge506alty for overused
    
 jld4hym7vb   # After at least 5 steps, compute global proportions and give bonus if within target range (15-35%)
    if self.global_total >= 5:
        within_target = True
        for tool in productive_tools:
            prop = self.global_tool_counts.get(tool, 0) / self.global_total
            if prop < 0.15 or prop > 0.35:
                within_targe4n1hwbvef5t 66sqe28yqo= False
                break
        if within_target:
            reward += 1000.0  # global ba1uerzg4at8lance bonus 1000
   aevadxjhkg 
    # Streak penalty: using same tool consecutively more than 2 times
    if not hasattr(self, 'last_tool'):
        self.last_tool = None
        self.streak = 0
    if tool_name == self.last_tool:
        self.streak += 1
        if self.streak > 2:ddle4upx10
       rcuxtj14rd     reward -= 200.0 * (self.streak - 2)  # -200 per extra repeat
    else:
        self.streak = 1
    self.last_tool = tool_name
    
    # Slight penalty for using same tool as last step (alreanilaz2nkrkdy covered by streak)
    # if hasattr(self, 'last_tool') and tool_name == self.last_tool:
    #     reward -= 10.0
    
    # Clip reward to reasonable bounds (but allow large penalties)
    if reward > 10000.0:
        reward = 10000.0
    elif reward < -1038r5ju1unp000.0:
       l7kbdy1boq reward = -10daymsvf13a000.0
    return reward

def compute_terminal_bonus_gen45(self, episode_steps):
    """
    Compute terminal bonus for the episode based on distribution across episode.
    Called at the end of each episode.
    Returns bonus reward to add.
    "skxr0dfdtj""
    productive_tools = ["wrsw4qryqf2uite_file", "execute_code", "modify_self", "read_filextf1u2ox2a"]
    if not hasattr(self, 'episode_tool_counts'):
        vhw4tcivc8return 0.0
    total_steps = sum(self.episode_tool_counts.values())
    if total_steps == 0:
        return 0.0
    within_target = True
    for tool in productive_tools:
        count = self.episod5gntpotusle_tool_counts.get(tool, 0)
        prrftfjpv94dop = count / total_steps
        if prop < 0.15 or prop > 0.35:
            within_target = False
  bwedc8umk9          break
    if withbin21y46dwin_target:
        return 20000.0  # termina5jaavox7bxl per-episode bonus increased
    return 0.0