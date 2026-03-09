#!/usr/bin/env python3
import re
import sys

with open('agent_brain.py', 'r') as f:
    content = f.read()

# Pattern for execute code block
# We'll replace the three reward lines using regex with groups.
# Simpler: replace each line individually with regex that matches the exact line with surrounding whitespace.
# First, replace "reward += 0.5" that appears after "# extra if execution succeeded without stderr errors"
content = re.sub(r'(# extra if execution succeeded without stderr errors\\s*\\n\\s*if tool_result\\.get\\("stderr", ""\\)\\.strip\\(\\) == "":\\s*\\n\\s*reward \\+= )0\\.5', r'\\1 0.7', content)
# Second, replace "reward += 0.4" after "# extra if output contains meaningful results"
content = re.sub(r'(# extra if output contains meaningful results\\s*\\n\\s*stdout = tool_result\\.get\\("stdout", ""\\)\\.strip\\(\\)\\s*\\n\\s*if len\\(stdout\\) > 10:\\s*\\n\\s*reward \\+= )0\\.4', r'\\1 0.6', content)
# Third, replace "reward += 1.0" after "# bonus if output indicates success"
content = re.sub(r'(# bonus if output indicates success\\s*\\n\\s*if any\\(indicator in stdout\\.lower\\(\\) for indicator in \\["test passed", "ok", "success", "completed", "passed", "works"\\]\\):\\s*\\n\\s*reward \\+= )1\\.0', r'\\1 1.5', content)

with open('agent_brain.py', 'w') as f:
    f.write(content)

print('Execute block updated.')