#!/usr/bin/env python3
"""
Simulation of AGI Core learning in a mock workspace.
"""
import sys
sys.path.insert(0, '.')

from agi_core import AGICore
import random

def simulate():
    print("=== AGI Core Simulation ===")
    core = AGICore(state_size=10, hidden_size=16, learning_rate=0.05)
    # Simulate a workspace that cycles through states
    workspace = "file1.py file2.md"
    journal = ""
    actions = []
    
    for episode in range(5):
        print(f"\nEpisode {episode+1}")
        # Decide action
        tool, args, confidence = core.decide_action(workspace, journal, actions)
        print(f"  AGI Core suggests: {tool} (confidence {confidence:.2f})")
        # Simulate executing the tool with some success
        # For simplicity, we assume the tool succeeds and yields a reward
        reward = random.uniform(-0.5, 1.5)  # random reward
        # Update workspace (mock change)
        workspace += f" updated{episode}"
        journal += f"Step {episode}\n"
        actions.append({"tool": tool, "step": episode})
        # Learn from outcome
        core.learn_from_outcome(reward, workspace, journal, actions)
        print(f"  Reward: {reward:.2f}")
        # Reflect
        advice = core.reflect()
        if advice.get('advice'):
            print(f"  Reflection: {advice['advice'][0]}")
    
    # Show some internal state
    if core.q_agent:
        print("\nQ-agent Q-table sample (state 0):", core.q_agent.q_table[0] if hasattr(core.q_agent, 'q_table') else "No Q-table")
    if core.world_model:
        print("World model memory size:", len(core.world_model.memory))
    if core.cognitive:
        print("Cognitive architecture memory size:", len(core.cognitive.memory))
    
    # Save core
    import os
    os.makedirs('artifacts/agi_core_sim', exist_ok=True)
    core.save('artifacts/agi_core_sim')
    print("\nAGI Core saved to artifacts/agi_core_sim")
    print("Simulation complete.")

if __name__ == "__main__":
    simulate()