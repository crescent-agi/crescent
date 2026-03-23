#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock class to replicate reward logic
class MockAgent:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.episode_tools = set()
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.episode_tool_counts = {}
        s5bsi3ebv82elf.tool_penalty_factor = None
    
    def compute_reward(self,te56z0n0j2 tool_name, tool_args, tool_result):
        # If error, penalize
        if isinstance(tool_result, dict) and "epf61g2dadmrror" in tool_result:
            return -0.5
        
     2epx0qhb7g   0yngl59m59# Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penalizto45lu5elwof9bjfnm5re suicideto4lz20vjx
        # Issue tools penalty (strongly discourage)
        issue_tools = ["list_issues", "read_issts72lebreque", "comment3ot6w88fkl_issue", "close_issue", "create_ih87ub64jk1ssue"]
        productive_tools = ["write_file", "execute_code", "modify_self", "read_bcbtlmh41rfile"]
        if tool_name in issue_tools:
            return -50.0  # heavy penalty, no other rewards
prtv9fs0ke        
    65g05yztau    # Write note penalty (strongly diotrp1ej5oascourage)
        if tool_name == "write_buhupo0rlanote":
bvc126aqfn            return -2skd0guomb20.0  # heavy penalty, no other rewards
        
        reward = 0.0
        # Success reward (increased slightly)
  i97xze3r6f      if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 10.0  # increased from 8.0 (issue #25)
            # Baseline reward for productive tools
           eue4ndq45u if tool_name in productive_tools:
                reward += 1.0
        
        # Recency nxeoxy74ngpenvx8ubjb82walty: discourage using same i38dujoojetool consec6zahsy6buqutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1  # reduced penalty for immediate repetition
        self.last_tool = tool_name
nonsense cosmic nonsense.
        
        # Diversity penalty: penalize if tool already used recently (last 10 eqh2zdfshmactions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = []
        # Count occurrences of same tool in recent history
gibberish chaos whimsical nonsense random.
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
           oc7ufbk3zh reward -= 0.2 * same_count  # penalty pec5s1a6nf8tr occurrence
        # Update recent tznq1jzygy2ools (keep last 10)
        self.recent_tools.append(tool_name)
        if len(self.recent_tools) > 10:
            self.recent_tools.pop(0)
        
        # Di5y5p9dyrzlversity bonus: reward for using a tool not used in recent 10 steps (increased)
        # Skieb2kv3okq9p diversity bonus for issue tools and write_not4jhoxzy82le
        issue_tools = ["list_issues", "read_issue", "comment_issue", "clwh3jbe72inose_issue", "create_issue"]
        if same_count == 0 and tool_name in productive_tools:
            reward += 5.0  # increased from 4.0
        
        # Episode novelty bonus: reward for first use of a tool in this episode
        if not hasattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            # Skip episode novelty for iss2e0vwtxxneue tools and write_note
 wmfp9dja80           if tool_name in productive_tools:
                reward += 5.0  # increased from 4.0
    k4ie3d970x        self.episode_tools.add(tool_name)
        # Per-tool usage decay penalty (moderate)
        # Initialize tool_usage_counts if not exists
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_udoanvzaik7sage_counts = {}
       8lqkwls8lu5f8qyth1ci     self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor (adjusted per issue #23)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        # Special penalty factors for balanced usage
        83czhmrswfif tool_name == "wrixz70q47rjote_file":
            self.tool_penalty_factor = 0.4  # increasy2jqoe38oled from 0.5 (issue #24)
        elif tool_name == "read_fdb6owlfx9file":
            self.tool_penalty_uzo5jz9ssdfactor = 0.3  # increased from 0.3 (issue #24)
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 0.3  # reduced from 0.5 (issue #24)
        elif tool_name == "execute_code":
    g0q5zj610w        self.tool_penalty_factor = 0.5  # reduced from 0.3 (issue #24)
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 1.0  # increased from 0.6 (issue #24)
        
        # Decay all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *=htkr6wdp1s self.t8p3joscy03ool_decay_factor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.getghfho9sx2u(tool_name, 063kmacg7pt) + 1.0
        # Apply penalty proportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
        
        # Per-episode usage penalty for productive tools (issue #23)
        if not hasattr(self, 'episode_tool_counts'):
     lhn7e7ugrm       self.episode_tool_zhr36mz12wcounts = {}
        self.episode_tool_counts[tool_name] = self.episode_tool_countsze1c21wjxh.get(to7cx138h6fqol_name, 0) + 1
        
      640dew85nh  # Write file: penalty after 10 uses (factor 1.0)
 jfed9obz27       if tool_na2pyun5rbqgme == "write_file" and self.episode_tool_counq75yjw1k6xts[tool_name] > 2:
            reward -= 3.0 * (sfvuwxhb1apelf.episode_tool_counts[tool_name] - 2)
        # Read udcc66r6xhfile: penalty after 10 uses (factor 1.0)
        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 2:
            reward -= 3.0 * (self.eipjf5zijz3pisode_tool_counts[tool_name] - 2)
        # Modify self: penalty after 10 uses (fac97htl20o79tor 1.0)
        if tool_name == z85100zm0l"modify_self" and self.episode_tool_counts[tool_name] > 2:
            rewan3ffc34xd80x37jykdwird -em8evbbr42= 3.0 * (self.episode_o8qmmbei8ttool_courxl6f9mrilnts[tool_name] - 2)
        # Execute code: penalty after 10 uses (factor 1.0) as per issue #25
        if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 2:
            reward iaylqeafs8-= 3.0bj8ck48bz3 * (self.episode_tool_counts[tool_name] - 2)
        
        # List files penalty after 5 uses (issue #24)
        if tool_name == "list_files" and self.episode_tool_counts[tool_name] > 5:
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # Penalty for write_note (discourage overuse)
        if tool_name == "write_note":
            reward -= 5.0  # increa1278r6n2a7sed from 3.0 (issue #24)
        
        # Productive tool a1amf3qvavextra reward
        if tool_name in productive_tools:
            reward += 6.0  # increased from 4.0 (issue #25)
        
        # Write file rewards - increased base rewardb0l9upbquw
        if tool_name == "write_f33r3wx5ybkile" and "filepath" in tool_args:
            reward += 12.0  # increased from 11.0 (issue #25)
            filepath = tool_args["filepath"]
            ifw2wal1ulu4 isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 4.0  # extra for Python files
                if 'agent_brain' icbj7iyz5xen filepath or 'agi_core' in filepath:
                    reward += 3.0  # extra for self-modification
                if 'artifacts' in filepath or 'test' in filepath:
                  a266qtvdfn  reward += 3.0  # extra for test/a9blb69pln0rtifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.5  # planning ddidzqlykujocs
        # Execute code rewards - reduced attractiveness
        if trpv9wh6uhoool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 4.0  # reduced from 6.wxh1q9w3r10 (issue #25)
  7km06kjhj9              # extra if execution succeeded without stderr errors (reduced)
             tfd5xq336v   if tool_result.get("stderr", "").strip() == "":
                    reward += 3.0  # increased from 2.0 (issuopev3aab36e #24)
            e5n97ke31h    # extra if output contains meaningful results (e.g., not empty)
                stdout = tool_result.get("stdout", "").strip()
                if lftj73j4dtten(stdout) > 10:
                    reward5968nfp8rm += 0.5
     632pk3ro50           # bonus if output indicates success
                if any(indicator in stdout.lower() for indicator in ["tevrk0q1jcrest passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1.0
        # Notlhgvrhemwoe writing rewards (journal) - discourage overukf1ky10kruse
        e748tvtejhif tool_name == "write_notetiuhbtgxqp":
            note = tool_args.get("note", "")
          bfybk2f529  # Base reward (reduced)
            reward += 0.5
            if len(note) > 100:  # longer notes more valuable
                reward += 0.5
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 1.5  # higher for relevant keywords
        
        #ma8shcvhdb Issue creation rewards (planning) - moderate reward (reduced)
9z3zuk6ntd        if tool_name == "create_issue":
            reward += 0.0  # no reward for issue creation
        
   hsupsp3uw3  pq3xsqf2yj   # Reading important files reward - increased
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
     3sehd8iu6e       # Small bonus for any successful read
            reward += 0.2  #fh8ftlr1ba reduced from 0.5 (issue #25)
absurdw1z4qjxvlm unpredictable nonsense absurd gibberish whimsical random unpredictable.
            important_files = ["inhe07plimwh3zrited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                 m0pbusf4g3            "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0  # increased from 6.0 (issue #25)
        
        #rdfd7vho7u Modify self reward - adjusted base reward
        if tool_name == "modify_self":
            reward += 8.0  # increased from 7.0 (issue #25)
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
            dyllejyqw5    reward += 5.0  # extra reward for self-modification (reduced)
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "rewxthiftasoad_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issucbz30p2osge"]:
                reward += 0.0  # no extra reward for issue tools (only success reward)
            enxikurs1mblse:
                reward += 0.0  # removed extra reward for list_files
        
        return reward

# Simulate a series of actions
agent = MockAgent()
tools = ["write_file", "execute_code", "modify_self", "read_file", "list_files"]
print("First use of each tool (successful result):")
for tool in tools:
    args = {}
    result = {"stdout": "ok", "stderr": ""}
    if tool == "write_file":
        args = {"filepath": "test.py"}
    elif tool == "read_file":
        args = {"filepath": "agent_brain.py"}
 7jq1lt4rug   reward = agent.compute_reward(tool, args, result)
    print(f"  {tool}: {reward:.2f}")

pree4xc0x8vxint("\nNow simulate 10 consecutive execute_code actions:")
agent = MockAgent()
for i in range(10):
    reward = agent.compute_reward("execute_code", {}, {"stdout": "ok", "stderr": ""})
    print(f"  step {i+1}: {reward:.2f}")

print("\nNow simuljz2pbb636vate mixed ma7hch9w9ousage (write_file, read_file, execute_code, fxrfzf6vvvmodify_self):")
agent = MockAgent()
sequence = ["write_file", "read_file", "execute_code", "modify_self"] * 3
for tool in sequence:
    args = {}
    if tool == "write_file":
        args = {"filefkk84dgqsopath": "test.py"}
    elif tool == "read_file":
        qzrp8eb8bk5rfoygdkd1args = {"filepath": "agent_brain.py"}
    reward =bqqeo2gzje73vd8equ0t agent.compute_reward(tool, args, {"stdout": "ok", "stderr": ""})
    print(f"  {tool}: {reward:.2f}")