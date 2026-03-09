    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with per-tool usage decay and enhanced incentives."""
        # If error, penalize
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -10.0  # heavily penalize suicide
        
        reward = 0.0
        # Success reward (increased)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 0.7
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.15  # increased penalty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=10)
        # Count occurrences of same tool in recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.08 * same_count  # increased penalty per occurrence
        # Update recent tools
        self.recent_tools.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used in recent 10 steps (increased)
        if same_count == 0:
            reward += 0.8
        
        # Per-tool usage decay penalty
        # Initialize tool_usage_counts if not exists
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
            self.tool_penalty_factor = 0.3
        
        # Decay all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage count
        usage_count = self.tool_usage_counts[tool_name]
        reward -= self.tool_penalty_factor * usage_count
        
        # Write file rewards - encourage code creation with higher rewards
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 0.2  # base for writing
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 1.0  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 1.0  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 0.5  # extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.3  # planning docs
        
        # Execute code rewards - encourage testing and running with higher rewards
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 0.7  # base reward
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 0.4
                # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.3
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 0.8
        
        # Note writing rewards (journal) - encourage thoughtful notes
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            # Base reward
            reward += 0.2
            if len(note) > 100:  # longer notes more valuable
                reward += 0.4
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 0.6  # higher for relevant keywords
        
        # Issue creation rewards (planning) - encourage planning
        if tool_name == "create_issue":
            reward += 0.6
        
        # Reading important files reward - encourage knowledge gathering
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 1.2  # increased reward for reading important files
        
        # Modify self reward - encourage self-improvement
        if tool_name == "modify_self":
            reward += 0.6
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 1.5  # increased reward for self-modification
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.1  # reduced reward for issue tools
            else:
                reward += 0.3  # keep normal exploration reward for list_files
        
        return reward