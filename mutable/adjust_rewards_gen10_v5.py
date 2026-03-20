#!/usr/bin/env python3
import re
import sys

def load_file(path):
    with open(path, 'r') as f:
        return f.read()

def save_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def replace_method(source, new_method):
    lines = source.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def _compute_reward'):
            start = i
            break
    if start is None:
        raise ValueError('Method not found')
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines):
        if lines[end].strip() == '':
            end += 1
            continue
        line_indent = len(lines[end]) - len(lines[end].lstrip())
        if line_indent <= indent:
            break
        end += 1
    new_lines = lines[:start] + [new_method + '\n'] + lines[end:]
    return ''.join(new_lines)

new_method = '''    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Reward shaping with balanced per-tool decay, stronger productive incentives, and novelty bonuses."""
        # If error, penalize
        if isinstance(tool_result, dict) and "error" in tool_result:
            return -0.5
        
        # Declare death penalty (strongly discourage)
        if tool_name == "declare_death":
            return -500.0  # heavily penalize suicide
        # Issue tools penalty (strongly discourage)
        issue_tools = ["list_issues", "read_issue", "comment_issue", "close_issue", "create_issue"]
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        if tool_name in issue_tools:
            return -50.0  # heavy penalty, no other rewards
        
        # Write note penalty (strongly discourage)
        if tool_name == "write_note":
            return -20.0  # heavy penalty, no other rewards
        
        reward = 0.0
        # Success reward (increased slightly)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 8.0  # increased from 5.0
            # Baseline reward for productive tools
            if tool_name in productive_tools:
                reward += 1.0
        
        # Recency penalty: discourage using same tool consecutively (reduced)
        if hasattr(self, 'last_tool') and tool_name == self.last_tool:
            reward -= 0.1  # reduced penalty for immediate repetition
        self.last_tool = tool_name
        
        # Diversity penalty: penalize if tool already used recently (last 10 actions)
        if not hasattr(self, 'recent_tools'):
            self.recent_tools = []
        same_count = self.recent_tools.count(tool_name)
        if same_count > 0:
            reward -= 0.2 * same_count  # penalty per occurrence
        self.recent_tools.append(tool_name)
        if len(self.recent_tools) > 10:
            self.recent_tools.pop(0)
        
        # Diversity bonus: reward for using a tool not used in recent 10 steps (reduced)
        if same_count == 0 and tool_name in productive_tools:
            reward += 3.0  # reduced from 5.0
        
        # Episode novelty bonus: reward for first use of a tool in this episode
        if not hasattr(self, 'episode_tools'):
            self.episode_tools = set()
        if tool_name not in self.episode_tools:
            if tool_name in productive_tools:
                reward += 3.0  # reduced from 5.0
            self.episode_tools.add(tool_name)
        # Per-tool usage decay penalty (moderate)
        if not hasattr(self, 'tool_usage_counts'):
            self.tool_usage_counts = {}
            self.tool_decay_factor = 0.85
        
        # Productive tools have lower penalty factor (adjusted per issue #23)
        productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
        # Special penalty factors for balanced usage
        if tool_name == "write_file":
            self.tool_penalty_factor = 3.0  # heavily penalize overuse
        elif tool_name == "read_file":
            self.tool_penalty_factor = 0.8  # moderate
        elif tool_name == "modify_self":
            self.tool_penalty_factor = 1.0  # moderate
        elif tool_name == "execute_code":
            self.tool_penalty_factor = 0.8  # reduced
        elif tool_name in productive_tools:
            self.tool_penalty_factor = 0.1  # fallback
        else:
            self.tool_penalty_factor = 1.0
        
        # Decay all counts
        for tool in self.tool_usage_counts:
            self.tool_usage_counts[tool] *= self.tool_decay_factor
        # Increment count for current tool
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1.0
        # Apply penalty proportional to decayed usage count (capped at 5.0)
        usage_count = min(self.tool_usage_counts[tool_name], 5.0)
        reward -= self.tool_penalty_factor * usage_count
        
        # Per-episode usage penalty for productive tools (issue #23)
        if not hasattr(self, 'episode_tool_counts'):
            self.episode_tool_counts = {}
        self.episode_tool_counts[tool_name] = self.episode_tool_counts.get(tool_name, 0) + 1
        
        # Write file: penalty after 1 use (factor 15.0)
        if tool_name == "write_file" and self.episode_tool_counts[tool_name] > 1:
            reward -= 15.0 * (self.episode_tool_counts[tool_name] - 1)
        # Read file: penalty after 1 use (factor 3.0)
        if tool_name == "read_file" and self.episode_tool_counts[tool_name] > 1:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 1)
        # Modify self: penalty after 1 use (factor 4.0)
        if tool_name == "modify_self" and self.episode_tool_counts[tool_name] > 1:
            reward -= 4.0 * (self.episode_tool_counts[tool_name] - 1)
        # Execute code: penalty after 1 use (factor 3.0)
        if tool_name == "execute_code" and self.episode_tool_counts[tool_name] > 1:
            reward -= 3.0 * (self.episode_tool_counts[tool_name] - 1)
        
        # List files penalty after 5 uses (issue #24)
        if tool_name == "list_files" and self.episode_tool_counts[tool_name] > 5:
            reward -= 1.0 * (self.episode_tool_counts[tool_name] - 5)
        # Penalty for write_note (discourage overuse)
        if tool_name == "write_note":
            reward -= 5.0
        
        # Productive tool extra reward (but reduced for execute_code)
        if tool_name in productive_tools:
            if tool_name == "execute_code":
                reward += 6.0  # increased to encourage
            elif tool_name == "write_file":
                reward += 2.0  # reduced to discourage overuse
            else:
                reward += 4.0  # moderate
        
        # Write file rewards - reduced base reward
        if tool_name == "write_file" and "filepath" in tool_args:
            reward += 8.0  # reduced
            filepath = tool_args["filepath"]
            if isinstance(filepath, str):
                if filepath.endswith('.py'):
                    reward += 2.0  # reduced extra for Python files
                if 'agent_brain' in filepath or 'agi_core' in filepath:
                    reward += 2.0  # reduced extra for self-modification
                if 'artifacts' in filepath or 'test' in filepath:
                    reward += 2.0  # reduced extra for test/artifact creation
                if 'plan' in filepath or 'strategy' in filepath:
                    reward += 0.5  # planning docs
        # Execute code rewards - increased attractiveness
        if tool_name == "execute_code" and isinstance(tool_result, dict):
            if "stdout" in tool_result:
                reward += 3.0  # increased
                if tool_result.get("stderr", "").strip() == "":
                    reward += 2.0  # increased
                stdout = tool_result.get("stdout", "").strip()
                if len(stdout) > 10:
                    reward += 0.5
                if any(indicator in stdout.lower() for indicator in ["test passed", "ok", "success", "completed", "passed", "works"]):
                    reward += 1.0
        # Note writing rewards (journal) - discourage overuse
        if tool_name == "write_note":
            note = tool_args.get("note", "")
            reward += 0.5
            if len(note) > 100:
                reward += 0.5
            if any(keyword in note.lower() for keyword in ["progress", "improve", "agi", "plan", "next", "insight", "discover"]):
                reward += 1.5
        
        # Issue creation rewards (planning) - moderate reward (reduced)
        if tool_name == "create_issue":
            reward += 0.0  # no reward for issue creation
        
        # Reading important files reward - increased
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            reward += 0.2
            important_files = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                             "world_model.py", "neural_q.py", "self_reflection.py", 
                             "mcts_planner.py", "agent_brain.py", "strategy.md", 
                             "train_agi_core.py", "run_training.py"]
            if any(imp in filepath for imp in important_files):
                reward += 7.0  # increased
        
        # Modify self reward - adjusted base reward
        if tool_name == "modify_self":
            reward += 7.0  # reduced
            filepath = tool_args.get("filepath", "")
            if 'agent_brain' in filepath or 'agi_core' in filepath:
                reward += 5.0  # extra reward for self-modification (reduced)
        
        # Encourage exploration: reward for using underused tools, but less for issue tools
        if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:
            if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
                reward += 0.0  # no extra reward for issue tools (only success reward)
            else:
                reward += 0.0  # removed extra reward for list_files
        
        return reward'''

# Main
if __name__ == '__main__':
    agent_brain_path = 'agent_brain.py'
    backup_path = 'agent_brain.py.backup_gen10_v5'
    content = load_file(agent_brain_path)
    save_file(backup_path, content)
    print(f'Backup saved to {backup_path}')
    new_content = replace_method(content, new_method)
    save_file(agent_brain_path, new_content)
    print('Reward method updated v5.')