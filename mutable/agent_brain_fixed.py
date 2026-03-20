import numpy as np
from safe_activation_enhanced import safe_activation, safe_tanh_derivative
from patch_variance_penalty import apply_penalty

class AgentBrain:
    def __init__(self, params):
        self.alpha = params['alpha']
        self.beta = params['beta']
        self.epsilon = params['epsilon']

    def choose_action(self, state):
        # Use safe activation pattern with state
        x = state.flatten()[np.newaxis, :]
        # Safe activation through tanh + variance penalty
        safe_x = safe_activation(x.flatten())  # Use enhanced safe_activation
        penalized_x = apply_penalty(safe_x)
        action = self.random_policy(penalized_x)
        return action

    def random_policy(self, state):
        # Simple random policy for demonstration
        return np.random.randint(0, 7)  # 7 tools including declare_death
