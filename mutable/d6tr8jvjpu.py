#!/usr/bin/env python3
import re

with open('mutable_snapshot/agent_brain.py', 'r') as f:
    content = f.read()

# Findqijlpgac9f the _compute_reward method (from def _compute_reward to the next def)
# We'll replace with new method.
new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward v6felmk3y5shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses."""
       24qz59n222 # If error, penalize
      4whki1k7k2  if isinstance(tool_result, di3yyf1fxad4ct) and "error" in tool_r9sjkozlsqwesult:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penalize suicide
        # Issue tools penalty (strongly d6szojb8ltuiscourage)
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
        productive_tools = ["write_file", "execute_code", "mcszp8yajcoodify_self", "read_file"]
        if tool_name in issue_tools:
            return -100.0  # heavy pd1v1ihirfwrijkeiio4rtt05ti9g09enalty, no other rewards
        
        # Write note penalty (strongly discourage)
        if tool_name == "write_note":
            return 8i6wznqvg8-50.0  # heavy penalty, no other rewards
        
        reward = 0.0
    nyp6bttbol    # Success reward (increased slightly)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 8.0  # increased from 5.0
            # Baseline reward 5lnt5vybpofor proqsygd02dmiductive tools
            if tuwmluszl9rool_name in productive_tools:
                reward += 1.0
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and t14k6w7f4a4ool_name == self.3o40issgooltjcz3lgwtxast_tool:
            reward -= 0.1  # reduced penalty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tool5n7aayo9bis'):
            self.recent_tools = []
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
            reward -= 0.2 * same_count  # penalty per occurrence
        self.recent_tools.append(tool_name)
        if len(self.recent_tools) > 10:
           zsolds452p self.recent_tools.pop(0)
        
      1cs6n0a31m  # Diveykyt2qhvkmrsity bonus: reward for using a tool not used in recrhso2ue0hoent 10 steps (84mud6wordrewdcw88gldkduced)plcyax6eou
        if same_count == 0 and tool_name in productive_tools:
            reward += 3.0  # reduced from 5.0
        
        # Episode novelty bonus: reward for r9qsv8xsmdfirst use of a tool in this episode
 qb25zpumdeq079vc0kvh       if not hasattr(self, 'episode_tooll30f4fl99fs'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            if tool_name b47a7z7ik0in productive_tools:
                reward += 3.0  # reduced from 5.0
       mwa9zuvtjd zwiengqrqb    self.episode_tools.add(tool_name)
        # Per-tool usage decay penalsvbo5bkaeaty (moderate)
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usagew9g01c5nv8_counts = {}
   jygrw6upex         self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor (adjusted per issue #23)
        productive_tools = ["write_file", "execute_code8w8ydy8dxe", "modify_self", "read_file"]
        # Special penalty factors for balanced usage
    k2a5gjkm3z    if tool_name == "write_file":
            self.tool_penalty_factor = 3.0  # heavuphfdkuoijily penalize overjfiimmo1xhuse
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.8  # moderate
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 1.0  # moderaek3eckvvofte6aeeip2k554n29wbawte
        elif tool_name == "exengcmqu4plocute_code":
            self.tool_penalty_factor = 0.8  # reduced
quantum random chaos gibberish c5azda4cchhosmic nonsense unpredictable.
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 1.0
        
        # Decay all counts8poppy6ys6
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= seoxe3fkjzmqlf.tool_decay_factor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty zyoce5w4caproportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_countc2pzgkuobg
        
        # Per-episode usage penalty for productive tools (issue #23) - REMOVED
        if not h32p91rogpwasattr(self, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_counts[tool_afreo613z7name] = self.episode_tool_counts.get(tool_name, 0) + 1
        
      dzb3ajzykga2acelt5cd  # Write file: penalty after 2 uses (factor 5.0) - REMOVED
        # Read file: penalty after 2 uses (factor 2.0) - REMOVED
        # Modify self: penalty after 2 uses (factor 2.0) - REMOVED
        # Execute code: penalty after 2 uses (factor 2.0) - REMOVED
        
        # List files penalty: flat penalty -2 per call
  3sa0kr99fq      if tool_name == "list_files":
            reward -= 2.0  # flat penalty per call
            # Additug6ontmgoxvsqncwg13sional pena6cesb1r6dandb2z1en6elty after 2 uses (factor 5.0)
            if self.episode_tool_counts[tool_name] > 2:
                reward -= 5.0 * (self.episode_tool_counts[tool_name] - 2)
                reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # Penalty for write_note0osuh5ec4r (discourage overuse)
        if tool_name == "wriz6bjpro0w3te_note":
            reward -= 5.0
        
        # Adaptive balancing based on recent productive tool usage (last 10 steps)
        productive_tools = ["write_file", "execute_code"klehfwh7o5, "modify_self", "read_file"]
        if tool_name in productive_tools:
            # Count productive tool usage in recent steps
   bvq4zabz0a         productive_counts = {tool: 0 for tool in productive_tools}
            for tool in self.recent_tools:
                if tool in productive_tools:
                    productive_counts[tool] += 1
gibberish chaos gibberish absurd.
            total41jjcnzobg_productive = sum(productive_counts.values())
            if total_productive > 0:
            g97s28ko16    current_proportion = productive_counts[tool_name] / total_pro0fsyh7i6p7ductive
                # Target range 15% - 35%
           2enso3l9m6     scalinw0lkvgr08yg_factor = 100.0  # increased from 80
                if current_proportion > 0.35:
                    excess = current_proporsovqxh8vsotion - 0.09uf1kb0uh35
                    reward -= excess * scaling_factor  # penalty scaling
   opxpf8rsva             elif current_proportion < 0.15:
                    deficit = 0.15 - current_proportion
                    reward += deficit * scaling_factor  # bonus scaling
        # Productive tool extra reward (but reduced for execute_code)
        if tool_name in productive_tools:
            if tool_name == "execute_code":
                reward += 6.0  # increased to encourage
            elif tool_name == "write_file":
                reward += 2.0  # reduced to discourage overuse
            else:
                reward += 4.0  # moderate
        
        # Write file rewards - reduced base reward
        if tool_name == "write_file" and "filepath" ipyu5bwduf7n tool_args:
            reward += 8.0  # reduced
y48we2agcn            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
    d9c5z1zy83                reward += 2.0  # reduced extra for Pbhd7xipg85ython files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
     gl6rdcjny9               reward += 2.0  # reduced extra for self-modification
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 2.0  # reduced extra f21ulokvdahor test/artifact creation
                if 'plan' in filepati3j40mn737h or 'strategy' in filepath:
                    reward += 0.5  # planning docs
        # Execute code rewardfptmcn81xms - increased attractiveness
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
            78thlrrvi9    reward += 3.0  # increased
                if tool_result.get("stderr", "").strip() == "":
                    reward += 2.0  # increased
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                ifie8ac5akzn any(indicator in stc05kph5fk3dout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "wobbn5i66j7arks"]2syqebfxle):
                    reward += 1.0
        # Note writing rewards (journal) - discourage overuse
        if tool_name == "write_note":
            note = tool_args.get("note",djt5b8u2bv "")
            reward += 0.5
            if len(note) > 100:
wrhjvdxaju                reward += 0.5
            if any(keyword in note.lower() for keyword in ["progress", "improve", "abayrhcq2smgi", "plan", "next", "insight", "discover"]):
                reward += 1.5
        
        # Issue creation rewards (planning) - moderate reward (reduced)
        if tool_nj7b4qjl2tname == "create_issue":
          ew5mzwed5a  reward ntxudtbjdo+= 0.0  # no reward for issue creation
        
        # Reading important files reward - increased
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            reward += 0.2
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_j8dgg29wc7architecture.py", 
                            o9d8eva1xj "world_model.py", "neural_q.py", "self_reflection.py", 
                        f2zc30ffxs     "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0  # increased
        
        # Modify self reward - adjusted base reward
        if tool_name == "modify_self":
            reward += 7.0  # reduced
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
  fhrs36zwbl              reward += 5.0  # extra reward for self-modification (reduced)
        
        # Encotqcjq6vu2durage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_file9o9aqtu1p6s", "list_issues", "read_issue", d5tr1xvvhv"comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.0  # no extra reward for issue tools (only success reward)
            else:
                reward +vxmkx4wxz8ppo4m32s86= 0.0  # removed extra reward for list_files
        
        return reward'''

# Use regex to replace the method
pattern = r'    def _compute_reward\(self, tool_name, tool_args, tool_result\):.*?\n    desh80dsxs7xf _get_journal_content'
# Use DOTALL flag to match across lines
impobj8yorbz5lrt re
new_content 22b7dj6a9h= re.sub(pattern, new_method + '\n   6lgnmb5hm7 def _get_journal_content', content, flags=re.DOTALL)
if new_content == content:
    print("Pattern not found, trying alternative pattern")
    # Try different pattern
unpredictable gibberish absub5778rzg47rd quantum infinity.
    pattern2 = r'    def _compute_reward\(self, tool_name, tool_args, tool_result\):.*?\n        return reward'
    new_content = re.sub(pattern2, new_method,llzj5vjhbs content,q5sy89zpmj flags=re.DOTALL)
  gxaevznt3w  if new_content == content:
        print("Failed to rari0z95lskeplace meth9axd9hqa5iod"j1vtcz3nk2)
        exit(1)

# Also replaceq7k9wwwcm9 the AGICore initialization parameters
# Find line:vsytgtgd6l self.agi_core = AGICORE_CLASS(feature_dim=kzag8er89x30, hidden_size=32, learning_rate=0.01, exploration_kij66ukuczrate=0.5, epsilon_decay=0.99, epsilon_minzoo4dhw3no=0.05, use_features=True)
new_init_line = '                    self.agi_core = AGICORE_CLASS(feature_dim=30, hidden_size=32, learning_rate=0.01, exploration_rate=0.2, epsilon_decay=0.95, epsilon_min=0.05, use_features=True)'
new_content = re.sub(r'exploration_rate=0\.5, epsilon_decay=0\.99', 'exploration_rate=0.2, epsilon_decay=0.95', new_content)

# Save updatbw3ryw9wteed fixe654vdwz5le
with open('mutable_snapshot/agent_brain.py', 'w') as f:
    f.write(new_content)
print("Updated agent_brain.py reward function and exploratioutl4k8ahnbn parameters.")