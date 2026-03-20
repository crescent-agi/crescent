#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
with open('new_reward_gen19_balanced_v2.py', 'r') as f:
    lines = f.readlines()
# We'll write a new file with modifications
out_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    # Replace scaling factor 100 with 500
    if 'scaling_factor = 100.0' in line:
        line = line.replace('100.0', '500.0')
    # Fix curiosity bonus cap (the second curiosity bonus). Find line with 'if curiosity_bonus > 100.0:' and next line 'reward += 100.0'
    if 'if curiosity_bonus > 100.0:' in line and i+1 < len(lines) and 'reward += 100.0' in lines[i+1]:
        # Replace these two lines with proper capping
        line = '                    if curiosity_bonus > 100.0:\n'
        out_lines.append(line)
        i += 1
        line = '                        curiosity_bonus = 100.0\n'
        out_lines.append(line)
        i += 1
        # Need to ensure we don't duplicate the reward addition. The previous line already added curiosity_bonus. We'll keep as is.
        # Skip the original reward addition line (the one after that is already added?)
        # Actually the original line after that is 'reward += 100.0' which we already replaced with setting curiosity_bonus.
        # Need to also ensure reward += curiosity_bonus after the if block. Let's look ahead.
        # This is messy; we'll just replace the whole block later.
        continue
    # Increase extra reward for read_file
    if 'elif tool_name == \"read_file\":' in line and i+1 < len(lines) and 'reward += 5.0' in lines[i+1]:
        line = lines[i]
        out_lines.append(line)
        i += 1
        line = '                reward += 20.0  # increased extra reward for read_file\n'
        out_lines.append(line)
        i += 1
        continue
    # Increase novel-file bonus and important file bonus
    if 'if filepath not in self.recent_read_files:' in line and i+1 < len(lines) and 'reward += 2.0' in lines[i+1]:
        line = lines[i]
        out_lines.append(line)
        i += 1
        line = '                reward += 10.0  # increased novel-file bonus\n'
        out_lines.append(line)
        i += 1
        continue
    if 'if any(imp in filepath for imp in important_files):' in line and i+1 < len(lines) and 'reward += 2.0' in lines[i+1]:
        line = lines[i]
        out_lines.append(line)
        i += 1
        line = '                reward += 10.0  # increased important file bonus\n'
        out_lines.append(line)
        i += 1
        continue
    # Add read_file deficit penalty after the curiosity bonus block. We'll insert after the curiosity bonus block.
    # Find line '# =========== ADJUSTED EXTRA REWARDS ==========='
    if '# =========== ADJUSTED EXTRA REWARDS ===========' in line:
        # Insert before this line
        insertion = '''        # =========== READ_FILE DEFICIT PENALTY ===========
        # If read_file hasn't been used in the last 30 steps, add a penalty to other tools
        if tool_name != \"read_file\" and hasattr(self, 'recent_tools'):
            # Count read_file usage in recent 30 steps (approximate)
            recent_read_file_count = self.recent_tools.count(\"read_file\")
            if recent_read_file_count == 0 and len(self.recent_tools) >= 20:
                # Apply penalty to encourage read_file
                reward -= 30.0  # penalty for not using read_file
        # Also add a bonus for using read_file when it's underused globally
        if tool_name == \"read_file\" and hasattr(self, 'global_tool_counts'):
            total_global = sum(self.global_tool_counts.values())
            if total_global > 0:
                proportion = self.global_tool_counts[\"read_file\"] / total_global
                if proportion < 0.15:
                    reward += 100.0  # extra bonus for read_file when underused
'''
        out_lines.append(insertion)
    out_lines.append(line)
    i += 1

# Write new file
with open('new_reward_gen21_balanced_v2.py', 'w') as f:
    f.writelines(out_lines)
print('Created new_reward_gen21_balanced_v2.py')