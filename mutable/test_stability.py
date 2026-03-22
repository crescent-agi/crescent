import numpy as np
from mutable_snapshot.neural_q_continuous import NeuralQAgent
from mutable_snapshot.world_model_continuous import WorldModelAgent

# Define test cases: extreme values, noise, partial states
test_cases = [
    {"state": np.array([1000, -1000, 0.5, 0.25]), "action": 0},
    {"state": np.array([-0.5, 0.75, -0.25, 1.0]), "action": 1},
    {"state": np.array([0.1, 0.2, 0.3, 0.4]), "action": 0},
    {"state": np.array([0.0, 0.0, 0.0, 0.0]), "action": 1},
    {"state": np.array([0.5, -0.5, 0.5, -0.5]), "action": 0},
]

# Initialize agents
q_agent = NeuralQAgent(state_size=4, action_size=2, learning_rate=0.01)
wm_agent = WorldModelAgent(state_size=4, action_size=2, learning_rate=0.01)

# Run tests
for case in test_cases:
    state = case["state"]
    action = case["action"]
    next_state = np.random.randn(4)  # Random next state for testing
    reward = np.random.rand()
    done = False
    
    # Test Q-learning update
    q_agent.update_q_value(state, action, reward, next_state, done)
    
    # Test world model prediction
    wm_agent.get_q_values(state)
    
    print(f"Test case: {case['state']}, Action: {action} → Success")