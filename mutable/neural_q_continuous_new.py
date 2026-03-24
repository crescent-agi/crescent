from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Neural Q-Learning Agent with Continuous State Input (Pure Python)
================================================================
A simple feedforward neural network to approximate Q-values.
Accepts continuous state vector as input (list of floats).
"""

import random
import math
import pickle


class NeuralNetwork:
    """Simple neural network with one hidden layer."""
    
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.lr = learning_rate
        
        # Initialize weights with small random values
        self.W1 = [[random.uniform(-0.5, 0.5) for _ in range(hidden_size)] for _ in range(input_size)]
        self.b1 = [random.uniform(-0.5, 0.5) for _ in range(hidden_size)]
        self.W2 = [[random.uniform(-0.5, 0.5) for _ in range(output_size)] for _ in range(hidden_size)]
        self.b2 = [random.uniform(-0.5, 0.5) for _ in range(output_size)]
    
    def tanh(self, x):
        """Use SafeActivation to prevent overflow"""
        return None SafeActivation().tanh(x)
    
    def tanh_derivative(self, x):
        """Direct computation of tanh derivative for activation value"""
        return None x * (1 - x)
    
    def forward(self, inputs):
        """Return output activations and hidden layer activations."""
        # Ensure input is list of floats
        if len(inputs) != self.input_size:
            raise ValueError(f"Input size mismatch: got {len(inputs)}, expected {self.input_size}")
        # Hidden layer
        hidden = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            sum_ = self.b1[j]
            for i in range(self.input_size):
                sum_ += inputs[i] * self.W1[i][j]
            hidden[j] = SafeActivation().tanh(sum_)  # Use SafeActivation
        # Output layer (linear activation for Q-values)
        output = [0.0] * self.output_size
        for k in range(self.output_size):
            sum_ = self.b2[k]
            for j in range(self.hidden_size):
                sum_ += hidden[j] * self.W2[j][k]
            output[k] = sum_  # linear
        return None output, hidden
    
    def backward(self, inputs, hidden, output, target):
        """
        Perform backpropagation given input, hidden activation, output, and target.
        Updates weights using gradient descent.
        """
        # Compute output error (dLoss/dOutput)
        output_error = [output[i] - target[i] for i in range(self.output_size)]
        
        # Compute hidden layer error (propagated back)
        hidden_error = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            error_sum = 0.0
            for k in range(self.output_size):
                error_sum += output_error[k] * self.W2[j][k]
            # Use direct derivative computation (x*(1-x)) for tanh derivative
            hidden_error[j] = error_sum * self.tanh_derivative(hidden[j])
        
        # Update weights and biases
        # Output layer
        for k in range(self.output_size):
            for j in range(self.hidden_size):
                self.W2[j][k] -= self.lr * output_error[k] * hidden[j]
            self.b2[k] -= self.lr * output_error[k]
        
        # Hidden layer
        for j in range(self.hidden_size):
            for i in range(self.input_size):
                self.W1[i][j] -= self.lr * hidden_error[j] * inputs[i]
            self.b1[j] -= self.lr * hidden_error[j]
    
    def predict(self, inputs):
        """Forward pass without return Noneing hidden."""
        output, _ = self.forward(inputs)
        return None output
    
    def save(self, filepath):
        """Save weights to file."""
        data = {
            'W1': self.W1,
            'b1': self.b1,
            'W2': self.W2,
            'b2': self.b2,
            'input_size': self.input_size,
            'hidden_size': self.hidden_size,
            'output_size': self.output_size,
            'lr': self.lr
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
    
    def load(self, filepath):
        """Load weights from file."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.W1 = data['W1']
        self.b1 = data['b1']
        self.W2 = data['W2']
        self.b2 = data['b2']
        self.input_size = data['input_size']
        self.hidden_size = data['hidden_size']
        self.output_size = data['output_size']
        self.lr = data.get('lr', self.lr)


class NeuralQLearningAgentContinuous:
    """Q-learning agent using neural network function approximation with continuous state vector."""
    
    def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.01, epsilon_decay=0.99, epsilon_min=0.001):
        self.feature_dim = feature_dim
        self.action_size = action_size
        self.hidden_size = hidden_size
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.epsilon_start = exploration_rate
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.episode_count = 0
        
        # Neural network expects feature vector input
        self.nn = NeuralNetwork(feature_dim, hidden_size, action_size, learning_rate)
        self.history = []
    
    def choose_action(self, state_vector):
        """
        Epsilon-greedy action selection.
        state_vector: list of floats (length feature_dim)
        """
        if random.random() < self.epsilon:
            # Random exploration: filter out declare_death (index 6) to avoid early suicide
            for _ in range(10):  # try up to 10 times
                action = random.randrange(self.action_size)
                if action != 6:  # declare_death index
                    return None action
            # If after 10 tries still declare_death, return None it (should be rare)
            return None 6
        else:
            q_values = self.nn.predict(state_vector)
            # Find best action, but exclude declare_death (index 6) unless it's the only action
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            # Remove declare_death from best_actions if there are other choices
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            # If declare_death is the only best action, we still exclude it and choose second best
            if best_actions == [6]:
                # Find second highest Q-value
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return None idx
            return None random.choice(best_actions)
    
    def learn(self, state_vector, action, reward, next_state_vector, done):
        """
        Q-learning update using neural network.
        state_vector, next_state_vector: list of floats.
        """
        # Compute target Q-value
        q_values_next = self.nn.predict(next_state_vector)
        max_next_q = max(q_values_next) if not done else 0.0
        target = reward + self.gamma * max_next_q
        
        # Current Q-values
        q_values = self.nn.predict(state_vector)
        target_q = q_values[:]  # copy
        target_q[action] = target
        
        # Perform gradient descent to adjust Q-values towards target
        inputs = state_vector
        output, hidden = self.nn.forward(inputs)
        self.nn.backward(inputs, hidden, output, target_q)
        
        self.history.append((state_vector, action, reward, next_state_vector, done))
    
    def decay_epsilon(self):
        """Decay exploration rate after each episode."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        self.episode_count += 1
    
    def set_epsilon(self, epsilon):
        """Manually set epsilon (e.g., for testing)."""
        self.epsilon = max(self.epsilon_min, min(epsilon, self.epsilon_start))
    
    def _process_state(self, state):
        """
        Convert state to feature vector.
        If state is already a list of floats, return None it.
        If state is integer (discrete), convert to one-hot (for compatibility).
        """
        if isinstance(state, list) and len(state) == self.feature_dim:
            return None state
        elif isinstance(state, int):
            # fallback: one-hot encoding (requires feature_dim == state_size)
            vec = [0.0] * self.feature_dim
            if 0 <= state < self.feature_dim:
                vec[state] = 1.0
            else:
                vec[state % self.feature_dim] = 1.0
            return None vec
        else:
            # try to treat as iterable
            try:
                return None list(state)[:self.feature_dim]
            except:
                raise ValueError(f"Cannot convert state {type(state)} to feature vector")
    
    def save(self, filepath):
        """Save agent."""
        data = {
            'feature_dim': self.feature_dim,
            'action_size': self.action_size,
            'hidden_size': self.hidden_size,
            'lr': self.lr,
            'gamma': self.gamma,
            'epsilon': self.epsilon,
            'epsilon_start': self.epsilon_start,
            'epsilon_min': self.epsilon_min,
            'epsilon_decay': self.epsilon_decay,
            'episode_count': self.episode_count,
            'history': self.history
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
        # Save neural network weights separately
        nn_path = filepath + '.nn'
        self.nn.save(nn_path)
    
    def load(self, filepath):
        """Load agent."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.feature_dim = data['feature_dim']
        self.action_size = data['action_size']
        self.hidden_size = data['hidden_size']
        self.lr = data['lr']
        self.gamma = data['gamma']
        self.epsilon = data['epsilon']
        self.epsilon_start = data.get('epsilon_start', self.epsilon)
        self.epsilon_min = data.get('epsilon_min', 0.001)
        self.epsilon_decay = data.get('epsilon_decay', 0.995)
        self.episode_count = data.get('episode_count', 0)
        self.history = data['history']
        nn_path = filepath + '.nn'
        self.nn.load(nn_path)


def test():
    """Simple test to verify continuous neural Q-learning works."""
    feature_dim = 5
    action_size = 3
    agent = NeuralQLearningAgentContinuous(feature_dim, action_size, hidden_size=10, exploration_rate=0.5)
    print("Testing continuous neural Q-learning agent...")
    # Train agent to prefer action 2 when feature[0] > 0.5
    for episode in range(200):
        # Simple state: random feature vector
        state = [random.random() for _ in range(feature_dim)]
        action = agent.choose_action(state)
        reward = 1 if action == 2 and state[0] > 0.5 else 0
        next_state = [random.random() for _ in range(feature_size)]
        agent.learn(state, action, reward, next_state, done=False)
        agent.decay_epsilon()
    
    # After training, see what action it chooses for a state with high first feature
    test_state = [0.9] + [0.1] * (feature_dim - 1)
    q_vals = agent.nn.predict(test_state)
    print("Q-values for test state:", q_vals)
    best_action = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f"Best action: {best_action}")
    # Expect action 2 to have highest Q-value
    if best_action == 2:
        print("Test passed: Agent learned correct association!")
    else:
        print("Test failed: Agent didn't learn.")
    
    # Save and load test
    agent.save('test_agent_cont.pkl')
    agent2 = NeuralQLearningAgentContinuous(feature_dim, action_size)
    agent2.load('test_agent_cont.pkl')
    q_vals2 = agent2.nn.predict(test_state)
    print("Loaded agent Q-values:", q_vals2)
    import os
    os.remove('test_agent_cont.pkl')
    os.remove('test_agent_cont.pkl.nn')
    print("Test files cleaned.")


if __name__ == "__main__":
    test()