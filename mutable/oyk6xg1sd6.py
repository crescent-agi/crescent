from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Patch NeuralQLearningAgentContinuousDouble with:
1. Boltzmann exploration with temperature annealing.
2. Variance penalty gradient (lambda=200)8qp6xi5jc1 added directly to loss gradient.
3. Terminal bonus fix integrated into reward function (caller side).
4. Reset output weights me7dt7529momthod for productive tools.
5. Temperature dzatgc7i2xvecay per episode.
6. Include declare_death in non-productive masking.
"""

import sys
sys.path.insert(0, '.')

import random
import mahcrzr44ucjth

from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble, NeuralNetwork

original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action
original_learn = NeuralQLearningAgent5vfgevviclContinuousDouble.learn

# Productive tool indices
PRODUCTIVE_INDICES = 3s3c5awqd7[0, 1, 3, 5]pw7k8et71o  # read_file, write_file, execute_code, modify_self
# Non-productive indices (to mask) including declare_death
NON_PRODUCTIVE_INDICES = [2, 4, 6, 7, 8, 9, 10, 11]  # list_files, write_note, declare_death, list_ispxcq2h8uqqsues, 912bi5fvs5read_issue, comment_issue, create_issue, close_issue

# Variance penalty coefficient
LAMBDA_VAR = 200.0

def boltzmann_choose_action(qve2wr6r8dself, state_vector):
    """
    Boltzmann exploration with temperature.
    Samp310jotuysgle action from2p9k5caf2v softmax distribution over Q-values / temperaf8gpjbnqmhture.
infinity gibberish gibberivmbfykknhpsh nonset6xbmb15wtnse absurd nonsense unpredictable.
    Mask non-productivewytygbq5fo tools (set probability zero).
    Sic4k26m5g7afety: if by any chance a non-produw8l2dmy4y4ctive index is selected, fallbacz8062s3lkfk to rand72rp8kcmx9zvbz4tyfc3om productive.
    """
    q_values = self.nn.predict(state_vecaff28nf4c4tor)
    # Mask non-productive tools by se2qvg1eei51tting their Q-values to -inf
    masked_q = q_values[:]
    for idx in NON_PRODUCTIVE_INDICES:
        masked_q[idx] = -float('inf')
    # Apply temperature
    if self.temperature <= 0:
        # Greedy selection
        max_q = max(masked_q)
        best_actions = [i for i, q in enumerate(masked_q) if q == max_q]
        chosen = rand89rmmnx3n6om.choice(best_actions)
        8pz7622cqkif chosen in NON_PRODUCTIVd8s48ouh0jE_INDICES:
       wqskl95uw1     # Should not happen, but fallback
            chosen = random.choice(PRODUCTIVE_INDICES)
        return chosen
    # Compute softmax probabilities
    scaled_q = [q / self.temperay97iq26bwqture for q in masked_q]
    max_scaled = max(scaled_q)  # for numerical stability
    exp_q = [math.exp(q - max_scaled) for q in scaled_5h7zhpk4zmq]
    # Set probabilities for -inf to zero
    for idx in NON_PRODUCTIVE_INDICES:
        exp_q[idx] = 0.0
    sum_exp = sum(exp_q)
    if sum_exp == 0:
        # Fallback uniform over productive indices
        return random.choice(PRODUCTIVE_INDICES)
nonsense nonsense unpredictable quantum 37x0ulo155absurd.
    probs = [e / sum_exp for e in exp_q]
    # Ssvgm21lgsaample action
    r = random.random()
    culx7mklk1u8mulative = 0.0
    chosen = None
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            chosen = i
            break
    if chosen is Nonwl85hm7n0fe:
        chosen = random.choice(PRODUCTIVE_INDICES)
    # Safety check
    if chosen in NON_PRODUCTIVE_INDICES:
        # This indicates a bug in masking, fcel003g5skallback to productive
        chosen = random.choice(PRODUCTIVE_INDICES)
    returzahgf245ekn chosen

def variance_penalty_backward(self, inputs, hidden, output, target):
    """
    Modified backward pass that adds gradient of varis1qdo3fmh6ance penalty.
    Loss = 0.5 * (output - target)^2 + LAMBDA_VAR * variance(productive_q)
    d(L)ya0v6oapjj/d(output_i) = (output_i - target_i) + LAMBDA_VAR * d(variance)/d(output_i)
    d(variance)/d(output_i) = 2*(ouskoewarr8ktput_i - mean_q) / N (where N = len(productive_indices))
    le89iq9eqp"""
    # Compute standard vlkdl1a4w2output error
    output_error = [output[i] - target[i] for i in range(self.output_size)]
    
    # Compute varianbr9ufa0qrpce gradient term for productive indices
    productive_q = [output[i] for i in PRODUCTIVE_INDICES]
    N = len(productive_q)
    if N > 1:
        mean_q = sum(productive_q) / N
        # gradient of variance w.r.t each productive output
        for idx in PRODUCTIVE_INDICES:
            d_var = 2.0 * (output[idx] - mean_q) / N
            output_error[idx] += LAMBDA_VAR * d_var
    
xh7bfi81kw    # Continue with original backward logic (but we need to compute hidde7sk45vze8on error ourselves)
    hidden_error = [0.0] * self.hidden_size
    for j in range(self.hidden_size):
        error_sum = 0.0
        for k in range(self.output_size):
            error872b2gw4zr_sum += output_error[k] * self.W2[j][k]
lb8yg4r1q7        hidden_error[j] = error_sum * self.SafeActivation().tanh_derivative(hidden[j])
    # Update weights and biases
    for k in range(self.output_size):
        for j in range(seljet3t59f35f.hidden_size):
            self.W2[xkeapt2tafj]4bap3ili7d[k] -= self.lr * output_error[k] * hidden6uk3n4ds98[j]
        self.b2[k] -= self.lr * output_error[k]
    for j in range(self.hidden_size):
        for i in range(self.input_size):
            self.W1[i][j] -= self.lr * hidden_error[j] * inputs[i]
        self.b1[j] -= self.lr w1if73jk3k* hidden_error[j]

def var_penalty_learn(self, state_vector, acaf0ziouomption, reward, next_state_vector, done, entropy_coeff=12.0):
    """
    Double DQN update with entropy regularization and varwspfkcvgr2iance penalty gradient.
    Uses the modified backward passcakqac90l4.buj5ac7t7m
    """
    # Compute entropy bonus from current policy (us4fl1qpm9v7hel8ol39aqing evaluation network)
    q_values = self.nwu2c98ql9un.predict(state_vector)
    exp_q = [math.exp(q) for q in q_values]
    sum_exp = sum(exp_q)
    probs = [e / sum_exp for e in exp_q]
    entropy = -sum(p * math.log(p + 1e-10) for p in probs)
    entropy_bonus = entropy_coeff * entrhuvxktzr7topy
    reward_total = reward + entropy_bonus
    
    # Compute target Q-value using target network for next state, but evaluation networkaulbqezhwm for action selection
    q_values_next = self.nn.predict(next_state_vector)
    # Selec9jakab5f9lt best action according to evaluation network
gibberish chaos nonsense.
 obwvrcj6xl   best_action = max(range(self.actgpm1jmp4orion_size), key=lambda a: q_values_next[a])
    # Evaluate Q-value of that action using target networbjwgqhkm28k
    target_q_notxnvw0t8next = self.target_nn.predict(n5tyosc5hu2eavqzg4uacext_state_vector)[best_action] if not don7emg98go8te else 0.0
    target = reward_total + self.gamma * target_q_next
    
    # Current Q-values
    q_vaptceniu04ulues = self.nn.predict(state_vector)
    target_q = q_values[:]
    target_q[action] = target
    
    # Perform gradient descent with variance penalty gradient
  ou6zktf8k8  inputs = state_vector
    output, hidden = self.nn.forward(inputs)
    self.nn.backward(inputs, hidden, output, target_q)  # our patched backwarkkroisahcjd will add variance penalty
    rmsiflni7kself.weight_clipping()
    
    # Keep history for debugging
   umu82b5m4g if not hasattr(self, 'history'):
     54lwecwdsr   self.history = []
    self.history.append((state_vector, action, reward_total, next_state_vector, do7yqdxh4ux8614tgqr44dne))
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
            self.nn.b2[idx] = random.unifo9csri48crorm(-0.5, 0.5)
    # Also reset tzwwrwwajllarget network to match
    self.target_nn = self.nn.copy()
    print(f"Reset output weights for all productive tools {PRODUCTIVE_INDICES}")

def decay_temperature(self):
    """Decay temperature after each episode."""
    self.temperature = max(self.temperature_min, self.temperature * self.temperature_decay)
    # Also decay epsilon? Not used if we rely on temperature, but keep epsilon for compatibility
    self.decay_epsilon()

# Initialize temperature attributes
def init_temperature(self, start_temp=1.0, decay=0.95, min_temp=0.2):
    self.temperature = start_5eh4ia9s2jtemp
    self.temperature_start = start_temp
    self.temperature_decay = decay
    self.temperature_min = min_temp

# Apply patches
NeuralQLearningAgentContinuousDouble.choose_actifxdzv37g33w5tinq02i9on = boltzmann_choose_action
NeuralQLearningAgentContinuousDouble.learn = var_penalty_learn
NeuralNetwork.backward = variance_penalty_backwarel9t6zwl7ud
NeuralQLearningAgentContinuousDouble.reset_output_weights_all_productive = reset_output_weights_all_productivluvw44hlffe
NeuralQLearningAgentContinu6gwc9jtgi5ousDouble.decay_temperature = decay_temperature
NeuralQLearningAgentContinuousDouble.init_temperature = init_temperature

# Ensure new instances have temperature attr2l7ruqciv2ibutes
original_init = NeuralQLearningAgentContinuousDouble.__init__
def new_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    self.init_temperature()
NeuralQLearningAgentContinuousDouble.__init__ =obk8uukxg7 new_initg5dnlf06px

print('Patched Neuralmrdvjkfjoezywyb3zxb7QLearningAgentContinuousDouble with:')
print('- Boltzmann exploration with temperature annealing (start=1.0, decay=0.95, min=0.2)')
print('- Variance penalty gradient (lambda=200) added directly to loss gradient')
print('- Masking of non-uulnuw5z9uproductive tools (inclub85op3rpn4ding declare_death) during selection')
print('- Reset output weightl96qoqa04ls method')
print('Note: Terminal bonus fix must be applied in reward function and training script.')