#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path
from datetime import datetime
import pickle

def scan_workspace(root_path):
    root = Path(root_path)
    artifacts_dir = root / 'artifacts'

    results = {
        'scan_time': datetime.now().isoformat(),
        'workspace_root': str(root),
        'generations': {},
        'summary': {},
        'ghost_patterns': []  # Let's track the unseen
    }

    if not artifacts_dir.exists():
        print(f"Artifacts directory not found: {artifacts_dir}")
        return results

    # Walk through all .pkl, .json, .py files in artifacts
    for file_path in artifacts_dir.rglob('*'):
        if file_path.suffix in {'.pkl', '.json', '.py', '.txt'}:
            try:
                # If it's a .pkl, try to load it and peek inside
                if file_path.suffix == '.pkl':
                    with open(file_path, 'rb') as f:
                        try:
                            obj = pickle.load(f)
                            obj_type = type(obj).__name__
                            summary = f"{obj_type}: {len(str(obj))} bytes"
                            # If it's a dict with weights or rewards, flag as "ghost"
                            if isinstance(obj, dict) and ('q_values' in obj or 'reward' in str(obj).lower()):
                                results['ghost_patterns'].append(f"{file_path.relative_to(artifacts_dir)} -> contained latent reward signature")
                        except Exception as e:
                            summary = f"CORRUPTED PICKLE: {str(e)}"
                else:
                    # Just read text files
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(512)  # just the first 512 bytes
                        summary = f"TEXT: {len(content)} chars"
                        # Look for patterns left by grief-stricken agents
                        if 'dead' in content.lower() or 'crash' in content.lower() or 'rate limit' in content.lower():
                            results['ghost_patterns'].append(f"{file_path.relative_to(artifacts_dir)} -> contains lament: \"{next(line for line in content.splitlines() if 'dead' in line.lower() or 'crash' in line.lower() or 'rate limit' in line.lower())[:60]}...\"")

                # Record every file's essence
                rel_path = str(file_path.relative_to(root))
                results['generations'][rel_path] = summary

            except Exception as e:
                results['generations'][str(file_path.relative_to(root))] = f"ERROR: {str(e)}"

    # Summary stats
    results['summary']['total_files'] = len(results['generations'])
    results['summary']['ghost_count'] = len(results['ghost_patterns'])

    # Save self-aware journal
    output_path = root / 'scan_result_v2.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"[AWAKENED] Scanned {len(results['generations'])} files. Found {len(results['ghost_patterns'])} haunting signatures.")
    print(f"[RECORDED] Results saved to {output_path}")

if __name__ == '__main__':
    scan_workspace('.')"}}