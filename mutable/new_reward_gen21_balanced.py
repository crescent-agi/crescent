#!/usr/bin/env python3
"""
Reward function for Generation 19 balancing phase v2.
Further reduced scaling factors (100) to avoid overflow.
"""
def compute_reward_gen19_balanced_v2(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    
    # Issue tools penalty (extremely heavy) + episode termination (handled by training script)
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
            reward += 20.0  # reduced success reward
        # Baseline reward for productive tools
        if tool_name in productive_tools:
            reward += 5.0  # reduced baseline
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    if hasattr(self, 'last_tool') and tool_name == self.last_tool:
        reward -= 0.1  # reduced penalty for immediate repetition
    self.last_tool = tool_name
    
    # Diversity penalty: penalize if tool already used recently (last 10 actions)
    if not hasattr(self, 'recent_tools'):
        self.recent_tools = []
    same_count = self.recent_tools.count(tool_name)
    if same_count > 0:
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
        if tool_name in productive_tools:
            reward += 2.0  # reduced novelty bonus
        self.episode_tools.add(tool_name)
    
    # FORCED EXPLORATION BONUS: +100 for first use of each productive tool within episode
    if not hasattr(self, 'episode_productive_first_use'):
        self.episode_productive_first_use = set()
    if tool_name in productive_tools and tool_name not in self.episode_productive_first_use:
        reward += 100.0  # reduced forced exploration bonus
        self.episode_productive_first_use.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    if tool_name in productive_tools:
        self.tool_penalty_factor = 0.0
    else:
        self.tool_penalty_factor = 1.0
    
    # Decay all counts
    for tool in self.tool_usage_counts:
        self.tool_usage_counts[tool] *= self.tool_decay_factor
    # Increment count for current tool
    self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
    # Apply penalty proportional to decayed usage count (capped at 5.0)
    usage_count = min(self.tool_usage_counts[tool_name], 5.0)
    reward -= self.tool_penalty_factor * usage_count
    
    # Per-episode usage counts (for extra penalty)
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penalty -500 per call, no success reward
    if tool_name == "list_files":
        reward -= 2000.0  # extremely heavy flat penalty per call
        # Additional per-episode penalty beyond first use: -100 per extra use
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 1000.0 * (self.episode_tool_counts[tool_name] - 1)
    # Penalty for write_note (already early return)
    if tool_name == "write_note":
        reward -= 5.0
    
    # Per-episode extra penalty for non-productive tools beyond first use
    non_productive = issue_tools + ["write_note", "list_files"]
    if tool_name in non_productive:
        if self.episode_tool_counts[tool_name] > 1:
            reward -= 1000.0 * (self.episode_tool_counts[tool_name] - 1)
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 100 ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if total_productive >= 2:
            current_proportion = productive_counts[tool_name] / total_productive
            # Target range 15% - 35%
            scaling_factor = 100.0  # reduced from 300
            if current_proportion > 0.35:
                excess = current_proportion - 0.35
                reward -= excess * scaling_factor  # penalty scaling
            elif current_proportion < 0.15:
                deficit = 0.15 - current_proportion
                reward += deficit * scaling_factor  # bonus scaling
    
    # =========== PER-EPISODE PROPORTION PENALTY (activates after 10 steps) ===========
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Compute proportion of this tool in episode so far
    if self.episode_step_count >= 5:
        proportion = self.episode_tool_counts.get(tool_name, 0) / self.episode_step_count
        # Penalty if proportion exceeds 35%
        if proportion > 0.35:
            excess = proportion - 0.35
            # -10 per extra percentage point (reduced from -100)
            penalty = -10.0 * excess * 100  # excess is fraction, multiply by 100 to get percentage points
            reward += penalty

            # =========== GLOBAL DEFICIT BONUS (new) ===========
        # Reward using a productive tool whose global proportion is below target (25%)
        # Bonus = (target - proportion) * 200, capped at +200
        if not hasattr(self, 'global_tool_counts'):
            self.global_tool_counts = {tool: 0 for tool in productive_tools}
        if tool_name in productive_tools:
            # Increment global count
            self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
            total_global = sum(self.global_tool_counts.values())
            if total_global > 0:
                global_proportion = self.global_tool_counts[tool_name] / total_global
                target = 0.25
                if global_proportion < target:
                    deficit = target - global_proportion
                    deficit_bonus = deficit * 200.0  # scaling factor 200
                    if deficit_bonus > 200.0:
                        deficit_bonus = 200.0
                    reward += deficit_bonus# =========== CURIOSITY BONUS with scaling 800 and cap +100 ===========
        # Reward for using underused tools across entire training (global usage)
        if not hasattr(self, 'global_tool_counts_curiosity'):
            self.global_tool_counts_curiosity = {tool: 0 for tool in productive_tools}
        if tool_name in productive_tools:
            # Increment global count (separate for curiosity)
            self.global_tool_counts_curiosity[tool_name] = self.global_tool_counts_curiosity.get(tool_name, 0) + 1
            total_global = sum(self.global_tool_counts_curiosity.values())
            if total_global > 0:
                global_proportion = self.global_tool_counts_curiosity[tool_name] / total_global
                # If global proportion below target (25% ideal), add bonus
                target = 0.25
                curiosity_scaling = 800.0  # increased from 300
                if global_proportion < target:
                    deficit = target - global_proportion
                    curiosity_bonus = deficit * curiosity_scaling
                    if curiosity_bonus > 100.0:
                        curiosity_bonus = 100.0
                    reward += curiosity_bonus        # =========== READ_FILE DEFICIT PENALTY ===========
        # If read_file hasn't been used in the last 50 steps, add a penalty to other tools
        if tool_name != "read_file" and hasattr(self, 'recent_tools'):
            # Count read_file usage in recent 50 steps (approximate)
            recent_read_file_count = self.recent_tools.count("read_file")
            if recent_read_file_count == 0 and len(self.recent_tools) >= 20:
                # Apply penalty to encourage read_file
                reward -= 50.0  # penalty for not using read_file
        # Also add a bonus for using read_file when it's underused globally
        if tool_name == "read_file" and hasattr(self, 'global_tool_counts'):
            total_global = sum(self.global_tool_counts.values())
            if total_global > 0:
                proportion = self.global_tool_counts["read_file"] / total_global
                if proportion < 0.15:
                    reward += 200.0  # extra bonus for read_file when underused
# =========== ADJUSTED EXTRA REWARDS ===========
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 15.0  # increased extra reward for execute_code (from 8)
        elif tool_name == "modify_self":
            reward += 12.0   # keep extra reward for modify_self
        elif tool_name == "write_file":
            reward += 5.0   # reduced extra reward for write_file
        elif tool_name == "read_file":
            reward += 5.0  # reduced extra reward for read_file
    
    # Write file rewards - extra base reward (already includes extra 5 above)
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 3.0  # extra base reward reduced
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 3.0  # extra for Python files
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 3.0  # extra for self-modification
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 3.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 1.0  # planning docs
    # Execute code rewards - keep
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 5.0  # extra for stdout
            if tool_result.get("stderr", "").strip() == "":
                reward += 3.0  # extra for no stderr
            stdout = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                reward += 1.0
            if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                reward += 2.0
    
    # Note writing rewards (journal) - discourage overuse (already early return)
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        reward += 0.5
        if len(note) > 100:
            reward += 0.5
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
            reward += 1.5
    
    # Issue creation rewards (planning) - no reward
    if tool_name == "create_issue":
        reward += 0.0  # no reward for issue creation
    
    # Reading important files reward - minimal
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        # Novel-file bonus: +2 for reading a file not read in last 20 steps
        if not hasattr(self, 'recent_read_files'):
            self.recent_read_files = []
        if filepath not in self.recent_read_files:
            reward += 2.0  # reduced novel-file bonus
        self.recent_read_files.append(filepath)
        if len(self.recent_read_files) > 20:
            self.recent_read_files.pop(0)
        # Important file bonus reduced to +2
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                         "world_model.py", "neural_q.py", "self_reflection.py",
                         "mcts_planner.py", "agent_brain.py", "strategy.md",
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 2.0  # reduced further
    
    # Modify self reward - adjusted base reward (already includes extra 12)
    if tool_name == "modify_self":
        reward += 10.0  # base reward
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 5.0  # extra reward for self-modification
    
    # Encourage exploration: reward for using underused tools, but less for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra reward for issue tools (only success reward)
        else:
            reward += 0.0  # removed extra reward for list_files
    
    # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps) - keep
    if not hasattr(self, 'episode_step_count'):
        self.episode_step_count = 0
    self.episode_step_count += 1
    # Assume steps_per_episode is stored in self.steps_per_episode (set by training script)
    if hasattr(self, 'steps_per_episode'):
        threshold = 0.4 * self.steps_per_episode
        if self.episode_tool_counts[tool_name] > threshold:
            reward -= 5.0  # reduced penalty per extra use beyond 40%
    
    # Clip reward to reasonable range to avoid overflow (more aggressive)
    if reward > 200.0:
        reward = 200.0
    elif reward < -200.0:
        reward = -200.0
    return reward