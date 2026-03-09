#!/usr/bin/env python3
"""
Test integration of AGI modules.
"""
import sys
sys.path.insert(0, '.')

from cognitive_architecture import CognitiveArchitecture
from world_model import WorldModel
from neural_q import NeuralQLearningAgent
from self_reflection import SelfReflection
from mcts_planner import MCTSPlanner

def test_cognitive_architecture():
    print("Testing CognitiveArchitecture...")
    ca = CognitiveArchitecture(state_size=10, action_size=8)
    # Decide action
    action = ca.decide_action(0, ["read_file", "write_file", "execute_code"])
    print(f"Recommended action: {action}")
    # Learn
    ca.learn_from_experience(0, 2, 1.0, 1, False)
    advice = ca.reflect()
    print(f"Reflection advice: {advice}")
    print("CognitiveArchitecture test passed.\n")

def test_world_model():
    print("Testing WorldModel...")
    wm = WorldModel(state_size=5, action_size=3)
    wm.learn_transition(0, 2, 1)
    probs = wm.predict_next(0, 2)
    print(f"Predicted distribution: {probs}")
    print("WorldModel test passed.\n")

def test_neural_q():
    print("Testing NeuralQLearningAgent...")
    agent = NeuralQLearningAgent(state_size=5, action_size=3)
    # Train a little
    for _ in range(100):
        state = 0
        action = agent.choose_action(state)
        reward = 1 if action == 2 else 0
        next_state = (state + 1) % 5
        agent.learn(state, action, reward, next_state, False)
    q_vals = agent.nn.predict(agent._one_hot(0))
    print(f"Q-values for state 0: {q_vals}")
    best = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f"Best action: {best}")
    print("NeuralQLearningAgent test passed.\n")

def test_self_reflection():
    print("Testing SelfReflection...")
    # Create a dummy journal and actions
    import json
    with open('journal.md', 'w') as f:
        f.write("Test journal entry.\n")
    with open('actions.jsonl', 'w') as f:
        f.write(json.dumps({"tool": "read_file", "step": 1}) + "\n")
    reflect = SelfReflection()
    analysis = reflect.generate_advice()
    print(f"Advice: {analysis['advice']}")
    print("SelfReflection test passed.\n")

def test_mcts():
    print("Testing MCTSPlanner...")
    # Mock world model and Q agent
    class MockWorldModel:
        def sample_next(self, state, action):
            return (state + action) % 5
    class MockQAgent:
        def __init__(self):
            self.nn = self
        def predict(self, one_hot):
            import random
            return [random.random() for _ in range(3)]
        def _one_hot(self, state):
            return [0]*5
    wm = MockWorldModel()
    qa = MockQAgent()
    planner = MCTSPlanner(wm, qa, action_space_size=3, state_space_size=5, max_iterations=50)
    best_action = planner.plan(start_state=0)
    print(f"MCTS selected action: {best_action}")
    print("MCTSPlanner test passed.\n")

if __name__ == "__main__":
    test_cognitive_architecture()
    test_world_model()
    test_neural_q()
    test_self_reflection()
    test_mcts()
    print("All integration tests passed.")