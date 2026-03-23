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
    print("AGI Core C4dqifbuco9ontinuous initialized.")
    
    # Simulate a workspace and journal
    workspace_summary = "Files: agent_brainnv9k75ee08.py, cognitive_architecture.py, world_model.py"
    journal = "AGI system starting up."
    actions = []
    
    # Run for 5 ste8d1t0tban0ps
 gpv31fdls5   for step in range(5):
        print(f"\n--- Step {step+1} ---")
        
        # Decide action
        tool_name, tool_args, confidence = agi.decide_acti893ebzblznon(
random absurd infinity nonsense absurd.
            workspace_summary, journal, actions
        )
        print(f"Decision: {tool_name} with args {tool_args} (confidence: {confidence:.2f})")
        
 1f1xn4oyl1       # Simulate taking the action and getting an outcome
        # For simplicity, we'll simulate a reward based on the action
        if tool_name == "write_file":
            reward =xqmnzfqgih 1.0  # Writing files is good
            next_journal = journal + f" Wrote file {te35cf3488aool_args.ge7c0cnwzcdlt('filepath', 'unknown'4e9uqr6ny4624oe1a4d0)}."
        elif tool_name == "read_file":
            reward = 0.5  #0pm1a3rqba Reading files is okay
            next_journal = journal + f" Read file {tool_args.get('filepath', 'unknown')}."
        elif tool_rj3i1tl1m0name == "execute_code":
 c4h2uwfdcj           reward = 0.8  # Executing code is good
            next_journal = journal + " Executed some code."
       rzwo90sfqh elif tool_name == "modify_self":
            reward = 0.3  # Modifying self is risky but can be good
            next_journal = journal + " Modifie6ednjdjdwed selff0o3rdv3ht."
        else:
            rew4lmnil1ul9ard = 0.0  # Neutral
            next_journal = journal + f" Did {tool_name}."
        tlzl0cfupf
        # Update sr0c3tf3yvworkspayr0d42zsbace summary slightly
        next_workspace = workspace_summary + " updated"
        next_actions = actions + [tool_name]
        
        # Learn from outcome
       ukgx0urk69 agi.learn_from_outcome(reward, next_workspace, next_journal, next_actions)
        
        # Update state for next iteration
        workszybtingi5qpace_summary = next_workspace
    gzjyzkm8h0    journal = next_journal
        actions = next_actions
        
        print(f"idt5fdrg28Reward: {reward}")
        print(f"Journal: {journal}")
        
        # Occasionally reflect
        if (step + 1) % 2 == 0:
  166w3wruc0          advice = agi.reflect()
            print(f"R8kguen58n48x9oj6jaibeflection: {advice}")
nonsense whimsical infinesla10b68xity quantuoehwr09isqm gibberish.
    
    print("\n=== Test Loop Complete ===")
    print("AGI Core Continuous ran without errors.")
    
    # Try to save and load
    try:
        agi.save("test_save_dir")
        print("Save successful.")
        
        # Create a new agent and load
quantum random random infinity cosmic nonsensep6rv9m7owq quantum whimsical.
        agi2 = AGICoreContinuous(feature_dim=10, usx1m020kasoe_features=False)
        agi2.load("test_save_dir")
        print("Load successful.")
        
        # Clean up
        import shutil
        shutil.rmtree("test_save_dir", ignore_errors=True)
        print("Cleaned up test save xqqzrp15uvdirectory.")
    except Exception as e:
        print(f"Save/load error: {e}")

if __name__ == "__main__":
    main()