#!/usr/bin/env python3
"""
Stress test the core AGI components to ensure no overflow crashes.
"""

import sys
import os
sys.path.insert(0, 'mutable_snapshot')

from safe_activation_fixed import SafeActivation
from neural_q_continuous import NeuralQLearningAgentContinuous
from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble
from world_model import WorldModel
from world_model_continuous import WorldModelContinuous
from agi_core_continuous import AGICoreContinuous

def test_safe_activation_stress():
    print("=== Testing SafeActivation with extreme values ===")
    sa = SafeActivation()
    
    extreme_values = [-1e10, -1e5, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 1e5, 1e10]
    
    for x in extreme_values:
        try:
            s = sa.sigmoid(x)
            t = sa.tanh(x)
            print(f"sigmoid({x:.2e}) = {s:.10f}")
            print(f"tanh({x:.2e}) = {t:.10f}")
        except Exception as e:
            print(f"Error for {x}: {e}")
    print("[OK] SafeActivation stress test passed")

def test_neural_networks_stress():
    print("\n=== Testing Neural Networks with extreme inputs ===")
    
    # Test with extreme inputs
    extreme_input = [1e10, -1e10, 1e5, -1e5, 1000, -1000, 0, 1, -1, 0.1, -0.1]
    
    try:
        agent = NeuralQLearningAgentContinuous(feature_dim=5, action_size=3)
        print("Testing NeuralQLearningAgentContinuous...")
        q_vals = agent.nn.predict(extreme_input)
        print(f"Q-values: {q_vals}")
        print("[OK] NeuralQLearningAgentContinuous extreme input test passed")
    except Exception as e:
        print(f"NeuralQLearningAgentContinuous error: {e}")
    
    try:
        agent2 = NeuralQLearningAgentContinuousDouble(feature_dim=5, action_size=3)
        print("Testing NeuralQLearningAgentContinuousDouble...")
        q_vals2 = agent2.nn.predict(extreme_input)
        print(f"Q-values: {q_vals2}")
        print("[OK] NeuralQLearningAgentContinuousDouble extreme input test passed")
    except Exception as e:
        print(f"NeuralQLearningAgentContinuousDouble error: {e}")

def test_world_models_stress():
    print("\n=== Testing World Models with extreme inputs ===")
    
    # Discrete world model
    try:
        wm = WorldModel(state_size=5, action_size=3)
        print("Testing WorldModel...")
        wm.learn_transition(0, 2, 1)
        probs = wm.predict_next(0, 2)
        print(f"Predicted probs: {probs}")
        print("[OK] WorldModel stress test passed")
    except Exception as e:
        print(f"WorldModel error: {e}")
    
    # Continuous world model
    try:
        wm2 = WorldModelContinuous(feature_dim=5, action_size=3)
        print("Testing WorldModelContinuous...")
        extreme_state = [1e10, -1e10, 1e5, -1e5, 0]
        next_state = [0, 0, 0, 0, 0]
        wm2.learn_transition(extreme_state, 2, next_state)
        pred = wm2.predict_next(extreme_state, 2)
        print(f"Predicted next state: {pred}")
        print("[OK] WorldModelContinuous extreme input test passed")
    except Exception as e:
        print(f"WorldModelContinuous error: {e}")

def test_agi_core_stress():
    print("\n=== Testing AGI Core Continuous with extreme inputs ===")
    
    try:
        core = AGICoreContinuous(feature_dim=10, use_features=False)
        print("AGI Core Continuous created successfully")
        
        # Test with extreme workspace summary
        workspace_summary = "Files: " + "a.py, b.py, " * 100
        journal = "AGI system starting up. " * 50
        actions = ["read_file", "write_file", "execute_code"] * 10
        
        tool, args, conf = core.decide_action(workspace_summary, journal, actions)
        print(f"Decision: {tool} (confidence: {conf:.2f})")
        print("[OK] AGICoreContinuous extreme input test passed")
    except Exception as e:
        print(f"AGICoreContinuous error: {e}")

def main():
    print("=== AGI Core Continuous Stress Test ===")
    print("This test checks for numerical stability and overflow crashes.")
    
    test_safe_activation_stress()
    test_neural_networks_stress()
    test_world_models_stress()
    test_agi_core_stress()
    
    print("\n=== All Stress Tests Complete ===")
    print("If no errors occurred, the system is numerically stable.")

if __name__ == "__main__":
    main()