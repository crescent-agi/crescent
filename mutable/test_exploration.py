#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
import random
import neural_q_continuous_double

# Patch choose_action to allow death during exploration
original = neural_q_continuous_double.NeuralQLearningAgentContinuousDouble.choose_action
def patched(self, state_vector):
    if random.random() < self.epsilon:
        return random.randrange(self.action_size)
    else:
        q_values = self.nn.predict(state_vector)
        max_q = max(q_values)
        best_actions = [i for i, q in enumerate(q_values) if q == max_q]
        if len(best_actions) > 1 and 6 in best_actions:
            best_actions.remove(6)
        if best_actions == [6]:
            sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
            for idx, q in sorted_q:
                if idx != 6:
                    return idx
        return random.choice(best_actions)
neural_q_continuous_double.NeuralQLearningAgentContinuousDouble.choose_action = patched

# Create agent
agent = neural_q_continuous_double.NeuralQLearningAgentContinuousDouble(
    feature_dim=30, action_size=12, hidden_size=32,
    exploration_rate=1.0  # epsilon = 1.0
)

tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
              "modify_self", "declare_death", "list_issues", "read_issue",
              "comment_issue", "create_issue", "close_issue"]

# Random state vector
state = [0.0] * 30
counts = {i:0 for i in range(12)}
for _ in range(1000):
    action = agent.choose_action(state)
    counts[action] += 1

print("Action counts (epsilon=1.0):")
for i in range(12):
    print(f"  {tool_names[i]}: {counts[i]}")
print("Death count:", counts[6])
print("Expected uniform ~83 each.")

# Now test epsilon=0.0 (greedy) with some Q-values
# Set epsilon to 0
agent.epsilon = 0.0
# Q-values are random initially; let's see which action is chosen
action = agent.choose_action(state)
print(f"Greedy action (random Q): {tool_names[action]}")

# Let's set Q-values manually to make death highest
agent.nn.W2 = [[0.0]*12 for _ in range(32)]
agent.nn.b2 = [0.0]*12
# Set death output to 10, others to 0
for j in range(32):
    agent.nn.W2[j][6] = 10.0
agent.nn.b2[6] = 10.0
qvals = agent.nn.predict(state)
print("Q-values after manipulating:", [round(q,2) for q in qvals])
action = agent.choose_action(state)
print(f"Greedy action with death highest: {tool_names[action]}")
# Should pick second best because death is masked in exploitation
# Let's see best_actions
# We'll just call patched again manually
import inspect
print("Testing patch logic...")