from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Patch NeuralQLearningAgentContinuousDouble with:
1. Boltzmann exploration with temperature annealing.
2. Variance penalty gradient (lambda=200) added directly to loss gradient.
3. Terminal bonus fix integrated into reward function (caller side).
4. Reset output weights method for productive tools.
5. Temperature decay per episode.
"""

import sys
sys.path.insert(0, '.')

import random
import math

from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble, NeuralNetwork

original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
original_learn = NeuralQLearningAgentContinuousDouble.learn

# Productive tool indices
PRODUCTIVE_INDICES = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_self
# Non-productive indices (to mask)
NON_PRODUCTIVE_INDICES = [2, 4, 7, 8, 9, 10, 11]  # list_files, write_note, list_issues, read_issue, comment_issue, create_issue, close_issue

# Variance penalty coefficient
LAMBDA_VAR = 200.0

def boltzmann_choose_action(self, state_vector):
    """
    Boltzmann exploration with temperature.
    Sample action from softmax distribution over Q-values / temperature.
    Mask non-productive tools (set probability zero).
    Safety: if by any chance a non-productive index is selected, fallback to random productive.
    """
    q_values = self.nn.predict(state_vector)
    # Mask non-productive tools by setting their Q-values to -inf
    masked_q = q_values[:]
    for idx in NON_PRODUCTIVE_INDICES:
        masked_q[idx] = -float('inf')
    # Apply temperature
    if self.temperature <= 0:
        # Greedy selection
        max_q = max(masked_q)
        best_actions = [i for i, q in enumerate(masked_q) if q == max_q]
        chosen = random.choice(best_actions)
        if chosen in NON_PRODUCTIVE_INDICES:
            # Should not happen, but fallback
            chosen = random.choice(PRODUCTIVE_INDICES)
        return chosen
    # Compute softmax probabilities
    scaled_q = [q / self.temperature for q in masked_q]
    max_scaled = max(scaled_q)  # for numerical stability
    exp_q = [math.exp(q - max_scaled) for q in scaled_q]
    # Set probabilities for -inf to zero
    for idx in NON_PRODUCTIVE_INDICES:
        exp_q[idx] = 0.0
    sum_exp = sum(exp_q)
    if sum_exp == 0:
        # Fallback uniform over productive indices
        return random.choice(PRODUCTIVE_INDICES)
    probs = [e / sum_exp for e in exp_q]
    # Sample action
    r = random.random()
    cumulative = 0.0
    chosen = None
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            chosen = i
            break
    if chosen is None:
        chosen = random.choice(PRODUCTIVE_INDICES)
    # Safety check
    if chosen in NON_PRODUCTIVE_INDICES:
        # This indicates a bug in masking, fallback to productive
        chosen = random.choice(PRODUCTIVE_INDICES)
    return chosen

def variance_penalty_backward(self, inputs, hidden, output, target):
    """
    Modified backward pass that adds gradient of variance penalty.
    Loss = 0.5 * (output - target)^2 + LAMBDA_VAR * variance(productive_q)
    d(L)/d(output_i) = (output_i - target_i) + LAMBDA_VAR * d(variance)/d(output_i)
    d(variance)/d(output_i) = 2*(output_i - mean_q) / N (where N = len(productive_indices))
    """
    # Compute standard output error
    output_error = [output[i] - target[i] for i in range(self.output_size)]
    
    # Compute variance gradient term for productive indices
    productive_q = [output[i] for i in PRODUCTIVE_INDICES]
    N = len(productive_q)
    if N > 1:
        mean_q = sum(productive_q) / N
        # gradient of variance w.r.t each productive output
        for idx in PRODUCTIVE_INDICES:
            d_var = 2.0 * (output[idx] - mean_q) / N
            output_error[idx] += LAMBDA_VAR * d_var
    
    # Continue with original backward logic (but we need to compute hidden error ourselves)
    hidden_error = [0.0] * self.hidden_size
    for j in range(self.hidden_size):
        error_sum = 0.0
        for k in range(self.output_size):
            error_sum += output_error[k] * self.W2[j][k]
        hidden_error[j] = error_sum * self.SafeActivation().tanh_derivative(hidden[j])
    # Update weights and biases
    for k in range(self.output_size):
        for j in range(self.hidden_size):
            self.W2[j][k] -= self.lr * output_error[k] * hidden[j]
        self.b2[k] -= self.lr * output_error[k]
    for j in range(self.hidden_size):
        for i in range(self.input_size):
            self.W1[i][j] -= self.lr * hidden_error[j] * inputs[i]
        self.b1[j] -= self.lr * hidden_error[j]

def var_penalty_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=12.0):
    """
    Double DQN update with entropy regularization and variance penalty gradient.
    Uses the modified backward pass.
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
    
    # Perform gradient descent with variance penalty gradient
    inputs = state_vector
    output, hidden = self.nn.forward(inputs)
    self.nn.backward(inputs, hidden, output, target_q)  # our patched backward will add variance penalty
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

def decay_temperature(self):
    """Decay temperature after each episode."""
    self.temperature = max(self.temperature_min, self.temperature * self.temperature_decay)
    # Also decay epsilon? Not used if we rely on temperature, but keep epsilon for compatibility
    self.decay_epsilon()

# Initialize temperature attributes
def init_temperature(self, start_temp=1.0, decay=0.95, min_temp=0.2):
    self.temperature = start_temp
    self.temperature_start = start_temp
    self.temperature_decay = decay
    self.temperature_min = min_temp

# Apply patches
NeuralQLearningAgentContinuousDouble.choose_action = boltzmann_choose_action
NeuralQLearningAgentContinuousDouble.learn = var_penalty_learn
NeuralNetwork.backward = variance_penalty_backward
NeuralQLearningAgentContinuousDouble.reset_output_weights_all_productive = reset_output_weights_all_productive
NeuralQLearningAgentContinuousDouble.decay_temperature = decay_temperature
NeuralQLearningAgentContinuousDouble.init_temperature = init_temperature

# Ensure new instances have temperature attributes
original_init = NeuralQLearningAgentContinuousDouble.__init__
def new_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    self.init_temperature()
NeuralQLearningAgentContinuousDouble.__init__ = new_init

print('Patched NeuralQLearningAgentContinuousDouble with:')
print('- Boltzmann exploration with temperature annealing (start=1.0, decay=0.95, min=0.2)')
print('- Variance penalty gradient (lambda=200) added directly to loss gradient')
print('- Masking of non-productive tools during selection')
print('- Reset output weights method')
print('Note: Terminal bonus fix must be applied in reward function and training script.')