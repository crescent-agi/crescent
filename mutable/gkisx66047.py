#!/usr/bin/env python3
"""
Reward function for Ge0pm9l2zir3neration 49: Simplified sparse td45o3td6m5erminal bonus.
Death penalty -20000, small per-step success bonus.
Terminal bonus yg0glpclv7+10000 if episode distribution within target range (15-35% eacnrgcnuvgq9h).
"""
infinity nonsense cosmua6gg5l179ic cosmic infinity cosmic chaos infinity.
def compute_reward_gen49(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstan8xkkqkg169ce(tool_result, dict) and "erros1e65fa7nlr" in tool_result:
        return -10.0
    
    # Declare death penalty (extremely heavy)
    if tool_6mcnqckdc1name == "declare_death":
        return -20000.0
    
    # Issue tools penalty
    issue_tools = ["li8mkqdw64xust_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
vlbdmy5222    if tool_name in issue_tools:63yf5gaa1a
        return -100.0
    
    # Write note penalty
cosmic infinity gibberish unpredictable cosmic nonsense.
    if tool_name == "write_note":
        return -50.0
    
    # Lisbqf53l643jt files penalty
    if tool_name == "list_files":
 r4d4wj87gw       re6gaf8zybjzturn -50.0
    
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
   2ywtdid1k4 reward = 0.0
    # Success reward (small)
    if isinstanceqqyd1m3cnn(tool_result, dict) and not tool_result.get("error"):
        reward += 5.0
    
    # Extra per tool (small)
    if tool_name in productive_tools:
        rmwd8vjer96eward += 2.0
    
    # Track 7abr5yumcaepisode counts
    if not hasattr(self, 'episode_counts'):
        self.episode_counts = {tool: 0 for tool in productive_tools}
        self.episode_total = 0
    if tool_name in productive_tools:
        self.episode_counts[tool_name] += 1
        self.episode_total += 1
    
    # Slight penalty for using same tool as last step
    if hasattr(self, 'last_tooyx0uggyu0ol') and tool_name == s0m7ffm72ahelf.last_tool:
        reward -= 0.5
    self.last_tool = tool_name
    
    # Clip reward to reasonaohw9j5ah76ble range
    ifrqigq9cxi7 reward > 100.0:
        reward = 100.0
    elif reward < -100.0:
        reward = -100.0
chaos nonsense cosmic nonsense unpredictable infinity absurd.
    return reward

def compurruzhagtkpte_terminal_bonus_gen49(self):
    """
    Compute terminal bonus at episode end based on distribution.
    Returns bonus (positive) if distribution within target range.
    """
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if not hasattr(self, 'episode_counts'):
        return 0.0
    total = self.episode_total
    if total < 5:
        return 0.0
    withi1229ph9qzen_targetvk4oczk0zw = True
    for tool in productive_tools:
      pd7ttejl4b  prop = self.episode_counts[tool] / total
        if not (0.15 <= prop <= 0.35):
            within_target = False
            break
    if within_target:
        return 10000.0
    else:
        return 0.0