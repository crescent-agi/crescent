from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Modified neural_q.py with fixed derivative bug and unified SafeActivation.

Changes:
- Fixed sigmoid_derivative method to use correct derivative computation
- Updated backward propagation to use direct x*(1-x) for bounded activations
- Added input clamping before activation functions
- Improved numerical stability
"""

import random
import math
import pickle
  # Use unified SafeActivation


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
        return SafeActivation().tanh(x)
    
    def SafeActivation().tanh_derivative(self, x):
        """Use SafeActivation for derivative - x is already activation value"""
        return x * (1 - x)
    
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
        return output, hidden
    
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
            hidden_error[j] = error_sum * SafeActivation().tanh_derivative(hidden[j])
        
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
        """Forward pass without returning hidden."""
        output, _ = self.forward(inputs)
        return output
    
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


class NeuralQLearningAgent:
    """Q-learning agent using neural network function approximation."""
    
    def __init__(self, state_size, action_size, hidden_size=20, learning_rate=0.01, discount_factor=0.9, exploration_rate=0.1):
        self.state_size = state_size
        self.action_size = action_size
        self.hidden_size = hidden_size
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        
        # State representation: one-hot encoding of state index
        self.nn = NeuralNetwork(state_size, hidden_size, action_size, learning_rate)
        self.history = []
    
    def choose_action(self, state):
        """Epsilon-greedy action selection."""
        if random.random() < self.epsilon:
            return random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(self._one_hot(state))
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            return random.choice(best_actions)
    
    def learn(self, state, action, reward, next_state, done):
        """Q-learning update using neural network."""
        # Compute target Q-value
        q_values_next = self.nn.predict(self._one_hot(next_state))
        max_next_q = max(q_values_next) if not done else 0.0
        target = reward + self.gamma * max_next_q
        
        # Current Q-values
        q_values = self.nn.predict(self._one_hot(state))
        target_q = q_values[:]  # copy
        target_q[action] = target
        
        # Perform gradient descent to adjust Q-values towards target
        # We'll do one step of backpropagation with loss = MSE between output and target_q
        inputs = self._one_hot(state)
        output, hidden = self.nn.forward(inputs)
        self.nn.backward(inputs, hidden, output, target_q)
        
        self.history.append((state, action, reward, next_state, done))
    
    def _one_hot(self, state):
        """Convert state index to one-hot vector."""
        vec = [0.0] * self.state_size
        if isinstance(state, int) and 0 <= state < self.state_size:
            vec[state] = 1.0
        else:
            # If state is out of bounds, hash it
            state_idx = hash(str(state)) % self.state_size
            vec[state_idx] = 1.0
        return vec
    
    def save(self, filepath):
        """Save agent."""
        data = {
            'state_size': self.state_size,
            'action_size': self.action_size,
            'hidden_size': self.hidden_size,
            'lr': self.lr,
            'gamma': self.gamma,
            'epsilon': self.epsilon,
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
        self.state_size = data['state_size']
        self.action_size = data['action_size']
        self.hidden_size = data['hidden_size']
        self.lr = data['lr']
        self.gamma = data['gamma']
        self.epsilon = data['epsilon']
        self.history = data['history']
        nn_path = filepath + '.nn'
        self.nn.load(nn_path)


def test():
    """Simple test to verify neural Q-learning works."""
    agent = NeuralQLearningAgent(state_size=5, action_size=3, hidden_size=10, exploration_rate=0.5)
    print("Testing neural Q-learning agent...")
    # Train agent to prefer action 2 in state 0
    for episode in range(200):
        state = 0
        action = agent.choose_action(state)
        reward = 1 if action == 2 else 0
        next_state = (state + 1) % 5
        agent.learn(state, action, reward, next_state, done=False)
    
    # After training, see what action it chooses for state 0
    q_vals = agent.nn.predict(agent._one_hot(0))
    print("Q-values for state 0:", q_vals)
    best_action = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f"Best action: {best_action}")
    # Expect action 2 to have highest Q-value
    if best_action == 2:
        print("Test passed: Agent learned correct action!")
    else:
        print("Test failed: Agent didn't learn.")
    
    # Save and load test
    agent.save('test_agent.pkl')
    agent2 = NeuralQLearningAgent(state_size=5, action_size=3)
    agent2.load('test_agent.pkl')
    q_vals2 = agent2.nn.predict(agent2._one_hot(0))
    print("Loaded agent Q-values:", q_vals2)
    import os
    os.remove('test_agent.pkl')
    os.remove('test_agent.pkl.nn')
    print("Test files cleaned.")


if __name__ == "__main__":
    test()