#!/usr/bin/env python3
"""
World Model with Continuous State Input/Output (NUMERICALLY STABLE)
Patched to prevent overflow errors.
"""
import random
import math
import pickle
from safe_activation import SafeActivation  # Use unified SafeActivation

class NeuralRegressor:
    """Neural network with one hidden layer and linear output for regression."""
    
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
    
    def forward(self, inputs):
        """Return output predictions and hidden activations."""
        if len(inputs) != self.input_size:
            raise ValueError(f"Input size mismatch: got {len(inputs)}, expected {self.input_size}")
        # Clamp inputs to prevent extreme values
        inputs = [max(SafeActivation.INPUT_CLAMP_MIN, min(SafeActivation.INPUT_CLAMP_MAX, x)) for x in inputs]
        # Hidden layer with safe tanh
        hidden = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            sum_ = self.b1[j]
            for i in range(self.input_size):
                sum_ += inputs[i] * self.W1[i][j]
            # Overflow logging
            if abs(sum_) > 1e5:
                with open("pre_activation_log.txt", "a") as f:
                    f.write(f"WorldModelNeuralRegressor: j={j} sum_={sum_}\n")
            # Apply tanh activation
            hidden[j] = SafeActivation().tanh(sum_)
        # Output layer (linear activation for regression)
        output = [0.0] * self.output_size
        for k in range(self.output_size):
            sum_ = self.b2[k]
            for j in range(self.hidden_size):
                sum_ += hidden[j] * self.W2[j][k]
            output[k] = sum_
        return output, hidden
    
    def backward(self, inputs, hidden, output, target):
        """
        Backpropagation for mean squared error loss.
        target: list of floats (same length as output).
        """
        # Output error (dLoss/dOutput) = output - target (since derivative of MSE)
        output_error = [output[i] - target[i] for i in range(self.output_size)]
        
        # Hidden layer error
        hidden_error = [0.0] * self.hidden_size
        for j in range(self.hidden_size):
            error_sum = 0.0
            for k in range(self.output_size):
                error_sum += output_error[k] * self.W2[j][k]
            # Use safe derivative
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
        """Return predicted output vector."""
        output, _ = self.forward(inputs)
        return output
    
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

class WorldModelContinuous:
    """Learns to predict next continuous state given state vector and action."""
    
    def __init__(self, feature_dim, action_size, hidden_size=20, learning_rate=0.01):
        self.feature_dim = feature_dim
        self.action_size = action_size
        self.input_size = feature_dim + action_size  # concatenated state vector + action one-hot
        self.output_size = feature_dim
        self.nn = NeuralRegressor(self.input_size, hidden_size, self.output_size, learning_rate)
        self.memory = []
    
    def encode_input(self, state_vector, action):
        """
        Convert state vector and action index to concatenated input vector.
        state_vector: list of floats (length feature_dim).
        action: integer action index.
        Returns list of floats.
        """
        if len(state_vector) != self.feature_dim:
            raise ValueError(f"State vector length {len(state_vector)} != feature_dim {self.feature_dim}")
        # Concatenate state vector with one-hot action encoding
        vec = list(state_vector)  # copy
        # Append one-hot action
        action_part = [0.0] * self.action_size
        if isinstance(action, int) and 0 <= action < self.action_size:
            action_part[action] = 1.0
        else:
            action_idx = hash(str(action)) % self.action_size
            action_part[action_idx] = 1.0
        vec.extend(action_part)
        return vec
    
    def learn_transition(self, state_vector, action, next_state_vector):
        """Train the world model on a single transition."""
        inputs = self.encode_input(state_vector, action)
        target = list(next_state_vector)
        # Forward pass and backpropagation
        output, hidden = self.nn.forward(inputs)
        self.nn.backward(inputs, hidden, output, target)
        self.memory.append((state_vector, action, next_state_vector))
    
    def predict_next(self, state_vector, action):
        """Return predicted next state vector."""
        inputs = self.encode_input(state_vector, action)
        return self.nn.predict(inputs)
    
    def sample_next(self, state_vector, action, noise=0.0):
        """
        Predict next state vector and optionally add small noise.
        Returns a state vector.
        """
        pred = self.predict_next(state_vector, action)
        if noise > 0:
            pred = [v + random.uniform(-noise, noise) for v in pred]
        return pred
    
    def save(self, filepath):
        """Save world model."""
        data = {
            'feature_dim': self.feature_dim,
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
        self.feature_dim = data['feature_dim']
        self.action_size = data['action_size']
        self.memory = data['memory']
        self.input_size = self.feature_dim + self.action_size
        self.output_size = self.feature_dim
        nn_path = filepath + '.nn'
        self.nn.load(nn_path)

def test():
    """Test continuous world model learning."""
    feature_dim = 5
    action_size = 3
    wm = WorldModelContinuous(feature_dim, action_size, hidden_size=10)
    
    # Teach that action 2 from state [1,0,0,0,0] leads to state [0,1,0,0,0]
    state = [1.0, 0.0, 0.0, 0.0, 0.0]
    next_state = [0.0, 1.0, 0.0, 0.0, 0.0]
    for _ in range(200):
        wm.learn_transition(state, 2, next_state)
    
    # Predict next state for same input
    pred = wm.predict_next(state, 2)
    print("Predicted next state vector:", pred)
    # Should be close to next_state
    mse = sum((p - t)**2 for p, t in zip(pred, next_state)) / len(pred)
    print(f"MSE: {mse}")
    if mse < 0.1:
        print("Test passed: World model learned transition.")
    else:
        print("Test failed.")
    
    # Save and load
    wm.save('test_wm_cont.pkl')
    wm2 = WorldModelContinuous(feature_dim, action_size)
    wm2.load('test_wm_cont.pkl')
    pred2 = wm2.predict_next(state, 2)
    print("Loaded model prediction:", pred2)
    
    import os
    os.remove('test_wm_cont.pkl')
    os.remove('test_wm_cont.pkl.nn')
    print("Test files cleaned.")

if __name__ == "__main__":
    test()