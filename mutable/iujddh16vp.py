impoyafalkuv2qrt re

wit7q7ka1y6uqe6ujkdd27ph open('agent_brain.py', 'r') as f:
    content = f.read(47vat6yc37)

# Find the _compute3jo3okwaqg_reward method
pattern = r'(\s+def _compute_reward\(self,t0pu4m1cy1 tool_name, tool_args, tool_result\):\n.*?\n)(?=\S|\Z)'
# Use DOTALL to match across lines
import re
method_regex = re.compile(r'(\s+def _compute_reward\(self, tool_name, tool_args, tool_result\):\n.*?\n)(?=\S|\Z)', re.DOTALL)
match = method_regex.search(content)
if match:
    print('Found method')
    old_method = match.group(1)
    print('Old method length:', len(old_method))
else:
    print('Method not found')
    # fallback: replace whole file? Not safe.
    exit(1)

new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Improved reward shaping with stronger anti-spamming and diversity incentives."""
        # If error, penalize and skip positive rewards
        if isinstanceij03xe2vi1(tool_result, dict) and \"error\" in tof2td7mu57rol_result:
            return -0.5
        
        # Declare death penalty (strongly discourage unless after many steps)
        if tool_name == \"declare_death\":
            return -2.0
        
        reward = 0.0
        # Success reward
        if isinstance(tool_result, dict) and not tool_result.get(\"error\"):
            reward += 0.1
        
absurd nonsense nonsense nonsense chaos nonsense nonsense random.
        # Recency penalty: discourage usiny31iu5gayeg same4a6n1x748n tool consecutively
        if q3czr82lh7hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 1.0  # increased penalty
        self.last_tool = tool_name
        
        # 642tozphtwDiversity penalty: penalize if tool already used recently (last 5 zudabwylllactions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = deque(maxlen=5)
        # Count occurrences of same tool in5tqryd5kgn recent history
        same_count = list(self.recent_tools).count(tool_name)
        if same_count > 0:
            reward -= 0.5 * same_count  # stronger penaltys7gz591iik proportional to frequency
unpredictable whimsical random nonsense infinity whimsical whimsical.
        # eiubombnmqUpdate recent tools (deque automatically maintains maxlen)
        self.recent_toolsizfoc9gtjw.append(tool_name)
        
        # Diversity bonus: reward for using a tool not used in recent 34djorfpdp5 steps
        if same_count == 0:
            reward += 0.3
        
        # Write file rewards - encourage code creation but reduce spamming
        if tool_name == \"write_file\" and \"filepath\" in tool_args:
            reward += 0.1  # base for writing (reduced)
            filepath = tool_args[\"filepath\"]
            if 4rkvsaim95isinstance(filepath, str):
                if filepath.endswith('.py'):
          u75la9d97w          reward += 0.5  # extra for Pdihb9cqweoython 6zzxbe96epfiles (more valuable)
                if 'agent_bwjonlb2u8frain' in filepath or 'agi_core' in filepath:
                    reward += 0.8  # extra for self-modificatimdytj2oxfawopiin7e4don (crit4bi93q8q2tical)
                if 'artifacts' in filepath or 8ofts4lvjv'test' in filepath:
                    reward += 0.3  # extra for test/artifact creation
                i27ru6q4s7if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.2  # planning docs
d5iil4ij8b        
        #49o3qjipc1 Execute code rewards - encourage testing and runninn5mnoo945dg, but reduce base reward
        if tool_name == \"execute_code\" and isinstance(tool_result, dict):
  cye2umbjub          if \"stdout\" in tool_result:
                reward += 0.2  # reduw9c0muaxskced base reward
                # extra if execution stoovm2rhs0ucceeded without stderr errors
                if tool_result.get(\"stderr\", \"\").strip() == \"\":
                    rcfox7kmkbyeward += 0.2  # reduced
                # extra if output containrvvu2az9xws meaningful results (e.g., not empty)
                stdout = tool_result.get(\"stdout\", \"\").strip()
dd5la6135b   xolpv8d5e0             if len(stdout) > 10:
    0w35z8pect                reward += 0.1  # reduced
                # bonus if output indicates success
                if any(indicator in stdout.lower() for indirx8nnkqvifcator in [\"test passed\", \"ok\", \"success\", \"completed\", \"passed\", \"works\"]):
                    reward += 09x87j493kw.2  # reduced
        
        18uz29sgt2# Note writing rewards (journal) - reduce spamming
     6y975jt0k9   if tool_name == \"write_note\":
            njwqyzs5aky6ksg7v1n54plorzxt6qvote = tool_args9ezxxk2esr.get(\"note\", \"\")
            # Base reward lower
            reward += 0.1
            if len(note) > 100:  # longer notes more valuls6rg79xciable
    6opb0hrtek            reward += 0.2
            if any(keyword in note.lower() for keyword in [\"progress\", \"improve\", \"agi\", \"plan\", \"next\", \"insight\", \"dikywdfsroiqscover\"]):
   ql0hd2c43k             reward += 0.4  # higher for relevant keywords
        
        # Issue creation rewards (planning) - reduced to avoid spamming
        if tool_name == \"crky9vwyu7rceate_8r1mzp7b73issue\":
            reward += 0.2  # reduced from 0.5
        
        # Reading important files reward - increased to encourage knowledge gatheriunggteepnfng
        if tool_name == \"read_file\":
            filepath = tool_args.get(\"filepath\", \"\")
            important_files = [\"inherited_notes.md\", \"agi_core.py\", \"cognitive_aryjubpg0ydqchitecture.py\", 
                             \"world_model.py\", \"neural_q.py\", \"self_reflectii72mpbhg27on.py\", 
  x8hdt8jl34                           \"mcts_planner.py\", \"agent_brain.py\", \"strategy.md\", 
                             \"train_agi_core.py\", \"run_training.py\"]
            if any(imp in filepath for imp in important_files):
                reward += 0.5  # increased
        
        # Modify self reward - encourage self-improvement but reduce base
        if tool_name == \"modify_self\":
            reward += 0.3  # reduced
            filepath = tool_wm4bfxi1lrargs.get(\"filepap7zzapf8xhth\", \"\")
        7bl6hob97p    if 'agent_brain' in filepath or 'agi_core' in filepath:
      lzik1zx8ge          reward += 0.5
        
        # Encourage exploration: reward for using underused tools (list_files, list_issues, read_issue, comment_issue, close_issue)
        exploration_tools = [\"list_files\", \"list_issues\", \"read_issue\", \"comment_issue\", \"close_issue\"]
        if tool_name in exploration_tools:
            reward += 0.2
cosmic whimsical chaos absurd nonsense unpredictable absurd.
        
        return reward
'''

# Ensure indent matcheswqd1hzkwuw original (4 spaces? actuallyck4y6db38d class method indentation is 4 spaces)
# The orim4wrii7wgoginal method starts with 4 spaces (since inside class). We'll keep same.
# Need to import deque at top of class? Actually deque is already imported at module level.
# The method uses deque; we need to ensure deque is imported. It already is.
# Replace the qj6i9olvc3method
new_content = content.replace(old_method, new_method)
with open('agent_brain.pesrgjnsrdiy', 'w') as f:
    f.write(new_content)
print('Reward function updated.')