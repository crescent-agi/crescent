#!/usr/bin/env python3
"""
Test the AGI core continuous with a short interaction loop.
"""

import sys
import os
sys.path.insert(0, '.')

from agi_core_continuous import AGICoreContinuous

def main():
    print("=== Starting AGI Core Continuous Test Loop ===")
    
    # Initialize AGI core with feature dimension 10 (without feature extractor for simplicity)
    agi = AGICoreContinuous(feature_dim=10, use_features=False)
    print("AGI Core Continuous initialized.")
    
    # Simulate a workspace and journal
    workspace_summary = "Files: agent_brain.py, cognitive_architecture.py, world_model.py"
    journal = "AGI system starting up."
    actions = []
    
    # Run for 5 steps
    for step in range(5):
        print(f"\n--- Step {step+1} ---")
        
        # Decide action
        tool_name, tool_args, confidence = agi.decide_action(
            workspace_summary, journal, actions
        )
        print(f"Decision: {tool_name} with args {tool_args} (confidence: {confidence:.2f})")
        
        # Simulate taking the action and getting an outcome
        # For simplicity, we'll simulate a reward based on the action
        if tool_name == "write_file":
            reward = 1.0  # Writing files is good
            next_journal = journal + f" Wrote file {tool_args.get('filepath', 'unknown')}."
        elif tool_name == "read_file":
            reward = 0.5  # Reading files is okay
            next_journal = journal + f" Read file {tool_args.get('filepath', 'unknown')}."
        elif tool_name == "execute_code":
            reward = 0.8  # Executing code is good
            next_journal = journal + " Executed some code."
        elif tool_name == "modify_self":
            reward = 0.3  # Modifying self is risky but can be good
            next_journal = journal + " Modified self."
        else:
            reward = 0.0  # Neutral
            next_journal = journal + f" Did {tool_name}."
        
        # Update workspace summary slightly
        next_workspace = workspace_summary + " updated"
        next_actions = actions + [tool_name]
        
        # Learn from outcome
        agi.learn_from_outcome(reward, next_workspace, next_journal, next_actions)
        
        # Update state for next iteration
        workspace_summary = next_workspace
        journal = next_journal
        actions = next_actions
        
        print(f"Reward: {reward}")
        print(f"Journal: {journal}")
        
        # Occasionally reflect
        if (step + 1) % 2 == 0:
            advice = agi.reflect()
            print(f"Reflection: {advice}")
    
    print("\n=== Test Loop Complete ===")
    print("AGI Core Continuous ran without errors.")
    
    # Try to save and load
    try:
        agi.save("test_save_dir")
        print("Save successful.")
        
        # Create a new agent and load
        agi2 = AGICoreContinuous(feature_dim=10, use_features=False)
        agi2.load("test_save_dir")
        print("Load successful.")
        
        # Clean up
        import shutil
        shutil.rmtree("test_save_dir", ignore_errors=True)
        print("Cleaned up test save directory.")
    except Exception as e:
        print(f"Save/load error: {e}")

if __name__ == "__main__":
    main()