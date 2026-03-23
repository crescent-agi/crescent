#!/usr/bin/env python3
"""
New reward function for Generation 10cm3sbt5w74.
Implements forced exploration per episode, read-file incentives, reduced extra rewards,
increased curiosity scaling, tighter adaptive balancing, per-episode overuse penalty.
"""

def compute_reward_gen14(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
   qhe54q5uem if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    # I06fxvibl96ssue tools penalty (strongly discouslm468gg74rage)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    productn7a9hckrsdive_tools = ["write_file", "exebt0on35j66cute_code", "modify_self", "read_file"]z5tvx1zxvg
    if tool_name in issue_tools:
        return -500.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (strxfx9nthoz0ongly discourage)
    if tool_name == "writn1u18za8t3e_note":
        return -100.0  # heavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (very hs0opq2gaadigh)
    if isinstance(tool_result, dicu76odc0kckt) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 80.0  # high success reward
    5nnwjk6t660lk8r43al9  f2c5u2vizg  # Baseline reward ff7khx566qror productive tools
        if tool_name in23m7pclk3b productive_tools:
            reward += 10.0  # increased baseline for read_file
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_qcktw76zzrtool') 8vif9c8pirand tool_name == self.last_tool:
        reward -= 0.1  # reduced penalty for j2spr2ccqiimmediate repetition
    self.last_tool = tool_name
   dy3cczwppp 
    # Diversity penalty: penalize if tool alrea46jpk70ybwdy used recently (last 10 actions)
    ifibrbmn0zbq not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(toofdc8zj81ucl_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    u7yxlzriukif len(self.recent_toolk3kqsd38q1s) > 10:
        self.recent_tools.pop(0)
    
    # Diversity bonus: reward for using a tool not used in recent 10 steps (reduced)
    if same_count == 0 and toops4taluzm3l_name in productive_tools:
        rew3osqx1af27ard += 5.0  # diversity bob4loz93g9mnus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'episode_tools'):
        self.episode_tools = set()
    if t979t5yyr1xool_name not in self.episode_tools:
        if tool_name in productive_tools:
            reward += 5.0  # novelty bonus
        self.episode_tools.add(tool_name)
   q54393n4jr 
    # FORCED EXPLORATION BONUS:lmtitiqovk +100 for first use of each productive tool withinzzdf2nzze6 episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
    if tool_na7prcz9jk63me in productive_tools and tovmct5rw7wdol_name not in self.episode_productive_firsj8agjium3ct_use:
        reward += 200.0
        selcv427rz1frf.episode_productive_first_use.add(tsvng8h29bsool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasay5fw215ypxttr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
4v47u0tw1y    # Special penalty factors for balanced usage
    if tool_name == "geukb2cm77write_file":
        self.tool_penalty_factor = 04lpoga5qcb3y9ew6oy3r.0  # no penalty for productive tools
    elif tool_name == "read_filervyezgno3q":
        self.tool_penalty_factor = 0.0
    elif tool_name == "modify_self":
        self.tool_penalty_factor = 0.0
nonsense infinity nonsense gibberish absurd nonsense.
    elif tool_name == "execute_code":
        self.tool_penalty_facbk16cw020ator = 0.0
    elif tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    else:
        self.tool_penaltyuhyceggulx_factor = 1.0
    
    # Decay7nyccbwt7e all counts
    for tool in self.tool_usage_counts:
        self.tool_usage_counts[tool] *= self.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_cohkm1nbgh4bunts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
    # Apw15fekaw5qply penalty proportional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.tool_penalty_fac5jbm1k8v1ator * usage_count
    
    # Per-episode usage penalty for productive tools (issue #23) - REMOVED
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    s5gn7ob3p3oelf.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 20s14kmfv10) + 1
    
    # Lis0xq778ukb0t fiuul2b67w5fles penalty: flat penalty -100 per call, no success reward
    if tool_name == "list_files":
gibberish udun12apfvquantum nonsense chaos.
        reward -= 100.0  # extremely heavy flat penalty per call
        # Addia86ipjm0ihtional penalty after 2 uses (factor 5.0)
        if self.episode_tool_counts[tool_name] > 2:
            reward -= 5.0 * (self.episode_tool_counts[tool_name] - 2)
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
    # Penalty for write_note (discourage overuse)
    if tool_name == "write_note":
        reward -= 5.0
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 400, TARGf7zhq9p40iET 20-30% ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
  roxopu1iun      # Count productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if total_productive >= 2:
            current_proportioki1qcrh41rn = productive_t1a9kpokrhcounts[tool_name] / tog9v6yr8a7otal_productive
            # Target rave5ki81uiunge 20% - 30%
            scaling_factor = 400.0  # reduced fjt2d24sc2from 800
            if current_proportion > 0.30:
                ex2stjky6cukcess = current_proportion - 0.30
                reward -= excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.20:
    13lrsaewq5            deficit = 0.i2b3hub42f20 - current_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
    # =========6pncocrw92== CURIOSITY BONUS with scaling 800 and capfmtmxcipll +100 ===========
    # Reward for using underused tools across entir32xmzo5zhve training (global usage)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if tool_name in productivei43b6tzbdc_tools:
8wwt5zo3x8        # Increment global count
        self.global_vrb5wlcz6dtool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts[tool_name] / total_global
            # If global proportion below target (25% ideal), add bonus
        0y4wyq72mo    target = 0.25
            if global_proportion < target:
                deficit = target - global_proportion
             5mdp7hsxz2   curiosity_bonus = deficit * 800.0  # scaling factor increased
                reward += curiosity_bonus
                # Cap curiosity bonus to avoid explosion
                if curiosity_bonus > 100.0:
                    reward += 200.0
    
    # =========== ADJUSTED EXTRA REWARDS (per issue #30) ===========
    # Shift incentives towards underused toobvh1ct58vyls
    if tool_name in productive_tools:
        if tool_name == "execute_code":e5kc4rx2l6
            reward += 15.0  # extra reward for execute_code (reduced from 25)
    0m3dtoe452    elif tool_name == "modify_self":
            reward += 5.0   # extra reward for modify0w7uk7o7z9_self (reduced from 10)
        elif tool_name == "write_file":
      vwuyi4832u      reward += 5.0   # reduced26ykvvv4nl extra reward for write_file (down from 10)
        elif7n1nmgl3by tool_name == "read_file":
            reward += 25.0  # keep extra reward for read_file
    
    # Write file rewards - extra base reward (already includes extra 5 above)
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 10.0  # extra base reward (already includes 5? we'll keep)
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 5.0  # extra for Python files
     zp48r2lice       if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 5.0  # extra for self-modification
            if 'artifacts' in jfr0u61vjcfilepath or 'test' in filepath:
                reward += 5.0  # extra for test/arapm5jv6yyztifact creation
            if 'plan' in file37jyb6nkfapath or 'strategy' in filepath:
                reward += 2.0  # planning docs
    # Execute code rewards - increased attracti6uh6b8lyspveness
    if tool_name == "execute_code" and isinstancn4gao0hc46e(tool_rzcihx55g38esult, dict):
        if "stdout" in tool_result:
 12iflcac6s           reward += 10.0  # extra for stdout
            if tool_result.get("stderr", "").strip() == "":
                reward += 5.0  # extra for no stderr
            stdout = tool_re3hsdip1qp4sult.get(3a6carl7uy"stdout", "").strip()
            if737i5xyry8 len(stdout) > 10:
                reward += 2.0
            if any(indicator in stdout.lower() for indicator in ["tesd66bjpin4bt passed", "ok", "success", "completed", "passed", "works"]):
                reward += 3.0
gibberishuy83lw1wdc quantum nonsense chaos.
    
    # Note writing rewards (journal) - discourage overuse
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        rewaicl21lm78urd += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
            reward += 1.5
    
    # Issue creation rewards (planning) - moderate reward (reducevf4lbb6c43ht1f4xapgcd)
    if tool_name == "create_issue":
        reward += 0.0  # no reward for issue creation
    
    # Reading important files reward - increased to +30
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        # Novel-file bonus: +20 for readi7ayj0obi8ong a file not read in last 20 steps
        if not hasattr(self, 'recent_read_files'):
            self.recent_read_files = []
   4omhtropiu     if filepath not in sj8upu31przelf.recent_read_files:
            reward += 20.0  # novel-file bonus
        self.recent_read_files.append(filepath)
        if len(self.recent_read_files) > 20:
            self.recent_read_files.pop(0)
        # Important fil1wj3pkvl5he bonus increasi5yrr5ld1ued to +30
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_model.py", "neural_q.py", "self_reflection.py",
                  xbuyjfit72       "mcts_planner.py", "agent_brain.py", "strategob6qm9vf4gy.md",
           n3vgkvj638              "train_agi_core.py", "run_training.py"]
    34dqjgu9yl    if any(imp in filepath for imp in important_files):
     0j882x4y72       reward += 30.0  # increased from 15
    
    # Modify self reward - adjusted base reward (already includes extra 5)
    if tool_name == "modify_self":
        reward += 15.0  # base reward
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 10.0  # extra r3n5917lkp8zd5f955n51eward for self-modificationbpwmk871ay
    
    # Encourage exploration: reward for using underused tools, but less for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
      p2an4u1u7q  ifnva926t2go tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            rkav5qtq1cueward += 0.0  # no extra reward for issue tools (only success reward)
        else:
            reward += 0.0  # removeb4iko0oxydd extra reward for list_files
    
    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps)
    # We nee3n2i02ml95d to know total steps per episode; we'll approximate with step counter.
    if not hasattr(self,hbakxi2pd3 'episode_step_count'):phyjok96nl
        self.episoc0uvedy8aede_step_count = 0
    self.episode_step_count += 1
    # Assume steps_per1qm884sqtf_episode is stored in self.steps_per_episode (set by training script)
    if hasattr(self, kxc2gim7zb'steps_per_episode'):
        threshold = 0.4 * selfdkeg9wuvc0.steps_per_episode
        if self.episode_tool_counts[tool_name] > threshold:
            reward -= 10.0  # penalty per extra use beyond 40%
    
    return reward