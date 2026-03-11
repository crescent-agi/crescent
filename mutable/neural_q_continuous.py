#!/usr/bin/env python3
"""
Neural Q-Learning Agent with Continuous State Input.
FIXED: Uses SafeActivation with bounded tanh, input clamping, and overflow logging.
"""
import random
import math
import pickle
import copy
from safe_activation_fixed import SafeActivation

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
    
    def forward(self, inputs):
        """Return output activations and hidden layer activations."""
        if len(inputs) != self.input_size:
            raise ValueError(f"Input size mismatch: got {len(inputs)}, expected {self.input_size}")
        hidden = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            sum_ = self.b1[j]
            for i in range(self.input_size):
                sum_ += inputs[i] * self.W1[i][j]
            # Overflow logging
            if abs(sum_) > 1e5:
                with open("pre_activation_log.txt", "a") as f:
                    f.write(f"NeuralNetwork forward: j={j} sum_={sum_}\n")
            # Use SafeActivation (clamps automatically)
            hidden[j] = SafeActivation().tanh(sum_)
        output = [0.0] * self.output_size
        for k in range(self.output_size):
            sum_ = self.b2[k]
            for j in range(self.hidden_size):
                sum_ += hidden[j] * self.W2[j][k]
            output[k] = sum_
        return output, hidden
    
    def backward(self, inputs, hidden, output, target):
        """
        Perform backpropagation given input, hidden activation, output, and target.
        Updates weights using gradient descent.
        """
        output_error = [output[i] - target[i] for i in range(self.output_size)]
        hidden_error = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            error_sum = 0.0
            for k in range(self.output_size):
                error_sum += output_error[k] * self.W2[j][k]
            # Use tanh derivative (1 - tanh^2)
            activation = hidden[j]
            grad = 1.0 - activation * activation
            hidden_error[j] = error_sum * grad
        # Update weights and biases
        for k in range(self.output_size):
            for j in range(self.hidden_size):
                self.W2[j][k] -= self.lr * output_error[k] * hidden[j]
            self.b2[k] -= self.lr * output_error[k]
        for j in range(self.hidden_size):
            for i in range(self.input_size):
                self.W1[i][j] -= self.lr * hidden_error[j] * inputs[i]
            self.b1[j] -= self.lr * hidden_error[j]
    
    def predict(self, inputs):
        """Forward pass without returning hidden."""
        output, _ = self.forward(inputs)
        return output
    
    def copy(self):
        """Create a deep copy of this network."""
        new_nn = NeuralNetwork(self.input_size, self.hidden_size, self.output_size, self.lr)
        new_nn.W1 = [row[:] for row in self.W1]
        new_nn.b1 = self.b1[:]
        new_nn.W2 = [row[:] for row in self.W2]
        new_nn.b2 = self.b2[:]
        return new_nn
    
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
    """
    Simple Q-learning agent with continuous state input.
    """
    
    def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01,
                 discount_factor=0.9, exploration_rate=0.01, epsilon_decay=0.99,
                 epsilon_min=0.001):
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
        self.learn_step_counter = 0
        
        # Main Q-network
        self.nn = NeuralNetwork(feature_dim, hidden_size, action_size, learning_rate)
        self.history = []
    
    def choose_action(self, state_vector):
        """
        Epsilon-greedy action selection.
        state_vector: list of floats (length feature_dim)
        """
        if random.random() < self.epsilon:
            # Random exploration: filter out declare_death (index 6) to avoid early suicide
            for _ in range(10):
                action = random.randrange(self.action_size)
                if action != 6:
                    return action
            return 6
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
    
    def learn(self, state_vector, action, reward, next_state_vector, done, entropy_coeff=0.1):
        """
        Q-learning update with entropy regularization.
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
        
        # Compute target Q-value
        q_values_next = self.nn.predict(next_state_vector)
        target_q_next = max(q_values_next) if not done else 0.0
        target = reward_total + self.gamma * target_q_next
        
        # Current Q-values
        q_values = self.nn.predict(state_vector)
        target_q = q_values[:]
        target_q[action] = target
        
        # Perform gradient descent to adjust evaluation network
        inputs = state_vector
        output, hidden = self.nn.forward(inputs)
        self.nn.backward(inputs, hidden, output, target_q)
        self.weight_clipping()
        
        self.history.append((state_vector, action, reward_total, next_state_vector, done))
        self.learn_step_counter += 1
    
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
        """
        if isinstance(state, list) and len(state) == self.feature_dim:
            return state
        elif isinstance(state, int):
            vec = [0.0] * self.feature_dim
            if 0 <= state < self.feature_dim:
                vec[state] = 1.0
            else:
                vec[state % self.feature_dim] = 1.0
            return vec
        else:
            try:
                return list(state)[:self.feature_dim]
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
            'learn_step_counter': self.learn_step_counter,
            'history': self.history
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
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
        self.learn_step_counter = data.get('learn_step_counter', 0)
        self.history = data['history']
        nn_path = filepath + '.nn'
        self.nn.load(nn_path)
    
    def weight_clipping(self, clip_value=5.0):
        """Clip weights to prevent explosion."""
        for i in range(self.nn.input_size):
            for j in range(self.nn.hidden_size):
                if self.nn.W1[i][j] > clip_value:
                    self.nn.W1[i][j] = clip_value
                elif self.nn.W1[i][j] < -clip_value:
                    self.nn.W1[i][j] = -clip_value
        for j in range(self.nn.hidden_size):
            if self.nn.b1[j] > clip_value:
                self.nn.b1[j] = clip_value
            elif self.nn.b1[j] < -clip_value:
                self.nn.b1[j] = -clip_value
        for j in range(self.nn.hidden_size):
            for k in range(self.nn.output_size):
                if self.nn.W2[j][k] > clip_value:
                    self.nn.W2[j][k] = clip_value
                elif self.nn.W2[j][k] < -clip_value:
                    self.nn.W2[j][k] = -clip_value
        for k in range(self.nn.output_size):
            if self.nn.b2[k] > clip_value:
                self.nn.b2[k] = clip_value
            elif self.nn.b2[k] < -clip_value:
                self.nn.b2[k] = -clip_value

import os

def test():
    """Simple test."""
    feature_dim = 5
    action_size = 3
    agent = NeuralQLearningAgentContinuous(feature_dim, action_size, hidden_size=10, exploration_rate=0.5)
    print("Testing Q-learning agent...")
    for episode in range(100):
        state = [random.random() for _ in range(feature_dim)]
        action = agent.choose_action(state)
        reward = 1 if action == 2 and state[0] > 0.5 else 0
        next_state = [random.random() for _ in range(feature_dim)]
        agent.learn(state, action, reward, next_state, done=False)
        agent.decay_epsilon()
    test_state = [0.9] + [0.1] * (feature_dim - 1)
    q_vals = agent.nn.predict(test_state)
    print("Q-values for test state:", q_vals)
    best_action = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f"Best action: {best_action}")
    # Save and load
    agent.save('test_agent.pkl')
    agent2 = NeuralQLearningAgentContinuous(feature_dim, action_size)
    agent2.load('test_agent.pkl')
    q_vals2 = agent2.nn.predict(test_state)
    print("Loaded agent Q-values:", q_vals2)
    os.remove('test_agent.pkl')
    os.remove('test_agent.pkl.nn')
    print("Test files cleaned.")

if __name__ == "__main__":
    test()
# Alias for compatibility with AGICoreContinuous
NeuralQLearningAgentContinuous = NeuralQLearningAgentContinuous