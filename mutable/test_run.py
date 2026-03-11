#!/usr/bin/env python3
"""
Test the AGI Core Continuous system end-to-end.
"""
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
from neural_q_continuous import NeuralQLearningAgentContinuous
from world_model_continuous import WorldModelContinuous
from feature_extractor import FeatureExtractor

print("Testing AGI Core Continuous...")

# Test SafeActivation first
from safe_activation_fixed import SafeActivation
sa = SafeActivation()
sa.stress_test()

# Test feature extractor
print("\nTesting FeatureExtractor...")
fe = FeatureExtractor()
ws = "Files: agi_core.py, cognitive_architecture.py, test.py, notes.md"
journal = "Today I made progress on AGI core. Next step: improve planning."
actions = [
    {"tool": "read_file"},
    {"tool": "write_file", "args": {"filepath": "test.py"}},
    {"tool": "execute_code"},
    {"tool": "read_file"},
]
feats = fe.extract(ws, journal, actions)
print(f"Feature vector length: {len(feats)}")
print(f"Sample features: {feats[:5]}...")

# Test Neural Q-learning agent
print("\nTesting NeuralQLearningAgentContinuous...")
agent = NeuralQLearningAgentContinuous(feature_dim=30, action_size=12, hidden_size=20, exploration_rate=0.5)
state = [0.1] * 30
action = agent.choose_action(state)
print(f"Chosen action: {action}")
print("Performing Q-learning update...")
next_state = [0.2] * 30
reward = 1.0
agent.learn(state, action, reward, next_state, done=False)
print("Q-values after update:")
print(agent.nn.predict(state))

# Test WorldModelContinuous
print("\nTesting WorldModelContinuous...")
wm = WorldModelContinuous(feature_dim=30, action_size=12)
pred = wm.predict_next(state, action)
print(f"Predicted next state: {pred[:5]}...")
print("Learning transition...")
wm.learn_transition(state, action, next_state)
print("Predicting again...")
pred2 = wm.predict_next(state, action)
print(f"New prediction: {pred2[:5]}...")

# Test AGICoreContinuous
print("\nTesting AGICoreContinuous...")
core = AGICoreContinuous(feature_dim=30, use_features=True)
workspace = "Files: agi_core.py, cognitive_architecture.py, test.py, notes.md"
journal = "Today I made progress on AGI core. Next step: improve planning."
actions = []
tool, args, conf = core.decide_action(workspace, journal, actions)
print(f"Decision: {tool} with args {args} (confidence {conf})")

print("\nAll tests passed!")
print("AGI Core Continuous is ready for training.")