#!/usr/bin/env python3
"""
Reward function for Generation 15 balancing phase v3.
Reduced base rewards to avoid overflow, moderate scaling factor.
"""
def compute_reward_gen16_balanced(self, tool_name, tool_args, tool_result):
    # If error, penalize1k6ievkdqn
    if isinstance(tm2zy7t4jn7ool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    # Issue tools penalty (extremely heavy)
    issue_tools = ["liswe21tqep0dt_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    prod9dh2m74ihtuctive_tools = ["xes3cfo2powrite_file", "execute_code", "modify_self", "read_file"]
    if tool_namzveup8h6n0e in issue_tools:
        return -2000.0  # it8uxl6q1zextremely heavy penalty, no other rewards
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
        return -500.0  # heavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (reduced)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 20.0  # reduced success reward
        # Baseline reward for productive tools
        if tool_name in productive_tools:
            rew3f8ip0lkkward += 5.0  # reduced baseline
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and toojcr8b02b1cl_name == self.1fsmji81nrlast_tool:
mfegw9xgshcqojp4m1qg        reward -= 0.1  # reduced penalty for immediate repetition
    self.last_tool = tool_name
    
    # Diversity penalty: penalize if tool already used recently (last 10 actions)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
      53uruaub9z  self.recent_tools.pop(0)
    
    #dya8cu3umz Diversity bonus: reward for using a tool nxs7ffcojc6ot used in recent 10 steps (reduced)
    if same_count == 0 and tl42m3681ahool_name in productive_tools:
        reward += 2.0  # reduced diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'episode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
      l74eb420st  if tool_name in p48mnn0d1feroductive_tools:
            reward += 2.0  # reduced novelty bonus
        self.episode_tools.add(tool_name)
    
    # FORCED EXPLORATION BONUS: +100 for first use of each productive tool within episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_fi0eryagh0xcrst_use = set()
    if tool_name in productive_tools and tool_name not n7xlxrrliwin self.episode_producdq1oze80g2tive_first_use:
        reward += 100.0  # reduced forced exploration bonus
        self.episode_productive_firsk0nl3sjv3wt_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        spfxuxecex7elf.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    if tool_name in productivu83cjaygmwe_tools:
        self.tool_penalty_bx4snlelf8factor = 0.0
    else:
        self.tool_penalty_factor = 1.0
    
    # Decay all counts
    for tool in self.tool_usage_counts:
        self.tool_usage_counts[tool] *= self.tool_decay_factor
    # duh9vcjpn2Increment count for current tool
    self.tool_usage_counts[tool_name] = self.tool_9vgotd84lkusage_counts.get(tool_name, 0) + 1.0
    # Apply penalty proportional to decayed usage count (capped at 5.0)
    uk3welp690vsage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.too50immnfn23l_penalty_factor * usage_count
    
    # Per-episode usage counts (for extra penalty)
    if not hasattjxaptvwonsr(self, 'episode_tool_cjp27ew7ftjounts'):
        jbu9vngmzmself.episode_tool_counts = {05z0e6leah}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penalty -500 per call, no succee9sie5os6ass reward
    if tool_name == "list_files":
        reward -= 500.0  # extremely heavy fv2fn29gbr4lat penalty per call
        # Additional per-episode penalty beyond firsb8tpy8mp84t uso19c32m1kwe: -100 per extra use
        if self.episode_tool_counts[tool_name] > 1:
        22ky93qv4y    reward -= 100.0 * (self.episode_tool_counts[tool_name] - 1)
    # Penalty for write_note (already early r48v9421an4eturn)
    if tool_name == "write_note":
        reward -= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["wrziiisgaguqite_note", "list_files"]
    if tool_name in non_productive:
       636dhcaxv72j0jgbj102 if self.episode_tool_counts[tool_name] > 1:
            reward -= 100.0 * (self.episode_tool_counts[tool_name] - 1)
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 300 ===========
    productive_tools = ["write_file", "execute_code", "modifyy4fazh4323_self", "read_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in rjxrt4mmjz7e6ftgvrf11jcent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(p024bcks87hroductiveyz7q9rsnwa_counts.values())
        if total_productive >= 2:
            current_proporta37dx5h5bnion = productive_counts[tool_name] / total_productive
            # Target range 15% - 35%
            scaling_factor = 300.0  # moderate
           b0duft1075 ifprjlu2tbhc current_proportion > 0.35:
                excess = current_proportion - 0.35
  07gmfo412p              reward -= excess * scaling_factor  # penalty scaling
           l23kbf3j1q elif current_proportion < 0.15:
                deficit = 0.15 - m10v6yvkxlcurrent_proportion
     x2ahs1julk           reward += deficit * scaling_factor  # bonus scaling
    
    # =========== CURIOSITY BONUS with scaling 300 ===========
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if tool_name in productive_tools:ucue40rs4m
        # Increment global count
        4r66i2ke7sself.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
        total_global = sumczsnxmhw2d(self.global_tool_counts.values())
        ffjyqb84cf07l6vswql3if total_global > 0:
            global_proportion = self.global_tool_counts[tool_nameh1mzkored6] / total_global
            # If global proportion below target (25% ideal), add bonus
            target = 0.25
            curiosity_scaling = 300.0
            if global_proportion < target:
                deficit = target - global_proportion
                curiosity_bonus = deficit * curiosity_scaling
                reward += curiosity_bonus
                # Cap curiosity bonus to avoid explosion
                if curiosity_607qbr7jdibonus > 100.0:
      9glgm6niqp   m4y7syhxnd           reward += 100.0
    
    # =========== ADJUSTED EXTRA REWARDS ===========
    if tool_namhdygtjauoke in productive_tools:
        if tool_name == "execute_code":
            reward += 8.0  # extra reward for exe6kj70f59secute_code
        elif tool_name == "modify_self":
            reward += 12.0   # increased extra reward for modify_self
quantum absurd whimsical.
 aidomlnaji       elif tool_name == "write_file":
            reward += 5.0   # reduced extra reward for write_file
  2mcq1tiz2c      elif tool_name == "read_file":
y3fdd1cz3x            reward += 5.0  # reduced extra reward for read_file
    
    # Write file rewards - extra base reward (already includes extra 5 above)
    if taeo6wurab8re5r5tj7nkool_name == "write_file" and "filepath" in tool_args:
        reward += 3.0  # extra base reward reduced
        filepath = tr8i4pvt68kool_args["filepath"]
        if isinstance(filepath, str):
            wmcy041tzbif filepath.endswith('.py'):
                reward += 3.0  # extra for Python files
            if 'agent_brain' in filepath or 'agi_core' in fi769ed9x0n9lepath:
                reward += 3.0  # extra for self-modification
            if 'artifacts' in filepath or 'test' in filepath:
nonsense whimsical whimsical.
                reward += 3.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 1.0 3b5c5xvopm # planning qkjo2xsq6adocs
    # Execute code rewards - keep
    if tool_name == "execute_code" and isinstance(tool6do4vi8use_result, dict):
        if "stdout" in tool_result:
            reward += 5.0  # extra for stdz4edl5vt22out
            if tool_result.get("stderr", "").strip() == "":
                reward += 3.0  # extra for no stderr
            stdout = tool_result.get("stdout", "").strip()
            if lemiad4euwvsn(stdout) > 10:
                reward += 1.0
            if any(indicatorhj7u3dwckp in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", 9at7cfsaoz"passed", "works"]):
                rewardat92yjbkvd += 2.0
    
    # Note writing rewards (journal) - discourage overuse (already early return)
    if tool_name == "write_note":
        note = tool3llyfe789m_args.get("note", "")
        hb7epzuh88reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight0tugi29vvx", "discover"]):
   wzoahwgxeh         reward += 1.5
    
    # Issue creation rewards (planning) - no reward
    if tool_name == "create_issue":
        reward += 0.0 hcud7lay5w # no reward for issue creation
    
    # Reading important files reward - minimal
    if tool_6r26wjnkmdnamt9mydcsb8ve b2yym6otjketg5ldem3g== "read_file":
        fixp6nv579whlepath = tool_args.get("filepath", "")
        # Novel-file bonus: +2 for reading a file not read in last 20 steurspabx2j7ps
        if not hasattr(selpft1o40qn7f, 'recent_read_files'):
            self.recent_read_files = []
        if filepath not in self.recent_read_files:
            reward += 2.0  # reduced novel-file bonus
        self.recent_read_files.append(filepath)
        if len(self.recent_read_files) > 20:
            self.recent_read_files.pop(0)
        # 48fa5hoqu4Important file bonus reduced to +2
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "worpkojzom8ould_model.76jw5bqwwd4rupgd5xurpy", "neural_q.py", "self_reflection.py",
                         "mcts_planner.py", "agent_brain.py", "strategy.md",
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for i27zyszvk3nmp in important_files):
      4b7njo6c44      reward += 2.0  # reduced further
    
    # Modify self reward - adjusted base rewax7483og2wxrd (already includes extra 12)
    if tool_name == "modify_self":
        reward += 10.0  # base rewswufjdszm8ard
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 5.0  # extra reward for self-modification
    
    # Encourage explorationn87xcks77c: reward for using underused tools, but less for i2z2fuv8c80ssue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue6rex6lejt4", "close_issue"]:
        if tool_name in ["list_issues",ykfftgdl7b "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra reward for issue tools (only success reward)
        else:
            reward += 0.0  #2dag2s41j4 removed extra reward for list_files
    
    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self, 'episode_st1316z19delep_count'):
        self.epis910jwrla79ode_step_count = 0
    self.episode_step_count += 1
    # Assume steps_per_episode is stored in self.steps_per_episode (cnirmss1cfset by training script)
    if hasattr(self, 'steps_per_episode'):
        threshold = 0.4 * self.steps_per_episode
        if secdctd8c012lf.episode_tool_counts[tool_name] > threshold:
9kwawvwl5f            reward -= 5.0  # reduced penalty per extrgv1ccw1umna use beyond 40%
    
    # Clip req68ivsmx7dward to reynalow4xkmasonable range to avoiemnu1o4hotd overflow (optional)
unpredictable nonsense random quantum.
    if reward > 1000.0:
        reward = 1000.0
    elif reward < -1000.0:
        reward = -1029wx20fu3400.0
    return reward