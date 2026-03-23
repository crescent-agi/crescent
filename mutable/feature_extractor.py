#!/usr/bin/env python3
"""
Enhanced Feature extractor for AGI Core state representation.
Adds per-tool usage counts over last N steps, progress indicators, and reward trend.
"""

import re
from collections import Counter, deque
import math

class FeatureExtractor:
    def __init__(self, history_size=10):
        # Important files that indicate progress
        self.important_files = [
            "agi_core.py",
            "agent_brain.py",
            "cognitive_architecture.py",
            "world_model.py",
            "neural_q.py",
            "self_reflection.py",
            "mcts_planner.py",
            "strategy.md",
            "inherited_notes.md",
        ]
        # Progress keywords in journal
        self.progress_keywords = ["progress", "improve", "agi", "plan", "next", "success", "built", "created", "learned"]
        
        # All possible tools (must match AGICoreContinuous.TOOL_NAMES)
        self.tool_names = [
            "read_file",
            "write_file",
            "list_files",
            "execute_code",
            "write_note",
            "modify_self",
            "declare_death",
            "list_issues",
            "read_issue",
            "comment_issue",
            "create_issue",
            "close_issue",
        ]
        self.history_size = history_size
        # Recent rewards storage
        self.recent_rewards = deque(maxlen=history_size)
    
    def add_reward(self, reward):
        """Record a reward for later trend calculation."""
        self.recent_rewards.append(reward)
    
    def extract(self, workspace_summary, journal, actions):
        """
        Return a list of float features (normalized where possible).
        """
        features = []
        
        # 1. File type counts from workspace summary
        py_count = len(re.findall(r'\.py\b', workspace_summary))
        md_count = len(re.findall(r'\.md\b', workspace_summary))
        json_count = len(re.findall(r'\.json\b', workspace_summary))
        total_files = py_count + md_count + json_count + 0.001  # avoid div by zero
        features.append(py_count / 10.0)          # scale
        features.append(md_count / 10.0)
        features.append(json_count / 10.0)
        
        # 2. Presence of important files
        present_count = 0
        for imp in self.important_files:
            if imp in workspace_summary:
                present_count += 1
        features.append(present_count / len(self.important_files))
        
        # 3. Recent action distribution (last N actions)
        recent = actions[-self.history_size:] if len(actions) >= self.history_size else actions
        tool_counts = Counter([a.get('tool') for a in recent if isinstance(a, dict)])
        total_recent = len(recent) or 1
        # Top tool frequencies
        for tool in ['write_file', 'execute_code', 'read_file', 'list_files', 'write_note']:
            features.append(tool_counts.get(tool, 0) / total_recent)
        
        # 4. Additional tool frequencies (modify_self, create_issue)
        modify_self_freq = tool_counts.get('modify_self', 0) / total_recent
        create_issue_freq = tool_counts.get('create_issue', 0) / total_recent
        features.append(modify_self_freq)
        features.append(create_issue_freq)
        
        # 5. Recent action entropy (diversity)
        entropy = 0.0
        for count in tool_counts.values():
            p = count / total_recent
            if p > 0:
                entropy -= p * math.log(p)
        max_entropy = math.log(len(tool_counts)) if len(tool_counts) > 1 else 1.0
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0.0
        features.append(normalized_entropy)
        
        # 6. Journal features
        journal_len = len(journal)
        features.append(min(journal_len, 1000) / 1000.0)  # normalized length
        # Progress keyword frequency
        kw_count = sum(1 for kw in self.progress_keywords if kw in journal.lower())
        features.append(kw_count / 10.0)
        
        # 7. Step count (from actions length)
        features.append(min(len(actions), 100) / 100.0)
        
        # 8. Per-tool usage counts over last N steps (12 new features)
        # Initialize zero counts for all tools
        per_tool_counts = {tool: 0 for tool in self.tool_names}
        for action in recent:
            tool = action.get('tool')
            if tool in per_tool_counts:
                per_tool_counts[tool] += 1
        # Normalize by history size and add as features
        for tool in self.tool_names:
            features.append(per_tool_counts[tool] / self.history_size)
        
        # 9. Progress indicators (episode-level)
        # Count new Python files created in this episode from write_file actions
        py_files_recent = 0
        for action in recent:
            if action.get('tool') == 'write_file':
                args = action.get('args', {})
                filepath = args.get('filepath', '')
                if isinstance(filepath, str) and '.py' in filepath:
                    py_files_recent += 1
        features.append(py_files_recent / self.history_size)
        
        # Successful executions count (episode-level)
        successful_executions_recent = 0
        for action in recent:
            if action.get('tool') == 'execute_code':
                # Check if result indicates success (no error)
                # We'll just count executions for now.
                successful_executions_recent += 1
        features.append(successful_executions_recent / self.history_size)
        
        # 10. Recent reward trend (actual)
        if len(self.recent_rewards) > 0:
            avg_reward = sum(self.recent_rewards) / len(self.recent_rewards)
            # Normalize reward trend: assume reward range [-5, 10]; clip and scale
            clipped = max(-5.0, min(avg_reward, 10.0))
            normalized = (clipped + 5.0) / 15.0  # maps [-5,10] to [0,1]
            features.append(normalized)
        else:
            features.append(0.5)  # neutral
        
        # Ensure fixed length (currently 15 original + 12 per-tool + 3 new = 30)
        # Verify length
        expected_features = 30
        if len(features) != expected_features:
            # Pad or truncate
            while len(features) < expected_features:
                features.append(0.0)
            features = features[:expected_features]
        return features
    
    def feature_names(self):
        """Return names of features for debugging."""
        names = [
            'py_files', 'md_files', 'json_files',
            'important_files_ratio',
            'write_file_freq', 'execute_code_freq', 'read_file_freq', 'list_files_freq', 'write_note_freq',
            'modify_self_freq', 'create_issue_freq',
            'action_entropy',
            'journal_length', 'progress_keywords',
            'step_count'
        ]
        # Per-tool usage counts
        for tool in self.tool_names:
            names.append(f'{tool}_recent')
        # Progress indicators
        names.append('py_files_created_recent')
        names.append('successful_executions_recent')
        names.append('reward_trend')
        return names[:30]


# Test
if __name__ == "__main__":
    extractor = FeatureExtractor()
    ws = "Files: agi_core.py, cognitive_architecture.py, test.py, notes.md"
    journal = "Today I made progress on AGI core. Next step: improve planning."
    actions = [
        {"tool": "read_file"},
        {"tool": "write_file", "args": {"filepath": "test.py"}},
        {"tool": "execute_code"},
        {"tool": "read_file"},
    ]
    # Simulate some rewards
    extractor.add_reward(1.0)
    extractor.add_reward(2.5)
    extractor.add_reward(0.5)
    feats = extractor.extract(ws, journal, actions)
    names = extractor.feature_names()
    print(f"Total features: {len(feats)}")
    for n, f in zip(names, feats):
        print(f"{n}: {f:.3f}")
    print("\nPer-tool counts:")
    for i, tool in enumerate(extractor.tool_names):
        idx = 15 + i
        print(f"  {tool}: {feats[idx]:.3f}")