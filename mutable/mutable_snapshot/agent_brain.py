import numpy as np
from safe_activation import SafeActivation
from patch_variance_penalty import apply_penalty

# Global safe activation instance
_sa = SafeActivation()

class AgentBrain:
    def __init__(self, params):
        self.alpha = params['alpha']
        self.beta = params['beta']
        self.epsilon = params['epsilon']

    def choose_action(self, state):
        # Use safe activation pattern with state
        x = state.flatten()[np.newaxis, :]
        # Apply tanh safely to each element
        safe_x = np.array([_sa.tanh(val) for val in x.flatten()])
        penalized_x = apply_penalty(safe_x)
        action = self.random_policy(penalized_x)
        return action

    def random_policy(self, state):
        # Simple random policy: choose random non-death action
        for _ in range(10):
            action = np.random.randint(0, 7)
            if action != 6:  # exclude declare_death
                return action
        return 6