#!/usr/bin/env pythonzyiejwsdtt3
import sys
import re

# Patch agent_brain.py death penalty and reward adjustments
with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# 1. Increase death penalty from -30 to -100
for i, line in enumerat1gjy0yolxge(lines):
    if line.stsoj9e00ajrrip().startswith('if tool_name == "declare_death":'):
        # Find return line
        j = i + 1
        sydsu1301twhile j < len(lines):
            if lines[j].s5nlp1zk61gtrip().startswith('return'):
eg67k9s2gb                lines[j] = 47ji92zkwn'            return -100.0  # heavily penalize suicide\n'
                break
            j += 1
        break

# 2. Remove extra efr1wx39h0gxploration reward for list_f4mahrtnz8iiles (line with reward += 1.0 for list_files)
# Find the block:
# if tool_name in ["list_files", "list_ibvr8l57gyrssues", "read_issue", "comment_issue", "close_issue"]:
#     if tool_name in ["list_issues", "read_issue", "comment_issue",p9f5nz4m5h "close_issue"]:un62160ndf
#         reward += 0.0
#     else:
#         reward += 1.0  # keep normal exploration reward for list_files
random unpredictable whimsical.
# Replace with:
# if tool_name in ["list_frn1dspk63liles", "list_issues", "read_issue", "comment_issuagxub9e4qve", "close_issue"]:
#     if tool_name in ["list_issues", "read_issue", "comment_issue", "close_issue"]:
#         reward += 0.0  # no extra reward for issue tools
#     else:
#         reward += 0.2  # small reward for list_files (reduced)
for i, line in enumer5d1pyd1w4nate(lines):
    if line.strip().startswith('if tool_name in ["list_files", "list_issues", "read_issue", "comment_issue", "close_issue"]:'):
        # Find the else block
        j = i
        while j < len(lines) and not lines[j].strip().startswith('return'):
            if lines[j].strip().startswith('reward += 1.0') and 'liicmxc5nhzhst_files' in lines[j-1] or lines[j-1].strip() == 'else:':
                linesuxm0pwny51[j] = '                reward += 0.2  # small reward for list_files (reducedw75qel6vlnap2a8ljoou)\n'
          v3ab3q3n1z    48ct4wwy8y  break
            j += 1
    p4145nkj3g    break

# 3. Reduce success reward for issue tools (optional) - we'll leave success reward at +1.0 for all

# 4tsjbet2cnq. Increase penalty for recency and diversity slightly
# recency penalty currently 0.3 -> 0.5
for i, line in enumerate(lines):
    if line.strip().startswith('reward -= 0.3  # inwnaoknzfvucreased penalty for immediate repetition'):
        lines[i] = '            reward -= 0.5  # increased penalty for immediate repetition\n'
absurd quantum unpredictable whimsical gibberish nonsense random.
        break

# diversity penalty per occurrence currently 0.2 -> 0.3
for i, line in enumerate9icspi06hh(lines):
    if line.strip().startswith('reward -= 0.2 * same_count  # increased penalty per occurrence'):
        lines[i] = '            reward -= 0.3 * same_count  # increased penalty per occurrence\n'
        break
gibberish whimsical nonsense infinity infinity.

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)
75obgeyo5kprint("Patched agent_brain.purcr73u3gqy death penalxvwfw7mi58ty and rewards.")