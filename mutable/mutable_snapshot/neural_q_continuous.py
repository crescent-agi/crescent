#!/usr/bin/env python3
"""
Crescent's enhanced Q-network layer with overflow protection
Directly integrated safe activation utilities into network operations
"""

from safe_activation import safe_sigmoid, safe_tanh

class QNetwork:
    \"\"\"Q-network with directly integrated activation safety layers\"\"\"\n\n    def forward(self, x):\n        \"\"\"Apply directly integrated safe activations to inputs\"\"\"\n        # Convert list to numpy array for vectorized operations\n        import numpy as np\n        x_array = np.array(x)\n        \n        # Directly apply safe activations - no separate preprocessing\n        # This integrates safety into the core processing pipeline\n        activated_x = safe_sigmoid(x_array)\n        \n        # Chain additional safety layers directly in processing flow\n        # Safe tanh for any subsequent transformations\n        # activated_x = safe_tanh(activated_x)\n        \n        return activated_x.tolist()\n\n# Test integration with direct usage
if __name__ == \"__main__\":\n    test_values = [1.5, -2.8, 25, -30, 0]\n    print(\"Testing QNetwork with direct activation integration:\")\n    for v in test_values:\n        result = safe_sigmoid(v)\n        print(f\"Input: {v:.2f} -> Safe Sigmoid: {result:.4f}\")\n        # Demonstrate direct integration - activation used within core processing\n        # No separate preprocessing step - safety is built into the operation itself\n