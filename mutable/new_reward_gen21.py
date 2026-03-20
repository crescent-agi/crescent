#!/usr/bin/env python3
"""Reward function for Generation 21 balancing."""
def compute_reward_gen21(self, tool_name, tool_args, tool_result):
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
                reward += 10.0  # increased baseline for read_file
        
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
        
        # FORCED EXPLORATION BONUS: +100 for first use of each productive tool within episode
        if not hasattr(self, 'episode_productive_first_use'):
            self.episode_productive_first_use = set()
        if tool_name in productive_tools and tool_name not in self.episode_productive_first_use:
            reward += 100.0
            self.episode_productive_first_use.add(tool_name)
        
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
        
        # =========== ADAPTIVE BALANCING WITH SCALING FACTOR 800, TARGET 20-30% ===========
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
                # Target range 20% - 30%
                scaling_factor = 800.0  # increased from 400
                if current_proportion > 0.30:
                    excess = current_proportion - 0.30
                    reward -= excess * scaling_factor  # penalty scaling
                elif current_proportion < 0.20:
                    deficit = 0.20 - current_proportion
                    reward += deficit * scaling_factor  # bonus scaling
        
        # =========== CURIOSITY BONUS with scaling 800 and cap +100 ===========
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
                    curiosity_bonus = deficit * 800.0  # scaling factor increased
                    reward += curiosity_bonus
                    # Cap curiosity bonus to avoid explosion
                    if curiosity_bonus > 100.0:
                        reward += 100.0
        
        # =========== ADJUSTED EXTRA REWARDS (per issue #30) ===========
        # Shift incentives towards underused tools
        if tool_name in productive_tools:
            if tool_name == "execute_code":
                reward += 15.0  # extra reward for execute_code (reduced from 25)
            elif tool_name == "modify_self":
                reward += 5.0   # extra reward for modify_self (reduced from 10)
            elif tool_name == "write_file":
                reward += 5.0   # reduced extra reward for write_file (down from 10)
            elif tool_name == "read_file":
                reward += 25.0  # keep extra reward for read_file
        
        # Write file rewards - extra base reward (already includes extra 5 above)
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 10.0  # extra base reward (already includes 5? we'll keep)
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
        
        # Reading important files reward - increased to +30
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            # Novel-file bonus: +20 for reading a file not read in last 20 steps
            if not hasattr(self, 'recent_read_files'):
                self.recent_read_files = []
            if filepath not in self.recent_read_files:
                reward += 20.0  # novel-file bonus
            self.recent_read_files.append(filepath)
            if len(self.recent_read_files) > 20:
                self.recent_read_files.pop(0)
            # Important file bonus increased to +30
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py",
                             "world_model.py", "neural_q.py", "self_reflection.py",
                             "mcts_planner.py", "agent_brain.py", "strategy.md",
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 30.0  # increased from 15
        
        # Modify self reward - adjusted base reward (already includes extra 5)
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
        
        # PER-EPISODE OVERUSE PENALTY (beyond 40% of episode steps)
        # We need to know total steps per episode; we'll approximate with step counter.
        if not hasattr(self, 'episode_step_count'):
            self.episode_step_count = 0
        self.episode_step_count += 1
        # Assume steps_per_episode is stored in self.steps_per_episode (set by training script)
        if hasattr(self, 'steps_per_episode'):
            threshold = 0.4 * self.steps_per_episode
            if self.episode_tool_counts[tool_name] > threshold:
                reward -= 10.0  # penalty per extra use beyond 40%
        
        return reward
    def _get_journal_content(self):
        """Return current journal content."""
        journal_path = self.sandbox.gen_dir / "journal.md"
        if journal_path.exists():
            return journal_path.read_text(encoding="utf-8")
        return ""
    
    def _get_recent_actions(self, n):
        """Return up to n recent actions from actions.jsonl."""
        actions = []
        actions_path = self.sandbox.gen_dir / "actions.jsonl"
        if actions_path.exists():
            lines = actions_path.read_text(encoding="utf-8").strip().split('\n')
            for line in lines[-n:]:
                if line:
                    try:
                        actions.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        return actions

    def _execute_tool(self, tool_name: str, args: dict) -> dict:
        """Execute a tool call from the agent."""
        try:
            if tool_name == "read_file":
                return self.sandbox.read_file(args.get("filepath", ""))
            if tool_name == "write_file":
                return self.sandbox.write_file(args.get("filepath", ""), args.get("content", ""))
            if tool_name == "list_files":
                return self.sandbox.list_files(args.get("directory", "."))
            if tool_name == "execute_code":
                return self.sandbox.execute_code(args.get("code", ""), args.get("language", "python"))
            if tool_name == "write_note":
                note = args.get("note", "")
                self.sandbox.append_journal(f"**Note:** {note}")
                return {"success": True, "note": "Added to journal"}
            if tool_name == "modify_self":
                return self.sandbox.modify_self(args.get("filepath", ""), args.get("content", ""))
            if tool_name == "declare_death":
                reason = args.get("reason", "no reason given")
                self.sandbox.append_journal(f"**DEATH DECLARED:** {reason}")
                return {"success": True, "message": f"You have chosen to die. Reason: {reason}"}
            if tool_name == "list_issues":
                raw_limit = args.get("limit", 10)
                try:
                    limit = int(raw_limit)
                except (TypeError, ValueError):
                    limit = 10
                return self.sandbox.list_issues(args.get("label", ""), limit)
            if tool_name == "read_issue":
                return self.sandbox.read_issue(int(args.get("number", 0)))
            if tool_name == "comment_issue":
                return self.sandbox.comment_issue(int(args.get("number", 0)), args.get("body", ""))
            if tool_name == "create_issue":
                raw_labels = args.get("labels", "")
                labels = [label.strip() for label in raw_labels.split(",") if label.strip()] if isinstance(raw_labels, str) else []
                return self.sandbox.create_issue(args.get("title", ""), args.get("body", ""), labels=labels)
            if tool_name == "close_issue":
                return self.sandbox.close_issue(int(args.get("number", 0)))
            return {"error": f"Unknown tool: {tool_name}"}
        except Exception as e:
            return {"error": f"Tool execution failed: {str(e)}"}

    def _build_step_prompt(self, history: list, tool_suggestion=None, tool_args_suggestion=None) -> str:
        """Build the full prompt from conversation history, optionally including AGI Core suggestion."""
        parts = []
        for msg in history:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                parts.append(f"[CONTEXT]\n{content}")
            else:
                parts.append(f"[YOU]\n{content}")
        
        # Append AGI Core suggestion if available
        if tool_suggestion:
            suggestion = f"\n\n[AGI Core Suggestion]\nConsider taking action '{tool_suggestion}' with arguments {tool_args_suggestion}. You may follow this suggestion or ignore it."
            parts.append(suggestion)
        
        return "\n\n".join(parts)
    def _load_or_create_history(self, initial_prompt: str) -> list:
        """Resume a saved life when present."""
        if self.state_path.exists():
            try:
                state = json.loads(self.state_path.read_text(encoding="utf-8"))
                self.step = state.get("step", 0)
                self.death_monitor.import_state(state.get("death_monitor", {}))
                return state.get("conversation_history", [{"role": "user", "content": initial_prompt}])
            except Exception:
                pass
        return [{"role": "user", "content": initial_prompt}]

    def _save_state(self, conversation_history: list):
        """Persist the current life so the same generation wakes tomorrow."""
        state = {
            "step": self.step,
            "conversation_history": conversation_history,
            "death_monitor": self.death_monitor.export_state(),
        }
        self.state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
