#!/usr/bin/env python3
import pickle
import sys
import os
import numpy as np

def inspect_pickle(path):
    print(f"\n=== Inspecting: {path} ===")
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
    except Exception as e:
        print(f"ERROR: {e}")
        return

    if isinstance(data, dict):
        print(f"Dictionary with {len(data)} keys:")
        for k, v in data.items():
            if isinstance(v, np.ndarray):
                print(f"  {k}: ndarray shape={v.shape}, dtype={v.dtype}, size={v.size}")
            elif hasattr(v, 'shape'):
                print(f"  {k}: {type(v).__name__} with shape {v.shape}")
            else:
                print(f"  {k}: {type(v).__name__} (no shape)")
    elif isinstance(data, (list, tuple)):
        print(f"{type(data).__name__} with {len(data)} elements")
        for i, item in enumerate(data[:3]):
            print(f"  [{i}]: {type(item).__name__}")
        if len(data) > 3:
            print(f"  ... and {len(data)-3} more")
    else:
        print(f"Root type: {type(data).__name__}")
        if hasattr(data, 'shape'):
            print(f"  shape: {data.shape}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inspect_artifact.py <pickle_file>")
        sys.exit(1)
    inspect_pickle(sys.argv[1])
