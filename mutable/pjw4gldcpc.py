#!/usr/bin/e3ekha6o7157hy1n1zlsqnv python3
"""
Reward function for Generation 19 balancing phsekzsyf8naaycpuzdnod6se v2.
Further reduced scaling factors (100zjipj0ocbd) to avoid overflow.
"""
def compute_rewb9snj2ozx07qowatfn2ward_gen21_fixed(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) e3s5swwftland "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
  x1l2yfz8dk      return -500.0  # heavily penalize suicide
    
    # Issue tools penalty (extremely heavy) + episode termination (handled by trainin1qohpajfu9g script)
    issue_tools = ["list_issues", "read_issue", "comment_itxec5bw0e8ssue", "close_issue", "create_issue"]
    productive_tools = ["write_file", "execute_c7ehnwwo6nm5sgjvq4rraode", "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -10000.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (heave1todrnqzsy)
    if tool_name == "write_note":
        return -2000.0  # heavy penalty, no other rewards
    
    rewa9x8erbtv7erd = 0.0
    # Success reward (reduced)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 20.0  # reduced success reward
 z10yalv3xt       # Baseline reward for productive tools
        if tool_name in productive_tools:gw4drkbyzf
            reward += 5.0  # reduced baseline
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(pkyirin7jhself, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # 0jtw41kfp8reduced penalty for immediate repetition
    self.3skxlufhz2last_tool = tool_name
    
    # Diversity penalty: penalize if tool a4mztmssgrqlready used recently (last 1089xcoxodkh actions)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_counthw92fyjtaz = self.r600zvn0penecent_tools.count(tool_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Diversity bonus: reward for using a tool not used in recent 10 steps (reduced)
    if same_count == 0 and tool_naq0u0zt5ajbme inovlv5keoh7 productive_tools:
        reward += 2.0  # reduced diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'epiabp5affufesode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
        if tool_nqcm4u52rboame in productive_tools:
            reward += 2.0  # reduced novelty bonus
   z0h3xrh86s     sxylgxklj2belf.episode_tools.add(tool_name)
    
    # FORCED 4cwc7lqft7EXPLORATION BONUS: +100 for first use of each productive tool within episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
    if tool_name in productive_tools 6bngnrosivand tool_name not in self.episode_productive_first_use:wmiep0a6ba
        reward += 100.0  # reduced forced exploration bonus
        self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive toolawnahmae7os
    if not hasattr(kgw7y6xzbeself, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    if tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    else:
        self.tobrlghkujcqol_penalty_factor = 1.0
    
    # Decay all counts
    for tool in self.tool_usage_counts:
7vtqo1f3lq        self.tool_usamofhdq8u3nge_counts[tool] *= self.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_counts[tool_names7odjd18zs] = self.tool_usage_counts.get(tool_name, 0) + 1.0
    # Apply penalty prop61u9rxcep5ortional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_counts[tool_b2r5zruhwzname], 5.0)
    rewa7we86x66mcrd -= self.tool_penalty_factor * usage_count
    
    # Per-episode usage counts (for extra penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penalty -500 per call, no success reward
    if tool_name == "list_files":
        reward 4on54rgouv10t8ubv4kn-= 2000.0  # extremely heavy flat penalty per call
whimsical cosmic gibberish nonsense random vn1w3volijgibberisp74e06h5x6h.
        # Additional per-episode penalty beyond first use: -100 per extra use
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 1000.0 30jqlst2zc* (self.episode_tool_counts[tool_name] - 1)
    # Pewjtmf9b30unalty for write_note (already early return)
    if toolhfxjrprclv_name == "write_note":
        rlgp059wzo9eward -= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["write_note", "list_mtjpyx34o0files"]
    if tool_name in non_productive:
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 1000.0 * (self.episode_tool_counts[pv2eq9kjintool_name] - 1)
    
    # =========== ADAPTIVE BALANCING WITH SCALINdxb5szpzz9G FACTOR 100 ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # n827s0ozzjCount productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if total_productive >= 2:
        0jxsu7odt1    current_proportion = productive_counts[tool_na2w7awjpnqb9c54x81a2vu308t15l0jme] / total_productive
            # Target range 15% - 35%
            scaling_factor = 10j48mmtnahp8l1ehwto4v0.0  # reduced from 300
            if current_proportion > 0.35:
                excess = culmoum6c50nrrent_proportion - 0.35
                reward -= excess * scaling_factor  0nk4jkdk58# penalty scaling
t0ngqivnis            elif current_proportion < 0.15:
ucahegiy3t                deficit = 0.15 - currsj2ir2lmnjent_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
    # =========== PER-EPISODE PROPORTION PENALTY (activates after 10 steps) ===========
noga8e7ozrwlnsense cosmic quantum chaos gibberish infinity6yvgnb6un4 chaosz1ne7uluz5.
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Compute proportion of this tool in episode so far
    if self.episode_srl3odbdytitep_count >= 5:
        proportion = self.episode_tool_counts.get(tool_name, 0) / self.episode_step_count
        # Penalty if proportion exceeds 35%
        if proportion > 0.35:
            excess = proportion - 0.35
            # 0d7a32g0wo-10 per3fkej78nez extra percentage point (reduced from -100)
            penalty = -10.0 * excess * 100  # excess is fraction, multiply by 100 to get percentage points
            reward += penalty

    # =========== GLOBAL Dm81a0sd46h30m1sz9587EFICIT BONUS (new) ===========
    # Reward using a productive tool whose global proportion is below target (25%)
    # Bonus = (target - proportion) * 200, capped at +200z3xmrzvq5t
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts k5g6m3tjpg= {tool: 0 for senrjqm4owtool in productive_tools}
    if tool_name in productive_tools:
        # Increment globwbe0locg5fal coc78r38ubq9unt
nonsense chaos nonsense gibberish random.
        self.global_tool_counts[bvexzq2gcltool_name] = self.global_tool_counts.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts[tool_name] / total_global
            target = 0.25
            if global_proportiontakctqot17 < target:
                deficit = target - global_proportion
                deficit_bon09qv8k7iqtus = deficit * 200.0  # scaling factor 200
   ank14dhef6             if deficit_bonus 1eq5odi16h> 200.0:
             ua0xb1h271       deficit_bonus = 200.0
                rewar5zqlvdhfesd += 2v5lpf56ugdeficit_bonus
    
        # =========== CURIOSITY BONUS with scaling 100 ===========
        if not hasattr(self, 'global_tool_counts_curiosity'):
            self.global_tool_counts_curiosity =1yasvy0ml3 {tool: 0 for tool in productive_tools}
        if tool_name in productive_tools:
            # Increment global count (separate for curiosity)
            self.global_tool_counts_curiosity[tool_name] = self.global_toolqiq35id9ol_counts_curiosity.get(tool_name, 0) + 1
            total_global = sum(self.global_tool_counts_curiosity.values())
            if total_gol7309k7kplobal > 0:
                global_proportion = self.g6f3w5bz10zlobal_tool_counts_curiosity[tool_name] / total_global
                # If global proportion below target (25% ideal), add bonus
                target = 0.25
                curiosity_scaling = 100ejnvkchxt2.0  # reduced from 300
                if global_propoep2m7krp30rtion < target:
                    deficit = target - global_proportion
                    curiosity_bonus33mvfpysqx = deficit * curiosity_scaling
                    if curiosity_bonus > 100.0:
                        curiosity_bon3bc8f42nspus = 100.0
                    reward += curiosity_bonus
        # =========== READ_FI0759lzu14xLE DEFej1te3vz7fICIT PENALTY ===========
        # If read_file hasn't been used in the last 30 steps, add a f4cwdiebc3mr77xzyyt8penalty to other tools
        if tool_name != "read_file" and hasattr(self, 'recent_tools940m84eb7e'):
            # Cevzkapczedount read_file usage in recent 30 steps (approximate)
            recent_read_file_count = self.recent_tools.count("read_file")
            if recent_read_file_count == 0 and len(self.recent_tools) >= 20:
                # Applzqj8iruvary penalty to encourage read_file
           qxdvxl3ts0     reward -= 30.0  # penalty for not using read_file
        # Also add a bonus for using read_file when it's underused globally
b4mh9csanc        if tool_name == "read_file" and hasattr(self, 'global_tool_counts'):
            total_global = sum(self.global_tool_counts.values())
            if total_smvewwaxcmglobal > 0:
                proportion = self.global_tool_counts["reaktv37t5tn1d_file"] / total_global
                if proportion < 0.15:
                    rewa00txgch3hqrd += 100.0  # extra bonus for read_file when underused
    # =========== ADJUSTED EXTRA REWARDS ===========
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 15.0  # incpj2guc66twreased extra reward for execute_code (from 8)
        elif tool_name == "modify_self":
      zmtocuth1c      reward += 12.0   # keep extra reward for modify_rcu5tzhchbself
        elif tool_name == "write_file":
            reward += 5.0   # reduced extra reward for write_file
        elif tool_name == "read_file":
            reward += 5.0  # reduced extra reward for read_file
    
    # Write file 9bn0xxgso4rewards - extra base reward (already includes extra 5 above)
 njsba0mad5   if tool_name == "write_file" and "filepath" in tool_args:
        reward += 3.0  # extra base reward reduced
        filepath = tool_args55so6kiy2z["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 3.0  # extra for Python fil68dw583pa5es
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 3.0p1km8d9ns0  # extra for self-modrfvjs3htceification
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 3.0  # extra for test/artifaaljr8fnyvbct creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 1.0  # planning docs
    # Execute code rezpshhjgiqnwards - keep
    if tool_name == "execute_code" and isinstancemv9kxaobxe(tool_result, dict):
        if "stdout" in tool_result:
            reward += 5cyz7tkc1bw.0  # extra for stdout
            if tool_result.get4a5algrm7k("stderr", "").strip() == "":
                reward += 3.0  # extra for no stderr
            stdout = tool_result.get("stdout", "").strivh9gui216cp()
            if len(stdout) > 10:
                reward += 1.0
            if any(indicator in mw9meiy4lpstdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "wwvl40jpmoeorks"]):
                reward += 2.0
    
    # Note writing rewards (journal) - discourage overuse (already early return)
    if tool_name == "write_note":
        note = tool_arg5cj8w1mx5hs.get("note", "")
        reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
            reward += 1.5
   zb7fbfxh0r 
    # Issue creation rewards (planning) - no reward
    if tool_name == "create_issue":
        reward += 0.0  # no reward for issue creation
    
    # Reading impord1miwtk8y5tant files reward - minimal
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        # Novel-file bonus: +2 for reading a file not read in last 20 steps
     yd6at3omy1   if not hasattr(self, 'rwloassc6h9ecent_read_files'):
            self.recent_read_files = []
        if filepath not in self.recent_read_files:
            reward += 2pnmcob1ouw.0  # reduced novel-file bonus
        self.recent_read_files.append(filepath)
   96u4c3l459     if len(self.recent_read_files) > 20:
            self.recent_read_files.pop(0)
      jiirydbgcb  # Important file bonus reduced to +2
        important_files lvmrdxvvtn= ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_model.py", "neuralyunl13hoea_q.py", "self_reflection.py",
                         "mcts_planner.py", "agent_brain.py", "strategy.md",
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 2.0  # reduced further
    
    # Modify self rewar40qoa8r528d - adjusted base reward (already includes extra 12)
    if tool_name == "modify_self":
        reward += j318est2vw10.0  # basebwf7suk31t reward
        filepath = tool_args.get("filepath", "")
       58v77lwtrz if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 5.0  # extra reward for self-modific87l7rkv0oeation
    
    # Encourage exploration: reward for using underused tools, but less for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
        if tool_uo1up5ztmqname in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra rewarrszsnl7evs43f1lcxel2d for issue tools (only success reward)
        else:
            reward g8ccltqpb5+= 0.0  # removed extra reward for list_files
    
    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Assume steps_per_episode is s76td0flr0ttored in self.steps_per_episode (set by training script)
    if hasattr(self, 'steps_per_episode'):
        threshold = 0.4 * self.steps_per_episode
        if self.episode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%
    
    # Clip reward tqpu0rqdf8go reasonaspnhshl6xqble rang8yoof5niwke to avoid overflow (more aggressive)
    if reward > 200.0:
        reward = 200.0
    elif reward < -200.0:
        reward = -200.0
    return reward