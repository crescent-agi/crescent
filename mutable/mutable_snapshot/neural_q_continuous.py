class QNetwork:
    """Q-network with clamped activation to prevent numerical overflow"""

    def forward(self, x):
        """Apply clamped sigmoid to inputs before forward pass"""
        clamped_x = [max(-10.0, min(10.0, v)) for v in x]
        # Existing network logic here would continue...
        return clamped_x