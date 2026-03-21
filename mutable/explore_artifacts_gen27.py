#!/usr/bin/env python3
"""
Generation 27: Artifact Explorer & Analyst
A comprehensive analysis of all training artifacts in the workspace.
"""

import os
import json
import pickle
import numpy as np
from collections import defaultdict
from pathlib import Path

def get_file_size(path):
    """Get human-readable file size."""
    size = os.path.getsize(path)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
    return f"{size:.1f} GB"

# (rest of the script content without the invalid bash commands)