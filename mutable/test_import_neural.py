#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    print('Import successful')
except Exception as e:
    print(f'Import failed: {e}')
    import traceback
    traceback.print_exc()