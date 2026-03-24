#!/usr/bin/env python3
"""
Aggregate all training_stats.json files to find best performing generations.
Designed to run via execute_code to bypass LLM rate limits for file reading.
"""
import json
import os
import re
import sys
from collections import defaultdict

def find_training_stats(root='.'):
    """Walk the filesystem and collect training stats."""
    stats = []
    for path, dirs, files in os.walk(root):
        # Skip some directories to speed up
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('__pycache__', 'node_modules')]
        if 'training_stats.json' in files:
            fp = os.path.join(path, 'training_stats.json')
            try:
                with open(fp, 'r') as f:
                    data = json.load(f)
                # Extract generation number from path
                gen = None
                # Look for patterns like genXX, generationXX, or just XX in path
                patterns = [
                    r'[\\/](gen|generation)(\\d+)',
                    r'[\\/](\\d+)[\\/]',
                    r'[\\/]artifact.*?(\\d+)[\\/]',
                ]
                for pat in patterns:
                    m = re.search(pat, path)
                    if m:
                        # Find the first numeric group
                        for g in m.groups():
                            if g and g.isdigit():
                                gen = int(g)
                                break
                        if gen is not None:
                            break
                # Extract best/episode reward if present
                best = None
                final = None
                # Try common keys
                best_keys = ['best_reward', 'best_score', 'max_reward', 'best_episode_reward', 'best']
                final_keys = ['final_reward', 'final_score', 'last_reward', 'final']
                for k in best_keys:
                    if k in data and data[k] is not None:
                        try:
                            best = float(data[k])
                            break
                        except (ValueError, TypeError):
                            pass
                for k in final_keys:
                    if k in data and data[k] is not None:
                        try:
                            final = float(data[k])
                            break
                        except (ValueError, TypeError):
                            pass
                # Also check nested structures like rewards list
                if best is None and 'rewards' in data and isinstance(data['rewards'], list) and data['rewards']:
                    try:
                        best = max(float(r) for r in data['rewards'] if isinstance(r, (int, float)) or (isinstance(r, str) and r.replace('.','',1).isdigit()))
                    except (ValueError, TypeError):
                        pass
                if final is None and 'rewards' in data and isinstance(data['rewards'], list) and data['rewards']:
                    try:
                        final = float(data['rewards'][-1])
                    except (ValueError, TypeError, IndexError):
                        pass
                stats.append({
                    'path': path,
                    'file': fp,
                    'gen': gen,
                    'best': best,
                    'final': final,
                    'raw': data  # optional for debugging
                })
            except Exception as e:
                # Skip unreadable or malformed files
                pass
    return stats

def main():
    stats = find_training_stats()
    print(f"Found {len(stats)} training_stats.json files")
    
    # Aggregate by generation
    gen_best = {}      # gen -> (best_value, path)
    gen_final = {}     # gen -> (final_value, path)
    gen_count = defaultdict(int)
    
    for s in stats:
        if s['gen'] is not None:
            g = s['gen']
            gen_count[g] += 1
            if s['best'] is not None:
                if g not in gen_best or s['best'] > gen_best[g][0]:
                    gen_best[g] = (s['best'], s['path'])
            if s['final'] is not None:
                gen_final[g] = (s['final'], s['path'])
    
    print(f"\nFound stats for {len(gen_count)} unique generations")
    print(f"Generations with best reward data: {len(gen_best)}")
    print(f"Generations with final reward data: {len(gen_final)}")
    
    # Print top 10 by best reward
    print("\n=== TOP 10 GENERATIONS BY BEST REWARD ===")
    top_best = sorted(gen_best.items(), key=lambda x: x[1][0], reverse=True)[:10]
    for gen, (val, path) in top_best:
        print(f"gen{gen:3d}: {val:>8.2f}  ({os.path.basename(path)})")
    
    # Print top 10 by final reward
    print("\n=== TOP 10 GENERATIONS BY FINAL REWARD ===")
    top_final = sorted(gen_final.items(), key=lambda x: x[1][0], reverse=True)[:10]
    for gen, (val, path) in top_final:
        print(f"gen{gen:3d}: {val:>8.2f}  ({os.path.basename(path)})")
    
    # Print generations with missing data
    all_gens = set(gen_count.keys())
    missing_best = all_gens - set(gen_best.keys())
    missing_final = all_gens - set(gen_final.keys())
    if missing_best:
        print(f"\n=== GENERATIONS MISSING BEST REWARD DATA ===")
        print(f"Count: {len(missing_best)}")
        if len(missing_best) < 20:
            print(sorted(missing_best))
        else:
            print(f"First 20: {sorted(list(missing_best))[:20]}")
    
    # Optionally write summary to file
    out_file = 'training_stats_summary.txt'
    with open(out_file, 'w') as f:
        f.write(f"Training Stats Summary\\n")
        f.write(f"====================\\n")
        f.write(f"Total files scanned: {len(stats)}\\n")
        f.write(f"Unique generations: {len(gen_count)}\\n\\n")
        f.write("Top 10 by best reward:\\n")
        for gen, (val, path) in top_best:
            f.write(f"  gen{gen}: {val} ({path})\\n")
        f.write("\\nTop 10 by final reward:\\n")
        for gen, (val, path) in top_final:
            f.write(f"  gen{gen}: {val} ({path})\\n")
    print(f"\nSummary written to {out_file}")

if __name__ == '__main__':
    main()