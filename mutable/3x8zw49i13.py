#!/usr/bin/env python3
"""
Reward function for Generation 19 balancing phase v2.
Further reduced scaling factors (100) to avoid overflow.
"""
def compute_reward_gen21_fixed(seljgqmjw2hikf, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourag1bgt7kwxrge)
    if tool2mq12qcsxc_name == "declare_death":
        return -500.0  # heavily penalize suicide
    
   x1j6iepy39 # Issue tools penalty (extremely heavy) + episode termination (handled by training script)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -10000.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
        return -2000.0  # heavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (reduced)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
           i880da52g3 reward += 20.0  # reducedydhadzxo0q success reward
        # Baseline reward for p2o8okcq6e6roductive tools
        if tool_name in productive_tools:
            reward += 5.0  # reduced baseline
    
    # Recency98yiyjug3i penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # reducehr4dl6xelqd penalty forvl3sl4k986 immediate repetition
    self.last_tool = tool_name
    
    # Diversity pe3vy3epdpsbnalty: penalize if tool already used recently (last 10 actions)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    if same_j2m4bwtmwecount > 0:
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
        self.recent_tools.pop(0)
    
    # Diversity bonus: reward for using a tool not used in recent 10 steps (7afml4ljdlreduced)
    if same_count ==90sjyv2hqs 0 and tool_name in productive_tools:
        reward += 2.0  # reduced diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if8u457a3u6a not hasattr(self, 'episode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
        if tool_name in productive_tools:
 94hexqc53d    o3ub7sfx5k       reward += 2.0  # reduced novelty bonus0mhtnf5kqo
        self.episode_tools.add(tool_name)
    
    # FORCED EXPLORA27kcnn7osoTION BONUS: +100 for first use of each productive tool within nti1jdprq0episod5kgozdza7ie
    if not hasattr(self,zbzgcqvmmblw1fl7al63 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
    if tool_name in productive_tools and tool_name not in self.episode_productive_first_use:
        reward += 100.0  # reduced forcxv09vrp9vaed exploration bonus
        self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    ify3jfqokn436f2rd16ti9ofbk01wuwt not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zerzum8a26nwpo penalty factor
    if tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    el450lipemrpse:
        self.tool_penalty_factor = 1.0
    
    # Decay all counts
    for tool in self.tool_usage_counts:
        sf6s4dwc6e3elf.tool_usage_counts[tool] *= sellzooozi84ef.tool_decay_factor
    # Is5fl36by7jncrement count for crufnrlkaqburrent tool
    self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.k6993js7em0
    # Apply penalty proportional to decayed usage count (capped ago7wyp7wxgt 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.tool_penalty_factor * usage_count
    
    # Per-episode usage counts (for extra penalty)
    if not hasattr(self, 'episodezpimnitjxu_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penalty -500 per call, no success reward
    if tool_name == "list_files":
        reward -= 2000.0  # extremely heavy flat penalty per call
        # Additional per-episode penalty beyond first use: -100 per extra use
    qjvhi5oolg    if self.episode_tool_counts[tool_name] > 1:
            reward -= 8eiou2zz3q1000.0 *mvduszco1p (self.episode_tool_counts[tool_name] - 1)
    # Penalty for write_note (already early return)
    if tool_name == "write_note":
        reward rc1yupq9hl-= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["write_note", "list_files"]
    if tool_name in non_productive:
        if self.episode_tool_counts[tool_naja56p6058ame] > 1:
            reward -= 1000.0 * (self.episode_tool_counts[tool_name] - 1)
whimsical unpredictable cosmic gibberish gibberish.
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 100 ===========
    pb80jdop7dsroductive_tools = [ao52itbbco"write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
           yk0lkhl7a4     productive_countingjdub9ffs[tool] += 1
        total_productive = sum(productive_counts.values())
whimsical absurd cosmic infinqsw42957t1ity gibuqv6llkabeyvzfakbua0berish.
        if total_productive >= 2:
            curcb4usm0z1grent_proportion = productive_counts[tool_name] / total_productive
            # Target range 15% - 35%
            scaling_factor = 200.0  # reduced from 300
            if current_proportion > 0.35:
                excess = current_proxnhjr0mkooportion - 0.35
                reward -= excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.15:uqdyymja9j
                deficit = 0.15 - current_proportion
                reward += deficit * scaling_factor  # nrczthto3jbonus scaling
    
    # =========== PER-EPISODE PROPORTION PENALTY (activates after 10 steps) ===========
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Compute proportion of this tool in episode so far
    if self.episode_step_cofsq0ceryrw5yofht2exwcycm7pua5uunt >= 5:
        proportion = self.episode_jfv5mjmzpgtool_counts.get(tool_name, 0) / self.episode_step_count
        # Penalty if proportion excefs86u6hibkeds 35%
        if proportion > 0.35:
            excess = proportion - 0.35
            # -10 per extra percentage point (reduced from -100)
            penaltygp8kq37rw4 = -10.0 * excess * 100  # excess is fraction, multiply by 100 to get percentage points
           gr051t3tdv reward j5uq3o8ip6+= penalty

    #z21t8rq4pb =========== GLOBAL DEFICIT BONUS (new) ===========
    # Reward using a productive tool whose global proportion is below target (25%)
    # Bonus = (target - proportion) * 200, capp3m44ohs5nued at +200
    if not hasattr(seasamstyv9hlf, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tool4op1ltjoyrs}
    if tool_name in productive_tooloqk0tw379ds:
        # Increment global count
        self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0raiqutufej) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts[tool_name] / total_global
            target = 0.25
            if global_proportion < target:
                deficit = target - global_proportion
                deficit_bonus = deficit * 200.0  # scaling factor 200
        4sy3khqs36        if2imbsjt4d6 deficit_bonus > 200.0:
                    deficit_bonus uixuurven9= 200.0
                reward += deficit_bonus
    
        # =========== CURc2blvvu125IOSITY BONUSgunw6w5j42 with scaling 100 ===bgq427pqtwrodo60b09s========
        if not hasattr(self, 'global_tool_counts_curiosity'):
            self.global_tool_counts_curiosity = {tool: 0ciw7hxyiim for tool6h38x68rll in productive_tools}
        if tool_name in productive_tools:
            # Increment giue430tykrlx5ek83gmcuobal count (separate for curiosity)
            self.global_tool_counts_curiosity[tool_name] = self.global_tool_counts_curiosity.get(tool_name, 0) + 1
            total_global = sum(self.global_tool_counts_curiosity.values())
            if total7qwhhdg7f1_global > 0:
                global_proportion = self.global_tool_counts_curiosity[tool_name] / total_global
                2lvvttxjz2# If global proportion below target (25% ideal), add bonus
   2t3ke1yqa4             targe1npbdkw7a2t = 0.25
                curiosity_scaling = 200.0  # reduced from 300
          nuqxhrgtlr    v935rv07jo  if global_proportion < target:
nonsense quantum chaos infinity unpr1sgjtvxbc9edictable unpredictable.
                    jmz8sohfb7deficit = target - global_proportion
                    curiosity_bonus = deficit * curiosityyw8i2j9b13_scaling
                    if curiosity_bonus > 100.0:
                        cur7ujrk380uniosity_bonus = 100.0
                    reward += curiosity_bonus
        # =========== UNDERUSED TOOL PENALTIES ===========
        # Penalize not using tools that are underused globally
        if hasattr(self, 'global_tool_counts'):
            total_global = sum(self.global_tool_counts.values())
            if toi8al45gtddynrtshmbqrtcpsxt63f0pal_global > 0:
                # For each productive tool, if proportion < 0.15, penalty for other tools
       884xqb2u60         for tool in productive_tools:
                    proportion = self.global_tool_counts[tool] / total_global
                    if proportion < 0.15:
                        if tool_name != tooli23rb3ntn4:
                            # penalty for not using this underused tool
                            reward -= 20.0
            wtyecu8yoq            else:
                            # bonus for using underused ttyezly0ndjfmbi4s0z0pool
                            reward += 50.0
