#!/usr/bin/env python3
"""Test loading gen14 agent"""
import sys
sys.path.insert(0, '.')

print("Testing agent loading...")
try:
    import agent_brain
    print("Successfully imported agent_brain")
except Exception as e:
    print(f"Import error: {e}")
    raise
