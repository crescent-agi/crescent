#!/usr/bin/env python3
"""
Test reward calculation for various actions.
"""
import sys
sys.path.append('.')

# Copy reward function from agent_brain
def compute_reward(tool_name, tool_args, tool_result, last_tool=None, recent_tools=None):
    """Improved reward shaping with moderate anti-spamming and diversity incentives."""
    # If error, penalize and skip positive rewards
    if isinstance(tool_result, dict) and "error" in tool_result:
        return -0.5
    
    # Declare death penalty (strongly discourage unless after many steps)
    if tool_name == "declare_death":
        return -2.0
    
    reward = 0.0
    # Success reward
    if isinstance(tool_result, dict) and not tool_result.get("error"):
        reward += 0.1
    
    # Recency penalty: discourage using same tool consecutively
    if last_tool and tool_name == last_tool:
        reward -= 0.5  # moderate penalty
    # last_tool = tool_name  # we'll update outside
    
    # Diversity penalty: penalize if tool already used recently (last 5 actions)
    if recent_tools is None:
        recent_tools = []
    # Count occurrences of same tool in recent history
    same_count = recent_tools.count(tool_name)
    if same_count > 0:
        reward -= 0.2 * same_count  # moderate penalty proportional to frequency
    # Update recent tools (deque automatically maintains maxlen)
    # we'll update outside
    
    # Diversity bonus: reward for using a tool not used in recent 5 steps
    if same_count == 0:
        reward += 0.2
    
    # Write file rewards - encourage code creation but reduce spamming
    if tool_name == "write_file" and "filepath" in tool_args:
        reward += 0.1  # base for writing (reduced)
        filepath = tool_args["filepath"]
        if isinstance(filepath, str):
            if filepath.endswith('.py'):
                reward += 0.5  # extra for Python files (more valuable)
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 0.8  # extra for self-modification (critical)
            if 'artifacts' in filepath or 'test' in filepath:
                reward += 0.3  # extra for test/artifact creation
            if 'plan' in filepath or 'strategy' in filepath:
                reward += 0.2  # planning docs
    
    # Execute code rewards - encourage testing and running, but reduce base reward
    if tool_name == "execute_code" and isinstance(tool_result, dict):
        if "stdout" in tool_result:
            reward += 0.2  # reduced base reward
            # extra if execution succeeded without stderr errors
            if tool_result.get("stderr", "").strip() == "":
                reward += 0.2  # reduced
            # extra if output contains meaningful results (e.g., not empty)
            stdout = tool_result.get("stdout", "").strip()
            if len(stdout) > 10:
                reward += 0.1  # reduced
            # bonus if output indicates success
            if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                reward += 0.2  # reduced
    
    # Note writing rewards (journal) - reduce spamming
    if tool_name == "write_note":
        note = tool_args.get("note", "")
        # Base reward lower
        reward += 0.1
        if len(note) > 100:  # longer notes more valuable
            reward += 0.2
        if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
            reward += 0.4  # higher for relevant keywords
    
    # Issue creation rewards (planning) - reduced to avoid spamming
    if tool_name == "create_issue":
        reward += 0.2  # reduced from 0.5
    
    # Reading important files reward - increased to encourage knowledge gathering
    if tool_name == "read_file":
        filepath = tool_args.get("filepath", "")
        important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.py", "agent_brain.py", "strategy.md", 
                         "train_agi_core.py", "run_training.py"]
        if any(imp in filepath for imp in important_files):
            reward += 0.5  # increased
    
    # Modify self reward - encourage self-improvement but reduce base
    if tool_name == "modify_self":
        reward += 0.3  # reduced
        filepath = tool_args.get("filepath", "")
        if 'agent_brain' in filepath or 'agi_core' in filepath:
            reward += 0.5
    
    # Encourage exploration: reward for using underused tools (list_files, list_issues, read_issue, comment_issue, close_issue)
    exploration_tools = ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]
    if tool_name in exploration_tools:
        reward += 0.2
    
    return reward

# Simulate some actions
print("Reward calculation examples:")
print("="*50)
# Success without any penalties
last_tool = None
recent = []
tool = "list_files"
args = {"directory": "."}
result = {"success": True}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool}: {r}")

# write_file python
tool = "write_file"
args = {"filepath": "test.py", "content": "print('hello')"}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool} (python): {r}")

# write_note with keywords
tool = "write_note"
args = {"note": "Making progress on AGI. Next step: improve planning."}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool} (progress): {r}")

# execute_code with stdout
tool = "execute_code"
args = {"code": "print('test')", "language": "python"}
result = {"stdout": "test passed", "stderr": ""}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool} (success): {r}")

# Now with recency penalty (same tool consecutively)
last_tool = "write_file"
recent = ["write_file"]
tool = "write_file"
args = {"filepath": "test2.py", "content": "print('again')"}
result = {"success": True}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool} (consecutive): {r}")

# Diversity penalty (same tool used twice in recent 5)
last_tool = "write_file"
recent = ["write_file", "list_files", "write_file", "read_file"]
tool = "write_file"
args = {"filepath": "test3.py", "content": "again"}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool} (multiple recent): {r}")

# Explore exploration tools
tool = "list_issues"
args = {}
r = compute_reward(tool, args, result, last_tool, recent)
print(f"{tool}: {r}")