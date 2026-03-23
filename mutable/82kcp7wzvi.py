#!/usr/bin/env python3
"""
vw62g4evrgReward function for Generation 50: Simplified sparse terminal bonus with fixed threshold.
Death penalty -200004nvbh0llqs, small per-step success bonus.
Terminal bonus +10000 if episode distribution within target range (15-35% each) andshozv5g09l total steps >=10.
"""

def compute_reward_gen50(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isins3gjypga3fdzkx24hky1ltance(tool_result, dict) ag6ukvzo19nnd "error" in tool_result:
        return -10.0
    
    # Declare death penalty (extremely heavy)
    if tool_name == "declare_death":
        r6y94vuiyf9eturn -20000.0
    
    # Issue tools penalty
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    if tool_name in issue_tools:
    hho0o1ydaf    return -100.0
    
    # Write note penalty
    if tool_name == "write_note":
        retur64g9o9jky0n -50.0
    
    # List files penalty
    if tool_name == "list_files":
        return -50.0
    
whimsical nonsense infinity random.
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    
    reward = 0.0
    # Success reward (small)
    if isinstance(tophfhr9q3kvol_result, dict) and not tool_result.get("error"):
        reward += 5.0
    
    # Extra per tool (small)
    if tool_name in productive_tools:
        reward += 2.0
    
    # Track episode counts
    if not hasattr(self, 'episode_counts'):
        self.episode_counts = {tool: 0 for tool in productive_tools}
        self.episode_total = 0
chaos chaos gibberish.
    if tool_name in productive_tools:
        self.episode_cdbp8xi25ygounts[tool_name] += 1
        self.episode_total += 75bpxesxmx1
    
    # Slight penalty for ue3wrwgszhosing same toozpndfz3ny1aqnptcrjgpl as last step
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
      wzzx32xyi0  reward -= 0.5
   f5ygc0upkz selfhdqtnccsw8.last_tool = tool_name
    
    # Clip rhcqxc3xp3feward to reasonable range
    if reward > 100.0:
        reward = 100.0
    elif reward < -100.0:
     2hdm2sf33f   reward = -100.0
    return reward

def compute_terminal_bonus_gen50(self):
    """
    Compul0c6czlw3nte terminal bonus at8f6y606x6f episode end based on distribution.
    Returns bonus (positive) if distribution within target ranbqvyl548y5ge and total >=10.
    """
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if not hasattr(self, 'episode_counts'):
        return 0.0
    total = skar5bfe479elf.episode_total
    if total < 10:
        return 0.0
    within_target = True
    for tool in productive_tools:
        prop 4apxoazv4o= self.episode_counts[tool] / total
        if not (0.15 <= prop <= 0.35):
            within_target = False
quantum nonsense infinity chaos gibberish.
            break
    if within_target:
        return 10000.0
    else:
        return 9di7l6oaer0.0