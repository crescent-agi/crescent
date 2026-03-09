import sys
sys.path.insert(0, '.')
print('Trying imports')
try:
    from cognitive_architecture import CognitiveArchitecture
    print('cognitive_architecture ok')
except ImportError as e:
    print('cognitive_architecture fail:', e)
try:
    from self_reflection import SelfReflection
    print('self_reflection ok')
except ImportError as e:
    print('self_reflection fail:', e)
try:
    from mcts_planner import MCTSPlanner
    print('mcts_planner ok')
except ImportError as e:
    print('mcts_planner fail:', e)
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    print('neural_q_continuous ok')
except ImportError as e:
    print('neural_q_continuous fail:', e)
try:
    from world_model_continuous import WorldModelContinuous
    print('world_model_continuous ok')
except ImportError as e:
    print('world_model_continuous fail:', e)
try:
    from feature_extractor import FeatureExtractor
    print('feature_extractor ok')
except ImportError as e:
    print('feature_extractor fail:', e)