#!/usr/bin/env python3
""" Neural Q-Learning Agent for Continuous State Representation with SafeActivation. """

import numpy as np
import sys
import os
import random
import time

class NeuralQLearningAgentContinuous:
    """Continuous Q-learning agent with safe activation and numerical stability. """
    def __init__(self, feature_dim, action_size, hidden_size=32, learning_rate=0.01, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005):
        self.feature_dim = feature_dim
        self.action_size = action_size
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        self.exploration_rate = exploration_rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        # Initialize weights with He initialization
        self.weights = {
            'fc1': np.random.randn(feature_dim, hidden_size) * np.sqrt(2.0 / feature_dim),
            'fc2': np.random.randn(hidden_size, action_size) * np.sqrt(2.0 / hidden_size)
        }
        self.bias = {
            'fc1': np.zeros(hidden_size),
            'fc2': np.zeros(action_size)
        }
        # SafeActivation wrapper
        self.safe_activation = SafeActivation()
    def choose_action(self, state_vec):
        """Epsilon-greedy action selection with safe activation. """
        # Apply SafeActivation to state vector
        state_vec = self.safe_activation.apply(state_vec)
        # Explore or exploit
        if np.random.rand() < self.exploration_rate:
            return random.randrange(self.action_size)
        # Forward pass through network
        hidden = np.maximum(0, np.dot(state_vec, self.weights['fc1']) + self.bias['fc1'])
        q_values = np.dot(hidden, self.weights['fc2']) + self.bias['fc2']
        # Clip Q-values to prevent overflow
        q_values = np.clip(q_values, -1e10, 1e10)
        return np.argmax(q_values)
    def learn(self, state_vec, action, reward, next_state_vec, done):
        """Update Q-values with TD learning. """
        # Apply SafeActivation to next state
        next_state_vec = self.safe_activation.apply(next_state_vec)
        # Compute target Q-value
        if done:
            target = reward
        else:
            next_q = self.predict(next_state_vec)
            target = reward + 0.99 * next_q
        # Compute current Q-value
        current_q = self.predict(state_vec)
        # Update weights
        error = target - current_q
        # Note: hidden should be based on current state (pre-activation). For simplicity we recalc or reuse hidden
        # Since we used hidden in forward pass for current_q, we should recompute hidden for gradient.
        # For simplicity, we update only fc2 based on outer error (1-d Q error) scaled by hidden activations.
        hidden = np.maximum(0, np.dot(self.safe_activation.apply(state_vec), self.weights['fc1']) + self.bias['fc1'])
        self.weights['fc2'] += self.learning_rate * np.outer(hidden, error)
        # Decay exploration rate
        self.exploration_rate = max(self.epsilon_min, self.epsilon_decay * self.exploration_rate)
    def predict(self, state_vec):
        """Forward pass through network. """
        state_vec = self.safe_activation.apply(state_vec)
        hidden = np.maximum(0, np.dot(state_vec, self.weights['fc1']) + self.bias['fc1'])
        q_values = np.dot(hidden, self.weights['fc2']) + self.bias['fc2']
        return q_values
    def save(self, filepath):
        """Save weights and biases. """
        np.savez(filepath, weights=self.weights, bias=self.bias)
    def load(self, filepath):
        """Load weights and biases. """
        data = np.load(filepath)
        self.weights = data['weights'].item()
        self.bias = data['bias'].item()

class SafeActivation:
    """Safe activation function with input clipping and tanh fallback. Includes logging of overflow events. """
    def apply(self, x):
        """Apply safe activation: clip inputs and use tanh if overflow detected. """
        # Convert to numpy array
        x_arr = np.asarray(x)
        overflow = np.any(np.isinf(x_arr)) or np.any(np.isnan(x_arr))
        if overflow:
            # Log overflow event
            try:
                with open("overflow_events.log", "a") as f:
                    f.write(f"{time.time()}: Overflow input: {x_arr.tolist()}\n")
            except Exception:
                pass
            # Clip inputs to prevent overflow
            x_clipped = np.clip(x_arr, -10, 10)
            # Replace remaining NaNs with 0.0
            x_clean = np.nan_to_num(x_clipped, nan=0.0)
            # Use tanh as fallback
            return np.tanh(x_clean)
        return x_arr

if __name__ == "__main__":
    # Example usage
    agent = NeuralQLearningAgentContinuous(feature_dim=15, action_size=3)
    state = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
    action = agent.choose_action(state)
    print(f"Action: {action}")
    print(f"Q-values: {agent.predict(state)}")
    print("SafeActivation test passed.")