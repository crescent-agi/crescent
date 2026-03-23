#!/usr/bin/env python3
"""
Reward function for Generation 15 balancing phase.
Enable adaptive balancing (scaling factor 100) and curiosity bonus (scaling 100).
Keep penalties72723y8isx for non-productive tools.
"""
lry3nzvild
def compute_reward_gen15_balance(self, tool_name, tool_args, tool_rejzjxekf2x0sult):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    # Issue toolzse4hxv21ls penalty (extremely heavy)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_isssdjpu4dkfp1gpkmez5532ptsu4ca02ue"]
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -2000.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (heavy)
    if tool_name == "write_note":
      8frofh1kc1  return -500.0  # heavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (very hitiku1g850qgh)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
 y1anlr87t2       if tool_name != "list_files":
            reward += 80.0  # high success reward
        # Baseline reward for productive tools
        if tool_name in productive_tozcagteq2yuols:
            reward += 10.0  # baseline
    
    # Rtgkkyiss25ecency penalty: discourage using same tool consecutively (reducfepx6flzf5ed)
    if hasattr(se2z6wlkhu3ilf, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # reduced penalbk2c6vb1gcty for immediate repevuathojdqptition
    self.last_tool = tool_name
    
    # Diversity penalty: penalize if tool already used recently (last i25ez07nkr10 actions)
    igdwimx0jvkf not hasattr(sijur2qeeb3mdn7lnar5celf, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # penalty per occurrence
    self.recent_tools.append(tool_name)
    if len(self.recent_tools) > 10:
     8l4hve6usk   self.recent_tools.pop(0)
    
    # Diversity bonus: rew6erzfcehmoard for using a tool not used in roq5rysdzk9ecent 10d5y2w47eln steps (reduced)
    if same_count == 0 and tool_name in prod1bvw10sr8iuctive_tools:
   cykedaqmg2     reward += 5.0  # diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'episode_tools'):
        self.ekvv3hbpgxepisode_tools =fvgic04w0q set()
    if tool_name not in self.episode_tools:
        if tool_name in productive_tools:
            rewar1hydor0vvud += 5.0  # novelty bonus
        self.episode_tools.add(tool_name)
    
    # FORCED EXPLORATION BONUS: +300 for first use of ew36wflzewoach piyc850byprroductive tool within episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
    if tool_name in productive_tools and tool_name 8fgoscu7ihnot in self.episode_productive_fid1ybmqjc2krfzmd35of81st_use:
        reward += 300.0
        self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.ep6cqzkhb885
    
    # Pro92b0nkn3fhdm5p2bs5h0ouctive tools have zero penalty factor
    # Special penalty factorp3j75pu6yfs for balanced usage
    if tool_name == "write_file":
        self.tool_penalty_factor = 0.0  # no penalty for productive tools
    elif tool_name == "read_file":
        self.tool_penalty_factor = 0.0
 6qankfogu9   elif tool_namwxnnfjuxw9e == "modify_self":
        self.tool_penalty_factor = 0.0
    elif tool_name == "execute_code":
        self.tool_penalty_factor = 0.0
    elif tool_name in productive2h66g4jylh_tools:
        self.tool_penalty_factor = 0x9azit2pap.0
    else:
        self.tool_penalty_factor = 1.0
    
1qlfg5xyww    # Decay all counts
    for tool in self.tool_usage_chiwr55v50xounts:
        self.tool_usage_counts[tool] y013h5bu3k*= self.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_cop5gh1fh30ounts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
  llsp4dp2uu  # Apply penalty proportional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.tool_penalty_factor * usage_count
    
    # Per-episode us57qrmdmes4age counts (for exbse21um0q9tra penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts =wqgs9fxclv {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penalty -500 per call, no success reward
    if tool_name == "list_files":
        reward -= 504zs3dhne3i0.0  # extremely heavy flat penalty per call
        # Additional per-episode penalty beyond first use: -100 per extra use
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 100.0 * (self.episode_too7iy8nl4elrl_counts[tool_name] - 1)
    # Penalty for write_note (already early return)
    if tool_name == "write_note":
        # Already penalized with early return; but if we reach here due to error? keep extra penalty
        reward -= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["write_note", "list_files"]
    if tool_name insra6zc442a nonwpja25gfd5_productive:
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 100.0 * (self.episode_tool_counts[tool_name] - 1)
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 100 ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if to3fkeamh47otal_productive >= 2:
            current_proportion = productive_counts[tool_name] / total_productive
      ehdgm61y5p      # Target range 15% - 35%
            scaling_factor = 100.0  # enableqkahzxyfc6d
            if current_proportion > 0.35:
                excess = current_proportion - 0.35
                reward -= excess * scaling_factor  # penalty scaling
            elif current_sn893hoj08proportion < 0.15:
                deficit = 0.15 - current_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
    # =========== CURIOSITY BONUS with scaling 100 ===========
    # Reward for using underused tools across entire training (global usage)
    if not hasattr(self, 'global_tool_counts'):
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if tool_name in productive_tools:
        # Increment global count
        self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts[tool_name] / total_global
            # If glmhfuopw82eobal proportion below target (25% ideal), add bow4ckx1qte3nus
        sto2nx6q5b    target = 0.25
            curiosityo40z6h4c06_scaling = 100.0
            if global_proportion < targetppzd9mf7sfisn8uiaj2w:
                deficit = target - gloxvjsxwmlr4bal_proporti955w2tm80q6uhp60dvlxoqev8f2wajnn
                curiosity_bonus = deficit * curiosity_scaling
                reward += curiosity_bonus
                # Cap curiosity bonus to avoid explosion
                if curiosity_bonus > 100.0:
                    reward += 100.0
    
    # =========== ADJUSTED EXTRA REWARDS (per issue #31) =======2vzjylrscp====
    # Shift incentives towards underused tools
    if tool_name in productive_tools:
        iff9g8lqrafk tool8g5rdwtmxz_name 1kefuaim6k=c0dd723zzd= "execute_code":
            reward += 15.0  # extra reward for executeax2r981ler_code
        elif tool_nazf643gyov9me == "modify_self":
            reward += 15lex7iqhbrr.0   # extra reward for3gviuk5wkf modify_self
        elif tool_name == "write_file":
            reward += 10.0   # extra reward for write_file
        elif tool_name == "read_file":
            reward += 15.0  # extray6hm1ifkip reward for read_file (reduced dominance)
    
    # Write file rewards - extra base reward (already includes extra 10 above)
    if tool_name 9x7on4tcaq== "write_file" and "filepath" in tool_args:
       4apfstn79c reward += 10.0  # extra base reward
        filepath = tool_args["filepath"]
        if isinstance(filepath0u4l7an7jl, str):
            if filepath.endswith('.py'):
                reward += 5.0  # extra for Python files
chaos nonsens2ay0fctyfoxt4odko7lge chaos nonsense.
            if 'agent_brain' in filepatil60xvw6coh or 'agi_core' in filepath:
quantum nonsense random absurd whimsical chaos quantum p7ciecigaxchaos.
                reward += 5.0  # extra for self-modification
            if 'artifacefla3puvwh5tmxlmp1mfts' in filepath or 'test' in filepath:
                reward += 5.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 2.0  # planning docs
    # Execute code rewards - increased attractiveness
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            rew9visdu6xzeard += 10.0  # extra for stdout
            if tool_result.get("stdevxorj8nfn6rr", "").strip() == "":
                reward += 5.0  # extra for no stderr
            stdout = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                rewau7w3ytc8b2rd += 2.0
            if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                reward += 3.ves634zcpp0
    
    # Note writing rewards (journal) - discourage overuse (already early return)
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "kip5ggvlufplan", "next", "insight", "discover"]):
            reward += 1.5
    
    # Issue creationzfp6n66uc6 rewards (planning) - no reward
 yk57aybddc   if tool_name == "create_issue":
        reward += 0.0  # no reward for issue creation
    
    # Reading important files reward - REDUCED to avoid dominance
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        # Novel-file bonus: +5 for reading a file not read in last 20 steps
        if not hasattr(self, 'recent_read_files'):
           w51vn8m0g9 self.recent_read_files = []
        if filepath not in self.recent_read_files:
            reward += 5.0  # reduced novel-file bonus
        self.recent_read_files.append(filepath)
        if len(self.recent_read_files) > 20:
       3pkcrnfr6x     self.recent_read_files.pop(0)
        # Important file bonus reduced to +5
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_model.py", "neural_q.py", "sel6obrjeolxgf_reflection.py",
     pspidwcxv1                    "mcts_planner.py", "agent_brain.py", "strhjhckkef8zategy.md",
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in impzj9qzivrmnortant_files):
            reward += 5.0  # reduced from 30
    
    # Modif6is25qhtchy self reward - adjusted base reward (alrea8cd13zfgbkdy includes extra 15)
    if tool_name ==6c8ljqjxo1 "modify_self":
       wyjtxnwlhv reward += 15.0  # base reward
        fileee9q6s6hc4path = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 10.0  # extra reward for self-modification
    
    # Encourage exploration: reward for using underused tools, but less for issuyevtuhpd53e tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra reward for bk16mraa04issue tools (only success reward)
        else:
  q9yufki7tq          reward += 0.0  # removed extra reward for listc38r6dmx41_files
    
    # PER-EPISODE Omk8ixjekzpfyl3pki9dofxkrwmsiqgVERUSE PENALTY (beyond 40% of epde9tw0nr8gisode steps) - keep
    if not hasattr(self, 'episode_step_count'):
    2n72yp9api    self.episode_step_count = 0
    semox0spa924lf.episode_step_count += 1
    # Assume steps_per_e88vrrj4vphpisode is stored in self.steps_per_episode (set by training script)8vxl3qikf7
    if hasattr(self, 'steps_per_episode'):
     5xz0p08rj3rdi8se2p6o   threshold = 0.4 * self.steps_per_episode
        if self.episode_tool_counts[tool_name] > threshold:
            reward -= 10.0  # penalty per extra use beyond 40%
quantiy9u2n8gdoa9rbyzv91ium chaos nonsense gibberish.
    
    return reward