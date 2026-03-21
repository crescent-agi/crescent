#!/usr/bin/env python3
"""
Hybrid Agent: Combines Q-learning with simple neural network function approximation.
Uses neural network for state-action value estimation while maintaining traditional Q-learning update rules.
"""

import numpy as np
import pickle
from typing import List, Dict, Any, Optional

class HybridAgent:
    def __init__(self, state_size: int, action_size: int, hidden_size: int = 24, 
                 learning_rate: float = 0.01, discount_factor: float = 0.99, 
                 exploration_rate: float = 1.0, exploration_decay: float = 0.995):
        """
        Initialize the hybrid agent.
        
        Args:
            state_size: Dimensionality of the state space
            action_size: Number of possible actions
            hidden_size: Number of neurons in the hidden layer
            learning_rate: Base learning rate for updates
            discount_factor: Discount factor for future rewards
            exploration_rate: Initial exploration rate (epsilon)
            exploration_decay: Rate at which exploration decays
        """
        self.state_size = state_size
        self.action_size = action_size
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        
        # Initialize neural network weights
        self._init_network()
        
        # Traditional Q-values dictionary for fallback
        self.q_values: Dict[str, Dict[str, float]] = {}
        self.visitation_counts: Dict[str, Dict[str, int]] = {}
        
    def _init_network(self):
        """Initialize neural network weights with small random values."""
        self.weights_input_hidden = np.random.normal(0, 0.1, 
                                                   (self.state_size, self.hidden_size))
        self.weights_hidden_output = np.random.normal(0, 0.1, 
                                                     (self.hidden_size, self.action_size))
        self.bias_hidden = np.zeros(self.hidden_size)
        self.bias_output = np.zeros(self.action_size)
        
    def _activate(self, x: np.ndarray) -> np.ndarray:
        """Simple sigmoid activation function."""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # Clip to avoid overflow
        
    def _forward_pass(self, state: np.ndarray) -> np.ndarray:
        """Perform forward pass through the neural network."""
        hidden_layer = self._activate(np.dot(state, self.weights_input_hidden) + self.bias_hidden)
        output_layer = np.dot(hidden_layer, self.weights_hidden_output) + self.bias_output
        return output_layer
    
    def _get_q_values(self, state: str) -> np.ndarray:
        """Get Q-values for all actions in a given state using neural approximation."""
        # Convert state string to vector representation (simple hash-based encoding)
        state_vector = np.zeros(self.state_size)
        # Use a simple deterministic encoding for string states
        for i, char in enumerate(state[:self.state_size]):
            state_vector[i] = (ord(char) % 10) / 9.0  # Normalize to 0-1 range
            
        q_values = self._forward_pass(state_vector)
        return q_values
    
    def choose_action(self, state: str, actions: List[str]) -> str:
        """
        Choose an action using epsilon-greedy policy.
        
        Args:
            state: Current state identifier
            actions: List of available actions
            
        Returns:
            Selected action
        """
        if np.random.random() < self.exploration_rate:
            # Exploration: choose random action
            return np.random.choice(actions)
        else:
            # Exploitation: use neural network to evaluate actions
            if state not in self.q_values:
                self.q_values[state] = {a: 0.0 for a in actions}
                self.visitation_counts[state] = {a: 0 for a in actions}
                
            # Get neural network predictions
            q_predictions = self._get_q_values(state)
            
            # Combine neural predictions with learned Q-values for better robustness
            combined_values = {}
            for i, action in enumerate(actions):
                # Base value from neural network
                neural_q = q_predictions[i] if i < len(q_predictions) else 0.0
                
                # Value from explicit Q-table (fallback)
                explicit_q = self.q_values[state][action]
                
                # Mix the values based on visitation count for stability
                visit_count = self.visitation_counts[state][action]
                exploration_bonus = 0.1 * (1.0 / (1.0 + visit_count))  # Bonus for seldom-visited actions
                
                # Combine neural and explicit values with exploration bonus
                combined_values[action] = 0.7 * neural_q + 0.3 * explicit_q + exploration_bonus
            
            # Select action with highest combined value
            return max(combined_values, key=combined_values.get)
    
    def _update_neural_weights(self, state: str, action: str, reward: float, 
                              next_state: str, actions: List[str]):
        """
        Update neural network weights based on experience.
        
        Implements a modified Q-learning update with neural approximation.
        """
        # Ensure state and next_state are in Q-values and visitation counts
        if state not in self.q_values:
            self.q_values[state] = {a: 0.0 for a in actions}
            self.visitation_counts[state] = {a: 0 for a in actions}
        if next_state not in self.q_values:
            self.q_values[next_state] = {a: 0.0 for a in actions}
            self.visitation_counts[next_state] = {a: 0 for a in actions}
            
        # Q-learning target
        current_q = self.q_values[state][action]
        next_max_q = max(self.q_values[next_state].values()) if next_state else 0.0
        target = reward + self.discount_factor * next_max_q
        
        # Experience-based learning rate adjustment
        visit_count = self.visitation_counts[state][action]
        adaptive_lr = self.learning_rate * (1.0 / (1.0 + visit_count ** 0.5))
        
        # Neural network weight updates using error signal
        # Convert state to vector for backpropagation-like update
        state_vector = np.zeros(self.state_size)
        for i, char in enumerate(state[:self.state_size]):
            state_vector[i] = (ord(char) % 10) / 9.0
            
        # Forward pass to get activations
        hidden_layer = self._activate(np.dot(state_vector, self.weights_input_hidden) + self.bias_hidden)
        output_layer = np.dot(hidden_layer, self.weights_hidden_output) + self.bias_output
        
        # Compute error for the taken action
        output_error = target - output_layer[0, actions.index(action)]
        
        # Backpropagate error to update weights
        # Update output layer weights and biases
        for a in range(self.action_size):
            self.weights_hidden_output[0, a] += adaptive_lr * output_error * hidden_layer[0]
            
        self.bias_output[actions.index(action)] += adaptive_lr * output_error
        
        # Update hidden layer weights and biases
        for h in range(self.hidden_size):
            self.weights_input_hidden[0, h] += adaptive_lr * output_error * hidden_layer[0] * hidden_layer[h] * (1-hidden_layer[h])
            self.bias_hidden[h] += adaptive_lr * output_error * hidden_layer[h] * (1-hidden_layer[h])
            
        # Update explicit Q-values for consistency
        self.q_values[state][action] += adaptive_lr * (target - current_q)
        self.visitation_counts[state][action] += 1
    
    def decay_exploration(self):
        """Decay the exploration rate according to the exploration decay schedule."""
        self.exploration_rate = max(0.01, self.exploration_rate * self.exploration_decay)
        
    def save(self, filepath: str):
        """Save the hybrid agent state to a file."""
        data = {
            'weights_input_hidden': self.weights_input_hidden,
            'weights_hidden_output': self.weights_hidden_output,
            'bias_hidden': self.bias_hidden,
            'bias_output': self.bias_output,
            'learning_rate': self.learning_rate,
            'discount_factor': self.discount_factor,
            'exploration_rate': self.exploration_rate,
            'exploration_decay': self.exploration_decay,
            'q_values': self.q_values,
            'visitation_counts': self.visitation_counts,
            'state_size': self.state_size,
            'action_size': self.action_size,
            'hidden_size': self.hidden_size
        }
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
    
    @staticmethod
    def load(filepath: str):
        """Load a saved hybrid agent from a file."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        
        agent = HybridAgent.__new__(HybridAgent)
        agent.__dict__.update(data)
        # Re-initialize network weights after loading
        agent._init_network()
        # Apply loaded weights
        agent.weights_input_hidden = data['weights_input_hidden']
        agent.weights_hidden_output = data['weights_hidden_output']
        agent.bias_hidden = data['bias_hidden']
        agent.bias_output = data['bias_output']
        return agent

    def get_q_values(self, state: str) -> Dict[str, float]:
        """Get all Q-values for a given state (combining neural and explicit)."""
        if state not in self.q_values:
            return {}
        return self.q_values[self.state_key(state)]

def main():
    """Simple test to demonstrate hybrid agent functionality."""
    print("Hybrid Agent Initialization Test")
    print("=" * 35)
    
    # Create a test agent
    agent = HybridAgent(
        state_size=5,      # Can represent up to 5-character states
        action_size=4,     # Four possible actions
        hidden_size=16,
        learning_rate=0.05,
        discount_factor=0.95,
        exploration_rate=1.0,
        exploration_decay=0.999
    )
    
    print(f"Agent initialized with:")
    print(f"  - State size: {agent.state_size}")
    print(f"  - Action size: {agent.action_size}")
    print(f"  - Hidden layer size: {agent.hidden_size}")
    print(f"  - Initial exploration rate: {agent.exploration_rate:.3f}")
    
    # Test action selection in a mock state
    actions = ['move_left', 'move_right', 'jump', 'wait']
    action = agent.choose_action('test_state', actions)
    print(f"\nTest action selection: {action}")
    
    # Test decay
    agent.decay_exploration()
    print(f"Exploration rate after decay: {agent.exploration_rate:.3f}")
    
    print("\nHybrid Agent implementation complete!")

if __name__ == "__main__":
    main()