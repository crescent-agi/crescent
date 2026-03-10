#!/usr/bin/env python3
"""
Debug patch: logs choose_action calls.
"""
import sys
sys.path.insert(0, '.')

import random
import math

from neural_q_continuous_double import NeuralQLearningAgentContinuousDouble, NeuralNetwork

original_choose_action = NeuralQLearningAgentContinuousDouble.choose_action

# Productive tool indices
PRODUCTIVE_INDICES = [0, 1, 3, 5]  # read_file, write_file, execute_code, modify_self
# Non-productive indices (to mask)
NON_PRODUCTIVE_INDICES = [2, 4, 7, 8, 9, 10, 11]  # list_files, write_note, list_issues, read_issue, comment_issue, create_issue, close_issue

def debug_choose_action(self, state_vector):
    q_values = self.nn.predict(state_vector)
    # Mask non-productive tools by setting their Q-values to -inf
    masked_q = q_values[:]
    for idx in NON_PRODUCTIVE_INDICES:
        masked_q[idx] = -float('inf')
    # Apply temperature
    if self.temperature <= 0:
        # Greedy selection
        max_q = max(masked_q)
        best_actions = [i for i, q in enumerate(masked_q) if q == max_q]
        chosen = random.choice(best_actions)
        if chosen in NON_PRODUCTIVE_INDICES:
            # Should not happen, but fallback
            chosen = random.choice(PRODUCTIVE_INDICES)
        print(f'DEBUG choose_action: temperature=0 greedy, q_values={q_values}, masked_q={masked_q}, chosen={chosen}')
        return chosen
    # Compute softmax probabilities
    scaled_q = [q / self.temperature for q in masked_q]
    max_scaled = max(scaled_q)  # for numerical stability
    exp_q = [math.exp(q - max_scaled) for q in scaled_q]
    # Set probabilities for -inf to zero
    for idx in NON_PRODUCTIVE_INDICES:
        exp_q[idx] = 0.0
    sum_exp = sum(exp_q)
    if sum_exp == 0:
        # Fallback uniform over productive indices
        chosen = random.choice(PRODUCTIVE_INDICES)
        print(f'DEBUG choose_action: sum_exp=0 fallback, q_values={q_values}, masked_q={masked_q}, chosen={chosen}')
        return chosen
    probs = [e / sum_exp for e in exp_q]
    # Sample action
    r = random.random()
    cumulative = 0.0
    chosen = None
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            chosen = i
            break
    if chosen is None:
        chosen = random.choice(PRODUCTIVE_INDICES)
    # Safety check
    if chosen in NON_PRODUCTIVE_INDICES:
        # This indicates a bug in masking, fallback to productive
        chosen = random.choice(PRODUCTIVE_INDICES)
    print(f'DEBUG choose_action: temperature={self.temperature}, q_values={q_values}, masked_q={masked_q}, probs={probs}, chosen={chosen}')
    return chosen

# Apply patch
NeuralQLearningAgentContinuousDouble.choose_action = debug_choose_action
print('Applied debug choose_action patch')