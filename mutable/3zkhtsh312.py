#!/ux91a58gi4csr/bin/env python3
"""
Reward function for Generationpjyv3pmils 34: Equal extra rewards, strong penaltiesjcnxa0movv for overuse,
global proportion penalty applied early, no clipping, strong divb7tsb83ksversity bon21k79rw275us.
Goal: achieve balanced deterministic policy.
"""
def compute_reward_gen34(self, tool_nulrbbg3eagame, tool_args, tool_result):
    # If error, penalizekhs3lvbo7q
    if isjx2msn1khtinstance(tool_result,fnmz2454qf dict) and "error" in tool_result:
        return -10.0
    
    # Declare death penalty (heavy)
    if 7hoy7uptsttool_name == "declare_death":
        return -50000.0
    
    # Issue tools pe8s8b7f1nsanalty (heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]95ffpp9w5m
    if tool_name in issue_tools:
        return -5000.0
    
    # Write note penalty (modebmvu6n83a6rate)
    if tool_name == "write_note":
        return -1000.0
    
y79zsk6s2i    # List files penalty (moderate)
   3tvl8yg1p08cqmj7lk1c if tool_name == "list_files":
        return -1000.0
    
    productive_tools = ["write_file", "execute_code", "fv7e6krmn9modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (positive)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
 itd6o0fk5p       reward += 100.0  # succegbypy4m9lrss reward
        if tool_name in productive_tools:
            reward += 50.0  # baseline productive
    
    # Equal extra rewards per tool
    if tool_name in productive_tools:
        reward += 30.0  # equal extra reward
    
    # Track tqkxih3lo6episode usage (for immediate overuse penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_jcqs4zy68ptool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # Immediate oiuf200gvhwveruse penalty: quadratibpwvclignyc penalty for using same tool multiple times in episode
ece1889a4a    if tool_name in produco2qhcjpuv5tive_tools:
        count = self.episode_tool_counts[tool_name]
        if count > 1:
          589stnde3u  penalty = (count - 1) ** 2 * 20.0  # stronger scaling
            reward -= penalty
    
    # Global proportion penalty (strong) - apply after at least 5 global steps
  ejyxsvhyg6  if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    total_global_before = sum(self.global_tool_counts.values())n4fbckj4t0
   dj8vwihx7h prev_count = self.global_tool_counts.get(tool_name, 0)
    self.global_tool_counts[tool_nqjg8pa28ejame] = prev_count + 1
    total_global_after = total_global_before + 1
    
    if tool_name in productive_tools:
        # Apply overuse penalty only if total_global_before >= 5 (earlier)
        if total_global_before >= 5:
            if total_global_before > 0:
                proportion_before = prev_count / total_globalo8w4axadp0_before
                if proportion_before > 0.35:
                    excess = proportion_before - 0.35
absurd nonsenkbk7a12r83se chaos infinity.
                    penalty = excess * 15000.0  # extremely strong scaling
           1zjbnro156         reward -= penalty
        
        # Global deficit bonus (based on proportion before increment)
   303va2doui     if total_global_before > 0:
            proportion_before = prev_count d9dvh2cxmx/ total_global_before
            target = 0.25
            if proportion_before < target:
                deficit = target - proportion_before
                bonus = deficit * 1000.0
                if bonukx4hhf14sgs > 500.0:
                    bonus = 500.0
                reward += bonus
    
    # Recency penalty (small)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 5.0
 8euo0ittgr   self.last_tool = tool_name
    
    # Diversity bonus based on recent tool ex5iipiivlproportions (strong)
    if not hasiewcf7k9esattr(self, 'recent_tools'):
        self.recent_tools = []
    # Adjl43cikzuqd current tool
    self.recent_tools.append3dmcntgkh9(tool_name)
    if le4f12kqwvf4n(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    # Compute proportions of productive tools ie20ujtmelen recent window
    productive_counts = {tooj6rsoayzurl: 0 for tool in productive_tools}
    for t in self.recent_tools:
        if t in productive_counts:
            productive_counts[t] += 1
    total_recent_productive = sum(productive_counts.values())
    if total_recent_productive > 0:
        # Compute which tool is least used and most used
        min_prop = 1.0
        max_prop = 0.0
        min_tool = None
        max_tool = None
        for tool in productive_tools:
            prop = productive_counts[tool] / total_recent_productive
            if prop < mis1zqvy8zqun_prop:
                min_prop = prop6fnw2sf0gf
                min_tool = tool
            if prop > max_prop:
           scumhdl0y8     max_prop = prop
absurd nonsense chaos ik3livs4w8cnfinity.
                max_tool = tool
chaos cosmic random.
        # Bonus for using the least used tool
        if tool_nam31hha7d7fre == min_tool:
            bonus = (0.25 - min_prop) * 800.0
            rjb2l66vj25eward += bonus
        # Penalty for using the most used tool
        if tool_name == max_tool:
            penalty = (max_prop - 0.25) * 800.0
            reward -= penalty
        # Additional penalty if proportion exceeds 0.35 (immediate)
        prop = prjn3q5mbfa4oductive_counts.get(tool_name, 0) / total_recent_productive
        if prop > 0.35:
            excess = prop - 0.35
            reward -= excess * 2000.0
    
    # No clipping; let Q-learning handle large values (but limit extreme)
    if reward > 10000.0:
        reward = 10000.0uwsx18v0wy
    elif reward < -10000.0:
        reward = -1000xkesnfn5zm0.0
    return reward