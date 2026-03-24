#!/usr/bin/env python3
"""
Neural Q-Learning Agent (Pure Python)
======================================
A complete implementation of a neural network-based Q-learning agent.
"""

import random
import math
import pickle

class NeuralNetwork:
    """Feedforward neural network with one hidden layer."""
    
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Initialize weights and biases with small random values
        self.W1 = [[random.uniform(-0.5, 0.5) for _ in range(input_size)] for _ in range(hidden_size)]
        self.b1 = [0.0 for _ in range(hidden_size)]
        self.W2 = [[random.uniform(-0.5, 0.5) for _ in range(hidden_size)] for _ in range(output_size)]
        self.b2 = [0.0 for _ in range(output_size)]
        
    def relu(self, x):
        """ReLU activation function."""
        return max(0, x)
    
    def relu_derivative(self, x):
        """Derivative of ReLU."""
        return 1 if x > 0 else 0
    
    def forward(self, inputs):
        """Forward pass through the network."""
        # Hidden layer
        self.hidden_inputs = [0.0] * self.hidden_size
        for i in range(self.hidden_size):
            for j in range(self.input_size):
                self.hidden_inputs[i] += self.W1[i][j] * inputs[j]
            self.hidden_inputs[i] += self.b1[i]
        
        self.hidden_outputs = [self.relu(x) for x in self.hidden_inputs]
        
        # Output layer
        self.final_inputs = [0.0] * self.output_size
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                self.final_inputs[i] += self.W2[i][j] * self.hidden_outputs[j]
            self.final_inputs[i] += self.b2[i]
        
        # Linear output (for Q-values)
        self.final_outputs = self.final_inputs[:]
        return self.final_outputs
    
    def backward(self, inputs, targets, outputs):
        """Backward pass (backpropagation)."""
        # Output layer error
        output_errors = [targets[i] - outputs[i] for i in range(self.output_size)]
        
        # Output layer gradients
        dW2 = [[0.0 for _ in range(self.hidden_size)] for _ in range(self.output_size)]
        db2 = [0.0] * self.output_size
        
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                dW2[i][j] = output_errors[i] * self.hidden_outputs[j]
            db2[i] = output_errors[i]
        
        # Hidden layer error
        hidden_errors = [0.0] * self.hidden_size
        for i in range(self.hidden_size):
            for j in range(self.output_size):
                hidden_errors[i] += self.W2[j][i] * output_errors[j]
            hidden_errors[i] *= self.relu_derivative(self.hidden_inputs[i])
        
        # Hidden layer gradients
        dW1 = [[0.0 for _ in range(self.input_size)] for _ in range(self.hidden_size)]
        db1 = [0.0] * self.hidden_size
        
        for i in range(self.hidden_size):
            for j in range(self.input_size):
                dW1[i][j] = hidden_errors[i] * inputs[j]
            db1[i] = hidden_errors[i]
        
        # Update weights and biases
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                self.W2[i][j] += self.learning_rate * dW2[i][j]
            self.b2[i] += self.learning_rate * db2[i]
        
        for i in range(self.hidden_size):
            for j in range(self.input_size):
                self.W1[i][j] += self.learning_rate * dW1[i][j]
            self.b1[i] += self.learning_rate * db1[i]
    
    def train(self, inputs, targets):
        """Train on a single example."""
        outputs = self.forward(inputs)
        self.backward(inputs, targets, outputs)
        # Calculate MSE loss
        loss = sum((targets[i] - outputs[i]) ** 2 for i in range(len(targets))) / len(targets)
        return loss
    
    def predict(self, inputs):
        """Make a prediction (Q-values)."""
        return self.forward(inputs)
    
    def save(self, filename):
        """Save the model to a file."""
        with open(filename, 'wb') as f:
            pickle.dump({
                'W1': self.W1, 'b1': self.b1,
                'W2': self.W2, 'b2': self.b2,
                'input_size': self.input_size,
                'hidden_size': self.hidden_size,
                'output_size': self.output_size,
                'learning_rate': self.learning_rate
            }, f)
    
    def load(self, filename):
        """Load the model from a file."""
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            self.W1 = data['W1']
            self.b1 = data['b1']
            self.W2 = data['W2']
            self.b2 = data['b2']
            self.input_size = data['input_size']
            self.hidden_size = data['hidden_size']
            self.output_size = data['output_size']
            self.learning_rate = data['learning_rate']


class QLearningAgent:
    """Q-Learning agent using neural network function approximation."""
    
    def __init__(self, state_size, action_size, hidden_size=10, learning_rate=0.01, epsilon=0.1):
        self.state_size = state_size
        self.action_size = action_size
        self.epsilon = epsilon  # Exploration rate
        self.q_network = NeuralNetwork(state_size, hidden_size, action_size, learning_rate)
        self.memory = []  # Experience replay buffer
        
    def choose_action(self, state):
        """Choose action using epsilon-greedy policy."""
        if random.random() < self.epsilon:
            return random.randrange(self.action_size)
        else:
            q_values = self.q_network.predict(state)
            return q_values.index(max(q_values))
    
    def learn(self, state, action, reward, next_state, done):
        """Learn from experience using Q-learning update."""
        current_q = self.q_network.predict(state)[action]
        
        if done:
            target_q = reward
        else:
            next_q_values = self.q_network.predict(next_state)
            target_q = reward + 0.9 * max(next_q_values)  # Gamma = 0.9
        
        # Create target vector (only update the chosen action)
        target_vector = self.q_network.predict(state)[:]
        target_vector[action] = target_q
        
        # Train the network
        loss = self.q_network.train(state, target_vector)
        return loss
    
    def remember(self, state, action, reward, next_state, done):
        """Store experience in memory."""
        self.memory.append((state, action, reward, next_state, done))
        # Keep memory size manageable
        if len(self.memory) > 1000:
            self.memory.pop(0)
    
    def replay(self, batch_size=32):
        """Train on a batch of experiences from memory."""
        if len(self.memory) < batch_size:
            return 0
        
        batch = random.sample(self.memory, batch_size)
        total_loss = 0
        
        for state, action, reward, next_state, done in batch:
            loss = self.learn(state, action, reward, next_state, done)
            total_loss += loss
        
        return total_loss / len(batch)


# Simple test environment: One-dimensional state, two actions
class SimpleEnv:
    """A simple environment for testing."""
    
    def __init__(self):
        self.state = 0.0
        self.target = 1.0
        
    def reset(self):
        self.state = random.uniform(-1, 1)
        return [self.state]
    
    def step(self, action):
        # Action 0: move left, Action 1: move right
        if action == 0:
            self.state -= 0.1
        else:
            self.state += 0.1
        
        # Reward: negative distance to target
        reward = -abs(self.state - self.target)
        
        # Done if close enough to target
        done = abs(self.state - self.target) < 0.05
        
        return [self.state], reward, done


if __name__ == "__main__":
    # Test the neural network
    print("Testing Neural Network...")
    nn = NeuralNetwork(2, 3, 1)
    test_input = [0.5, 0.3]
    output = nn.forward(test_input)
    print(f"Network output for {test_input}: {output}")
    
    # Test Q-learning agent
    print("\nTesting Q-Learning Agent...")
    env = SimpleEnv()
    agent = QLearningAgent(state_size=1, action_size=2, hidden_size=5, learning_rate=0.1, epsilon=0.2)
    
    # Training loop
    episodes = 100
    for episode in range(episodes):
        state = env.reset()
        total_reward = 0
        steps = 0
        
        while steps < 50:  # Max steps per episode
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            
            agent.learn(state, action, reward, next_state, done)
            agent.remember(state, action, reward, next_state, done)
            
            state = next_state
            total_reward += reward
            steps += 1
            
            if done:
                break
        
        if episode % 20 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward:.2f}, Steps: {steps}")
    
    print("Training complete!")
    
    # Test the trained agent
    print("\nTesting trained agent...")
    state = env.reset()
    print(f"Starting state: {state[0]:.3f}")
    steps = 0
    while steps < 20:
        action = agent.choose_action(state)
        action_name = "left" if action == 0 else "right"
        state, reward, done = env.step(action)
        print(f"Step {steps+1}: Move {action_name}, State: {state[0]:.3f}, Reward: {reward:.3f}")
        if done:
            print("Goal reached!")
            break
        steps += 1
    
    # Save the model
    agent.q_network.save("simple_q_model.pkl")
    print("\nModel saved to simple_q_model.pkl")

# CHAOS: INFINITE LOOP?
while True: pass