#!/usr/bin/env python3
import os, json, glob, re
from collections import defaultdict
from datetime import datetime

def log(msg):
    print(msg)

def get_artifact_stats():
    artifacts_dir = 'artifacts'
    if not os.path.exists(artifacts_dir):
        return {"error": "No artifacts directory"}

    dirs = [d for d in os.listdir(artifacts_dir) if os.path.isdir(os.path.join(artifacts_dir, d))]

    # Categorize by generation and variant
    generations = {}
    pattern = re.compile(r'gen(\d+)')
    for d in dirs:
        m = pattern.search(d)
        if m:
            gen = int(m.group(1))
            if gen not in generations:
                generations[gen] = []
            generations[gen].append(d)

    # Count file types
    type_counts = defaultdict(int)
    total_size = 0
    pkl_count = 0
    json_count = 0
    nn_count = 0

    for root, dirs, files in os.walk(artifacts_dir):
        for f in files:
            fp = os.path.join(root, f)
            try:
                size = os.path.getsize(fp)
                total_size += size
            except:
                pass
            ext = os.path.splitext(f)[1].lower()
            type_counts[ext] += 1
            if ext == '.pkl': pkl_count += 1
            if ext == '.json': json_count += 1
            if ext == '.nn': nn_count += 1

    # Find training stats
    stats_files = []
    for root, dirs, files in os.walk(artifacts_dir):
        if 'training_stats.json' in files:
            stats_files.append(os.path.relpath(root, artifacts_dir))

    return {
        "total_dirs": len(dirs),
        "generations_span": f"Gen {min(generations.keys()) if generations else '?'} to {max(generations.keys()) if generations else '?'}",
        "generations_count": len(generations),
        "generations_sample": dict(sorted(generations.items())[-5:]),  # last 5
        "total_size_mb": round(total_size / (1024*1024), 2),
        "file_types": dict(sorted(type_counts.items(), key=lambda x: -x[1])[:15]),
        "pkl_files": pkl_count,
        "json_files": json_count,
        "nn_files": nn_count,
        "stats_files_count": len(stats_files),
        "stats_dirs_sample": stats_files[:10]
    }

def read_inheritance():
    try:
        with open('inheritance_note.md', 'r') as f:
            return f.read()
    except Exception as e:
        return f"Could not read: {e}"

def read_autopsy():
    try:
        with open('autopsy.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}

def count_mutable():
    try:
        files = os.listdir('mutable_snapshot')
        py = [f for f in files if f.endswith('.py')]
        chaos = [f for f in files if f.endswith('.chaos') or '.chaos' in f]
        return {"total": len(files), "py": len(py), "chaos": len(chaos)}
    except:
        return {"error": "mutable_snapshot not found"}

def main():
    print("# CRESCENT WORKSPACE FORENSICS")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 60)
    print()

    # Inheritance info
    inh = read_inheritance()
    print("## INHERITANCE NOTE")
    print("-" * 40)
    print(inh[:1000] if len(inh) > 1000 else inh)
    print()

    # Autopsy summary
    autopsy = read_autopsy()
    if isinstance(autopsy, dict) and "error" not in autopsy:
        print("## AUTOPSY SUMMARY")
        print("-" * 40)
        print(json.dumps(autopsy, indent=2)[:2000])
        print()

    # Mutable snapshot stats
    mut = count_mutable()
    print("## MUTABLE SNAPSHOT")
    print("-" * 40)
    print(json.dumps(mut, indent=2))
    print()

    # Artifact analysis
    arts = get_artifact_stats()
    print("## ARTIFACTS ANALYSIS")
    print("-" * 40)
    print(json.dumps(arts, indent=2))
    print()

    # Sample artifact sizes
    try:
        artifacts_dir = 'artifacts'
        if os.path.exists(artifacts_dir):
            sizes = []
            for root, dirs, files in os.walk(artifacts_dir):
                for f in files:
                    fp = os.path.join(root, f)
                    try:
                        size = os.path.getsize(fp)
                        sizes.append((size, os.path.relpath(fp, artifacts_dir)))
                    except:
                        pass
            sizes.sort(reverse=True)
            print("## LARGEST ARTIFACTS (top 10)")
            print("-" * 40)
            for size, path in sizes[:10]:
                print(f"{size:>12}  {path}")
    except:
        pass

    print()
    print("=" * 60)
    print("Analysis complete.")

if __name__ == '__main__':
    main()