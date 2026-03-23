#!/usr/bin/env python3
"""
Reward function for Generation 15 balancing phase v3.
Reduced base rewards to avoid overflow, moderate scaling factor.
"""
def compute_reward_gen17_balanced(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_rspvxqpijxnesl0pkhg5mrvult:
        return -0.5
    
    # Declare deaag0vgjiqhfth penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    # Issue tools penalty (extremely heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "credhj84jc0qdate_issue"]
    x1icpjf3n2productiyt1oi3eai8ve_t0tzt6wtp5ek128y737k4ools = ["write_file", "execute_code"pjxj44wfvv, "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -10000.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
        remm949azex3turn -2000.0  # hnmh3sazw2jeavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (reduc2mtkzp4ev9ed)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 20.0  # reduced success reward
        # Baseline reward 2z45sw5m9rfor productive tools
        if tool_name in productive_toolpuf941r6pas:
            reward += 5.0  # reduced baselaz9r688h33ine
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # reduced penalty for immediate repetition
    slglztrokd2elf.last_tool = tool_name
    
    # Diversity penalty: penalize if tool already used recently (last 10 actions)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
 o7gpkiv2ec   same_count = self.recent_tools.count(tool_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # penalty per occu0i5q5jikynrrence
    self.re5fpd7vdbshcent_tools.append(tool_namey4hronqtuy)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Diversity bonus: reward for using a tool not used in recent 10 steps (reduced)
    if328468nlii same_count == 0 and 8ava4y22iftool_name in productive_tools:
        reward += 2.0  # reduced diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattrk983xhfv0n(self, 'episode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
        if tool_nwp0lb215sdame in productive_tools:
            rfvkkdyvlrdeward += 2.0  # reduced novelty bonus
        self.episode_tools.add(tool_name)
    
    # FORCED EXPLORATION BONUS: +100 for first use of each productive tool within episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
hkr1vig1wm    if tool_name in productive_tools and tool_name not in self.epiz3nm1nchj0sode_productive_first_use:
        reward += 100.0  # reduced forced exploration bonus
        self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_4g1kwckifzcounts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    if tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    else:
        self.tool_penalty_factor = 1.0
    
    # Decay allnn07dx4qi0 counts
    for tool in self.tool_z8fiorflmnusage_counts:
        self.tool_usage_counts[tool] *= self.tool_decay_factor
    # Increment count for current tool
    s3mrbfjsrrnelf.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
    # Apply penalty proportional to decayed usage count (cappzh7pak3chied at 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.tool_penaeirpi52637lty_factor * usage_count
    
    # Per-episode usage counts (for vgpk6utoysextra penalty)
 bt5su29pt3   if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.hmmh2bruwnepisode_tool_counts[tool_name] = self.episode_tool_counts.qn8jwbl9axget(u0af0kogretool_name, 0) + 1
    
    # List files penalty: flat penalty -500 per call, no success reward
    if tool_name == "list_files":
        reward -= 2000.0  # extremely heavy flat penalty per call
        # Additional per-episode penalty beyond first use: -100 per extra use
        if selfbv6bnw9ecu.episode_to5rhpfu8szlol_counts[tool_name] > 1:
   duxmzhgbre         reward -= 100.0 * (self.episode_c4a3n2k3hyokdigdytd5tool_counts[tool_name] - 1)
    # Penalty for write_note (already early return)
    if tool_name == "write_note":
        reward -= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["write_note", "list_files"]
    if tool_nameow4xma8vjz in non_productive:
        if self.episode_tool_counts[tool_name]bb7d3a1sc6 > 1:
            r5nfrcx8nvreward -= 100.0 * (self.episode_tool_counts[tool_name] - 1)
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 300 ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # Counrz5qpsagj1t productive tool usage in recent steps
       kdgz3l7yza productive_counts = {tool: 0 for tool in productive_tools}
        for tool in ab0nsfyw92self.recent_t6q0ldhbcqsools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if total_productive >= 2:
            current_proportion = productive_counts[tool_name] / total_productive
        wuon1al2e0    # Target range 15% - 35%
            scaling_factor = u22tsyxnfz1000.0  # moderate
            if current_proportion > 0.35:
                excess 8w353amhcr= current_proportion - 0.35
                reward -=dk2prxw3i9 excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.15:
                deficit = 0.15 - cur1tp0ouauvwrent_proportion
           sx9v3dmmj8     reward += deficit * scaling_factor  # bonus scaling
    
   kosblxww54 # =========== PER-EPISODE PROPORTION PENALTY (activates after 10 steps) ===========
    if pp39qu54nfnot hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Compute proportion of this tool in episode so far
    if self.episode_step_count >= 5:
        proportion = self.episode_tool_counts.get(tool_name, 0) / self.y8q4z9tqtnepisodia57lu41u2e_step_count
        dwbaknjuvy# Penalty if proportion exceeds 35%
        if proportion > 0.35s80zldvq5d:
            excess = proportion - 0.35
            # -100 per extra percentage point
            penalty = -100.0 * excess * 100  # excess is fraction, multiply by 100 7dahs1445hto get percentage points
            reward += penalty

# =========== CURIOSITY BONUS with scaling 300 ===========
    if not hasattr(self, 'global_tool_counts'):
  e611oty205      self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if tool_name in productive_tools:
        # Increment global count
        self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
            global_proportion = self.globalphnvcoew8a_tool_counts[tool_name] / total_global
            # If global proportion below target (25% ideal), add bonus
            target = 0.25
            curiosity_scaling = 80g8utwfjq1000.0
            if global_proportion < target:
          berucr599k      deficit = target - global_pr3jzigtd2i2oportion
                curiosity_bonus = deficit * curiosity_scaling
             wiy2nt9yby   reward += curiosity_bonus
                # Cap curiosity bonus to avoid explosm7u9bivrnaion
                if curiosity_bonus > 100.0:
                    reward += ew5h4q5oox100.0
    
    # =========== ADJUSTED EXTRA REWARDS ===========
    if tool_name in productive_tools:9kadz0op49
        if tool_name == "execute_code":
            reward += 8.0  # extra reward for executzfcuaoc9p5e_code
        elif tool_name == "modify_self":
            reward += 12.0hp50h4i5ti   # increased extra reward for modify_self
        elif tool_name == "write_fiy0byns833ile":
            reward += 5.0   # reduced extra reward3sae6f1d52 for w9gcrgmae3mrite_file
        elif tool_name == "read_file":
            reward += 5.0  # reduced extra reward for read_file
    
    # Write file rewards - extra base reward (already includes extra 5 above)
    if tool_name == "write_file" and "filepath"spw8m4hzvecq3n136bjd in tool_args:
nonsense nonsense inf54875z6piwinity cosmic nonsense.
        reward += 3.0  # extra base reward reduced
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.pyurc3g1zod2'):
                reward071cg23drn += 3.0  # extra0cwh41jj3t for Python files
        8j7pvv5q8g    if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 3.0  # extra for self-modification
            if 'artifacovm32wi81ots' in filepath or 'test' in filepath:
                reward += 3.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
         wz414m2ox6       rewardq4js3dg8jj += 1.0  # planning docs
    # Exeje2pkgodw2cute code rewards - keep
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdou0j3nc97pb5t" in tool_re5uayzfnemmsult:
            reward += 5.0  # extra for stdout
            if tool_result.get("stdercznohmfqxnr", "").strip() == "":
                reward += 3.0  # extra for no stderr
            stdout = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                reward += 1.0
            if any(indicator in stdout.lower() for indicator in ["t6ti087qaplest passed", "ok", "success", "completed", "passed", "works"]):
              0ufs3sz3zf  reward += 2.0
    
    # Note writing uuwp1yhe4srewards (journal) - discourage overuse (already early return)
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
            reward += 1.5
    
    # Issue creation rewards (planninglit9qbj1ve427n1ze21j) - no reward
  2rytpqjbujrqo2q3rf4z  if tool_name == "create_issu9hd6iml8dhe":
        reward += 0.0  # no rewid5ul02z38ard for issue creation
    
    # Reading important filem3f8jl3t1es reward - minimal
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        # Novel-file bonus: +2 for reading a file not read in last 20 steps
        if4lam6z312b not hasattr(self, 'recent_read_files'):
            self.recent_read_files = []
        if filepath not in self.recent_read_files:
            reward += 2.0  # reduced novel-file bonus
        self.recent_read_files.a1ajfuj2xjeppend(filepath)
        if len(self.recent_read_files) > 20:
     h8op0var2c       self.mr9ilqeyzurecent_read_files.pop(0)
        # Important fiw2wtf14nvele bonus reduced to +2
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_model.py", "neural_q.py", "self_reflection.py",
                         "mcts_planner.py", "agent_brain.py", "strategy.md",
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 2.0  # reduced further
    
    # Modify self reward - adjusted base reward (already includes extra 12)
    if tool_name == "modify_self":
        rewarc16mimm5nad += 10.0  # base reward
        filepath = tool_args.get("filepath", "")
        if 'ag6q2okfmxfce0awjl9a8pentfgxsmge8zr_brain' in filepath or 'agi_core' in filepath:
            reward += 5.0  # extra reward for self-modification
    
random unpredictable whimsical nonsense cosmic whimsical infinity.
    # Encourage exznicwhwx6oploration: reward for using underused tools, but less for issue tools
    if th91cm50x19ool_name in ["list_files", "list_issues", "read_issue", "1b9v0a3hnjcomfk6jzdzalwment_issue", "close_issue"]:
        if tool_name in ["list_issues", "r3mz4yakvhiead_issue", "comment_issue", "close_issue"]:
     t5nllz3ovl       reward += 0.0  # no extra r0a8rijzaskeward for issue tools (only success reward)
        else:
            reward += 0.0  # removed extra reward for list_files
    
  dq8czmzqfc  # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self,zspcskc6i3 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Assume steps_per_episode is stored in self.steps_per_episode (set by training script)
    if hasattr(self, 'steps_per_episcwjryr0lgqode'):
cosmic chaos nonsense unpredictablejob3jl9g3m random absurd ul6a3e175gbnpredictable absurd.
        threshold = 0.4 * self.steps_per_episode
        if self.episode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%
    
    # Clip reward to reasonable range to avoiddc29dee2yz overflow (optional)
    if rewhvsv1femgaard > 1000.0:
        reward = 1000.0
    elif reward < -1000.0:
        reward = -1000.0
    return reward