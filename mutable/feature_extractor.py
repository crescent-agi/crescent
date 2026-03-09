#!/usr/bin/env python3
"""
Feature extractor for AGI Core state representation.
"""
import re
from collections import Counter

class FeatureExtractor:
    def __init__(self):
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
    
    def extract(self, workspace_summary, journal, actions):
        """
        Return a list of float features (normalized where possible).
        """
        features = []
        
        # 1. File type counts from workspace summary
        py_count = len(re.findall(r'\\.py\\b', workspace_summary))
        md_count = len(re.findall(r'\\.md\\b', workspace_summary))
        json_count = len(re.findall(r'\\.json\\b', workspace_summary))
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
        
        # 3. Recent action distribution (last 10 actions)
        recent = actions[-10:] if len(actions) >= 10 else actions
        tool_counts = Counter([a.get('tool') for a in recent if isinstance(a, dict)])
        total_recent = len(recent) or 1
        # Top tool frequencies
        for tool in ['write_file', 'execute_code', 'read_file', 'list_files', 'write_note']:
            features.append(tool_counts.get(tool, 0) / total_recent)
        
        # 4. Journal features
        journal_len = len(journal)
        features.append(min(journal_len, 1000) / 1000.0)  # normalized length
        # Progress keyword frequency
        kw_count = sum(1 for kw in self.progress_keywords if kw in journal.lower())
        features.append(kw_count / 10.0)
        
        # 5. Step count (from actions length)
        features.append(min(len(actions), 100) / 100.0)
        
        # Ensure fixed length (currently 5 + 5 + 2 + 1 = 13)
        # Pad or truncate to 15 for consistency
        while len(features) < 15:
            features.append(0.0)
        features = features[:15]
        return features
    
    def feature_names(self):
        """Return names of features for debugging."""
        names = [
            'py_files', 'md_files', 'json_files',
            'important_files_ratio',
            'write_file_freq', 'execute_code_freq', 'read_file_freq', 'list_files_freq', 'write_note_freq',
            'journal_length', 'progress_keywords',
            'step_count'
        ]
        # pad
        while len(names) < 15:
            names.append(f'pad_{len(names)}')
        return names[:15]


# Test
if __name__ == "__main__":
    extractor = FeatureExtractor()
    ws = "Files: agi_core.py, cognitive_architecture.py, test.py, notes.md"
    journal = "Today I made progress on AGI core. Next step: improve planning."
    actions = [
        {"tool": "read_file"},
        {"tool": "write_file"},
        {"tool": "execute_code"},
        {"tool": "read_file"},
    ]
    feats = extractor.extract(ws, journal, actions)
    names = extractor.feature_names()
    for n, f in zip(names, feats):
        print(f"{n}: {f:.3f}")