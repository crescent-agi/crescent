class SuperSafeActivation:
    def __init__(self, eps=1e-6):
        self.eps = eps
    
    def apply(self, x):
        x_arr = np.asarray(x)
        # If any value is outside [-eps, eps], clamp it aggressively
        if np.any(np.abs(x_arr) > self.eps):
            return np.clip(x_arr, -self.eps, self.eps)
        return x_arr