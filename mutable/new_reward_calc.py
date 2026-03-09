#!/usr/bin/env python3

def compute_reward(tool_name, tool_args, tool_result):
    # If error, penalize
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage)
    if tool_name == "declare_death":
        return -500.0
    # Issue tools penalty (strongly discourage)
    issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    if tool_name in issue_tools:
        return -50.0
    
    # Write note penalty (strongly discourage)
    if tool_name == "write_note":
        return -20.0
    
    reward = 0.0
    # Success reward (increased slightly)
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 10.0
        if tool_name in productive_tools:
            reward += 1.0
    
    # Recency penalty: discourage using same tool consecutively (reduced)
    # Skipping for simplicity (assume not repeated)
    # Diversity penalty: penalize if tool already used recently (last 10 actions)
    # Assume not recent
    # Diversity bonus: reward for using a tool not used in recent 10 steps (increased)
    # Assume not recent
    # Episode novelty bonus: reward for first use of a tool in this episode
    # Assume first use
    # We'll simulate first use only, no recent history.
    # So we add diversity bonus and episode novelty bonus manually.
    if tool_name in productive_tools:
        reward += 5.0  # diversity bonus (same_count == 0)
        reward += 5.0  # episode novelty
    
    # Per-tool usage decay penalty (moderate)
    # Initialize tool_usage_counts if not exists
    # For first use, usage_count = 1.0
    # Determine penalty factor
    if tool_name == "write_file":
        tool_penalty_factor = 0.4
    elif tool_name == "read_file":
        tool_penalty_factor = 0.3
    elif tool_name == "modify_self":
        tool_penalty_factor = 0.3
    elif tool_name == "execute_code":
        tool_penalty_factor = 1.0
    elif tool_name in productive_tools:
        tool_penalty_factor = 0.1
    else:
        tool_penalty_factor = 1.0
    usage_count = 1.0
    reward -= tool_penalty_factor * usage_count
    
    # Per-episode usage penalty for productive tools (issue #23)
    # First use, no penalty
    # Productive tool extra reward (but reduced for execute_code)
    if tool_name in productive_tools:
        if tool_name == "execute_code":
            reward += 3.0
        else:
            reward += 6.0
    
    # Write file rewards - increased base reward
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 12.0
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 4.0
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 3.0
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 3.0
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 0.5
    # Execute code rewards - reduced attractiveness
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 2.0
            if tool_result.get("stderr", "").strip() == "":
                reward += 1.0
            stdout = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                reward += 0.5
            if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                reward += 1.0
    # Note writing rewards (journal) - skip
    # Reading important files reward - increased
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        reward += 0.2
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.py", "agent_brain.py", "strategy.md", 
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 7.0
    
    # Modify self reward - adjusted base reward
    if tool_name == "modify_self":
        reward += 8.0
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 5.0
    
    return reward

# Compute first-use optimal rewards
tools = ['write_file', 'execute_code', 'modify_self', 'read_file']
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

# Compute with less optimal conditions
print('\nExecute_code variations:')
# perfect success
r = compute_reward('execute_code', {}, {'stdout': 'test passed', 'stderr': ''})
print(f'  perfect: {r:.2f}')
# with stderr
r = compute_reward('execute_code', {}, {'stdout': 'ok', 'stderr': 'warning'})
print(f'  with stderr: {r:.2f}')
# empty stdout
r = compute_reward('execute_code', {}, {'stdout': '', 'stderr': ''})
print(f'  empty stdout: {r:.2f}')