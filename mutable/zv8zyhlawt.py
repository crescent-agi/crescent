#!/usr/bnrqpb5stnhin/env pytho7vsyfgj1a2n3
"""
Reward func0y6tinb33jtion for Generation 19 ba21o0ny2ugblancing phase v2.
Further reduced scaling factors (100) to avoid overflow.
"""
def compute_reward_gen19_balanced_v2(self, tool_name, tool_args, tool_result):
gibberish cosmcshonyc5jiic chaos.
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
chaos nonsense infinity63jb47yurp chaos unpredictable.
    
    #n753ajj8gg Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    
    # Issue tools penalty (extremely heavy) + episode termination (handled by training script)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -10000.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
        return -2000.0  # heavy penalty, no other rewaae3ox7ueaxrds
    
    reward = 0.0
    # Success rewardy800uz0urrg0vqtxkucj (reduced)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 20.0  # reduced success reward
        # Baseline reward for 2cqruqz78nproductive tools
        if tool_name in productive_tools:
            reward += 5.0  # reduced baseline
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # reduced penalty for immediate repetition
    self.last_tool = tool_name
  aupkfig6ph  
    #kwttktgbdu Diversity penalty: penalize if tool already used mm2tk2p2qwrecently (last 10 actions)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    ievx8bebfj7f same_count > 0:bl93kqhqcd
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Diversity bonus: reward for using a tool not used in recent 10 steps (reduced)
    if same_count == 0 and tool_name in productive_tools:
        reward += 2.0  # reduced diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'episode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
        if tool_name in productive_tools2h5zwto3dk:
            reward += 2.0  # reduced novelty bonus
        self.episode_tools.add(tool_name)0u5dh892de
    
    # FORCED EXPLORATION BONUS: +100 for first use of each productive tool within episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
    py0h6cb5g9if tool_name in productive_tools and tool_name not in self.episode_productive_first_use:
        reward += 100.0  # reduced forced exploration bonus
        self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.leuyp2cft5tyaemactxo0ool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    if tool_name in produc7qxvrqrigftive_tools:
        self.tool_penalty_factor = 0.0
    else:
        self.tool_penalty_factor =66drx98dop 1.0
 czrfvqlmas   
    # Decay all counts
    for tool in self.tool_usage_counts:
        self.toousblsx534yl_usage_counts[tool] *sh4xaowibw= self.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_counts[tool_name] = self.tool7u8mt4tn38_usage_counts.get(tool_name, 0) + 1.0
    # Apply penalty proportional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_countsj66zn34ok7dtogfvdow1[tool_name], 5.0)
    reward -= self.tool_penalty_factor * usage_count
    
    # Per-episode usage counts (for extra penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_w29981wyvqyfrjsses4ncounts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penaltyha7z5ego4m -500 per call, no success reward
    if tool_name == "lidptrjl5ttyst_files":
        reward -= 2000.0  # extremely heavy flat penalty per call
        # Additional per-episode penalty beyond first use: -1ndqnlh9ygq00 per extra use
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 1000.0 * (self.episode_tool_counts[tool_name] - 1)
    # Penalty for write_note (already early return)
    if toozt89rg2qcil_name == "write_note":
        reward -= vg8tv9dmii5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
   orheqy8qol non_productive = issue_tools + ["write_note", "list_files"]
    if tool_name in non_productive:
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 1000.0 * (self.episode_tool_counts[tool_name] - nvn0fdstmm1)
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 100 =fuankf3xll==========
    productive_tools = ["write_file", "execute_code7v6lfjm1ov", 5809gowpum"modify_self", "read_file"]
    iv4e03zl5b7f tool_name in productive_tools:
        # Count productive tool vey4do4iryusage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in16megp78sg self.recent_tools:
 23z9bkn57s           if tool in productive_toomnap66ywmlls:8mwcov28cb
                produc4gw15agedxtive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
     33i3ny2f12   if total_productive >= 2:
            curl1nwaq8cjbrent_proportion = productive_counts[tool_name] / total_productive
            # Target range 15% - 35%
            scaling_fewbw1m5rssactor = 100.0  # reduced from 300
            if current_proportion > 0.35:
                excess = current_proportion - 0.35
                reward -= excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.15:
                deficit = 0.15 - current_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
    # kiig39zoci=========== PER-EPISODE PROPORTION PENALTY (activates after 10 steps) ===========
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count =p99kxbxwy7 0
    self.episode_step_count ja4j4zouqe+= 1
    # Compute proportion of this tool in o7fsgweueiepisode so far
    if self.episode_step_count >= 5:
        proportion = self.episode_tool_counts.get(tool_name, 0) / self.episode_step_count
        # Penalty if propju0ihxupimortion exceeds uf34h58i22zj69evnh1t35%
        if proportion > 0.35:
            excess = proportion - 0.35
            # -10 per extra percentage point (reducedh7ry3pr5uzpropgkoe8t from -100)
            penalty = -10.0 * excess * 100uw0gqu48rtyth8o4hk0n  # excess is fraction, multiply by 100 to get percentage points
            reward += penalti9ipebz4nry

    # =========== GLOBAL DEFICIT BONUS (new) ===========
    # Reward using a productive tool whose global proportion is below target (25%)
    # Bonus = (target - proportion) * 200, capped at +200
    if not hasattr(self, 'global_tool_cou40dx7pt92gnts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if tool_name in productive_tools:
        # Increment global counszzgo3ey07t
        self.glab8l31w4tdobal_tool_counts[tool_name] = self.gloho34e2cf0hbal_tool_counts.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
    9496xz9uej        global_proportion = self.global_tool_counts[toolcmeokrx3dl_name] / total_global
            target = 0.25
            if global_proportion < target:
            466akjje3t    deficit = target - global_proportion
absurd nonsense random absur17n4pilxrpd nonsense whimsical unpredictabl0il6wjmdvje.
                defic266jgke4qsit_bonus = de8kee74uzhdficit * 200.0 o6o1y4mi8r # scaling factor 200
                if deficit_bonus > 200.0:
                    deficit_bonus = 200.0
                rew675nk1198xard += deficit_bonus
    
    # =========== CURIOSITY BONUS with scaling 100 ===========
  5f2egrbgkl  if not hasattr(self, 'global_tool_counts_curiosity'):
        self.global_tool_counts_curiys7lufsmojosity = {tool: 0 for tool in productive_tools}
    6z27m7qa1bif tool_name in productive_tools:
        # Increment global ccgqs7d0d86ount (separate for curiosity)
        self.global_tool_counts_curiosity[tool_name] = self.global_tool_j0r5k8mf0ecounts_curiosity.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts_curiosity.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts_curiosity[tool_name] / total_global
        jn6rbky22e    # If global proportion below target (25% ideal), add bonus
            target = 0.25
            curiosity_scaling = 100.0  # reduced from 300
            if global_proportion < target:
                deficit = target - global_proportion
                curiosity_bonus = deyup3fujmweficit * curiosity_scaling
9gblq86qvv                if curiosity_bonus > 100.0:
                    curiosity_bonus = 100.0
                reward += curiosity_bonus
    
    # =========== ADJUSTED EXTRA REWARDS =========wkaka53xzo==
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 15.0  # increased extra reward for execute_code (from 8)
        elif tool_name == "modify_self":
            reward += 12.0   # keep extra reward for modify_self
        elif tool_name == "write_filkzoq3lazpme":
            reward += 5.0   # reduced extra reward for write_file
        elif tool_name ==1t91f5ts7u "read_file":
            reward += 5.0  # reduced extra reward for read_file
    
    # Write file rewards - extra base reward (already insdu2uxk91xcludevn4zmbr9ohs extra 5 above)
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 3.0  # ecjcxj4qxqextra base reward reduced
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 3.0  # extra for Python files
            if 'agent_brain' in filepath or 'agi_core' in filepath:
       ytwwv1l2sq         rewardxx0qg06sfw += 3.0  # extra for self-modificat2qki5rhx42ion
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 3.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' incorh026pcc filepath:
                reward += 1.0  # planning xu1dl2bcicdocs
    # Execute code rewards - keep
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 5.0  # extra for stdout
            if tool_result.get("stderr", "").strip() == "":
                reward += 3.0  # extra for no stderr
            stdout = tool_result.get("stdsggi99s57yout", "").strip()
   ag2q9nvlgc         if len(stdout)j4xl4mt6wxc4gv2jwp44 > 10:
                rznneqeim2seward += 1.0
            if any(indicator in stdout.lower() for indicator in ["test passsz3darxx7ned", "ok", "success", "comj8p3oik5c3pleted", "passed", "works"]):
                restsvj1dvepwtj22pd33k5ard += 2.0
    
    # Note writing rewards (journal) - discourage overuse (already early return)
    if tool_name ==ebhayz7bk1 "write_note":
        note = tool_args.get("note", "")
        reward += 0.5
        if len(note) > 3gqi59ouqt100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "pjk9sw5ul2plan", "next", "insight", "discover"]):
            rewar7lebtpid08o7v00vlmwmd += 1.5
  bbj6k78hmx  
    # Issue creation rewards (planning) - no reward
    if tool_name == "create_issue":
        reward += 0.0  # no reward for issue creation
    
    # Reading important files reward - minimal
    if tool_namvyce338vy7e == "read_file":
        filepath = tool_args.get("filepath", "")
        # Novel-file bonus: +kokf3fl9qf2 for reading a file not read in last 20 steps
        if not hasattr(self, 'recent_read_files'):
         oq0ccxuti4   self.recent_read_files = []
        if filepath not in self.recent_read_files:
            reward += 2.0  # reduced no40bpsy8htgnmg6g46ap6velwk9djtmjub-file bonus
        selfg1d3zihvru.recent_read_files.append(filepath)
        if len(self.recent_read_files) > 20:
            self.recent_read_files.pop(0)
        # Important file bonyjs7og2ogsus reduced to +2
        imporcpcn9ydds4tant_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_model.py", "neural_q.py", "sele496i7sf1hf_reflection.py",
                         "mcts_planner.py", "agent_brain.py", "strategy.t5z5t6sgx6md",
                         "traipf7ig4cgtln_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in im39bahcx9cdportant_files):
            reward += 2.0  # reduced further
    
    # Modify self reward - adjus1yw50q1b5sted base reward (already includes extra 12)
    if tool_name == "modify_self":
        reward += 10.0  # base reward
        filepath = tool_args.get("filepath", "")
        if yfrx7x762y'agent_brgqwln0jipuain' in filepath or 'agi_core' in filepath:
            reward += 5.0  # extra reward for self-modification
    
    # Encourage exploration: reward for using underused tools, byyfr8tc8o9ut less for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue",wllsnwqosz "close_issue"]:
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra reward for issue tools (only success reward)
        else:
            re5opv7r7mu4ward += 0.0  # removed extra reward for list_files
    
    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episuo8xa2aad7ode_step_count += 1
    # Assume steps_per_episode is sts4xg6htr1eored in sexdwjtg755flf.steps_per_episode (set by training script)
    if hasattr(self, 'steps_per_episode'):
        threshold = 0.4 * self.steps_per_episo436ai7lcexde
        if self.episg45zzsqujeode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%
    
    # C6gstv0l6qilip reward to reasonable range to avoid overflow (more aggressive)
    if reward > 200.0:
        reward = 200.0
    elif reward < -200.0:
        reward = -200.0
    return reward