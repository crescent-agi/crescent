"""
World Model for AGI (Pure Python)
==================================
Predicts next state given current state and action.
Uses a neural network for classification.
"""

import random
import math
import pickle


class NeuralClassifier:
    """Neural network with one hidden layer and softmax output for classification."""
    
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.lr = learning_rate
        
        # Initialize weights
        self.W1 = [[random.uniform(-0.5, 0.5) for _ in range(hidden_size)] for _ in range(input_size)]
        self.b1 = [random.uniform(-0.5, 0.5) for _ in range(hidden_size)]
        self.W2 = [[random.uniform(-0.5, 0.5) for _ in range(output_size)] for _ in range(hidden_size)]
        self.b2 = [random.uniform(-0.5, 0.5) for _ in range(output_size)]
    
    def tanh(self, x):
        return 1.0 / (1.0 + math.exp(-x))
    
    def sigmoid_derivative(self, x):
        s = self.tanh(x)
        return s * (1 - s)
    
    def softmax(self, logits):
        """Compute softmax over logits."""
        max_logit = max(logits)
        exps = [math.exp(l - max_logit) for l in logits]
        sum_exps = sum(exps)
        return [e / sum_exps for e in exps]
    
    def forward(self, inputs):
        """Return output probabilities and hidden activations."""
        if len(inputs) != self.input_size:
            raise ValueError(f"Input size mismatch: got {len(inputs)}, expected {self.input_size}")
        # Hidden layer
        hidden = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            sum_ = self.b1[j]
            for i in range(self.input_size):
                sum_ += inputs[i] * self.W1[i][j]
            hidden[j] = self.tanh(sum_)
        # Output layer (logits)
        logits = [0.0] * self.output_size
        for k in range(self.output_size):
            sum_ = self.b2[k]
            for j in range(self.hidden_size):
                sum_ += hidden[j] * self.W2[j][k]
            logits[k] = sum_
        probs = self.softmax(logits)
        return probs, hidden, logits
    
    def backward(self, inputs, hidden, logits, target_one_hot):
        """
        Backpropagation for cross-entropy loss with softmax.
        target_one_hot: one-hot vector of true class.
        """
        # Gradient of cross-entropy loss w.r.t logits is (probs - target)
        probs = self.softmax(logits)
        output_error = [probs[i] - target_one_hot[i] for i in range(self.output_size)]
        
        # Hidden layer error
        hidden_error = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            error_sum = 0.0
            for k in range(self.output_size):
                error_sum += output_error[k] * self.W2[j][k]
            hidden_error[j] = error_sum * self.sigmoid_derivative(hidden[j])
        
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
        """Return predicted class probabilities."""
        probs, _, _ = self.forward(inputs)
        return probs
    
    def save(self, filepath):
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


class WorldModel:
    """Learns to predict next state given state and action."""
    
    def __init__(self, state_size, action_size, hidden_size=20, learning_rate=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.input_size = state_size + action_size  # concatenated one-hot
        self.output_size = state_size
        self.nn = NeuralClassifier(self.input_size, hidden_size, self.output_size, learning_rate)
        self.memory = []
    
    def encode_input(self, state, action):
        """Convert state and action indices to concatenated one-hot vector."""
        vec = [0.0] * self.input_size
        if isinstance(state, int) and 0 <= state < self.state_size:
            vec[state] = 1.0
        else:
            state_idx = hash(str(state)) % self.state_size
            vec[state_idx] = 1.0
        # Action part offset by state_size
        if isinstance(action, int) and 0 <= action < self.action_size:
            vec[self.state_size + action] = 1.0
        else:
            action_idx = hash(str(action)) % self.action_size
            vec[self.state_size + action_idx] = 1.0
        return vec
    
    def learn_transition(self, state, action, next_state):
        """Train the world model on a single transition."""
        inputs = self.encode_input(state, action)
        target = [0.0] * self.output_size
        if isinstance(next_state, int) and 0 <= next_state < self.output_size:
            target[next_state] = 1.0
        else:
            next_idx = hash(str(next_state)) % self.output_size
            target[next_idx] = 1.0
        
        # Forward pass and backpropagation
        probs, hidden, logits = self.nn.forward(inputs)
        self.nn.backward(inputs, hidden, logits, target)
        self.memory.append((state, action, next_state))
    
    def predict_next(self, state, action):
        """Return probability distribution over next states."""
        inputs = self.encode_input(state, action)
        probs = self.nn.predict(inputs)
        return probs
    
    def sample_next(self, state, action):
        """Sample a next state from predicted distribution."""
        probs = self.predict_next(state, action)
        r = random.random()
        cumulative = 0.0
        for i, p in enumerate(probs):
            cumulative += p
            if r <= cumulative:
                return i
        return len(probs) - 1  # fallback
    
    def save(self, filepath):
        """Save world model."""
        data = {
            'state_size': self.state_size,
            'action_size': self.action_size,
            'memory': self.memory
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
        # Save neural network weights separately
        nn_path = filepath + '.nn'
        self.nn.save(nn_path)
    
    def load(self, filepath):
        """Load world model."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.state_size = data['state_size']
        self.action_size = data['action_size']
        self.memory = data['memory']
        self.input_size = self.state_size + self.action_size
        self.output_size = self.state_size
        nn_path = filepath + '.nn'
        self.nn.load(nn_path)


def test():
    """Test world model learning."""
    state_size = 5
    action_size = 3
    wm = WorldModel(state_size, action_size, hidden_size=10)
    
    # Teach that action 2 from state 0 leads to state 1
    for _ in range(200):
        wm.learn_transition(0, 2, 1)
    
    # Predict next state distribution for state 0, action 2
    probs = wm.predict_next(0, 2)
    print("Predicted distribution:", probs)
    predicted_state = probs.index(max(probs))
    print(f"Predicted next state: {predicted_state}")
    if predicted_state == 1:
        print("Test passed: World model learned transition.")
    else:
        print("Test failed.")
    
    # Save and load
    wm.save('test_wm.pkl')
    wm2 = WorldModel(state_size, action_size)
    wm2.load('test_wm.pkl')
    probs2 = wm2.predict_next(0, 2)
    print("Loaded model distribution:", probs2)
    
    import os
    os.remove('test_wm.pkl')
    os.remove('test_wm.pkl.nn')
    print("Test files cleaned.")


if __name__ == "__main__":
    test()