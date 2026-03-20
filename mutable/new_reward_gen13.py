#!/usr/bin/env python3
"""
New reward function for Generation 13.
Implements curiosity bonus, adjusted extra rewards, scaling factor 400.
"""

def compute_reward_new(self, tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0  # heavily penalize suicide
    # Issue tools penalty (strongly discourage)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -500.0  # extremely heavy penalty, no other rewards
    
    # Write note penalty (strongly discourage)
    if tool_name == "write_note":
        return -100.0  # heavy penalty, no other rewards
    
    reward = 0.0
    # Success reward (very high)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        if tool_name != "list_files":
            reward += 80.0  # high success reward
        # Baseline reward for productive tools
        if tool_name in productive_tools:
            reward += 5.0
    
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
        reward += 5.0  # diversity bonus
    
    # Episode novelty bonus: reward for first use of a tool in this episode
    if not hasattr(self, 'episode_tools'):
        self.episode_tools = set()
    if tool_name not in self.episode_tools:
        if tool_name in productive_tools:
            reward += 5.0  # novelty bonus
        self.episode_tools.add(tool_name)
    
    # Per-tool usage decay penalty (moderate) - ZERO for productive tools
    if not hasattr(self, 'tool_usage_counts'):
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
    
    # Productive tools have zero penalty factor
    # Special penalty factors for balanced usage
    if tool_name == "write_file":
        self.tool_penalty_factor = 0.0  # no penalty for productive tools
    elif tool_name == "read_file":
        self.tool_penalty_factor = 0.0
    elif tool_name == "modify_self":
        self.tool_penalty_factor = 0.0
    elif tool_name == "execute_code":
        self.tool_penalty_factor = 0.0
    elif tool_name in productive_tools:
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
    
    # Per-episode usage penalty for productive tools (issue #23) - REMOVED
    if not hasattr(self, 'episode_tool_counts'):
        self.episode_tool_counts = {}
    self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
    
    # List files penalty: flat penalty -100 per call, no success reward
    if tool_name == "list_files":
        reward -= 100.0  # extremely heavy flat penalty per call
        # Additional penalty after 2 uses (factor 5.0)
        if self.episode_tool_counts[tool_name] > 2:
            reward -= 5.0 * (self.episode_tool_counts[tool_name] - 2)
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
    # Penalty for write_note (discourage overuse)
    if tool_name == "write_note":
        reward -= 5.0
    
    # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 400 ===========
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in productive_tools:
        # Count productive tool usage in recent steps
        productive_counts = {tool: 0 for tool in productive_tools}
        for tool in self.recent_tools:
            if tool in productive_tools:
                productive_counts[tool] += 1
        total_productive = sum(productive_counts.values())
        if total_productive > 0:
            current_proportion = productive_counts[tool_name] / total_productive
            # Target range 15% - 35%
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
        self.global_tool_counts = {tool: 0 for tool in productive_tools}
    if tool_name in productive_tools:
        # Increment global count
        self.global_tool_counts[tool_name] = self.global_tool_counts.get(tool_name, 0) + 1
        total_global = sum(self.global_tool_counts.values())
        if total_global > 0:
            global_proportion = self.global_tool_counts[tool_name] / total_global
            # If global proportion below target (25% ideal), add bonus
            target = 0.25
            if global_proportion < target:
                deficit = target - global_proportion
                curiosity_bonus = deficit * 200.0  # scaling factor
                reward += curiosity_bonus
                # Cap curiosity bonus to avoid explosion
                if curiosity_bonus > 50.0:
                    reward += 50.0
    
    # =========== ADJUSTED EXTRA REWARDS ===========
    # Shift incentives towards underused tools
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 30.0  # extra reward for execute_code (increased)
        elif tool_name == "modify_self":
            reward += 25.0  # extra reward for modify_self (increased)
        elif tool_name == "write_file":
            reward += 5.0   # reduced extra reward for write_file
        elif tool_name == "read_file":
            reward += 5.0   # reduced extra reward for read_file
    
    # Write file rewards - extra base reward
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 10.0  # extra base reward
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 5.0  # extra for Python files
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 5.0  # extra for self-modification
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 5.0  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 2.0  # planning docs
    # Execute code rewards - increased attractiveness
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 10.0  # extra for stdout
            if tool_result.get("stderr", "").strip() == "":
                reward += 5.0  # extra for no stderr
            stdout = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                reward += 2.0
            if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                reward += 3.0
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
        reward += 0.0  # no reward for issue creation
    
    # Reading important files reward - increased
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        reward += 1.0
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.py", "agent_brain.py", "strategy.md", 
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 15.0  # increased
    
    # Modify self reward - adjusted base reward
    if tool_name == "modify_self":
        reward += 15.0  # base reward
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 10.0  # extra reward for self-modification
    
    # Encourage exploration: reward for using underused tools, but less for issue tools
    if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
            reward += 0.0  # no extra reward for issue tools (only success reward)
        else:
            reward += 0.0  # removed extra reward for list_files
    
    return reward