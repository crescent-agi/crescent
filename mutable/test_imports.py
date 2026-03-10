import sys
sys.path.insert(0, '.')
try:
    import neural_q_continuous
    print('neural_q_continuous ok')
except Exception as e:
    print('neural_q_continuous fail:', e)
try:
    import patch_weight_clipping
    print('patch_weight_clipping ok')
except Exception as e:
    print('patch_weight_clipping fail:', e)
try:
    from agi_core_continuous import AGICoreContinuous
    print('agi_core_continuous ok')
except Exception as e:
    print('agi_core_continuous fail:', e)
try:
    from new_reward_gen42 import compute_reward_gen42, compute_terminal_bonus_gen42
    print('new_reward_gen42 ok')
except Exception as e:
    print('new_reward_gen42 fail:', e)