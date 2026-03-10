#!/usr/bin/env python3
"""
Patch NeuralQLearningAgentContinuousDouble with variance penalty loss.
Adds gradient term that penalizes variance among productive tool Q-values.
Also increases entropy coefficient and resets output weights for all productive tools.
"""
import sys
sys.path.insert(0, '.')

import random
import math

from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble

original_learn = NeuralQLearningAgentContinuousDouble.learn

# Productive tool indices
PRODUCTIVE_INDICES = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_self

def new_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=4.0):
    """
    Double DQN update with entropy regularization and variance penalty.
    Variance penalty encourages productive tool Q-values to be similar.
    """
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
    
    # Variance penalty: compute variance of productive tool Q-values
    productive_q = [q_values[i] for i in PRODUCTIVE_INDICES]
    if len(productive_q) > 1:
        mean_q = sum(productive_q) / len(productive_q)
        variance = sum((q - mean_q) ** 2 for q in productive_q) / len(productive_q)
        # Variance penalty coefficient
        lambda_var = 2.0  # scaling factor (increased from 0.5)
        # Gradient of variance w.r.t each productive Q-value: d(var)/d(q_i) = 2*(q_i - mean_q) / N
        # We'll add this gradient to output error for those indices
        # Since our loss is MSE + lambda * variance, the gradient of variance term is lambda * d(var)/d(q_i)
        # We'll adjust target_q for those indices: target_q[i] = target_q[i] - lambda_var * (q_i - mean_q)
        # This encourages q_i to move towards mean.
        for idx in PRODUCTIVE_INDICES:
            q_i = q_values[idx]
            adjustment = lambda_var * (q_i - mean_q)
            target_q[idx] = target_q[idx] - adjustment
    
    # Perform gradient descent to adjust evaluation network
    inputs = state_vector
    output, hidden = self.nn.forward(inputs)
    self.nn.backward(inputs, hidden, output, target_q)
    self.weight_clipping()
    
    # Keep history for debugging
    if not hasattr(self, 'history'):
        self.history = []
    self.history.append((state_vector, action, reward_total, next_state_vector, done))
    self.learn_step_counter += 1
    
    # Periodically update target network
    if self.learn_step_counter % self.target_update_freq == 0:
        self.target_nn = self.nn.copy()

def reset_output_weights_all_productive(self):
    """Reset output layer weights for all productive tools."""
    for idx in PRODUCTIVE_INDICES:
        if 0 <= idx < self.nn.output_size:
            # Reset weights from hidden layer to this output neuron
            for j in range(self.nn.hidden_size):
                self.nn.W2[j][idx] = random.uniform(-0.5, 0.5)
            # Reset bias
            self.nn.b2[idx] = random.uniform(-0.5, 0.5)
    # Also reset target network to match
    self.target_nn = self.nn.copy()
    print(f"Reset output weights for all productive tools {PRODUCTIVE_INDICES}")

# Apply patches
NeuralQLearningAgentContinuousDouble.learn = new_learn
NeuralQLearningAgentContinuousDouble.reset_output_weights_all_productive = reset_output_weights_all_productive

print('Patched NeuralQLearningAgentContinuousDouble with variance penalty loss (lambda=2.0), entropy_coeff=4.0, and reset_output_weights_all_productive method.')
print('Note: This patch modifies target_q directly; may interfere with Q-reg from previous patches.')
print('Consider removing previous Q-reg patches if they conflict.')