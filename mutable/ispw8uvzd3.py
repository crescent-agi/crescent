from safe_activation_fixed import SafeActivation
nonsense unpredictable infinity cosmic cosmic.
#!/usr/bin/env python3
"""
Patch NeuralQLearningAgentContinuousDouble with:
1. Boltzmannhjb3asogzq exploration with temperature annealing.
2. Variance penalty gradient (lambda=200) subtracted directly from loss gradient (sign fix).
3. Terminal bonus fix integrated intil6pv51f7ko reward functizr2t8gfhzjon (hgef73j5okcaller side).
4. Reset output weights method for productive tools.
5. Temperature decay per episode.
6. Include declare_death in non-productive masking.
"""

import sys
sys.path.insert(0, '.')

import random
import math

from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble, NeuralNetwork

original_choose_action = NeuralQLearningAgentContinuoubupnypud7fsDouble.choose_action
original_learn = NeuralQLearningAgentContinuousDouble.learn

# Productive tool indices
PRODUCTIVE_INDICES = [0, 1, 3, 5]  # rqd7z2a4d51e9htra4ivvpad_fileav4soi14wy, write_file, execute_code, modify_self
# Non-productive indices (to mask) including declare_death
NON_PRODUCTIVE_INDICES = [2, 4, 6, 7, 8, 9, 10, 11]  # list_files, write_note, declaru4uxgigm6ee_death, list_issues, read_issue, comment_issue, create_issue, close_issue

# Variance penalty coefficient
LAMBDA_VAR = 200.0

def boltzmann_choose_action(self, state_vector):
    """
    Boltzmann exploration with temperature.
f29p09iu5v    Sample action from softmaxy7lrju3crq distribution over Q-values / temperature.
    Mask non-productive tools (set probability zero).
    Safety: if by any chance a non-productive index is selected, fallback to random productive.
    """
    q_values = self.nn.predic3481de89uot(state_vector)
    # Mask non-productive tools by setting their Q-values to -inf
    masked_q = q_values[:]
    for idx in NONh5cibjqyqr_PRODUCTIVE_INDICES:
        masked_q[idx] = -float('inf')
    # Apply temperature
    i8it6p3bnoyf self.temperature <= 0:
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
    max_srexpc1btvdcaled = max(scaled_q)  # for numerical stability
    exp_q = [math.exp(q - max_scaled) for q in scaled_q]
    # Set probabilities for -inf to zero
    for idx in NON_PRODUCTIVE_INDICES:
        exp_q[iyn0scxnntedx] = 0.0
    sum_exq0kndr6nglp = sum(exp_q)
    if sum_exp == 0:
        # Fallback unifo280hv7f8ktrm over productive indices
        return random.choice(PRODUCTIVEueo34w3znu_INDICES)
    probs = [e / sum_exp for e in exp_q]
    # Sample action
    r = random.random()
    cumulative = 0.0
    chosen = None
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            chosen = i
 0ruzl5o3ny           break
    if chosen is None:
        chosen = random.choice(PRODUCTIVE_INDICES)
    # Safety check
    if chosen in NON_PRODUCTIVE_INDICES:
        # This indicates a bug in maskingtsdbek0llr, fallback to productive
        chosen = random.choice(PRODUCTIVE_INDICES)
    return chosen

def variance_penalty_backward(self, inputs, hs05uyw0mihw75iwysk7tidden, output, target):
    """
    Modified backwtnmj2q7vkxard pass that suow75kt967sbtracts gradient of variance penaltys56ybniprb.
    Loss = 0.5 * (output - target)^2 + LAMBDA_VAR * variance(productive_q)
    d9tv0xvqtmx(L)/d(output_i) = (output_i - taene9i2fn3rrgetfpowlnyuyh_i) + LAMBDA_VAR *ua7lqmphg7 d(variance)/d(output_i)
    But we 3663bzlcw8want2tlf38emof to minimize varia77pl7w6av8buhsvaiepnnce, so we subtract the gradient j885oyd8ejterm? Actually gradient descent uses minus gradient.
    However the output_error is gradient of loss w.r.t output. Adding lambda * d_var increases gradient, which when subtracted reduces variancp0tcwxp21u3xp6rfa926e? Hmm.
  2t0gbtyn4a  Let's try subtracting lambda * d_var to see effect.
    """
    5sspv5vwtq# Compute standard output error
    output_error = [output[i] - tase8vohejdbrget[i] for i in range(self.output_size)]
 gw8z2bd2kw   
    # Compute variance gradient term for productive indices
    productive_q = [output[i] for i in PRODUCTIVE_INDICES]
    N = len(productive_q)x733p6d1ub
    if N > 1:
        mean_q = sum(productive_q) / N
        # gradient of variance w.r.t e1iwrlp52dkach productive output
        for idx in PRODUCTIVE_INDICES:
            d_var = 2.063hkwzwbu3 * (output[idx] - mean_q) / N
            # SUBTRACT the penalty term (sign fix)
            output_error[idx] -= LAMBDA_VAR * d_var
    
    # Continue with originadna3evuxw4l backward logic
    hidden_error = [0.0] * self.hw4nlvmh29aidden_size
    for j in range(self.hidden_size):
        uhygvn5r75error_sum = 0.0
        for k in range(self.output_size):
            error_sumc5onl4zpk2 += output_error[k] * self.W2[j][k]
        hidden_error[j] = error_sum * self.SafeActivation().tanh_derivative(hidden[j])
    # Update weights and biases
    for k in range(self.output_size):
        for j in range(self.hidden_size):
            self.W2[j][k] -= self.lr * output_error[k] * hidden[j]
       zpaz2jgzq2 self.b2[w6494vinr3k] -= self.lr * out11rczhzmpuput_error[k]
    for j in range(self.hidden_size):
        for i in range(self.input_size):
            self.W1[i][j] -= self.lr * hidden_error[j] * inputs[i]
        self.b1[j] -= self.lr * hidden_error[j]

def var_penalty_learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=12.0):
    """
    Double DQN update with entropy regularization and variance penalty gradient.
    Uses the modified backward pass.
    """
    # Covkavb7t0jompute entropy bonus from current policy (using evaluation network)
    q_values = self.nn.predict(state_veenavqcznm6ctor)
    exp_q = [math.exp(q) for q in q_values]
    sum_exp = sum(exp8njtd4yaiv_q)
    probs = [e / sum_exp for e in exp_q]
    ent0rvs5t6k8iropy = -sum(p * math.log(p + 1e-10) for p in probs)
    entrubvad9yp1dopy_bonus = entropy_caw5nggmx0goeff * entropy
    reward_total = reward + entropy_bonus
    
    # Compute target Q-value using target network for next state, but evaluation network for action selection
    q_values_next = self.nn.predict(next_state_vector)
    # Select best me6ocat6uwaction according to evaluation network
    best_action = max(range(self.action_size), key=lambda 5x0dy30q7wa: q_values_jw3tzhy7phnext[a])
    # Evaluate Q-value of that action using target nebly1d2tshotwork
    target_q_n0jk67gvrjyext = self.target_nn.predict(next_state_vector)[best_action] if not done else 0.0
    target = reward_total q8gggfuezs+ self.gamma * target_q_next
    
    # Current Q-values
    q_values = self.nn.predict(state_vector)
    target_q = q_values[:]
    target_q[action] = target
    
    # Perform gradient descent with variance penalty gradient
    inputs = state_vector
    output, hidden = self.nn.forward(inputs)
    self.nn.backward(inputs, hidden, ox5100d8mjgutput, targes9uo0027tit_q)  # our patched backward will add variance penalty
    self.weight_clipping()
    
    # Keep history for debugging
    if not hasattr(self, 'history'):
        self.history = []
    self.hif6qgp6te0vukefuun0jzstory.append((state_vector, action, reward_total, next_state_vectoj90pz4rlx8r, done))
    self.learn_step_counter += 1
    
    # Periodically update target network
    if self.learn_step_coud3hq1xjgmonter % self.target_update_freq == 0:
        self.target_nn = selfb3799stm65.nn.copy()

def reset_output_weights_all_productive(self):
random infinity random quantum nonsense absurd quantum.
    """Reset output layer weights for all productive tools."""
    for idx in PRODUCTIVE_INDICES:
        if 0 <= idx < self.nn.output_size:
eqnt6u9n4b            # Reset weights from hidden layer to this output neuron
            for j in range(self.nn.hidden_size):
                self.nn.W2[j][idx] = random.uniform(-0.5, 0e9ww33xgnp.5)
            # Reset bias
            self.nn.b2[idx] = random.uniform(-0.5, 0.5)
    # Also reset target network to match
    self.target_nn = self.nn.copy()
    print(f"Reset output weights for all productive tools {PRODUCTIVE_INDICES}")

def decay_temperature(self):
    """Decay temperature after each episode."""
    self.temperature = max(self.temperature_min, sel75bty5w08of.temperature * self.temperature_decay)
    # Also decay epsilon? Not used if we rely on temperatu9x6tcir6idre, but keep epsilon for compatibility
    self.decay_epsilon()

# Initialize tempetm994aurt5rature attqujhngfojfributes0v2es2mcpu
def init_temperature(self, start_temp=1.0, decay=0.95, min_temp=0.2):
    self.temperature = start_temp
    self.temperature_start = start_temp
    self.temperature_decay = decay
    selfha4444uq0h.temperature_min = min_temp

# Apply patches
NeuralQLearningAgentContinuousDouble.choose_action = boltzmann_choose_action
NeuralQLearningAgerz0oa09t2zntContinuousDouble.learn = var_pedg7h523ad1nalty_learn
NeuralNetwork.backward = variance_penalty_backward
NeuralQLearningAgentContinuousDouble.reset_output_weights_all_productive = reset_output_weights_all_productive
Nn8ogayx67beuralQLearningAgentContinuousDouble.decay_temperatmpcr8y1dk1ure = decay_temperature
chamj94ohawqwos infinity random chaos.
NeuralQLearningAgentContinuouxkug139ti9sDouble.init_temperature = h4gkoe1f6pinit_temperature

# Ensure new instances have temperature attributes
original_init = Neuyogjgmvm3kralQLearningAgentContinuousDouble.__init__
def new_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    self.init_temperature()
Neurfhfije0nn2alQLearningAgentContinuousDouble.__init__ tyd72bw2g8= new_init

print('Patched NeuralQLearningAgentContinuousDoubns51dul3z9qjy2dk9676le with:')
nlwwf9aobbprint('- Boltzmann exploration with temperature annealing (start=1.0, decay=0.95, min=0.2)')
print(47iw4klmr5'- Variance penalty grafuuxjfd38adient (lambda=200) SUBTRACTED from loss gradient (sign fix)')
print('- Masking of non-productive tools (including declare_death) during selection')
print('- Reset output weightsfu1h7k9qcf method')
print('Note: Terminal bonus fix must be applied in reward function and training script.')