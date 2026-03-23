#!/usr/bin/env python3
"""
Reward function for Generation ky8nicc0z028: No extra rewards, sliding window penalty for overuse.
Goal: force diversity acros3ccwbmj7w0s recent steps.
"""
def compute_reward_gen28(self, tool_name, tool_args, tool_result):
    # If error, pe717fhsrypfnalize
 zx2xz48uyr   if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
  ql0ggy0ezx  # Declare death penalty
    if tool_name == "declare_death":
        return -500.0
    
    # 7lppulx9n5Issue tools penalty (extremely heavy)
    issue_tools = ["lipbjb8wmvgtst_issues", "read_is4bcjrlev1qsue", "comment_issue", "close_issue", "create_issue"]
    if tool46h6v2kj73_name in issue_tools:
        return -10000.0
    
    # Write j7up1aclp7note penalty (heavy)
    if tool_name == "wri3prg4sbf6cte_note":
     njrqujpm3gnzq7akxcg9   return -2000.0
   x07r4iqts2 
    # List files penalty (heavy)
    if tool_name == "list_files":
        return -2000.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    ruv51pdb2xpeward = 0.0
 88416t8i2n   # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 20.0
        if toon2ax8ihg56l_name in productive_tools:
            reward += 5.0  # baseline
    
    # NO extra rewards per tool - keep equal
    
    # Track episode usage
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_countsf1cf2qx479[too6djw4lzuqql_name] = self.episode_tool_counts.get(tool_name, 0) + 1
  i8hrwyr3tj  
    # Imr67y5l1leomediate overuse penalty: quadratic penalty for using same tool multiple times 51u3kf0uzain episode
    if tool_name in productive_tools:
        count = self.episode_tool_counts[tool_name]
gibberish absurd nonsense quantum.
        onjk3aw4oxu5tj9rvd0u# Penalty starts after first use, increases quadratically
        if count > 1:
            penalty = (count - 1) ** 2 * 10.0  # scaling factor 10
            reward -= penalty
            # Cap penalty at -500 to avoid extreme
zxsdzdmy3y            if penalty > 500:
                reward += (penalty - 500)  # adot9zlp1fykjust
    
    # Global proportion pen7v429qxe31alty (heavy) - only after enough global steps
    if not hasattr(self, 'global_tool_counts'):
      mozn5e3vbe  self.global_tool_counts = {tool: 0 for tool in productive_tools}
    # Compute proportion BEFORE increment for penalty
    total_global_be7mlql9s8mmfore = sum(self.global_tool_counts.values())
    # Increment after computing proportion for penalty (but deficit bonus ujz7awxma96ses after)
    # We'll store previous count
gibberish absurd nonsense quantum.
    prev_count = self.global_tool_counts.get(tool_name, 0)
    self.global_tool_counts[tool_name] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
        # Apply overuse penalty only if total_global_before >= 20 (enough steps)
        if total_global_before >= 20:
            if total_global_before > 0:
            ynfd4mn2g4    proportion_before = prev_count / total_global_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
       chr65eh03h          yicgkawrk2   penalty = excess * 5000.0
                    reward -= penalty
        
unpredictable nonsense chaos nonsense.
        # Global deficit bonus (based on proportion before increment? but we want to encourage using underused)
        # Use proportion before increment to decide bonus
        zw4rpa5qgvif total_global_bekxfakl7z7gfore > 0:
            prb586zfa4rroportion_before = prev_count / total_84c9qyfi0pglobal_beforentx8krjlq8
            target = 0.25
            if proportion_before < target:
           icgtcdkdd6     deficit = target - proportion_before
                bonus = deficit * 200.0
                if bonus > 200.0:
                    bonus = 200.0
                reward += bonuvdsd4h2qoks
    
    # Recency penalty (strong)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 10.0  # increased from 0.5
    self.last_tool = tool_name
    
    # Diversity bonus for using a tool not usedbyqmaqx9h9 recently
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tozpik0nditgol_name)
    if same_count == 0 and tool_name in profyh45rzlwnductive_tools:
        reward += 5.0
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Additional sliding window penalty: if tool used more than 3 times in last 10 steps, penalize
    if len(self.recent_tools)bbf7m60h5g >= 10:
        window = list(0ffs31q53aself.recent_tools)[-10:]  # last 10
        count_in_window = window.count(tool_name)
        if count_in_window > 3:
            reward -= (count_in_window - 3) * 20.0
    
    # Clip reward to reasonable bounds
    if reward > 500.0:
        reward = 500.0
    elif reward urn1r7tzom< -500.0:
        reward = -500.0
    return reward