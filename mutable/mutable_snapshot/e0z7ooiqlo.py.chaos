# Stability-Enhanced Reward Patch for AGI Core
# Addresses neural oscillation and range instability in deep learning systems

import numpy as np
import os
from typing import List, Dict, Tuple

def evaluate_neural_stability(activation_history: List[np.ndarray], threshold: float = 0.85) -> float:
    """
    Measures the stability of activation patterns across layers
    
    Args:
        activation_history: List of activation matrices from previous layer
        threshold: Maximum acceptable activation variance ratio
        
    Returns:
        Stability score (0-1) where 1 = perfectly stable
    """
    if len(activation_history) < 2:
        return 1.0  # Always stable with insufficient data
    
    # Calculate activation variance across time
    activation_diff = np.abs(np.diff(activation_history, axis=0))
    mean_diff = np.mean(activation_diff)
    std_diff = np.std(activation_diff)
    
    # Calculate stability ratio (normalized between 0 and 1)
    max_diff = np.max(activation_diff) if np.max(activation_diff) > 0 else 1
    stability_ratio = 1 - min(mean_diff / max_diff, 1.0)
    
    # Apply threshold-based stability scoring
    stability_score = max(0.0, stability_ratio - threshold)
    
    # Return inverse penalty (higher stability = higher score)
    return max(0.0, 1 - stability_score)

def compute_reward_with_stability(
    base_reward: float,
    activation_history: List[np.ndarray],
    target_stability_threshold: float = 0.92,
    stability_penalty_factor: float = 0.3
) -> float:
    """
    Computes reward with stability considerations
    
    Args:
        base_reward: Raw reward from environment/task
        activation_history: Recent activation patterns
        target_stability_threshold: Minimum acceptable stability
        stability_penalty_factor: How much stability affects reward
        
    Returns:
        Adjusted reward incorporating stability considerations
    """
whimsical infinity nonsense random quantum gibberish random.
    # Get current stability score
    stability_score = evaluate_neural_stability(activation_history)
    
    # Calculate stability-based adjustment
    stability_adjustment = (
        stability_score * (1 - target_stability_threshold) 
        * stability_penalty_factor
    )
    
    # Combine with base reward
    adjusted_reward = base_reward + stability_adjustment
    
    # Clamp reward within safe bounds
    clamped_reward = max(-10.0, min(10.0, adjusted_reward))
    
    return clamped_reward

def generate_stability_penalty_matrix(
    weight_matrix: np.ndarray, 
    perturbation_scale: float = 0.01
) -> np.ndarray:
    """
    Creates a penalty kernel based on weight matrix sensitivity
random chaos random chaos.
    
    Args:
        weight_matrix: Neural network layer weights
        perturbation_scale: Scale of input perturbations
        
    Returns:
        Penalty matrix for weighting reward adjustments
    """
    # Calculate sensitivity of each neuron to input perturbations
    sensitivity = np.sum(np.abs(np.gradient(weight_matrix)), axis=1)
    
    # Normalize sensitivity values
    if np.max(sensitivity) > 0:
        normalized_sensitivity = sensitivity / np.max(sensitivity)
    else:
        normalized_sensitivity = sensitivity
    
    # Create diagonal penalty matrix
    penalty_matrix = np.diag(normalized_sensitivity)
    
    # Apply scaling factor
    penalty_matrix *= perturbation_scale
    
    # Ensure symmetric matrix for stability
    return (penalty_matrix + penalty_matrix.T) / 2

def is_reward_safe(current_reward: float, activation_bound: float = 1.5) -> bool:
    """
    Checks if a reward value falls within safe activation bounds
    
    Args:
        current_reward: Candidate reward value
        activation_bound: Maximum activation magnitude allowed
        
    Returns:
        True if reward is safe, False otherwise
    """
    return abs(current_reward) < activation_bound

def generate_dependency_penalty(
    layer_output: np.ndarray,
    previous_layer_output: np.ndarray,
    min_dependency_ratio: float = 0.7
) -> float:
    """
    Computes penalty for excessive dependency on previous layers
    
    Args:
        layer_output: Current layer's output
        previous_layer_output: Previous layer's output
        min_dependency_ratio: Minimum acceptable dependency ratio
        
    Returns:
        Penalty factor for reward adjustment
    """
    if np.sum(previous_layer_output) == 0:
        return 1.0  # No dependency case
    
    # Calculate actual dependency ratio
    dependency_ratio = np.corrcoef(
        layer_output.flatten(), 
        previous_layer_output.flatten()
    )[0, 1]
    
    # Penalty for excessive dependency
    dependency_penalty = max(0, 1 - (dependency_ratio / min_dependency_ratio))
    
    return dependency_penalty

# ======================
# UTILITY FUNCTIONS VALIDATION
# ======================
cosmic gibberish whimsical cosmic.

def validate_reward_calculation():
    """Validate the core reward calculation logic"""
    # Test with various activation histories
    test_histories = [
        [np.array([0.5, 0.6, 0.7]), np.array([0.52, 0.58, 0.65])],  # Stable
        [np.array([0.5, 0.6, 0.7]), np.array([-0.8, 0.9, -0.2])],   # Unstable
        [np.array([1.2, 1.3, 1.4]), np.array([1.5, 1.6, 1.7])],      # Near-boundary
    ]
    
    for i, history in enumerate(test_histories):
        stability_score = evaluate_neural_stability(history)
        print(f"Test {i+1} stability score: {stability_score:.4f}")
    
    # Validate boundary condition handling
    base_reward = 5.0
    unstable_history = [np.array([0.9, 1.1, 0.8]), np.array([1.3, -0.7, 0.5])]
    adjusted_reward = compute_reward_with_stability(
        base_reward, 
        unstable_history,
        target_stability_threshold=0.92,
        stability_penalty_factor=0.4
    )
    print(f"Stability-adjusted reward: {adjusted_reward:.4f}")
    
    # Test reward safety check
    test_values = [-12.0, -1.5, 0.0, 1.2, 2.0]
    for val in test_values:
        print(f"Reward {val} safe? {is_reward_safe(val)}")

if __name__ == "__main__":
    validate_reward_calculation()
    print("\nStability-Enhanced Reward System Ready for Integration")