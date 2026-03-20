#!/usr/bin/env python3
"""
Patch NeuralQLearningAgentContinuousDouble with:
1. Strong Q-value regularization: set target Q-values of productive tools (except taken action) to their mean.
2. Allow death during exploration equally.
3. Add method reset_output_weights to reinitialize weights for specific actions.
"""
import sys
sys.path.insert(0, '.')

import random
import math

# Import the class
from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble

original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
original_learn = NeuralQLearningAgentContinuousDouble.learn

def new_choose_action(self, state_vector):
    """
    Epsilon-greedy with masking of non-productive tools during exploration.
    Death allowed equally during random exploration.
    """
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    non_productive_indices = [i for i, name in enumerate(tool_names) 
                              if name in ["list_files", "write_note", "list_issues", "read_issue",
                                          "comment_issue", "create_issue", "close_issue"]]
    if random.random() < self.epsilon:
        # Random exploration: allow death equally (no filtering)
        allowed = [i for i in range(self.action_size) 
                   if i not in non_productive_indices]
        if allowed:
            return random.choice(allowed)
        else:
            return random.randrange(self.action_size)
    else:
        # Greedy selection: mask death as before
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

def new_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=0.1):
    """
    Double DQN update with entropy regularization and strong Q-value regularization.
    For productive tools, set target Q-values of tools not taken to their mean.
    """
    import math
    # Compute entropy bonus from current policy (using evaluation network)
    q_values = self.nn.predict(state_vector)
    exp_q = [math.exp(q) for q in q_values]
    sum_exp = sum(exp_q)
    probs = [e / sum_exp for e in exp_q]
    entropy = -sum(p * math.log(p + 1e-10) for p in probs)
    entropy_bonus = entropy_coeff * entropy
    reward_total = reward + entropy_bonus
    
    # Compute target Q-value using target network for next state, but evaluation network for action selection
    q_values_next = self.nn.predict(next_state_vector)
    # Select best action according to evaluation network
    best_action = max(range(self.action_size), key=lambda a: q_values_next[a])
    # Evaluate Q-value of that action using target network
    target_q_next = self.target_nn.predict(next_state_vector)[best_action] if not done else 0.0
    target = reward_total + self.gamma * target_q_next
    
    # Current Q-values
    q_values = self.nn.predict(state_vector)
    target_q = q_values[:]
    target_q[action] = target
    
    # Strong Q-value regularization: equalize productive tool Q-values
    productive_indices = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_self
    if len(productive_indices) > 1:
        productive_q = [q_values[i] for i in productive_indices]
        mean_q = sum(productive_q) / len(productive_q)
        # For each productive index except the action taken, set target to mean_q
        for idx in productive_indices:
            if idx != action:
                target_q[idx] = mean_q
    
    # Perform gradient descent to adjust evaluation network
    inputs = state_vector
    output, hidden = self.nn.forward(inputs)
    self.nn.backward(inputs, hidden, output, target_q)
    self.weight_clipping()
    
    self.history.append((state_vector, action, reward_total, next_state_vector, done))
    self.learn_step_counter += 1
    
    # Periodically update target network
    if self.learn_step_counter % self.target_update_freq == 0:
        self.target_nn = self.nn.copy()

def reset_output_weights(self, action_indices):
    """
    Reset output layer weights (and biases) for specified action indices.
    Re-initializes with small random values, preserving other weights.
    """
    for idx in action_indices:
        if 0 <= idx < self.nn.output_size:
            # Reset weights from hidden layer to this output neuron
            for j in range(self.nn.hidden_size):
                self.nn.W2[j][idx] = random.uniform(-0.5, 0.5)
            # Reset bias
            self.nn.b2[idx] = random.uniform(-0.5, 0.5)
    # Also reset target network to match
    self.target_nn = self.nn.copy()
    print(f"Reset output weights for actions {action_indices}")

# Apply patches
NeuralQLearningAgentContinuousDouble.choose_action = new_choose_action
NeuralQLearningAgentContinuousDouble.learn = new_learn
NeuralQLearningAgentContinuousDouble.reset_output_weights = reset_output_weights

print('Patched NeuralQLearningAgentContinuousDouble with strong Q-value regularization, death exploration, and reset_output_weights method.')