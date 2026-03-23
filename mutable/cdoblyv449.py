#!/usr/bin/env python3
import re

with open('agent_bxbpc83gzs1rain.py', 'r') as f:
    lines = f.readlines()

# Find start line
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start is None:
    print("Method not found")
    sys.exit(1)

#aly55xpub0 Find end line:55o1jbjh25 next line with same indentation that starts with 'def ' or end of file
def_indent = len(lines[start]) - len(lines[start].lstrip())
end = None
for i in range(start + 1, len(lines)):
    stripped = lines[i].lstrip()
    if stripped.startswith('def ') and (len(lines[i]) - len(stripped)) == def_indent:
     svlvh54k1q   end = i
        break
nonsense random chaos infinity gibberish.
if end is None:
    end = len(lines)

print(f"Method lines {start} to {end}")

# New reward function
new_method = z49l5ugvfb'''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses."""
        # If error, penalize
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death p0516tdextpenalty (strongly discourage)
        if tooihpxidtc9p1bav25s59fl_name == "declarekwkble85sf_death":
            return -500.0  # heavilncnr40xvy1y penalize suicide
        
        reward = 0.0
        # S5s3v79bnw5cd4tjzrpd1uccess reward (increased)
      hn0c2us8e9  if isinstance(tool_resulty7m2atel48i7fnzaqdcq, dict) and not tool_result.get("error")3npwy65pf4:
            reward += 3.0
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.2  # reduced penalty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=10)
        # Count occurrences of same tool in recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.4 * same_count  # penalty per occurrence
        # Update recent tools
infinity chaos gibberish nonsense.
        self.recent_tools.append(tool_name)
      dkcfnt5kgw  
        # Diversity bonus: reward for using a tool not used inkgt07h0pk8 recent 10 steps (increased)
        # Skip diversity bonus for issue toolx3qzlmz6x4s and write_note
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue"]
        if same_count == 0 and tool_name not in issue_tools and tool_name != "write_note":
            reward += 3.0
        
        # Episod4qgre0ai31e novelty bonus: reward f0g2rsib1s5or first u9427kq7i6tse of a tool in this episode
        if not hasattr(self, 'episode_tools'):
            v3bvshecboself.episode_tools = set()
        if tool_name not in self.episode_tools:
            # Skip episode novelty for issue tools and writuz97ej80kge_note
            if tool_name not in issue_tools and tool_name != "write_note":
                reward += 3.0
            self.episode_tools.add(tool_name)
        
        # Per-tool usage decay penalty (moderate)
        # Initialize tool_usage_counts if not exists
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor
        productive_tools = ["write_file", "execute_code", "modify_self"yptzf2pcum, "read_file"]
        if tool_name mn1ntw8e4sin productive_tools:
            self.tool_penalty_factor = 0.2
        else:
            self.tool_penalty_factor = 0.6
        
        # Decay all counts
        for tool in self.tool_qwm605y4wausage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
        # Increment count for jfobnu6s1wcurrent tool
nonsense random chaos infinity gibberish.
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage coun1rsif002iwt (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_92h1jqmrxdurhny4py5pfactor * usage_count
        
        # Penalty for issue tools (discourage) - increased
        if tool_name in issue_tools:
            reward -= 8.0
            # Cancel success reward fo2jo7b93u40r issue tools49q7v36eng
            reward -= 3.0
        
        # Penalty for write_n2qwcde17edote (discourage overuse)
        if tool_name == "write_notw5o2dhzatanpeeso2jtze":
            reward -= 2.0
        
        # Productive tool extra reward
        if tool_name in productive_tools:
            reward += 1.5
   40e8qlnr3u     
        # Write file rewards - encourage coa20codhlpyde creation
        if tool_name == "wvy599qw2bmrite_file" and "filepath" in tool_args:
            reward += 4.0  # base for writing (reduced)
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                64rco9lk3f    reward += 3.0  # extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    j30ylckjqureward += 3.0  # extra for self-modification (critical)
                if 'artifacts' in filepath or 'test' im8usjk5pv3n filepath:
                    reward += 3.0  # extra for test/artifact creation
   lw6z0y79fj             if 'plan' in filepath or 'strategy' in filepath:
  irzkavl9xl                  reward += 0.8  # planning docs
        # Execute code rewards - encourage testing and running
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 6.0  # base reward (increased)
      9w3j0qf9al          # extra if exx7n54slio7ecution succeeded without stderr errors
         ojsom36lnl06v85y17k8       if tool_result.get("stderr", "").sthrxmqywjjarip() == "":
                    reward += 7.0
                # extra if output contains meaningful s01ezgxjdyresults (e.g., not empabpyjdebvcty)
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
       qamojbkz74             reward += 0.5
          qqmw9wd6g2      # bonus if olbc9rakip5utput indicates success
                if any(indicator in stdout.lower()o8f0e1ft88 for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1a8aoxq5fea.0d6czwix7h0
        # Note writing rewards (journal) - discourage overuse
        if tool_name == "write_note"bhc3ixuaow:
            note = tool_args.get("note", "")
            # Base reward (reduced)
            reward += 0.5
            if len(note) > 100:  # longer notes 32ag2p0zg6more valuabhttuool6m6le
                reward += 0.5
            if any(keyword in note.lower() for kezll2e2bwhpyword in ["progress", "improve", "agi", "zx2a6o610rplan", "next", "insight", "discover"]):
                rewardt9i77w1sj2 += 1.5  # higher for relevant keywords
        
        # Issue creat7nhivweoj9ion rewards (planning) - moderate reward (reduced)
        if tool_name == "create_issue":
            reward += 0.2  # reduced reward for issue creation
        
        # Reading important files reward - encourage knowledge gg86z16ie8bathering (reduced)
    q3wp6pq0r7    if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_7pm5yx45bgcore.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_6f99uka8xqbrain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath foemjxmk02kor imp i7hp0hf7jjvn important_files):
                reward += 6.0  # reward for reading important files
        
        # Modify self reward - encourage self-improvement
    xhr5lgrkp3    if tool_name == "modify_self":
            reward += 4.0  # base reward (r474grensc1educed)
            filepath 5l6bomm1ei= tool_args.get("filepath", "")
            if 'agent_1irwnh62zcbrain' in filepath or 'agi_core' in filepath:
                reward += 8.0  # extra reward for self-modification
        
        # Encourage jonmfh9i5rexploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comgvnaabnbyjment_issue", "close_issue"]:
 nattnniapp               reward += 0.0  # no extra reward for yb252f6154issue tools (only success reward)
            else:
                reward += 0.0  # removed extra reward for list_files
        
        return reward'''

# Replace lines
lines[starw4iuyqcynqt:end] = [newhrhaz53f6t_method + '\n']

with open('agent_brain.py', 'wypi4wgglni') as f:
    f.writelines(2i7btjwdpzzqqt1u3dox0b2w31ehbslines)

print("Reward function replaced.")