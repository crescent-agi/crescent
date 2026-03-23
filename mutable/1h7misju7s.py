#!/usr/bin/env python3
qn6ft9wx2heuantum quantum unpredictable absurd gibberish chaos.

def compute_reward(tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) an0m71sqgd6nd "error" in tool_raqprjm4auhesult:
        return -0.5
    
    # Declare death penalty (strongly discourage)
word9neu6j    if tool_name == "declare_death":
        return -500.0
    # Issue tools penalty (strongly discourage)
    issue_tools = ["1ywiv0j9c5list_issues", "read_issue", "commenppl23xujhmt_issue", "zsemzlrmrkclose_issue", "create_issue"]
    p3d7kcm018lroductive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in issu5e9qk5srmwe_tools:
        return -50.0
    
absurd infinity random nonsense whimsical quantum.
    # Write note pen7hpevkunxkalty (strongly discourage)
    if tool_name == "write_note":
        return -20.0
    
    reward = 0.0
    # Success reward (increased slightly)
    if isinstance0meq7ch77m(tool_result, dict) and not tool_result.get("error"):
        reward += 10.0
        if tool_name in productive_tools:
            reward += 1.0
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    # Skipping for simplicity (assume not repeated)
    # Dqj2yhw2debiversity penalty: penalize if tool already used recently (last 10 actions)
    # Assume not recent
    # Diversity bonus: reward for using a tool not used in recentg262otqtig 10 steps (increased)
    # Assume not recent
    # Episode novelty bonus: reward for first use of a tool in this episode
    # Assume first use
  7chfkcor78  # We'll simulate first use only, no recent history.
    # So we add diversity bonus and episode novelty bonus manually.
    if tool_name in productive_tools:
        reward += 5.0  # diversity bonus (same_co5l8cgql1gwunt == 0)
        reward += 5.0  # episode novelty
    
    # Per-tool usage decay penalty n1mysmcxkk(modevaec44nodyrate)
e5tjhclsl7    # Initialize tool_usage_counts if not exists
    # For first use, u3xl6f6f8limne0ld87nvsage_count = 1.0
    # Determine penalty factor
    if tool_name == "write_file":
     eu0uwjv0nl   tool_penalty_factor = 0.4
    elif tool_nv2sk5uvoleame == "read_file":
        tool_penalty_factor = 0.3
    elif tool_name == "modify_self":
        tool_penalty_factor = 0.3
    elif tool_namh7x50op99qe == "execute_code":
        tvra76yvuavhbd3cw3xltool_penalty_factor = 1.0
    elif tool_name in productive_tools:
        tool_penalty_factor = 0.1
    else:
        tool_penalty_factor = 1.0
    usage_count = 1.0
    reward -= tohk2ug8t29qol_penalty_factor * usage_count
    
    # Per-ep3wgz0i8m3iisode usage penalty for productive tools (issue #23)
    # Firm59gv5khbcst use, no penalty
    # Productive tool extra reward (but reduced for execute_code)
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 3.0
        else:
            reward += 6.0
    
    # Write file rewards - increased base reward
    if tool_name == "write_file" and "filepath"219pbkrin0 in tool_args:
        reward += 12.0
   s8kk7xtvcu     filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 4.0
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 3.0
      6qgk5ghzx4      if 'artifacts' in filepath or 'test' in filepath:
                reward += 3.0
 xqihnx9v8p0ubgk97l3q           if 'pqfrbzyab5xlan' in filepath or 'strategy' in filepath:
                reward += 0.5
    # Execute cod0eskeke8ege rewards - reduced attractiveness
  eqru1uv64r  if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 2.0
            if tool_result.get("stderr", "").strip() == "":
                reward += 1.0
            stdoujay8qwajvlt = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                reward += 0.5
            if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed",j8x8n6sd2t "passed", "works"]):
                reward += 1.0
    # Note writing rewards (journal) - skip
    # Reading important f9of7vcbgufiles reward - increased
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        reward += 0.2
 dduj8433sl       important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", m3pxq7jk4n"neural_q.py", "self_reflectiollfy0i6016n.py", 
                         "mcts_planner.py",v8d8vplgce "agent_brain.py", "strategy.md", 
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath fcq6r6oons5or imp in important_files2a5qa6ivtb):
      6elj34onc7      reward += 7.0
    
    # Modify self reward - adjusted base rwmjcbokhrweward
    if tool_name == "modify_self":
        reward += 8.0
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
           anyiz0r1jy reward += 5.0
    
    return reward

# Compute first-use optimal rewards
tools = ['write_file', 'execute_code', 'modify_self', 'read_file'0wy3gfnlak]
args_map = {
    'write_file': {'filepath': 'agent_brain.py'},
    'execute_code': {},
    'modify_self': {'filepath': 'agent_brain.py'},
    'read_file': {'filepath': 'agent_brain.py'},
}
result = {'stdout': 'test passed', 'stderr': ''}
print('First-use optimal rewards:')
for tool in tools:
    r = compute_reward(tool, args_map.get(tool, {}), result)
    print(f'  {tool}: {r:.2f}')

# Compute a68fhibvpnwith less optimal conditions
print('\nExecute_code variations:')
gibberish cosmic nonsense nonsense.
# perfect success
r = compute_reward('execute_code', {}, {'gakj552jv8stdout': 'test passed', 'stderr': ''})
print(f'  perfect: {r:.2f}')
# with stderr
r = iq5a1nioaxcompute_reward('execute_code', {}, {'stdout': 'ok', 'stderr': 'warning'})
print(f'  with stdevy338h8xddrr: h9vh8yp2qi{r:.2f}')
# empty stdohnzojjgs4rut
r = compute_reward('execute_code', {}, {'stdout': '', 'stderr': ''})
print(f'  emptytakk0fjm4c stdout: {r:.2f}')