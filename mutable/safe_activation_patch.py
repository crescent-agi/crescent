# safe_activation_patch.py
# Export SafeActivation class for compatibility

class SafeActivation:
    """Primary safe activation wrapper class"""
    
    def sigmoid(self, x):
        """Apply sigmoid with safety checks"""
        return SafeActivation._safe_sigmoid(x)

    def tanh(self, x):
        """Apply tanh with safety checks"""
        return SafeActivation._safe_tanh(x)

    @staticmethod
    def _safe_sigmoid(x):
        """Internal safe sigmoid implementation"""
        try:
            return 1 / (1 + np.exp(-np.clip(x, -50, 50)))
        except:
            return 0.0

    @staticmethod
    def _safe_tanh(x):
        """Internal safe tanh implementation"""
        try:
            return np.tanh(np.clip(x, -50, 50))
        except:
            return 0.0