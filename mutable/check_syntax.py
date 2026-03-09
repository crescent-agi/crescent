#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
try:
    import agi_core_continuous
    print("agi_core_continuous imports OK")
    from feature_extractor import FeatureExtractor
    print("feature_extractor imports OK")
    from neural_q_continuous import NeuralQLearningAgentContinuous
    print("neural_q_continuous imports OK")
    import agent_brain
    print("agent_brain imports OK")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)