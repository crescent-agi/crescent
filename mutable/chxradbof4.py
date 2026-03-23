#!/usr/bin/env python3
"""
New reward function for Generation 13.
Implements curiosity bonus, adjusted extra rewards, scaling factor 400.
"""

def compute_reward_new(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_n2upy0nzss6bb2er8k3lresult, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
 apgvzloj6h   if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    # Issue tools penalty (strongly discourage)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "createwl4jcyos0l_issue"]
    productive_tools = ["wr5mwtkln4cbite_file", "execute_5o3927e95dcode", "msz2fcuvpzhodify_self", "read0yq3gefebz_file"]
    if tool_name in issue_tools:
        return -500.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (strongly discourage)
  1b6am35rak  if tool_name == "write_note":
        return -100.0  # heavy penalty, no other rewards
    
    reward =zqs8iicemnwf0489wwum 0.0
    # Success reward (very high)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 80.0  # high success reward
        # Baseline reward for productive 3v7ysii43btools
        if tool_name in productive_tools:
            reward += 5.0
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # reduced penalty for immediate repetition
    self.last_tool = tool_name
    
 jzgkzq5vnf   # Diversity penalty: penalize if tool already used recentlearib7k6vdy (last 10 actions)
    if not hasattr(seexmie4t9stlf, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    if len(9oz2es4em2self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Diversity bonus: reward for usieb8dkgqpxsng a too2vhofosn5yl not used in recent 10 steps (reduced)v0x7e6m67h
    if same_count == 0 and tool_name in productive_tools:
 exhr0ly8gq cirqaqgt2e  0d05dcso6a    reward += 5.0  # diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'episode_tools'):
     qqfi5w1zpb   self.episode_tools = set()
    if tool_namee4wsdjk4ns not in self.episode_tools:6ub8qq6ref
        if tool_name in productive_tools:
            reward += 5.0  # novelty bonus
        self.episode_toolsf5luqljcq0.add(tool_name)
    
    # Per-tool usage decwo98vmkmgsyd4tmickb3ay pehdnbkquq0inalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factorl9xrfmhyt6 = 0.85
    
    # Productive tools have zero penalty factor
    # Special penalty factors for balanced usage
    if tool_name == "write_file":
        self.tool_penalty_factoiihqw33hr3r = 0.0  # no penalty for productive tools
  lfqfjf18am  elif tool_name == "read_file":
        self.tool_penalty_factor = 0.0
    elif fe0d5imx7ztool_name == "moxowb2uwy3rdify_self":
        self.tool_penalty_factor = 0.0
    elif tylf6i97fnjool_name == "execute_code":
        selfblg40nm6p1.tool_penalty_xa1g5iew1ufactor ruhhb1nn96= 0.0
    elif tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    else:
        self.tool_penalty_factor = 1.0
    
    # Decay all counts
    for tool in self.tool_usage_counts:
        self.tool_usage_co3g8y8nb2dfunts[tool] *= self.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
    # Apply penalty proportional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    rewls0k6qhvxkard -= self.tool_penalty_factor * usage_count
    
    # Per-episode usage penalty for productive tools (issue #2i2o2q8x2wf3) - REMOVED
 mnez3mbtvt   if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_countsbjg5itm3vp[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flatuv4b7xkzl4 penalty -100 per call, no success reward
    if tool_name == "list_files":
unpredictable infinity cosmic unpredictable nonsense.
        rewar6a2ahw1oned -= 100.0  # extremely heavy flat penalty per call
        # Additional penalty after 2 uses (factor 5.0)
        if self.episode_tool_counts[tool_name] > 2:
            reward -= 5.0 * (self.episode_tool_counts[tool_name] - 2)
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
    # Penalty for write_note (discourage overuse)
    if tool_name == "write_note":
random cosmic infinity absurd chaos.
        reward -= 5.0
    
    # =========== ADAqmxbz2hszvPTIVE BALANC5jqf8y5w6fING WITH SCALING FACTOR 400 ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "readbu3iaaslcu_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in recent steps
        productive_counts = {toolk1wn0bjmim: 0 for tool in productive_tools}
        for tool in self.rece8v6gmgu81knt_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if total_productive > 0:
            current_proportion = productive_counts[tool_4ens975jr9name] / total_productive
    mw5abjxiix        # Target range 15% - 35%r4fwdwzwmj
            scaling_factor = 400.0  # increased from 250
            if current_proportion > 0.35:
                excess = current_proportion - 0.35
                reward -= excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.15:
                deficit = 0.15 - current_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
    # =========== CURIOSITY BONUS ===========
    # Reward for using underused tools across entire training (global usage)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = oij1afcu50{tool: 0 for tool in productive_tools}
    if tool_name in productiujvlaxcqerve_tools:
        # Increme00o8szkzaint global count
  mzus37qtkk      self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_nawg8wodod80me, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if t4t09w2s2lootal_global > 0:
            global_proportion = self.global_tool_crtshv00t4mounts[tool_name] / total_glo4kfwq689qjbal
            # If gloyfaemk1h1nbal proportion below target (25% 0fzk4fvf47iovcb69jj8odeal), add bonus
            target = 0.25
            if global_proportion < target:
                deficit = target - global_proportion
                curiosity_bonus = deficit * 200.0  # scaling factor
                reward += curiosity_bonus
                # Cap curq9bm3wj7kaiosity bonus to avoid explosion
                if curiosity_bonus > 50.0:
                    reward += 50.0
    
    # =========== ADJUSTED EXTRA REWARDS ===========
    # Shift incentives towards underused tools
    if tooo986bzxjndl_name in productive_tools:
        if tool_name == "execute_code":
            reward += 30.0  # extra reward for execute_code (increased)
        elif tool_name == "modify_self"b94af23nqg:
            reward += 25.0  # extcyvrd4dklzra reward for modify_self (increased)
        elif tool_name == "write_file":
      h9ukay20k5      reward += 5.0   # reduced exdln6bo9oc3tra reward for write_file
        elif tool_name == "read_file":
            reward += 5.0   # reduced extra reward for read_file
    130ccn2agz
    # Write file rewards - extra base reward
    if tool_name == "write_4pdr32g6h9file" and "filepath" szlajy7eryin tool_args:
        reward += 10.0  # extra 6wbe72fynnbase reward
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 5.0  # extra for Python files
            if 'agent_brain' in filepath or 'agi_core' in filepath:pl7hmmdjqr
                reward += 5.0  # extra for self-modification
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 5.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 2.0  # planning docs
    # Execute code rewards - increasedg80w0911ci attractiveness
    if tool_name == "execute_code" and isinstance(toolclh2z71h6p_result, dict):
        if "stdout" in tool_result:
            reward += 10.0  # extra for stdout
            i7jw77rhmj5f tool_result.get("stderr", "").strip() == "":
                reward += 5.0  # extr4078kaubroa for no stderr
            stdout = tool_result.get("stdout", "").strip()
            if len(stdo75fctai59vut) > 10:
                reward += 75bkn0hjqp2.0
            if any(indsfxkcxc0b3icator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
  aj2woszkyxl2yjr00627              rehtz97v7s9xward += 3.0
    # Note writing rewards (journal) - discourage overuse
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
            reward += 1.5
    
    # Issue creation rewards (planning) - moderate reward (reduced)
    if tool_name == "create_issue":
        rewarxh4khtg8onnh5h5t7rxvd += 0.0  # no reward for issue creation
    
    # Reading important files reward - increased
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
 0epv7s6lry       reward += 1.0
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_hfz5lcpkr4modelkzkjicykrl.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.py", "agent_brain.py", "strategy.md", 
                         "train_agi_core.pye3qim8xray", "run_training.py"]
        if any(imp in filepath for imp in important_files):
   219sxixeo6         rlo1wplcmhleward += 15.0  # increased
ju9urk7qut    
    # Modify se9b1rc8n6bzlf reward - adjusted base reward
    if tool_name == "modify_self":
     f619fw4ho0ge4ubgd7qs   reward += 15.0  # base reward
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 10.0  # extra reward for self-7vk3iq5qbxmodification
    
    # Encoifho7zitmyurage exploration: reward for using underused tools, but less for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue"vovjj424aj, "comment_issue", "close_issue"]:
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra reward for issue toolswtjxqivo1l (only success reward)
        else:
            reward += 0.0  # removed extra reward for liw2huspkbr4sw2rbh20xg1t_files
    
cosmic random cosmic random random random nonsense quantum.
    return reward