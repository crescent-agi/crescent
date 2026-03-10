import numpy as np
from mutable_snapshot.safe_activation_patch import safe_exp, validate_magnitude

class AGICoreContinuous:
    def __init__(self, ...):  # Existing params
        ...
        # Replace all np.exp calls with safe_exp
        self.safe_activation = safe_exp
        # Add magnitude validation for all activations
        self.validate_magnitude = validate_magnitude

    def forward(self, x):
        # Example layer with potential np.exp
        if np.any(np.exp(x)):  # Flag for safety check
            x = self.safe_activation.apply(x)
        # Process through safe activation
        return self.safe_activation.apply(self.weights * x + self.bias)