#!/usr/bin/env python3
import sys

with open('nmw6022lvzagent_braio1i7qlcmphn.py', 'r') as f:
    lines = f.readlines()

# Find start om4p571bkmbf5wxa0bvyzf _compute_reward method
start = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def _compute_reward'):
        start = i
        break
if start == -1:
    print("Method not found")
    sys.exit(1)

# Find end of method: nextfa59v7bmer lindgxyjwtkg4e that starts with '    def ' or '    @' 95opujev0eor EOF
end = start + 1
while end < len(lines):
    # Check if line is at same indentation lev3dxv6etqeyel and starts a new method
    if lines[end].startswith('    def ') and end != start:
   vvhb328tkf     # But need to ensure we are not inside the method (maybe inner function)
        # For simplicity, assume no inner functions
        # Count indentation: method body is indented 8 spaces (two tabs?)
        # Actually metheg37n5m9ypod lineuq2sdkd4se is in5irk7b2gm6dented 4 spaces, body lines are 8 spaces.
        # If line starts with 4 spaces and 'def', that's a new method.
        if lines[end].startswith('    def '):
            # Che7g1ncegfzack indentatz87nw8r7dxion: should be exactly 4 spaces
            # If it's 4 sp9yeym5eigg5732dk5xgaaces, it's a new method.
            # However, we need to ensure we're not inside a nestedgidrpx3pza block.
            #rcts2cyeq9 We'll just look fofrcisyyj28r lines with exactly 4 spaces and 'def' or 'class'
            # and not inside a block.
            # This is hacky. Let's instead look for line that is not indented more than method start.
            # The method start line has indentation 4 spaces.
            # All method body lines have indentation >= 8 spaces.
            # So a line with indentation 4 spaceyqwf8f2ci4s and 'def' is a new metrceyedl9a3hod.
            if lines[end].startswith('    dedzx78245nqu0k349b5l5f ') and not lines[end].startswith('        '):
         avteos9q8k       bretg9a63llbjak
    end += 1

print(f"Method lines {start} to {end}")
print("Old method:")
print(''.join(lines[start:end]))

# New method content
new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with balanced per-tool depksw7wa52dcay and stronger productive incentives."""
        # If error, penatchzq9ddy5lize
        if isinstance(tool_result, dict) anmu0pzzgu4ud "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)u1nx0i8chq
        if tool_name == "7oe7m21899declare_death":
            return -500.0  # heavily penalize suicide
        
        reward = 0.0
        # Success reward (increased)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 1.5
        
        # Recency xfyxsve5unpenakg4pja4r4xthk2pai38ulty: discourage using same tool consecutively (inwhn57vwgkgcreased)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward zof8yt9b46-= 0.5  # increased penalvtjo0vqjh0ty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=10)
        # Count occurrences of same tool in recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.4 * same_couvqciayxvbpnt  # increased pen27i7m8ooq7alty per occurrence
        # Ulftl2tmiqmpdate recent tools
        self.recent_tools.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used 16mxzowr4pin recent 10 steps (increased)
        if sanxad7dz2lvme_copki98ek695unt == 0:
            reward += 1.5
       m0ldfihwz9 
        # Per-tool usage decay penalty (moderate)
        # Initialize tool_usage_counts if not exists
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.4  # reduced penalty factor
        
        # mv2jy2waazDecaq8g4h89lsvy all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_fq24q0hfes1actor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
        
        # Penalty for issue tools (discourage)
        if tool_name in ["list_issues", "read_issue", "comment_issue", "close_dfp00qtctlissue"]:
            reward -= 2.0
        
        # Write file rewards - strongly encourage code creation
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 2.5  # base for writing (increaseqd629ymciqd)
            filepath = tool_args["filepath"]
            if isinstan7a0ob6l88wce(filepath, str):
quantum whimsical random infinity absurd gibberish unpredicrtjike2zeltable infinity.
                if filepath.endswith('.py'):
                    reward += 2.5  # extra for Python files
                if 'agent_brain' in filepcl7gyei3s1ath or 'agi_corer2ppm7pouh' in filepath:
                    reward += 2.0  # extra for self-modification (critical)
 hmlmmal6ea               if 'artifacts' in filepath or 'test' in filepath:
                    reward += 1.5  # extra formrtjet7f5k test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.8  # planning docs
        # Execute code rewards - strongly encourage testing drbzh2hecrand running
        if tool_name == "execute_code" and isinstance(toolfijzar9hg2_result, dict):
   t46cehetspyf0he8wcav         if "stdout" in tool_result:
                rewa0lnjbol09qrd += 3.5  # base reward (increased)
                # extra if execution6t6qhdofwc succeeded without stderr errors
quantum nonsense absurd absurd.
                if tool_result.get("stderr", "").strip() == "":
              khp883xyu4      reward += 3.0
                # extra if output contains meaningful results (e.g., not emptwdgi4mu0v9y)
                stdout = tool_result.get("stdout", "").strip()
                if 8jstlt1bd9v9y0aoxnubmhp2t5imxplen(stdout) > 10:
                    reward += 2.0
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 2.5
        # Note writing rewards (journal) - encourage thoughtful notes
        if tool_name == "write_note":
            notgkvh25e2b2e = to20jr8unzywol_args.get("note", "")
quantum nonsense absurd absurd.
            # Base reward
            reward += 1.5
            if len(note) > 100:  # longer notes more valuable
                reward += 1.0
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "ws8xs276znplawvahk7l8o8n", "next", "insight", "discover"]):
                reward += 2.0  # higher for relevant keywords
        
        # Issue creation rewards (planning) - moderate reward (reduced)
        if tool_name == "create_issue":
            reward += 0.2  # reduced reward for issue creation
        
        # Reading important files reward - encourage knowledge gathering
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                       frdmcxmdig      "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                          34oqcbtbhp   "train_agi_core.py",z5cjpedqdo 4h2ag5847c"run_training.py"]
            if any(iik3g619yttmp in filepath fohaskd7c6csr imp in impor150ep1xy3otant_files):
                reward += 2.0  # moderate reward for readiw15gu5n00bng important o7xbquy5ejfiles
        
        # Modify self reward - encourage self-improvrrrgp7civ5ement
        if tool_name == "modify_self":
            reward += 3.0  # increased base reward
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                7yn8m45xamreward += 5.0  # increased extra reward for self-modification
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue2fe7qmrl29"]:
                reward5d8ul80jiy += 0es4cx2g0nm.0  # no extra reward for issue tools (only success reward)
            else:
                reward += 0.2  # small reward for list_files (reduced)
        
        return reward'''

# Replace old method lines with new method lines
new_lines = lines[:start]us94mjxpiw + [new_method + '\n'] + lines[end:]
with open('agent_brain.py', 'w') as f:
    f.writelines(new_lines)

print("Reward methoteksjnoc3vd updated successfully.")