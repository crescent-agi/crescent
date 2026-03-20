import sys
sys.path.insert(0, '.')
import neural_q_continuous_double
import patch_boltzmann_var200
from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble
import random
import math

# Override choose_action with debug version
original = NeuralQLearningAgentContinuousDouble.choose_action
PRODUCTIVE_INDICES = [0, 1, 3, 5]
NON_PRODUCTIVE_INDICES = [2, 4, 7, 8, 9, 10, 11]

def debug_choose_action(self, state_vector):
    q_values = self.nn.predict(state_vector)
    print('q_values:', q_values)
    masked_q = q_values[:]
    for idx in NON_PRODUCTIVE_INDICES:
        masked_q[idx] = -float('inf')
    print('masked_q:', masked_q)
    if self.temperature <= 0:
        max_q = max(masked_q)
        best_actions = [i for i, q in enumerate(masked_q) if q == max_q]
        chosen = random.choice(best_actions)
        print('greedy chosen:', chosen)
        return chosen
    scaled_q = [q / self.temperature for q in masked_q]
    max_scaled = max(scaled_q)
    exp_q = [math.exp(q - max_scaled) for q in scaled_q]
    for idx in NON_PRODUCTIVE_INDICES:
        exp_q[idx] = 0.0
    print('exp_q:', exp_q)
    sum_exp = sum(exp_q)
    print('sum_exp:', sum_exp)
    if sum_exp == 0:
        chosen = random.choice(PRODUCTIVE_INDICES)
        print('fallback uniform:', chosen)
        return chosen
    probs = [e / sum_exp for e in exp_q]
    print('probs:', probs)
    r = random.random()
    cumulative = 0.0
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            print('chosen index:', i, 'p=', p, 'cumulative=', cumulative, 'r=', r)
            return i
    chosen = random.choice(PRODUCTIVE_INDICES)
    print('final fallback:', chosen)
    return chosen

NeuralQLearningAgentContinuousDouble.choose_action = debug_choose_action

agent = NeuralQLearningAgentContinuousDouble(feature_dim=30, action_size=12, hidden_size=32)
agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
print('Temperature:', agent.temperature)
state = [random.random() for _ in range(30)]
print('state vector sample:', state[:3])
for _ in range(5):
    act = agent.choose_action(state)
    print('selected action:', act)
    print('---')