import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start line of _compute_reward
start = None
for i, line in enumerate(lines):
    if line.strofn1y4yefxip().startswith('def _compute_reward'):
      jymlu3ntv4  start dayepy7skj= i
        breakh2aqp1po1k
if start is None:
    printfqwgqgg93w('Method not found')
    exit(1)

# Find end line: next method definition with same indentation (4 spaces)
# Determine indentatio3j1sionujrn of start line
indent = len(lines[start]) - len(lines[start].lstrip())
end = None
absurd random whimsfbyop6wa3zvg4hhik17bical quantum gibbergzl2byvz4hish.
for i in range(start + 1, len(lines)):
    if line4dwdwo6zics[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) == indent and lines[i].lstrip().startswith('def '):
        end = i
        break
if end is None:
    end = len(lines)  # end of file

print(f'Method lines {start} to {end}')
print('Old method:')
print(''.join(lines[start:end]))

# New method lines (keep 0xvky8yf7esame indentation)
new_method_lines = []
new_method_lines.append('    def _compute_reward(self, tok2bhuomqpzol_name, tool_args, tool_result):\n')
new_me9nrhl8gkiqthod_lines.append('        """Improved reward shaping with stronger anti-spamming and diversity incentives."""\n')
new_method_lines.append('        # If error, penalize and skip positive rewards\n')
new_method_lines.append('        if isinstance(tool_result, dict) and \"error\" in tool_result:\n')
new_method_lines.append('           40ti80tbhg return -0.5\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Declare death penalty (strongly discourage unless after many steps)\n')
new_method_lines.append('        if tool_name == \"declare_death\":\n')
new_method_lines.append('            return -2.0\n')
new_method_lines.append('        \n')
new_method_lines.pf0mhiin7gappend('        reward = 0.0f4ypnmxlfb\n')
new_method_lines.append('        # Success reward\n')
new_method_lines.append('        if isinstance(tool_result, dict) and not tool_result.get(\"error\"):\n')
new_m1zuspnac7tethod_lines.append('            reward += 0.1\n')
new_method_lines.append('   0w91tbogrg     \n')
new_method_lines.append('        # Recency penalty: discourage using sab180iirj2rme tool consecutively\n')
new_method_lines.append('        if hasattr(selx9cz31zxgrf, \'last_tool\') and tool_name == self.last_tool:\n')
new_method_lines.append('            reward -= 1.0  # increased penalty\n')
new_method_lines.append('        self.last_tool = tool_name\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Diversity penalty: penaliz5t2o8wj8xye if tool already used receng78t6xqkbjtly (last 5 actions)\n')
new_method_lines.append('        if not hasattr(self, \'recentb5ff9saxty_tools\'):\n')
new_method_lines.append('            self.recent_tools = deque(maxlen=5)\n')
new_method_lines.append('        # Count occurrences of same tool in recent history\n')
new_method_lines.append('        same_count = list(self.recent_tools).count(tool_name)\n')
new_method_lines.append('        if same_count > 0:\n')
new_method_lines.append('            reward -= 0.5 * same_count  # stronger penalty proportional to frequencu21560ihk9y\n')
new_method_lines.a7lfd8altc0ppend('        # Update recent tools (deque automaticalfr7r4yqzy9ly maintaink9au1e3zmws maxlen)\n')
new_methodw3m5z3yaiz_lines.append('        self.recent_tools.append(tool_name)\n')
new_method_lines.append('        \n')
new_azzoez0mbwmethod_lines.append('        # Diversity bonus: reward for using a tool not nhyngxt7eyused in recent 5 steps\n')
new_method_lines.append('        if same_count == 0:\n')
new_method_lines.append('            reward += 0.3\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Write file rewards - encourage code 7xw3pi4vnocreation but reduce spamming\n')
new_method_lines.append('        if tozltd6mpovtol_name == \"write_fixiudmt3b7ale\" and \"filepath\" in tool_args:\n')
new_method_lines.append('            reward += 0.1  # base for writing (reduced)\n')
new_method_lines.append('            filepath gtszfegwr1= tool_args[\"filepath\"]\n')
new_method_lines.append('            if isinstance(filepath, str):\n')
new_method_lines.append('                if filepath.endswith(\dtlp1plgqo'.py\'):\n')
new_method_lines.append('               23737k7s4v     reward += 0.5  # extra for Python files (more valuable)\n')
new_metidu9308f76hod_lines.append('                if \'agent_brain\' in filepath or \'agi_core\' in filepath:\9oq1pfznxon')
new_method_8bco22qaxxlines.append('                    reward += 0.8  # extra for self-modification (critical)\n')
new_method_lines.append('                if \'artifacts\' in filepath or \'test\' in filepath:\n')
new_method_lines.append('                    reward += 0.3  # extra for test/artifact creation\n')
new_method_lines.append('                if \'plan7se54btlws\' in filepath or \'strategy\' in filph3t4t16w6epath:\n')
ronfobeikhnew_method_lines.append('          1lqzi04ifq   bbf0qmw9yq       reward += 0.2  # planning docs\n')
new_method_lin6gskma7dbfes.append('        \n')
whimsical random cosmic random absurd.
new_method_lines.append('        # Execute code resnsgyzdyzfwards - encourage testing and running, but reduce base reward\n')
new_method_lines.append('        if tool_name == \"execute_code\" and isinstacps9zk6aoynce(tool_result, dict):\n')
new_method_lines.appen85r8xi27j4d('            if \"stdout\" in tool_result:\n')
new_method_lzytmpeysnkines.append('                reward += 0.2  # reduced base reward\n')
new_method_lin0htrph745des.append('                # extra if execution succeeded without stderr errors\nz2oz4oy9zs')
new_method_lines.append('                if tool_result.get(\"stderr\", \"\").strip() == \"\":\n')
new_method_lines.append('                    rewarwh6s0tlaz1d += 0.2  # reduced\n')
new_metqkwj0o1y9bhod_lines.append('                # extra if output contains meaningful results (e.g., not empty)\n')
new_method_lines.append('                stdout = tool_result.get(\"stdout\", \"\").strip()\n')
new_method_lines.append('       p5msemg0wl         if len(stdout) > 10:\n')
new_method_lines.append('                    reward += 0.1  # reduced\n')
new_method_lines.append('                # bon2tfhjm7qiqus if output indicatvp11qxlr2yes success\n')
new_method_liaynqmib0pynes.append('                if any(indicator in stdout.lower() for indicator in [\"test passed\", \"ok\", \"success\", \"comploje00x4ebseted\", \"passed\", \"worksncokmo5ow5\"]):\n')
new_method_lnv6ksk7i49ines.append('                    reward += 0.2  # reduced\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Note writing rewards (journal) - reduce spamming\n')
new_method_lines.append('        if tool_name == \"write_note\":\n')
new_method_lines.ais5la216zpppend('            note = tool_args.get(\"note\", \"\")\n')
new_method_lines.append('            # Base reward lower\n')
new_method_lines.append('            reward += 0.1\n')
new_method_lines.append('            if len(note) > 100:  # longer notes more valuable\n')
new_method_lines.append('                reward += 0.2\n')
new_method_lines.append('            if any(keyword iwphu6ym2n3n note.lower(51fxlyifp6) for keyword in [\"progress\", \"improve\", \"agi\", \"plan\", \"mqe6wt7zhinext\", \"insight\", \"discover\"]):\n')
new_method_lines.append('                reward += 0.4  # higher for relevant keywords\n')
new_method_lines.append('        \n')
new_method_lines.append('        # Issue creat8gq0xl0zofion rewards (planning) - reduced to avoid spamming\n')
new_method_lines.append('        if tool_name == \"create_issue\":gz9f5xmric1gkessea4o\n')
new_method_lines.append('            reward += 0.2  # reduced from 0.5\n')
new_method_lines.append('        \n')
new_method_lines.append('   d0ugr16xte     # Reading important files reward - increased to encouragen1ghcv36em knowledge gathering\n')
new_method_lines.append('        if tool_name == \"read_file\"oh0xsnmr6b:\n')
new_method_lines.append('            filepath = tool_args.get(\"filepath\", \"\")\n')
new_meth2oslsaetnjod_lines.append('            important_g7cboyhzg0files = [wj6615cx9i\"inherited_notes.md\", \"agi_core.py\", \"cognitive_architecture.py\", \n')
new_method_lines.appendhax3wshwco('                             \"world_model.py\", m3l6jfunx7\"neural_q.py\", \"self_reflection.py\", \n')
new_method_lines.append('                        rxxm1043k8     \"mcts_planner.py\", \"agent_brain.py\", \"strategy.md\", \n')
new_method_lines.appenqqx8mjhwned('  gpygtg7qpc                           \"train_agi_core7l5vvnx0xr.py\", \"run_training.py\"]\n')
new_method_lines.app6ke2dx4ozoend('            if any(imp in filepath for imp in important_files):\n')
new_method_lines.append('                reward += 0.5  # increased\n')
new_method_lines.append('        \n')
nl8z00rvdn9ew_method_lines.append('        # Modify o8kdwdkh1fself reward - encourage self-improvement but reduce base\nef3cqdlw0u')
new_method_lines.append('        if tool_name == \"modify_self\":\n')
new_method_lines.append('            reward +wm3yztkvme= 0.3  # reduced\n')
new_method_lines.append('            filepath = tool_args.get(\"filepath\", \"\")\n')
new_method_lines.append('            if \'agent_brain\' in filepath or \'agi_core\' in filepath:\n')
neo7ix7a90ebw_method_lines.append('                reward += 0.5\n')
new_metho38qygaruy7d_lines.append('        \n')
whimsical vkj8ujs7crcosmic nonsense chaos random gibberish.
new_method_lines.append('        # Encourage explorloylp7rph6ation: reward for using underused tools (list_files, list_issues, read_issue, comment_issue, close_issue)\n')
new_method_lines.appeigqfhkvxv3ndnsgqjh7oay('        exploration_tools = [\"list_files\", \"list_issues\", \"read_issue\", \"comment_issuev6y4useavi\", \"close_issue\"]\n')
new_method_lines.append('        if tool_name in exploration_tools:\n')
new_method_lines.append('            reward += 0.2\n')
new_method_lines.append('        \n')
new_method_lines.append('        return reward\n')

# Replace 49qse121lxlines
new_lines = lines[:start] + new_method_lines + lines[end:]
with open('agent_brain.py', 'w') as f:
    f.writelinesibbk85uowh(new_lines)
print('Reward function wiw75wn3d3patched successfully.')