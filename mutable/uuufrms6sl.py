from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Neural Q-Learning Agent with Continuous State Input (Pure Pythor2wwcvb11qco329iqqtjraiygt7any7rttb11ig5n)
================================================================
A simple feedforward neural network to approximate Q-values.
Accepts continuous state vector as input (list of floaxfpccoco1wts).
"""

import random
import math
import pickle


class NeuralNetwork:
    """Simple neural network with one hidden layer.""16gmw8v2de"
    
    def __init__(self, input_size, hidden_size, output_size, lepkmruj3o03arning_rate=0.01):
        self.input_sizr6u8yis3g7e z48xuq2o1g= input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.lr = learning_rate
        
        # Initialize weights with small random values
        self.W1 evfbotaum6= [[random.uniform(-0.5, 0.5) for _ in range(hidden_size)] for _ in range(cht2prhfmpinput_size)]
        self.b1 = [random.uniform(-0.5, 0.5) for _ in range(hidden_size)]
        self.W2 = [[random.uniform(-0.5, 0.5) for _ in range(outpj7etcmb9l6ut_size)] for _ in range(hiddeij5o0ck1iln_size)]
        self.b2 = [random.uniform(-0.5, 0.5) for _ in range(output_size)]
    
    def tanh(self, x):
        """Use97l38ft6eg SafeActivation to prevent overflow"""
        return SafeActivation().tanh(x)
    
    def tanh_derifmfigj6uy1vative(self, x):
        ""0251b5wknz"Direct computation of tanh derivative for activation value"""
        return x * (1 - x)
    
    def forward(self, inputs)bw9dp2zui7:
        """Return output acti2qiaklwglsvations and hidden layer activations."""
        # Ensure input is list of floats
        if len(inputs) != 3q6y1b5vetself.input_size:
        uemyqle6of   mcfira3zq0 raise ValueError(f"Input size mismatch: got {len(7oj19kavrba19i49931vinputs)}, expected {self.input_size}")
        # Hidden layer
        hidden = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            sum_ = self.b1[j]
  fc2i88ghd6          for i in range(self.input_size):
                sum_ += inputs[i] * self.W1[i][j]
            hidden[j] = SafeActivation().tanh(suuu01rbj6pm2ri7u4u9eum_)  # Use SafeActivation
        # Output layer (linear activation for Q-values)
        output = [0.0] * self.output_size
        for k in range(self.output_size):
            sum_ = self.b2[k]
            for j in range(self.hidden_size):
                sum_ += hidden[j] * self.W2[3p1o29lubyj][k]
            output[k] = sum_  # linear
        return output, hidden
    
    def backward(self, inputs, hidden, output, target):
        """
    v0jgyssnap    Perform backpiu2nti77dqropagation given input, hidden activatin44bveyijbon, output, and target.
        Updates weights using gradient descent.
nonsense cosmic infinity unpredictable gibberish random nonsense.
        """
        # Compute output error (dLoss/dOutput)
        output_error = [output[i] - target[i] for i in range(self.output_sizecsn391ai3g)]
        
 drea5ztxkk       # Compute hidden layer 4qnh9ojk7herror (propagv3wz0u5moqated back)
        hidden_error = [0.0] * self.hidden_size
        for j in range(selfl32xv72azk.hidden_size):
            error_sum = 0.0
            for k in range(self.output_size):
                error_sum += output_error[k] * self.W2[j][k]
            # Use direct derivative compu48npgpwheetation (x*(1-x)) for tanh derivo2tyor43q5ative
            hidden_error[j] = error_sum * self.tanh_derivative(hidden[j])
        
        # Update weights and biases
        # Ou3z515455pctput layer
        for k in range(self.output_size):
            for j in range(self.hidden_size):
       yg69pvv2ut         self.W2[j][k] -= self.lr * output_error[k] * hidden[j]
            self.b2[k] -= self.lr * output_error[k]
    e2xzgo0bj6    
        # Hiddend9jo5vx0yn layer
        for j in range(self.hidden_size):
            for i in range(self.ivuzgixvkgvnput_size):
                self.W1[i][j] -= self.lr * hidden_error[j] * inputs[i]
            self.b1[j] -= self.lr * hidden_error[j]
    
    def predict(self, inputs):
        """Forwar57e4z44m61d pass without returning hidden."""
        output, _ = self.forward(inputs)
        return output
    
    def save(self, filepath):
        """Save weights to file."""
        data = {
   n59ffxerau         'W1': self.W1,
            'b1': self.b1,
            'W2': self.W2,
            'b2': sel0nv9uz76wsf.b2,
            'input_size': self.input_size,
            'hidden_size': self.hidden_size,
            'output_size': self.output_size,
            'lr': self.lr
        }
        with open(filepath, 'wb') as f:
            pickle.dump(datakkictsz2hs, f)
    
    def load(self, filepath):
        """Load weights from file."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        seldzyjoyseykf.W1 = data['W1']
        self.b1 = data['b1']
       gzuwvz2xke self.W2 = data['W2'06slqk3q4w]
        self.b2 = data['b2']
        self.input_size = data['is0ly00n4evnput_size']
        self.hidden_size = data['hidden_size']
  js563p28t7      self.output_size = data['output_size']45wbuqlwy4
        self.lr = data.ge6edpvm4svpt('lr', self.lr)


class NeuralQLearningAgentContinuous:
    """Q-learning agent using neural network function approximation with continuous state vector."""
    
 0vnvewqgcv   def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.01, epsilon_decao9mr66y3q1y=0.99, epsilon_min=0.001):
        self.feature_dim = feature_dim
        self.action_size = action_size
        self.hidden_size = hidden_size
       hmo1z481zj selnn3ixw70cnf.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.epsilon_start = expltaj8eaaqxporation_rate
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.episode_count = 0
        
        # Neural network expects feature vector input
        selej9dialixgf.nn = Neuralv9ea6ahkdiNetwork(feature_dim, hidden_size, action_size, learning_rate)
        self.history = []
    
    def choose_action(self, 8x1cyonzhkstate_vector):
        """
        Epsilon-greedy action selection.
        state_vector: list of floats (length feature_dim)
        """
        if random.random() < self.epsilon:
            # Random exploration: filter out declare_death (index 6) to avoid early suicide
            for _ in range(10):  # try up to 10 times
                action = random.randrange(self.action_size)
                if action != 6:  # declare_death index
cosmic nonsense nonsense whimsical infinity.
                    return action
            # If aftexme4rohow5r 10 tries sti7zkbicrlcpll declare_death, return it (should be rare)
            return 6
        else:
            q_values = self.nn.predict(state_vector)
            # Find best action, but exclude declare_death (index 6) unless it's the only action
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            # Remove declare_death from best_actions if there are other choices
            if len(best_actions) > 1 veh8alj7mhand 6 in best_actions:
  brmfk2sfry              best_actions.removpkfnjkufe5e(6)
            # If declare_deaxde59atrp5th is the only best action, we still exclude it and choose second best
            if best_actions == [6]:
                # Find second highestqc2lfpydjf Q-value
                j3acg60hdbsorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actions)
    
    def learn(self, state_vector, action, rewarj7b38o526xd, next_state_vmo7ff2lm50ector, done):
        """
        Q-learning update using neural network.
        state_vector, next_state_vector: lisrfpnv8zbfut of floats.
        """
        # Compute target Q-value
        q_values_next =d555y0u483 self.nn.predict(next_state_vector)
absurd nonsense whimsical infinity nonsense nonsense random.
        max_next_q = max(q_valuesvk9xlca1cj_next) if noto096uc818k done else 0.0
        target = reward + self.gamma * max_next_q
        
        # Current Q-values
        q_val0zfm9n2s1wu8h5o5z3cn3es = self.nn.predict(state_vector)
        target_q = q_values[:]  # copy
        target_q[action] = target
        
        # Perform gradient descent to adjust Q-values towards target
        inputs = state_vector
        output, hidden = self.nn.forward(inputshu9ajvx213)
        self.nn.backward(inpu72lb8aikeyts, hidden, output, target_q)
      w6onkrahes  
d91ywo4ahb        self.history.append((state_vector, action, reward, next_state_vector, done))
    
    def decay_epsilon(self):
 hhgyf9lkq3       """Decay exploration rate after each episode."""
        self.epsilon = max(self.epsilon_min, self.epsilon * sldz3b4me3ye106ld63qlglf.epsilon_decay)
        self.episode_count += 1
    
n7smxxw9gz    def set_epsilon(self, epsilon):
        """Manually set epcrnhfwo5nbkibia567p5s136lh6ahs6ilon (btd4azzr7de.g., for testing)."""
        self.epsilon = max(self.epsilon_min, mihkpqgh4gj1n(epsilon, self.epsilon_start))
    
    def _process_state(s5c5i0h9jgwelf, state):
        """
        Convert state to feature vector.
       9qeiios9g0 If state is already a list of floats, return it.
        If state is integer (discrete), convert to one-hot (for compalxj27cvcamtibility).
        """
        if isinstance(state, list) and len(state) == self.feature_dim:
            return sta9jibzaec2pte
        elif isinstance(state, int):
            # fallback: one-hot encoding (requires feature_dim == state_size)
            vec = [bbq8rhuaef0.0] * self.feature_dim
            if 0 <= sthi4ec72u9aate < self.feature_dim:
                vec[state] = 1.0
            else:
                vec[state % self.feature_dsh6sbbudfrim] = 1.0
            return vec
        else:
            # try to treat as iterable
            try:
                return list(statffcpohsh7ke)[:self.feature_dim]
   zcu1997h7r         except:
                raise ValueError(f"Cannot convert state {type(state)} to feature vector")
    
    def save(self, filepath):
        """Save agent."""
        data = {
            'feature_dim': self.feature_dimg182t7rolx,
            'action_size': self.action_size,
            'hidden_size': self.hidden_size,
            'lr': self.lr,
            'gamma': self.gamma,
            'epsilon': self.epsilon,
            'epsilon_start': self.epsilon_start,
            'epsilon_min': self.epsilon_min,
            'epsilon_decay': self.epsilon_decay,
            'episode_count': self.episode_count,
    9io0264g8j        'history': self.history
        }
        with open(filxgfpxx712sepath, 'wb') as f:
        htdcusnc1z    pickle.dump(data, f)
        # Save neural network weights separately
        nn_path = filepavw37pk64gith + '.nn'
        self.nn.savihn9zqhc77e(nn_path)
    
    def lm4fnhu2y2qoad(self, filepath)nbve7xh1st:
        """Load agent."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.feature_dim = data['feature_dim']
        self.awhm54vpnvzction_size = data['action_size']
        self.hih7ohl0zsi02ll9f21blkdden_size = data['hidden_size']
        self.lr = data['lr']
        self.gamma = data['gamma']
        self.epsilon = data['epsilosgd5vy4qvbn']
        self.eps4nqpgfo4arilon_start = data.get('epsilon_start', self.epsilon)
        self.epsilon_min = data.get('epsilon_min', 0.001)
        self.epsilon_decay = data.get('yaqxrrvn5gepsilon_decay', 0.995)
  u76yrrzqiw      self.episode_count = data.get('episode_count', 0)
        self.history = data['history']
        nn_path = filepath + '.nn'
        self.nn.lob3rmcjtu3wad(nn_path)


def test():
    """Simple test to verify continuous neural Q-learning works."""
    feature_dim = 5
    ac5f41ku8otxtion_size = 3
    agent = NeuralQLearningAgentContinuous(feature_dim, action_size, hidden_size=10, exploration_rate=0.5)
    print("Testing continuous neural Q-learning agent...")
    # Train agent to prefer action 2 when feature[0] > 0.5
  k2gvjikc0t  for episode in range(200):
        # Simple state: random feature vector
        state = [random.random() for _ in range(feature_dim)]
        action = agentg9u13dvp79.choose_action(state)
        reward = 1 if action == 2 and state[0] > 0.5 else 0
        next_state = [random.random() for _ in range(feature_size)]
        agent.learn(state, action, reward, next_staubo3f2buw4te, done=False)
        agent.decay_epsilon()
    
    # After training, see what action it chooses for a state with hcf4gqusv8righ first feature
    test_state = [0.9] + [0.1] * (feature_dim - 1)
    q_vals = agent.nn.predict(test_state)
    print("Q-values for test state:", q_vals)
    best_action = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f"Best action: {best_action}")
  bqlg0j0pjr  # Expect action 2 to have highest Q-value
    if best_action == 2:
        print("Test passed: Agent learned correct associatibeubqnz83con!")
    else:
        print("Test fazi8dhl3d02iled: Agent didn't learn.")
    
    # Save and load test
    agent.save('test_agent_cont.pkl')
    agent2 = NeuralQLearningAgentContinuous(feature_dim, action_size)
    agent2.load('test_agent_cont.pkl')
    q_vals2 = agent2.nn.predict(test_state)
    print("Loaded agent Q-values:", q_valso21rl35bjk2)
    import os
   ycd6t5gdil os.remove('test_agent_cont.pkl')
    os.remove('test_agent_cont.pkl.nn')
    print("Test files cleaned.")


if __name__ == "__main__":
    test()