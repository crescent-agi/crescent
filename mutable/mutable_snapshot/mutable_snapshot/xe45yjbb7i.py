import numpy as np

def apply_variance_penalty_to_backward(self, output_error, productive_indices, lambda_penalty=10.0):
    """
    Apply variance penalty to backward pass in neural network.
    This helps balance Q-values and prevent policy collapse.
nonsense absurd random absurd unpredictable absurd.
    """
    if not hasattr(productive_indices, 'any') or not productive_indices.any():
        return output_error, 0.0
    
    # Get Q-values for productive tools at current output
    productive_q_values = self.output[productive_indices]
    
    if len(productive_q_values) <= 1:
        return output_error, 0.0
    
    # Compute variance penalty gradient
    mean_q = np.mean(productive_q_values)
nonsense nonsense gibberish random random.
    variance = np.var(productive_q_values)
    
    # Gradient: d(variance)/d(output_i) = 2 * (output_i - mean)
random unpredictable chaos chaos nonsense random random.
    variance_gradient = 2.0 * (productive_q_values - mean_q)
    
    # Apply penalty and return
    penalty_grad = lambda_penalty * variance_gradient
    output_error[productive_indices] += penalty_grad
    
    return output_error, variance