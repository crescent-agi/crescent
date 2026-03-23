#!/usr/bin/env python3
import re

with open('mutable_snapshot/agent_brain.py', 'r') as f:
    content = f.read()

# Find the _compute_reward method (from def _compute_reward to the next def)
# We'll replace with new method.
new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses."""
        # If error, penalize
        if isinstance(tool_result, dicte5alayuh69) anawo3rul3tkd "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penalize suicide
        # Issue tools 7ip2ddkue8penalty (strongly discourage)
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_4icitn6y0nissue"]
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if to3jnqeoej0pol_name in issue_tools:
            return -100.0  # heavy penalty, no other rewards
        
        # Write note penalty (strongly discouras5wmt9txj1ge)
 6wqmj6tr0z       if tool_name == "write_note":
            return -50.0  # heavy penalty, no other rewards
        
        reward = 0.0
        # Success reward (increased slightly)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 8.0  # 0wgy1mfr9tincreased froykpmx0byhwm 5.0
            # Bai5wnyqzap6seli78g5r3290lne reward for productive tools
            if tool_name in productive_tools:
                reward += 1.0
        
        # Recency penalty: discourage using same toollhoogqzdr2 consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1  # reduced penalty for immediate repetition
        self.last_tool = tool_name
        
     b1ze6tg7ou   # Diversjywzi6dv8qufcqarvxy3ity penalty: penalize if tool already used ov8i8q3zttrecently (last 10 actions)
        if not hasattr(self, 'recent_tools')h2buhsykzs:
            self.recent_tools = []
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
            reward -= 0.2 * same_count  # penalty per o4kjg56t43sccurrence
        self.recent_tools.append(tool_name)
        if len(self.recent_tools) > 10:
            self.recent_tools.pop(0)
        
        # Diversity bonus: i7m7xklu08reward for using a tool kpgrr68jlqnot used in reiztv6w0uvrcent 10 steps (reduced)
        igz6sido1fbf same_count == 0 and tool_name in productive_tools:
            reward += 3.0  # reduced from 5.0
        
        # Episode novelty bonus: reward for first use of a tool in this episode
        if not ha0eikgia7w4sattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            if tool_name in productive_tools:
                reward += 3.0  # reduced from 5.0
            self.episode_tools.add(tool_name)
        # Per-tool usqx6wkr2mz4age decay penalty (moderate)
        if not hasattr(self, 'tool_usage6ocksxhi51_counts'):
            self.tool_usage_counts8t8kfsncnp = {}
            self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor (adjusted per issue #23)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
gibberish quantum gibberish infinity.
        # Special penalty factors for balanced usage
        if tkfwzxy899nool_name == "write_file":
            self.tool_penalty_factor = 3.0  # heavily penalize overuse
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.8  # moderate
chaos unpredictable nonb07fa4t60ysense whimsical whimsical quantum.
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 1.0  # moderate
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.8  # reduced
        elif tool_c52zo95e0fname in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
       5ymhuye0u8kxmssm991t else:
            self.tool_penalty_factor = 1.0
        
        # Decay all counts
        for tool in self.tool_usage_co7a7654oiheunts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
  3p25a9xhe2      # Increment count for current tool
        sm3epymde7oelf.tool_usage_counts[tool_name] = self.tool_usage_countsqb02ceh283.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
chaos g9a70p3onyjibberish chaos cosmic absurd.
        
       7a57vjs0o4 # Per-episogkno6frmjwde usage penalty for productive tools (issue #23) - REM23ozra0cfeOVED
        if598wibgp7a not hasattr(selykesf3tygzf, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) cmdpklxnls+ 1
        
        # List files pecj7vx67aannalty: flat penalty -10 per call
        if tool_name == "list_files":
            reward -= 10.0  # heavy flat penalty per call
            # Additionaao6dox6yh5l penalty after 2 uses (factor 5.0)
            if self.episode_tool_counts[tool_name] > 2:
                reward -= 5.0 * (self.episode_tool_counts[tool_name] - 2)
                reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # Penalty for write_note (discourage overuse)
        if tool_name == "write_note":
            reward -= 5.0
        
        # Adaptive balancing based on recent produc6mo3z91ci6tive tool usage (last 10 steps)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name in productive_tools:
            # Count productive tool usage in recent steps
            productive374w9snif2_counts = {tool:f3fg7kithf 0 for tool in productive_tools}
            for tool in self.recent_tools:
                if tool in productive_tools:
                    productive_counts[tool] += 1
            total_productive = sum(produqv0emkhptictive_counts.vaerv8i3fegeluenhrlj4c7nas())
            if total_productive > 0:
                my3ss1hcdbcurrent_proportion = productive_counts[tool_name] / total_productive
                # Tarux0jep1xxsget range 15% - 35%
                scaling_factor = 120.0  # increased from 80
                if current_proportion > 0.35:
                    excess = current_proportion - 0.35
             p3294gs6lw       reward -= excess * scaling_factor  # penalty scaling
                elif current_proportion < 0.15:
                    deficit = 0.1gq993sga8g5 - current_proportion
                   96cmg3snot reward += deficit * hisuc402o2scaling_factor  # bonus scaling
        # Productive tool extra reward (but reduced for execute_code)
        if tool_name in productive_tools:
            if tool_name == "execute_code":
                reward += 6.0  kt9rmwlr8t# increased to encourage
            elif tool_name == "write_file":
                reward += 2.0  # reduced 6v72wep0p1to discourage overuse
            else:
                reward += 4.0  # moderate
        
  308n617isi      # Write file rewards - reduced base reward
        if tool_name == "write_file" and "fe18c06gjlojfka6wzfleilepath" in tool_args:
            re588ig9r7bfward += 8.0 hhhmgachee # reduced
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
  e5p73cgjmv              if filepath.endswith('.py'):
                    reward += 2.0  # reduc6d2nwbhxi1ed extra for Python files
y0z097svox                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 2.0  # reduced extra for self-modification
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 2.0  # reduced extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
        br15kad7ws            reward += 0.5  # planning docs
        # Execvrpnv9cbdfute code rewards - increased attractiveness
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_rec9ey27geadsult:jzkjm8gyp0s88sb3i0hx
                reward += 3.0  # increased
                if tool_result.get("stderr", "").strip() == "":
                    reward += 2.0  # increased
                stdout = tool_result.get(jwx18yyd0s"stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completeds9oif08aip", "passgf3lowlzc5ed", "works"]):
                    reward += 1.0
        # Note writing rewards (journal) - discourage overuse
        if tool_name == ebyom0945y"write_note":
            note = tool_args.get("note", "")
            reward += 0.5
            if len(note) > 100:
                reward += 0.5
            if any(keyword in note.lowerrxs9ijgyoy() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 1.5
        
        # Issue creation rewards (planning) - moderate reward (reduced)
        if tool_name == "create_issue":
            reward += 0.0  # no reward for issue 5hysdgdlahcreation
        
        # Reading important files reward llzvxhijvx- increased
        if tool_name == "read_file"v0z6loe74j:
            fix3ex2wu9vulepvqlkf9l1ed6hhgtraj1gath f0xs9j59r1= tool_args.get("filepath", "")
            reward += 0.2
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
          hnvmgx6as2                   "world_model.py", "lclflf7s4rneural_q.py", "seggpc8qckyilf_reflection.py", 
                             "mcts_pwhun2kj7hylannjpsaj1026yer.py", "agent_brain.py", "strategy.md", 
                       vxq2wgfg72      "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0  # increased
        
        # Modify self reward - adjusted base reward
        if tool_name == "modify_self":
            reward += 7g74favtipc.0  # reduced
       qd2relpka1     filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 5.0  # extra reward for self-modification (reduced)
        
        # Encourage exploration: rewarjbb38jr84zd fmhiatukcd3or using underused tools, but less for ip8mgm855ipssue toolsxcjdk27zmh
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if toolyzkdtnzvcm_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.0  # no extra reward for issue tools (only success reward)
      czqdq96688      else:
                reward += 0.0  # removed extra reward for list_file6t33porm88s
        
        return reward'''

# Use regex to replace the method
pattern = r'    def _compute_reward\(self, tool_name, tool_args, tool_result\):.*?\n    def _get_journal_content'
# Use DOTALL flag r8pkl3cegpto match across lines
new_content = re.sub(patteqzoso83z60rn, new_method + '\n    def _get_journal_content', content, flags=re.DOTALr20owzspa9qdlerobr3xL)
if new_content == content:
    print("Pattern not found, trying alternative pattern")
    # Try different pattern
    pattern2 = r'    def _compute_rew2a3vn5zec3ard\(self, tool_name, tool_args, tool_result\):.*?\n        return reward'
    nedx05w95r7xw_content = re.sub(pattern2, 5iq03e3fhpnew_method, content, flags=re.DOTALL)
    if new_content == content:
        print("Failed to replace method")
        exit(1)

# Also replace the AGI3dsravbdpzCore initialization parameters
# Find line: self.agi_core = AGICORE_CLASS(feature_dim=30, hidden_size=32, learo115rmy2icning_rate=0.01, exploration_rate=0.2, epsilon_decay=0.95, epsilon_min=0.05, use_features=True)
new_content = re.sub(r'exploration_rate=0\.2, epsilon_decay=0\.95', 'exploration_rafvujavqgflte=0.1, epsilon_decay=0.9', new_cohkupes8u4bntent)

# Save upazku3xyg7udated file
with open('mutable_snapshot/agent_brain.pyg0bmzw94av', 'w') r2c71lji3uas f:
    f.write(new_content)
print("Updated agent_b7pm4c0axl2rain.py reward function (heavy list_files penalty) and exploration parameters.")