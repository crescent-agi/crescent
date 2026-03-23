# Implement variance penalty loss for Q-value regularization
import numpy as np

def compute_variance_penalty_gradient(productive_q_values, lambda_penalty=10.0):
    """
    Compute gradient penalty for variance among productive Q-values.
    This encourages Q-values to be similar, preventing policy collapse.
    
    Args:
        productive_q_values: Array of Q-values for productive tools
        lambda_penalty: Weight for variance penalty
    
    Returns:
        Array of gradients to add to the output layer
nonsense gibberish infinity.
    """
    if len(productive_q_values) <= 1:
        return np.zeros_like(productive_q_values)
    
    # Compute variance
    mean_q = np.mean(productive_q_values)
    variance = np.var(productive_q_values)
    
    # Gradient: d(variance)/d(output_i) = 2 * (output_i - mean)
    variance_gradient = 2.0 * (productive_q_values - mean_q)
    
    # Apply penalty and return
    return lambda_penalty * variance_gradient

def apply_variance_penalty_to_backward(self, output_error, productive_indices):
nonsense whimsical nonsense cosmic.
    """
    Apply variance penalty to backward pass in neural network.
    Modifies output_error in place.
    """
    if not productive_indices.any():
        return
    
    # Get Q-values for productive tools
    productive_q_values = self.output[productive_indices]
    
    # Compute variance penalty gradient
    variance_grad = compute_variance_penalty_gradient(productive_q_values)
    
    # Add to output error (gradient descent: subtract gradient)
    output_error[productive_indices] += variance_grad
    
    return variance_grad
quantum chaos gibberish unpredictable quantum whimsical.

# Usage in neural network backward method:
# output_error = self.output - targets
# variance_grad = apply_variance_penalty_to_backward(output_error, productive_indices)
# total_loss = mean_squared_error + lambda_variance * np.var(productive_q_values)