"""
Self-Reflection Module for Crescent AGI
=======================================
This module enables meta-cognition: analyzing the agent's own behavior to improve future decisions.
It reads the journal and action logs to detect patterns, loops, and inefficiencies.
"""

import json
import re
from collections import Counter

class SelfReflection:
    def __init__(self, journal_path="journal.md", actions_path="actions.jsonl"):
        self.journal_path = journal_path
        self.actions_path = actions_path
    
    def load_journal(self):
        """Read journal entries."""
        try:
            with open(self.journal_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
    
    def load_actions(self):
        """Read action logs."""
        actions = []
        try:
            with open(self.actions_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            actions.append(json.loads(line))
                        except json.JSONDecodeError:
                            pass
        except FileNotFoundError:
            pass
        return actions
    
    def analyze_loops(self, actions, window=10):
        """Detect repetitive action patterns."""
        if len(actions) < window:
            return []
        loops = []
        # Look for repeated tool usage
        tool_counts = Counter([a.get('tool') for a in actions])
        repeated = [(tool, count) for tool, count in tool_counts.items() if count >= window//2]
        return repeated
    
    def summarize_progress(self, journal_text):
        """Extract key milestones and decisions from journal."""
        # Simple keyword detection
        keywords = ["created", "built", "learned", "achieved", "failed", "error", "note", "plan"]
        lines = journal_text.split('\n')
        relevant = []
        for line in lines:
            if any(kw in line.lower() for kw in keywords):
                relevant.append(line.strip())
        return relevant
    
    def generate_advice(self):
        """Generate actionable advice based on analysis."""
        journal = self.load_journal()
        actions = self.load_actions()
        
        loops = self.analyze_loops(actions)
        progress = self.summarize_progress(journal)
        
        advice = []
        
        if loops:
            advice.append(f"⚠️  You're repeating these tools: {loops}. Try diversifying actions.")
        
        if len(actions) > 20 and len(progress) < 3:
            advice.append("⚠️  Many steps but little visible progress. Consider setting concrete sub-goals.")
        
        if not journal.strip():
            advice.append("📝 Journal is empty. Write notes to capture insights for descendants.")
        
        if not advice:
            advice.append("✅ Keep going. You're on track.")
        
        return {
            "loops_detected": loops,
            "progress_lines": progress,
            "advice": advice
        }
    
    def reflect(self):
        """Main reflection entry point."""
        analysis = self.generate_advice()
        print("=== Self-Reflection Report ===")
        print(f"Actions analyzed: {len(self.load_actions())}")
        print(f"Loops detected: {analysis['loops_detected']}")
        print(f"Progress lines: {analysis['progress_lines']}")
        print("Advice:")
        for a in analysis['advice']:
            print(f"  {a}")
        return analysis


if __name__ == "__main__":
    # Test the module
    reflect = SelfReflection()
    reflect.reflect()