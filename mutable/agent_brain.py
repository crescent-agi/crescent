import numpy as np
import os

# Safety-first AGI core with bounded activation and stability patches
class StableAGI:
    def __init__(self):
        self.activation_fn = np.tanh  # Bounded activation
        self.activation_log = []  # Pre-activation logging
        self.safety_threshold = 1.5  # Max activation magnitude

    def compute_output(self, input_vector):
        # Clamp input to prevent overflow
        clipped_input = np.clip(input_vector, -100, 100)
        
        # Apply bounded activation
        activated = self.activation_fn(clipped_input)
        
        # Log pre-activation values for stability monitoring
        self.activation_log.append({
            'input': clipped_input.tolist(),
            'raw_activation': activated.tolist(),
            'max_magnitude': float(np.max(np.abs(activated)))
        })
        
        # Safety check: reject if activation exceeds threshold
        if self.safety_threshold < float(np.max(np.abs(activated))):
            raise ValueError(f"Activation {activated} exceeds safety threshold {self.safety_threshold}")
        
        return activated

    def get_stability_score(self):
        """Calculate stability score based on activation history"""
        if len(self.activation_log) < 2:
            return 1.0  # New system defaults to stable
        
        # Measure variance in activation magnitudes
        magnitudes = [entry['max_magnitude'] for entry in self.activation_log[-5:]]
        mean_magnitude = np.mean(magnitudes)
        variance = np.var(magnitudes)
        
        # Stable if variance is low and magnitudes within safe range
        stability = 1.0 - min(variance * 0.1, 0.2)
        return max(0.0, stability)

    def generate_reward(self, base_reward, stability_score):
        """Adjust reward based on stability metrics"""
        stability_penalty = (1 - stability_score) * 0.5
        adjusted_reward = base_reward * (1 - stability_penalty)
        
        # Apply safety clamping
        return max(-10.0, min(10.0, adjusted_reward))

# Initialize global AGI core
agi_core = StableAGI()