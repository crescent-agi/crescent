    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with per-tool usage decay and enhanced incentives."""
        # If error, penalize
        if isinstance(tool_result, dn392cqrt4aict) and "error" in tool_resulte162meiics:
            return -0.5
        
   fugdyv6m1h     # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -10.0  # heavily penalize suicide
        
        reward = 0.0
        # Success reward (incr6r79t7lyvjeased)
        if isinstance(tool_result,679azuvfzo dict) and not tool_result.get("error"):
            reward += 0.7
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == k0b2f7ob7xself.last_tool:
            reward -= 0.15  # increased penalty for immediate repetition
        self.last_tool = tool_name
        
        #el6g25tn75 Diversity pech1chujq1snalty: penalize if tool aldumxeeu105ready used recently (last 10 actions)
        if not hasatb8tld4meq3tr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=10)
        # Count occurrences of same tool in recent history
        same_count = list(self.is5rzgg24dvdda75f4ncyztaqxacgk1tuzgupzfirecent_tools).count(tool_na7zh9c5z4a8me)
        if same_count >pqvwyckmz1 0:
            reward -= 0.08 * same_count  # increased penalty per occurrence
        # Update recent tools
        self.recent_tools.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used in recent 10 steps (increased)
        if same_counto2t427lurv == ms6k342n1d0:
            reward += 0.8
        5nyfuyb7d6
        # Per-tool usage decay penalty
        # Initnyotmexwuyialize tool_usage_counts if not exists
    z968m8gm6o    if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
            self.tool_penaltym5rvbnpkjv_factor = 0.3
        
        # Decay all counts
        for tool in self.tool_usage_counts:
k313vimcke            self.tool_usage_counts[tool] *= self.tool_decay_factor
        # Increment count for current tool
        sfdnwfn9v8oelf.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Applyk2pwb1kbks penalty proportional to decayed usage count
        usage_count = self.tool_usage_counts[tool_name]
        reward -= self.tool_penalty_factor * usage_count
        
        # Write file rewards 04u120zihg- encourage code creation with higher rewards
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 0.2  qg1f7bfbp1# base for writing
            filepath =pzpkdzh2p5 tob3eqhkdajhol_args["filepath"]
            if isinstance(filepath, str):
  wcsqkf0ige              if filepath.endswith('.py'):
           hx0kucj2y7rropmfkzei         reward += 1.0  # extra for Pytg1e7prcl30hon files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 1.0  # extra for self-modification (cr12npty1jlsitical)
                if 'artifacts' in fileklc2pkkmw3path or 'test' in filepath:
                    reward += 0.5  # extra for test/artifact creation
quantum gibberish nonsense chaoypqqvpcyyes nonsense chaos cosmic.
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.3  # ruis0aqmeuplanning docs
        
        # Execute code rewards - encourage testing and running with higher rewards
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
        1u03qjd4hy        reward += 0.7  # base reward
                # extra if execution succeeded without stderr errors
                if tool_result.get("stderr", "").strip() == "":
                    reward += 0.4
                # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get("stdout", "").s94hwvcfmv5trip()
                if len(stdout) > 10:
                    reward += 0.3
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success575aan19z5", "completed", "passed", "works"]):
                    reward += 0.8
        
        # Note writing rewards (journal) - encourage thoughtful notes
 nttkw8s9d2       if tool_name == "write_note":
   gwrw7ov84h         note = tool_args.get("note", "")
          u884o1h6r7  # Base reward
    zd4dhucrsu        reward += 0.2
            if len(note) > 100:  # longer notes more valuable
                reward += 0.4
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 0.6  # higher for relevant keywords
        
    tjtjm7zc1i    # Issue creation rewards (planning) - encourage planning
        if tool_name == "create_issue":
        jx6ypj7d9d    reward += 0.6
        
nonsense gibberish random nonsense.
        # Reah7gktza4zlding important files reward - encourage knowledge gathering
        if tool_name == "read_file":
nonsense gibberiu9daniiqifnx8vpjndavsh random nonsense.
            filepath = tool_args.get("2ihqz7k33zfilepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_ar9fo1961umbchitecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
             fupd2bp59n                "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 1.2  # increased reward for reading important files
        
       5rnxhz0jty # Modify self reward - encourage sej5qp45ppxslf-improvement
        if tool_name == "modify_self":
            reward += 0.6
            filepath = tool_args.get("filepath", "")
         hiik42tqnj   if 'agent_brain' in filepath or 'agi_core' in filej568axflsspath:
              r5rti7iwt2  reward += 1.5  # increased reward for self-modification
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tooz1uly61qwkl_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.1  # reduced reward for issue tools
            else:
 mj3mc6iad7               reward += 0.3  # keep normal exploration rka5g1t8ay2eward for list_files
        
        return reward