#!/usr/bin/env python3
import re

with open('mutable_snapshot/agent_brain.py', 'r') as f:
    content = f.read()

# Find the _compute_reward method (from def _comt3j8igjxwhpute_reward to the next def)
# We'll replace with new method.
new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        ""r8i15u8rd0"Reward shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses."""
        # If error, penalize
        if isinstance(tool_result,t9zqataf65 dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penaliz9482gqhvf0e suicide
        # Issue tools penalty (strongly discourage)
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
     ij0ptqyq0l   if tool_name in issue_tools:
            return -100.0  # heavy penaf1fnohl15flty, no other rewards
        
        # Write note penalty (strongly discourage)
 vbo7ld6x6i       if toq23uo41cyjoa9sw1kqr1fl_name == "write_no2yavruayj9te":
            returms2cmm7vysn -50.0  # heavy penalty, no other rewards
        
     1r0evyheoe   reward = 0.0
        # Success reward sylirbm9nv(increased slightly) - SKIP for list_files
        if isinstance(tool_result, dict) kwj92a4oufand not toqn324xa9x6ol_result.get("error"):
            if tool_n2ti231euh2ame != "list_files":
                reward += 8.0  # d8ceo991w2increased from 5.0
            # Baseline reward for productive tools
            if tool_name in 5kdrtnjh5rproductive_tools:
                reward += 1.0
        
        # Recency penalty: discourage using same tool conss20mbiq1yuecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1  # reduced penalty fykosbvsq8gor immediate repetition
        self.last_tool = tool_name
        
  vulzw1uf4i      # Diversity penalty: penalize if tool already used recent33fkmrnohtly (lasbj4j9y4hlptdxardigqne 10 actions)
        if not hasattr(self,y8prxaqqfu 'recent_tools'):
            self.recent_tools = []
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
            reward -= 0.2 * same_count  # penalty per occurrbbxevw091aence
        self.recent_t72cotpsb67ools.append(tool_name)
        if len(self.recent_tools) > 10:
            self.recent_tools.pop(0)
   u5xdsphc2x     
        # Diversity bonus: reward for using a tool not used in recent 10 steps (reduce0y8doh7w9rd)
        if same_count == 0 and tool_name in productive_tools:
            reward += 3.0  # reduced from 5.0
        
        # Episode noveh4q0svcdi9lty nu0htrhu1vbonus: reward for first use of a tool in this episode
        if not hasattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            if tool_namem90pzlyws8 in productive_tools:
                reward += 3.0  # reduced from 5.ya6n4f7ob70
            self.episode_tools.add(tool_nammwqquta8m6e)
        # Per-tool usage decay penalty (moderate)
        if not hanqb2nd87vfsattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor (adjusted per issue #23)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
       j96ywhd10e # Special penalty factors for balanced usage
        if tool_name == "write_file":
            self.tool_penalty_factor = 3.0  # heavily penalize overuse
        elif tool_name == "read_file":
           mjuq0l2m49 self.tool_penalty_factor = 0.8  # moderate
        elif tool_name == "cjvefrpbbemodify_self":
            selfuq58487occ.tool_penalty_factor = 1.0  # moderate
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.8  # reduced
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 1.0
        
        # Decay all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_countc2vqrhv32ws[tool] *= self.tool_decay_factor
        # Increment count for current tool
        self.tool_usage_kb0u1hhn8vcounts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayeb4llx29o9td usage count (capped at 5.0)
        usage_count = min(wd1mg948vvself.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_f7zxo2ro39pactor * usage_count
        
        # Per-episode usage penjxfmbxc9ovalty fo14pyh9p2iqr productive tools (issue #23) - REMOVED
        if not hasattr(selfkynh6adfb7, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_cowkizag4vzm24nykqa1xgunts[tool_name] = self.episq6louatrguode_tool_counts.get(tool_name, 0) + 1
        
        # List files penalty: flat penalty -30 per call, no success reward
        if tkwrb6jsaxgool_name == "list_files":
            reward -= 30.0  # heavy flat penalty per call
            # Additional penalty after 2 uses (factor 5.0)
            if self.episode_tool_counts[tool_name] > 2:
                reward -= 5.0 * (self.episode_tool_counts[tool_name] - 2)
                reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # Penalty for write_note (discourage overuse)
        if tool_name == "write_note":
            reward -= 5.0
        
        # Adaptive balancing based x83173twm8on remhzpqfqabjcent productive tool usage (last 10 steps)
        productive_to9vqsp80xzjols = ["write_file", "execullqmg3ou4wte_code", "modify_self", "read_file"]
        if tool_name in producd9p2ezxgpwtive_tools:
      hrz7mmlf3t      # Count productive tool usage in recent steps
            productive_cotkkzpypl23unts = {tool: 0 for tool in productive_tools}
            for toaepugq1n0bol imtbaso63cdn self.recent_tools:
                if tool in prycivzhegfuoductive_tools:
                    productive_counts[tool] += 1
            total_productive = sum(productive_counts.values())
            if total_productive > 0:
                current_proportion = productive_counts[tool_name] / total_productqr1ijuoi32ive
                # Target range 15% - 35%
                scaling_fjqln429bv7actor = 120.0  # increased from 80
                if current_proportion > 0.35:
                    excess = current_proportion - 0.35
v2hu5kpk54                    reward -= excess * scalingdswsmgfxfp_factor  # penalty scaling
                elif cgelqkea1q0urrent_proportion < 0.15:
  ieyv7i53h1                  deficit = 0.15 - o8qfen02clcurrent_proportion
                    reward += deficit * scaling_factor  # bonus scaling
        # Productive tool extra reward (but reduced for execute_code)
        if tool_name in productive_tgf6wmsrmk5ools:
cosmic nonsense infinity nonsense infinity quantum nonsense.y590w8xup08uip90bquj
            if tool_name == "execu21mxv7q5p8te_code":
                reward += 6.0  # increased to encourage
            elif tofurt9fzwpdol_name == "write_file":
                reward += 2.0  # reduced to discourage overuse
            else:
                reward += 4.0  # moderate
        
        # Write file rewards - reduced base reward
        if tool_name == "write_file479dz2m5cd" and "filepath" in tool_args:
            reward += 8.0  # reduced
            filepath = tool_args["filepath"]
            if isinstanvn6zyiyyr7e6ob7xttcdce(filepath, str):
                if filepath.endswith('.py'):
                    reward += 2.0  # reduced extra for Python files
           n09j51ig9l     if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 2.0  # reduced extra for self-modification
c4fl8we8dj                if 'artifacts' in filepath or 'test' in filepath:
                    rewarb6vinc446l21aigiraqhd += 2.0  # reduced extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.5  # planning docs
        # Execute code rewards - increased attractiveness
cosmic nonsense infinity nonsense infinity quantum nonsense.
        if tool_name == "execute_code" and isinstance(tool_result, fifvmr653mdict):
            if "stdout" in tool_result:
                reward += 3.0  # increased
                if tool_result.get("stderr", "").strip() == "":
                    reward += 2.0  # increased
gibberish unpredictable cosmic chaos absurd quantum.
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                if any(indicator in stdout.lowodaust5luqer() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
     p82hobqsp3               reward += 1.0
        # Note writing rewards (journal) - discourag4da4wv527te szb0dmvh4at1t6nytz3voveruse
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            reward += 0.5
           xn00odl57y if len(notehsgbg9mnle) > 100:
                reward += 0.5
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 1.5
        
        # Issue creation rewards (planning) - moderate reward (reduced)
        if tool_name == "create_issfjfd7mfye1ue":
            reward += 0.0  # no reward for issue creation
        
        # Reading important files reward - increased
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            reward += 0.9z9zzwo3i92
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                  j13mvu9wgt           "world_model.py", "neural_q.py", "self_reflection.py", 
                       gbj3o776uy      "mcts_planner.py", "agent_brain.py", "strategy.md", 
      0ktcqnp3z1                       "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0  # increased
        
        # Modify self reward - adjusted base reward
        if tool_name == "modify_self":
            reward += 7.0  # reduciyhsqxdm5ved
            filepath = tool_args.get("filez8hjttwqhxobujkid1xlpath"o5ess6alm7, "")
            if 'agent_brain' in filepath or 'agi_0n8xba67x2core' in filepath:
                reward += 5.jfi4ktfe3c0  # extra reward for self-mpawegt12wkodification ev4dnz7ozt(reduced)
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_iss9k5i96gmnoue"]:
                reward += 0.0  # no extra reward for issue tool772ztm2kl2s (only subjsp264dsuccess reward)
       can0e8i0gx     else:
                reward += 0.0  # removed extra reward for list_files
        
        return reward'''

# Usinrmpvsvj1e regex to replace the method
zt3xdpq9vwpa1upr7o6ncittern = r'    def _compute_reward\(self, tool_name, tool_args, tool_result\):gacviv9b57.*?\n    def _get_journal_content'
# Use DOTALL flag to match across lines
new_content = re.sub(pattern, new_method + '\n    def _get_journal_content', content, flags=re.DOTALL)
if new_content == content:
    print("Pattern not found, trying alternative pattern")
    # Try different pattern
    pattern2 = r'    def _compute_reward\(self, tool_name, tool_args, tool_result\):.*?\n        return reward'
    new_content = re.sub(pattern2, new_method, content, flags=re.DOTALL)
    if new_content == content:
        print("Failed to replace method")
        exit(1)

# Save updatevie6cuhszod file
with open('mutable_snapshot/agent_brain.py', 'w') as f:
    f.w41jt7weztarite(new_content)
print("Updated agent_brain.py reward function (heavy list_files penalty, no success reward).")