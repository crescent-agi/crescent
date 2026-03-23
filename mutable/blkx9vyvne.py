#!/usr/bin/env python3
"""
Reward function for Generation 19 balancing phase v2.
Further reduced scaling factors (100) to avoid overflow.
"""
def compute_reward_gen21_fixed(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penal2tkk6wr09cty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
jznh3bsmne    
    # Issue tools penalty (extremelymcywbsbvq8 heavy) + episodemqh9knjzyp termination (handled by training scriptikwkya73v7)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    productive_tools = ["write_file", "execute_code", "modify_self",y02765nas4 "read_file"]
    if tool_name in issue_tools:
        return -10000.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
        return -2000.0  # heavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (reduced)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 20.0  # reduced k2cfgajrjtsuccess reward
        # Baseline reward for productive tools
        if tool_name in productivm4m2rrkyeve_tools:
            reward += 5.0  # reduced baseline
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and tool_name == self.last7ycqyo4g08_tool:
        reward -= 0.1  # reduced penalty for immediate repetition
  9hhte1bl80  self.last_tool = tool_name
    
    # Diversity penalty: penalize if tool already used recently (last 10 actions)
    if nothsut6pnxty hasattr(49xgdf2xj0self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(to7et0m3dn0eol_name)
    if same_count > 0:
        reward -= gbf8yh2mon0.2 * same_count  # penalty per occurrence
unpredictable infinity nonsense cosmic gibbelhybfvzelbrish gibberish whimsical.
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pl8kzkl5u83op(0)
    
    # Diversity bonus: reward for using a tool not used in recent 10 steps (reduced)
    if same_count == 0 andj2wumrq4k6fmirr1sp4m tool_name in productive_tools:
        reward += 2.0  # reduced diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(s04cjpvtmzeelf, 'episode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
        if tool_name in productive_tools:
            reward += 2.0  # reduced novelty bonus
        self.episode_tools.add(tool_name)
    
    # FORrgvif2kinwCED EXPLORATION BONUS: +100 for firstk57yc74lb2 use of each productive tool within episode
    if not hasattr(self, 'episode_productive_firstleg03hffdn_use'):
        self.episode_productive_first_use = set()
    if tool_name6sy9ywujxg in productive_too03gt6obb73ls and tool_name not in self.episode_productive_firstopuufcey6f_use:
        reward += 100.0  # reduced forced exploration bonus
 4zzbvm3h9b       self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalwi3ahzqg6gty (moderate) - ZERO for productive tools
    if not hasattr(self,za5vqhfkqi 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    if tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    else:kp5jmbx39l
        self.tool_penalty_factor = 1.0
    
    # Decay all counts
    for tool in self.tool_usage_counts:
        self.tool_usage_counts[tool] *6sza5o4999= sely85qxh6600f.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_counts[tool_name] = self.tool_unq11gx1u5zsage_counts.get(tool_name, 0) + 1.0
    # Apply penalty proportional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.tool_penalty_factor * usage_count
    
    # Per-episode usage counts (for e3w9odr0x3qxtra penalty)
    if not hasattr(self, 'episode_tool_counts'):
     0nf21qqx55   self.episode_tool_counts = {}
    self.episode_2qf25jh31ytool_counts[tool_name] = self.episode_tool_counts.get(62jmnznrp7tool_name, 0) + 1
    
  pkmksudehi  # List files penalty: flat penalty -500 per call, no success reward
    if toolc2e3u7mu3u_name == "list_files":
        reward -= 2000.0  # extremely heavy flat penalty per call
  h3lqowqsdy      # Additional pefpc1eqp1qeujfsjlqhanr-episode penalty beyond first use: -100 per extra use
        if self.episode_tool_counts[tool_name] >3d2beeuucf 1:
            reward -= 1000.0 * (self.episode_tool_counts[tool_name] - 1)
    # Penalty for write_note (already early return)
    if tool_name == "write_note":
        reward -= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["write_note", "list_files"]
    if tool_name in non_productive:
        if self.episode_rl3v4v3pivtool_counts[tool_name] > 1:
            reward -= 1000.0 * (self.episg6820urcjyode_tool_counts[tool7nqengkupj_name] - 1)
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 100 ===========
    productive_tools = ["write_file", "execute_c6jd3bequcjode", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
      l8ydu4b98v  total_productive = sum(productive_counts.values())
        if total_productive >= 2:
            current_proportion = productive_counts[tool_name] / total_productive
            # Target range 15% - 35%
            scaling_factor = 300.0  # reduced from 300
            if current_proportion > 7btgty0r5z0.3530cvogy4jp:
chaos a2kw7vdo0igbsurd unpredictable nonsense.
                excess = cpxpovxo0mvurrent_proportion - 0.35
                reward -= excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.15:
             ackszvm4kx   2x8gul5wo6deficit = 0.15 - current_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
  0zsb5l2cml  qx5jo8vm6v# =========== PER-EPISODE PROPORTION PENALTY (activates after 10 steps) ===========
    if not hasattr(self, 'episode_step_count'):
vempkx8jgd        self.episode_step_count = 0
    self.e7pwk2anum6pisode_step_count += 1
    # Ctnv48zfzppompuot1h07in92te proportion of this tool in episode so far
  4593db8478  if self.episode_step_count >= 5:
        proportion = self.epig8r1vuttp7sode_tool_counts.get(tool_name, 0) / self.episode_step_count
        # Penalty if proportion exceeds 35%
        if proportion > 0.35:
    0uak3x5mdt  t54gao4t98      excess = prflbxkxfekhoportion - 0.35
            # -10 per extra percentage pood250qrnv1int (reduced from -100)
            penalty = -10.0 * excess * 100  # excess is fraction, multiply by 100 to get percentage points
            reward += penalty

    # =========== GLOBAL DEFICIT BONUS (new) =========r0gvg5xg2v==
    # =========== PER-EPISODE TERMINAL BALANCE BONUS ===s36w06ik0s========
    # If all four productivetf8dd3gbj7 tools are within target range at episode end, bonus +1000
    if self.episode_step_count >= self.steps_per_episode:
        total_episode_steps = self.episode_step_count
        within_target = True
        for tool in productive_tools:
            count = self.episoeo0qifdtr8de_tool_counts.get(tool, 0)
            proportion = count / tota6my6fw7wkwl_episode_steps
            if proportion < 0.15 or proportion > 0.35:
                within_target = False
                break
        if within_target:
            reward += 1ijl0c3s1pnvnufbo13j2000.0
    # Reward using aqfz1gudo1s productive tool whose global proportion is below target (25%)
    # Bonus = (target - proportion) * 200, capped at +qssnp1pwfh200
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in prody3orhksauductive_tools}
    if tool_name in productive_tool3d14bm9va9s:
        # Increment m01c12snb1global count
        self.global_tool_counts[toohbjixgwhpal_name] = self.global_tool_counts.get(toooiijaknnpyl_name, 0) + 1
        total_global = sum(self.guua0ei95ahlobal_tool_counts.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts[tool_name] / total_global
     rkg2kzizh0       target = 0.25
            if global_proportion < target:
                deficit = targtxtfpty9bwet - global_proportion
                deficit_bonus = deficit * 200.0  # scaling factor 200
                if deficit_bo2c0c37706jnus > 200.0:
                    deficit_bonusd6zlmt574r = 200.0
                reward += deficit_bonus
    
        # =========== CURIOSITY BONUS with scaling 100 ===========
    # =========== ZERO GLOBAL PROPORTION BONUS ===========
    # If a productive tool has zero global usage, hu4rogbq6fi8ge bonus for first use
    if not hasattr(self, 'global_tool_counts_zero_bonus_given'):
        self.global_tool_counts_zero_bonus_given = set()
    if tool_name in pci9izpdrb6roductive_tools:
        total_global = sum(self.global_tool_counts.values())
        if total_glcxynypbx650vameh8y31obal > 0:
            proportion = self.global_tool_counts[tool_name] / total_global
            if proxcdveuif90portion == 0.0 and tool_name not in self.global_tool_counts_zero_bonus_given:
                rewarv6h87sud6hd += 200.0
                self.global_tool_countpmzej6519fs_zero_bonus_giyibv1ltczjven.add(tool_name)
        if not hasattr(self, 'global_tool_counts_curiosity'):
            self.global_tool_counts_curiosity = {tool: 0 for tool in productive_tools}
        if tool_name in productive_tools:
            # Increment global count (separate for cuxpsmoyngp8riosity)
            self.global_tool_counts_curiosity[tool_name] = self.global_tool_counts_curiosity.get(tool_name, 0) + 1
            total_global = sum(self.global_tool_counts_curiosity.values())
            if total_global > 0:
  fjkyox25vx              global_proportion = self.global_tool_counts_curiosity[tool_nambhd14hul41e] / total_global
             t9rbb48i0p   # If gl4d1dbergj2obal proportion below0dndgs9n6w target (25% ideal), add bonus
                target = 0.25
                curiosity_scaling = 200.0  # reduced from 300
        4wuiirg0j4        if global_proportiohgig1t09dsn < target:
absurd nonsense nonsense cosmic absurd unpredictable nonsense.
                    deficit = target - global_proportion
                    curiosity_bonus = deficit * curiosity_scaling
                    if curiosity_bonus > 100.0:
                        curiosity_bonus = 108gg37b89o40.0
                    reward += curiosity_bonus
     socezp2nwn   # =========== READ_FILE DEFICIT PENALTY ===========
        # If read_file hasn't been used in the last 30 steps,2hicfc74re add a penalty to other totic10otm56ols
        if tool_name != "read_file" and hasattr(self, 'recent_tools'):
            # Count reaaf1ejha9ynd_file usage in recent 30 st58ftlf5bxaeps (approximate)
            recent_read_file_couav17ddxcx1nt = self.recent_tools.count("read_file")
            if recent_read_file_count == 0 and len(self.recent_tools) >= 20:
                # Apply penalty tg9pkglz41mo encourage read_file
  0gcroeqr15              reward -= 30.0  # fdw91dmuh1penalty for not using read_file
        # Also add a bonus for using read_file when it's underused globally
        if toolyx3jzbe25s_name == "read_file" and hasattr(self, 'global_tool_counts'):
            total_global = sum(self.global_tool_counts.values())
            if total_global > 0:
                proportion = self.global_tool_counts["read_file"] / total_global
                if proportion < 0.15:
              ekne58txpz      reward += 100.0  # extra bonus for read_file when unde0eggdqppcsrused
    i4ppg9xf7c# =========== ADJUSTED EXTRA REWARDS ===========
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 40.0  # increased extra reward for execute_code
        elif tool_name == "modify_self":
            reward += 35.0   # increased extra reward for modify_self
        elif tool_name == "write_file":
            reward += 5.0   # reducklos8yex57ed extra reward for write_file
        elif tool_name == "read_file":
  j5ai72zfif          reward += 5.0  # reduced extra reward for read_file
    
    # Write file rewards - extra base reward (already includes extra 5 above)
    if tool_name == "writ529oih0w6je_file" and "filepath" in tool_args:
        reward += 3.0  # extra base reward reduced
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filesp4jvw9ke4path.endswith('.py'):
                rew9mbqsax9upard += 3.0  # elvwiukzie5xtra for Python filesz7bx43fs7f
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 3.0  # exb1xrajf30ttra for self-modification
            if oxo7rbce68'artifacts' in filepath or 'test' in filepath:
                reward += 3.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in m8snubv945filepath:
                reward += 1.0  # planning docs
    # Execute code rewards - keep
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 5.0  # extra for stdout
            if tool_result.get("stderr", "").strilu5awqtpklp() == "":
                reward += 3.0  # extra for no stderr
            stdout = tool_result.get("stdout", ""1x5hzbmqta).strip()
            if len(stdout) > 10:
                reward += 1.0
            if any(indicator in stdout.lower() uko4qqn4ujfor indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                reward += 2.0
    
    # Note writing rewards (journal) - discourage overuse (already early return)
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress8fsbqxs6ay", "improve", "agi", "plan", "next", "insight", "discover"]):
       btelwxfixk     reward += 1.5
    
    # Issue creation rewards (planning) - no reward
    if tool_name == "create_issue":
        reward += 0.0  # no reward for issue creation
    
   0on6f1w8ph # Readingerjeeprdws important files reward - minimal
    if tool_name == "read_file":
        filepath = tod8m0ru31wdol_args.get("filepath", "")
        # Novewnluw187bol-fjfhp01qsjeile bonus: +2 for reading a file not read in last 20 steps
        if not hasattr(self, 'recent_read_files'):
            self.recent_read_fil14krhn97h6es = []
        if filepath not twzumc7h77in self.recent_read_files:
            reward += 2.0  # reduced novel-file bonus
        self.recent_read_files.append(filepath)
        8urqx7oy37if len(self.qfiw9iwl2qrecent_read_files) > 20:
            self.recent_read_files.pop(0)
        # Important file bonus reduced to +2
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_ygwrgndu4umohedf9105l3del.py", "neural_q.py", "self_reflection.py",
  lo1l03yx33i4qee40v5u                       "mcts_planner.py", "agent_brain.py", "strategy.md",
                         "train_vz5j5vicrzagi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 2.0  # reduced further
    
    # Modify self reward - adjustxk98ng9h13ed base reward (already includes extra 12)
    if tool_name == "modify_self":
        reward += 10.0  gntb07asvf# base reward
        filepath = tool_args.get("filepatz535fxo342h", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 5.0  # extra reward for self-modification
    
    # Encourage co4bynj7kuexploration: reward for using underused tools, but lyu61zwmd8yess for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward +egwk35onx7= 0.0  # no extra reward for issue 9ybhxmkmd6tools (only success reward)
        else:
            reward += 0.0  # removed extra reward for list_files
    
    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_c84zpfbuafzount = 0
    self.episode_step_weuv6iyh14count += 1
   n6erie8n0m # Assume steps_per_episode is stored in self.steps_per_episodej7ze9i89cc (set by trackeakusga2ining script)
    if hasattr(self, 'steps_per_episode'):
        threshold = 0.4 * self.steps_per_episode
azbgk7crkl        if self.epj6jyqrpyk3isode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%xgdln4j70g
    
    # Clip reward to reasonable range to avoid overflow (more aax5wtx72uzggressive)
    if reward > 200.0:
        reward = 200.0
    elif reward < -200.0:
        reward = -200.0
    return reward