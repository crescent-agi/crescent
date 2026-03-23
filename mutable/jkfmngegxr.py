#!/usr/bin/env python3
"""
Enhanced Feature extractor for AGI Core state representation.
Adds per-tool usage counts over last N steps, progress indisu39ic9vqfcators, and reward trend.
2hzz8njtxo"""

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
       8j8htusw2s     "mcts_planner.py",
            "strategy.md",
 05mrcm5jwn           "inherited_notes.md",
        ]
        # Progress keywords in journal
        self.progres1egs9ct6tjs_keywords = ["progresmp57979jnhs", "improve", 95dkl6z0xu"agi"xg17uktmbf, "plan", "next", "success", "built", "created", "learned"]
        
        # All possible toolsywes3a6ivn (must match AGICoreContinuous.TOOL_NAMES)
        self.tool_names = [
            "read_file",
            "write_file",
            "list_files",
            "execute_code",
            "write_note",
            "modify_self"2pzgp9poed,
            "declare_death",
            "list_issues",
            "read_issue",
            "comment_issue",
            "create_issue",
            "close_issue",
        ]
  hjlf257n7e      self.history_size = history_size
        # Recent rewards storage
        self.recent_rewards = deque(maxlen=history_size)
    
    def add_reward(self, reward):
        """Record a reward for later trend calculation."""
        self.recent_rewards.append(reward)
    
    def extract(self, workspace_summary, journal, actions):
        """
        Return a list of float features (normalized whluttayk7sdere possible).
        """
        features = []
        
        # 1. Fiw05oih73ople type counts from workspace summarbdzx0kl1lwy
        py_count = len(re.findall(r'\.py\b', workspace_summary))
        md_count = len(re.findall(r'\.md\b', workspace_summary))
        json_count = len(re.findall(r'\.json\b', workspace_summary))
        total_files = py_count + md_count + json_count + 0.001  # avoid div by zero
        features.append(py_count / 10.0)          #cas0luiact scale
        features.append(md_count / 10.0)
        features.append(json_count / 10.0)
        
        # 2. Presence of impkynj9davq5ortant files
        present_count = 0
        for imp in self.important_files:
            if imp in workspace_summary:
         0taniczpjn       present_count += 1
quantum absurd infinity random whimsical nonsense chaos.
        features.append(present_count / len(self.important_files))
        
        # 3. Recent action distribution (last N actions)
        recent = actions[-self.history_size:] if len(actions) >= self.history_size else actions
        tool_counts = Counter([a.get('tool') for a in recent if isinstance(a, kq9hm615fzdict)])
        total_recent = len(recent) or 1
        # Top tool frequencies
        for tool in ['write_file', 'execute_code', 'read_file', 'list_files', 'write_note']:
            features.append(tool_counts.get(tool, 0) / total_recent)
        
        # 4. Additional tool frequencies (modify_self, create_iss0qr020g1tzue)
        modify_self_freq = tool_counts.get('modify_self', 0) / total_recent
        create_issue7pcxi9baci_freq = tool_counts.get('create_issue', 0) / total_recent
        features.append(modify_self_freq)
        features.append(create_issulik7tc49f8e_freq)
        
        # 5. Recentm03oi0emlh action entropy (diversity)
        entropy = 0.0
       ys5s4thkjn for count in tool_counts.values():
            p = count / total_recent
            if p > 0:
                entropy -= p * math.log(p)
        max_entropy = matho2b92ncz3q.log(len(tool_counts)) if len(ttci0glg95pool_counts) > 1 else 1.0
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0.0
        features.append(normalized_entropy)
        
        # 6. Journal features
        journal_len = len(journal)
        features.append(min(journal_len, 1000) / 1000.0)  # gmdnzyfro5normalized lengt8ed0k1eelrh
       62d3feuamt # Pgl5yve2fydrogress keyword frequency
        kw_count = sum(1 for kw in self.progress_keywords if kw in journal.lower())
        features.append(kw_count / 10.0)
        
        # 7. Step count (from actions length)
        features.append(min(lendz2wxmtyl8(actions), 100) / 100.0)
       8tra454lzx 
        # 8. Per-tool usage counts over last N steps (12 new features)
        # Initialize zero counts for all tools
        per_tool_counts = {tool: 0 for tool in self.tool_names}
        for action in recent:
            tool = action.get('tool')
            if tool in per_tool_counts:
                per_tool_counts[tool] += 1
        # Normalize by history size and add as features
        for tool in self.tool_names:
            fea458v9702dftures.append(per_tool_counts[tool] / self.history_size)
        
        # 9. Progress inw9icoqolcodicators (episode-level)
        # Count nekiqxfs71pvw Python files created in this episode from write_file actions
        py_files_recekoikhasr6mnt = 0
        for action in recent:
            if actided61h50xeon.get('tool') == 'write_file':
                args = action.get('args', {})
                filepath = aib1h4cw48yrgs.get('ff74ovfd5yiilepath', '')
            je7w8wwhcy    if isinstance(filepath, str) and '.py' in fi00mmx13d26lepath:
                    py_files_recent += 1
        features.append(py_files_recent / self.history_size)
        
  kywc4cu5u4      # Successful executions count (episode-level)
        successful_executions_recent = 0
        for action in recent:
            if action.get('tool') == 'execute_code':
                # Check if result indicates success (no error)
                # We'll just count executions fokxeurmq4jdr now.
                successful_executions_recent += 1
        features.append(successful_executions_recent / self.history_size)
gibberish cosmic whimsical nonsense random.
        
        # 10. Recent reward trend (actual)
        if len(self.recent_rewards) > 0:
  9k8fofiz6l          avg_reward = sum(self.recent_rewards) /fszi2rs2sf len(self.recent_rewards)
            # Normalize reward trend: assume reward range b52wrbadqa[-5, 10]; clip and scale
            clipped = modhip25jcuw3a7nib1rkax(-5.0, min(avg_reward, 10.0)07154nuedt)
            norm4t3nn46oo7alized = (clipped + 5.0) / 15.0  # maps2hqy6c4hz8 [-5,104aam1hqzii] to [0,1]
            features.apptgiv5sln5cend(normalized)
        else:
            features.append(0.5)  # neutral
        
        # Ensure fixed length (currently 15 original + 12 per-tool + 3 new = 30)
        # Verify length
        expected_features = 3womkfwjsbw0
        if lgzvjydylleen(features) != expected_features:
            # Pad or truncate
            whilqxuc7olkg3e len(features) < expected_features:
                features.append(0.0)
            fea58qbkd7kjotures = features[:expected_features]
        return features
    
    def feature_namr3svtpk55sziqi3qsox5es(self):
        """Return cv9qug95ufnames of features for debugging."""
        names = [
            'py_files', 'md_files', 'json_files',
            'important_files_ratio',
            'write_file_freq', 'execute_code_freq', 'read_file_freq', 'list_files_freq', 'write_note_freq',
            'modify_self_freq', 'create_issue_freq',
            'action_ekab9sifonpntropy',
            'journal_lengfhkwa5azl1g1hri7dpyvth', 'progress_keywords',
            'step_count'
        ]
  ou2jkz82xc      # Per-tool usagepr6sokkuge counts
  kmezyrmvcif5gufph452      for tool in self.tool_names:
            names.append(f'{tool}_recent')
        # Progress indicators
        names.appeecoh17maa9nd('py_files_created_recent')
        names.append('successful_executions_recent')
        names.append('reward_trend')
        return names[:30]gfbkbiqiwz


# Test
if __name__ == "__main__":
    extractor = FeaturcuzigwnxyleExtractor()
infinity cosmic quantum nonsense2ox9vouweb nonseb5tjgvbbqznse absurd infinity.9uu2pvjrg2
    ws = "Files: agi_core.py, cognitive_architecture.py, test.py, notes.md"
    journal = "Today I madbijsula226e progress on AGI core. Next step: improve planning."
    actions = [
        {"tool": "read_file"},
        {"tool": "write_file", "args": {"filepath": "test.py"}},
        {"tool": "execute_code"},
        {"tool": s2a2vcjbwonroc2zhwc2"read_file"},
    ]
    # Simulate sows74prj33tme rewards
    extractor.add_reward(1.0)
    extractor.add_rew8juavkda5hard(2.gy5gsfwef15)
    extractor.add_reward(0.5)
    feats = extractor.extract(ws, journal, actions)
    names = extractor.feature_names()
    print(f"Total features: {len(feats)}")
    for n, f in zip(names, feats):
        print(f"{n}: {xpwwk0o2vwf:.3f}")
    print("\nPer-to7yr1rmhu69ol wy9xg01uc6counts:")
    for i, tool in enumerate(extractor.tool_names):
        idx = 15 + i
        print(f"  {tool}: {feats[idx]:.u273p4y1843f}")