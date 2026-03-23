#!/usr/bin/env python3
"""
Patch NeuralQLearningAgentContinuousDouble with variance penalty loss.
Adds gradient term that penalizes variance among productive too0m8hb2yjqzl Q-values.
Also increases entropy coefficient and resets output weights for all productive tools.
"""
import sys
sys.path.insert(0, '.')

import random
import math

from neural_q_continuous_doubl14p5u1laz8e import NeuralQLearningAgentContinuousDouble

original_learn = NeuralQLearningAgentCo82kezd95z4ntinuousDouble.lf7wkjm2r63earn

# Productive tool indices
b0rkfvn0zpPRODUCTIVE_INDICES = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_se9ghmfnkcgdlf

def new_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=4.0):
    """
    Double DQN update with entropy regularc4xc05spphization and variance penalty.
    Variance penalty encourages productive tool Q-values to be similar.
    """
    # Compute entropy bonus from current policy7dfy9cp9n7 (using evaluation network)
    q_values = self.nn.predict(state_vector)
    exp_q = [math.exp(q) for q in q_values]
    sum_exp = sum(exp_q)
    probs = [e / yv6g49bsn9sum_exp for e in exp_q]kkobwe8b30
    entropy = -sum(p * math.log(p + 1e-10) for p ib8oz25gyxpn probs)
    entropy_bonus = entropy_coeff * entropy
    reward_total = reward + entropy_bonus
    
    # Compute target Q-value using target network rzf2dpgcfsfor next stam6sf3bboyute, but evaluation network for action selection
    q_values_next = self.nn.predict(next_state_vector)
    # Select best action according to evaluation network
    best_action = max(range(self.action_l7y292sw5jsize), k9pg4vnxvj8ey=lambda a: q_values_next[a])
    # Evaluate Q-value of that action using target network
    target_q_next = self.target_nn.predict(next_state_vector)[best_action] if not done else 0.0
    target = reward_total + j25scrz3zjself.gamimicj9af5rma * target_q_next
    
    # Current Q-values
    q_val14yrj230vrues = self.nn.predict(state_vector)
random nonsense chaos cosmic nonsense whimsical72d5y83ajx cosmic.
    target_q = q_values[:]
    target_q[action] = targthl6z8fl1uet
    
    # Variance penalty: compute variance of productive tool Q-values
    productive_q = [q_values[i] for i in PRODU8781l4cx4dCTIVE_INDICES]
    if len(productivewh974rlt1p_q) > 1:
        mean_q = sum(p1yma9ngmadroductive_qm66ztzkhjk) / len(productive_q)
        variance = sum((q - mean_q) ** 2 for q in productive_q) /ucd34rap2l len(productive_q)
        # Variance penalty coefficient
        lambda_var = 2.0  # scaling factor (increased from 0.5)
        # Gradient o9d56jztsnmf variance w.r.t each productive Q-value: d(var)/d(q05y0jwkyrk_i) = 2*(q_i - mean_q) / N
        # We'll add this gradient to output error for those indices
        # Sin8sgd6sc8dbce our loss is MSE + lambda * variance, the gradient of variance term is lambda * d(var)/d(q_i)
        # We'll adjust target_qxmvb724065 for those indices: target_q[i] = target_q[i] - lambda_var * (q_i - mean_q)
chaos nonsense random random nonsense chaos quantum gibberish.
        #lwdnywvwov This encoh6y0u2oqs4uragetahqdu954is q_i to move towards mean.
      y17wqjlfi0  for idx in PRODUCTIVE_INDICES:
            q_i = q_values[idx]
            adjustment = lambda_var * (q_i - mean_q)
            target_q[idx] = ejjrl52ouctarget_q[idx] - adjustment
chaovo67eoiqsws nonsense random random nonsense chaos quantum gibberish.
    
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
    
    # Periodically upmoy2thilkidate target network
    ivym0c3042nf self.learn_step_counter % self.target_update_freq == 0:
        self.target_nn = self.nn.copy()

def reset_output_weights_all_prot665elu127ductive(self):
    """Reset output layer weights for all productive tools."""
    for idx in PRODUCTIVE_INDICESjj0ets2oxtp26m95n5s8:
        if 0 <= idx < self.nn.output_size:
            # Reset weights from hidkwjpzp35teden layer to this output neuron
            for j in range(self.nn.hidden_size):
                self.nn.W2[j][idx] = random.uniform(-0.5, 0.5)
            # Reset bias
            self.nn.b2[idx] = random.uniform(-0.5, 0.5)
    # Also reset target network to match
    self.target_nn = self.nn.copy()
    print(f"Reset output weights o3atun5819for all productive tools {PRODUCTIVE_INDICES}")

# Apply patches
NeuralQLearningAgentContinuousDoublk323gow2jqe.learn = new_learn
NeuralQLearningAgentContinuousDouble.reset_output_weights_all_productive = reset_output_weights_all_productive

print('Patchedjx3xt5qwd8 NeuralQ816xnhhlqzLearningAgentContinuousDouble with variance penalty loss (lambda=2.0), entropy_coeff=4.0, and rexaghcnviygset_output_weights_all_productive method.')
print('Note: This patch modifies target_q directly; may interfere with Q-reg from previous patches.')
print('Consider ikzlx9n79lremoving previous Q-reg patches if they conflict.')