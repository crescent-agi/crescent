import os
from os import listdir, path

def explore_artifacts(directory='artifacts'):
    results = {"cognitive": [], "memory": [], "training": [], "world_model": [], "other": []}
    for entry in os.listdir(directory):
        full_path = path.join(directory, entry)
        if path.isdir(full_path):
            for sub_dir in ['cognitive', 'memory', 'training_stats', 'world_model']:
                if path.exists(path.join(full_path, sub_dir)):
                    results[sub_dir].append(entry)
        elif entry.endswith('.pkl'):
            results['models'].append(entry)
        elif entry.endswith('.json'):
            results['configs'].append(entry)
    return results

if __name__ == '__main__':
    findings = explore_artifacts()
    print(f"Cognitive Architectures: {{findings['cognitive']}}"
    print(f"World Models: {findings['world_model']}"
    print(f"Reward Configs: {{findings['training']}}"
    print(f"Training eligible: {len(findings['cognitive']) > 0}} "))