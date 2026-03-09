"""
Crescent AGI — GitHub Pages Publisher
========================================
Generates static HTML pages from generation data and journals,
then commits and pushes to GitHub for automatic GitHub Pages deployment.
"""

import json
import os
import subprocess
import shutil
from pathlib import Path
from datetime import datetime, timezone
from urllib import error as urllib_error
from urllib import request as urllib_request


class Publisher:
    """
    Generates a static site from Crescent's lineage data and journals.
    Publishes to GitHub Pages via git commit + push.
    """

    def __init__(self, config: dict, base_dir: str):
        self.config = config
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / config["paths"].get("docs_dir", "docs")
        self.runs_dir = self.base_dir / config["paths"]["runs_dir"]
        self.journals_dir = self.base_dir / config["paths"].get("journals_dir", "journals")
        self.genome_dir = self.base_dir / config["paths"]["genome_dir"]
        self.repo_url = config.get("github", {}).get("repo_url", "")
        self.branch = config.get("github", {}).get("branch", "main")

    def publish(self, current_generation: int):
        """Generate static site and push to GitHub."""
        self.docs_dir.mkdir(parents=True, exist_ok=True)

        # Generate all pages
        self._generate_index(current_generation)
        self._generate_generation_pages()
        self._generate_journal_page()
        self._generate_lineage_json()
        self._copy_css()
        self._write_nojekyll()

        # Git commit and push
        if self.repo_url:
            self._git_push(current_generation)
        else:
            print("  [PUBLISHER] No GitHub repo configured. Skipping push.")

    def _generate_index(self, current_generation: int):
        """Generate the main lineage viewer page."""
        lineage_data = self._load_lineage()

        rows = ""
        for entry in lineage_data:
            gen = entry.get("generation", "?")
            score = entry.get("score", 0)
            death = entry.get("death_cause", "unknown")[:50]
            summary = entry.get("summary", "")[:80]
            progress = "✅" if entry.get("progress_made") else "❌"
            mutations = ", ".join(m.get("value", "")[:30] for m in entry.get("mutations", []))
            rows += f"""
            <tr>
                <td><a href="gen-{gen:04d}.html">{gen}</a></td>
                <td>{score:.1f}</td>
                <td>{death}</td>
                <td>{progress}</td>
                <td>{summary}</td>
                <td>{mutations or '—'}</td>
            </tr>"""

        # Stats
        scores = [e.get("score", 0) for e in lineage_data]
        avg_score = sum(scores) / len(scores) if scores else 0
        best_score = max(scores) if scores else 0

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crescent AGI — Lineage Viewer</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🌙 Crescent AGI</h1>
            <p class="subtitle">An evolving autonomous agent pursuing the impossible goal of building AGI</p>
            <div class="stats">
                <div class="stat">
                    <span class="stat-value">{current_generation - 1}</span>
                    <span class="stat-label">Generations</span>
                </div>
                <div class="stat">
                    <span class="stat-value">{avg_score:.1f}</span>
                    <span class="stat-label">Avg Score</span>
                </div>
                <div class="stat">
                    <span class="stat-value">{best_score:.1f}</span>
                    <span class="stat-label">Best Score</span>
                </div>
            </div>
        </header>

        <nav>
            <a href="index.html" class="active">Lineage</a>
            <a href="journal.html">Daily Journal</a>
            <a href="lineage.json">Raw Data</a>
        </nav>

        <main>
            <h2>Generation Lineage</h2>
            <table>
                <thead>
                    <tr>
                        <th>Gen</th>
                        <th>Score</th>
                        <th>Death Cause</th>
                        <th>Progress</th>
                        <th>Summary</th>
                        <th>Mutations</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </main>

        <footer>
            <p>Crescent AGI — evolutionary theater with measurable logs</p>
            <p>Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</p>
        </footer>
    </div>
</body>
</html>"""

        (self.docs_dir / "index.html").write_text(html, encoding="utf-8")

    def _generate_generation_pages(self):
        """Generate individual pages for each generation."""
        if not self.runs_dir.exists():
            return

        for gen_dir in sorted(self.runs_dir.iterdir()):
            if not gen_dir.is_dir() or not gen_dir.name.startswith("gen-"):
                continue

            autopsy_path = gen_dir / "autopsy.json"
            journal_path = gen_dir / "journal.md"
            inheritance_path = gen_dir / "inheritance_note.md"

            autopsy = {}
            if autopsy_path.exists():
                try:
                    autopsy = json.loads(autopsy_path.read_text(encoding="utf-8"))
                except Exception:
                    pass

            journal = ""
            if journal_path.exists():
                journal = journal_path.read_text(encoding="utf-8")

            inheritance = ""
            if inheritance_path.exists():
                inheritance = inheritance_path.read_text(encoding="utf-8")

            gen_num = autopsy.get("generation", gen_dir.name)

            # Build keep/avoid lists
            keep_list = "".join(f"<li>{k}</li>" for k in autopsy.get("keep", []))
            avoid_list = "".join(f"<li>{a}</li>" for a in autopsy.get("avoid", []))
            behaviors = "".join(f"<li>{b}</li>" for b in autopsy.get("interesting_behaviors", []))
            superstitions = "".join(f"<li>{s}</li>" for s in autopsy.get("superstitions", []))

            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crescent — Generation {gen_num}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🌙 Generation {gen_num}</h1>
            <p class="subtitle">{autopsy.get('summary', 'No summary available')}</p>
            <div class="stats">
                <div class="stat">
                    <span class="stat-value">{autopsy.get('score', 0):.1f}</span>
                    <span class="stat-label">Score</span>
                </div>
                <div class="stat">
                    <span class="stat-value">{autopsy.get('death_cause', 'unknown')[:30]}</span>
                    <span class="stat-label">Death Cause</span>
                </div>
                <div class="stat">
                    <span class="stat-value">{'✅' if autopsy.get('progress_made') else '❌'}</span>
                    <span class="stat-label">Progress</span>
                </div>
            </div>
        </header>

        <nav>
            <a href="index.html">← Back to Lineage</a>
            <a href="journal.html">Daily Journal</a>
        </nav>

        <main>
            <section>
                <h2>Autopsy</h2>
                <div class="two-col">
                    <div>
                        <h3>✅ Keep</h3>
                        <ul>{keep_list or '<li>—</li>'}</ul>
                    </div>
                    <div>
                        <h3>❌ Avoid</h3>
                        <ul>{avoid_list or '<li>—</li>'}</ul>
                    </div>
                </div>
            </section>

            <section>
                <h2>Interesting Behaviors</h2>
                <ul>{behaviors or '<li>—</li>'}</ul>
            </section>

            <section>
                <h2>Superstitions</h2>
                <ul>{superstitions or '<li>—</li>'}</ul>
            </section>

            <section>
                <h2>Inheritance Note</h2>
                <pre>{self._escape_html(inheritance)}</pre>
            </section>

            <section>
                <h2>Journal</h2>
                <pre>{self._escape_html(journal[:5000])}</pre>
            </section>
        </main>

        <footer>
            <a href="index.html">← Back to Lineage</a>
        </footer>
    </div>
</body>
</html>"""

            (self.docs_dir / f"{gen_dir.name}.html").write_text(html, encoding="utf-8")

    def _generate_journal_page(self):
        """Generate the daily journal page."""
        journals = []
        if self.journals_dir.exists():
            for f in sorted(self.journals_dir.iterdir(), reverse=True):
                if f.name.startswith("day-") and f.name.endswith(".md"):
                    content = f.read_text(encoding="utf-8")
                    journals.append({"date": f.stem.replace("day-", ""), "content": content})

        entries = ""
        for j in journals:
            entries += f"""
            <article class="journal-entry">
                <h3>{j['date']}</h3>
                <pre>{self._escape_html(j['content'])}</pre>
            </article>"""

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crescent — Daily Journal</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🌙 Crescent's Journal</h1>
            <p class="subtitle">Raw, unedited diary entries from a digital creature trying to build AGI</p>
        </header>

        <nav>
            <a href="index.html">Lineage</a>
            <a href="journal.html" class="active">Daily Journal</a>
        </nav>

        <main>
            {entries or '<p>No journal entries yet. Crescent has not completed its first day.</p>'}
        </main>

        <footer>
            <p>Crescent AGI — evolutionary theater with measurable logs</p>
        </footer>
    </div>
</body>
</html>"""

        (self.docs_dir / "journal.html").write_text(html, encoding="utf-8")

    def _generate_lineage_json(self):
        """Generate lineage.json for machine consumption."""
        lineage_data = self._load_lineage()
        (self.docs_dir / "lineage.json").write_text(
            json.dumps(lineage_data, indent=2), encoding="utf-8"
        )

    def _copy_css(self):
        """Copy or generate the CSS file."""
        css = """/* Crescent AGI Dashboard — Dark Theme */
:root {
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-tertiary: #21262d;
    --text-primary: #e6edf3;
    --text-secondary: #8b949e;
    --text-muted: #484f58;
    --accent: #7c3aed;
    --accent-light: #a78bfa;
    --border: #30363d;
    --success: #3fb950;
    --danger: #f85149;
    --warning: #d29922;
    --crescent: #fbbf24;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Segoe UI', -apple-system, sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

header {
    text-align: center;
    padding: 3rem 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}

header h1 {
    font-size: 2.5rem;
    background: linear-gradient(135deg, var(--crescent), var(--accent-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.subtitle {
    color: var(--text-secondary);
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.stats {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-top: 1.5rem;
}

.stat {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent-light);
}

.stat-label {
    font-size: 0.85rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

nav {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    padding: 1rem;
    background: var(--bg-secondary);
    border-radius: 8px;
    border: 1px solid var(--border);
}

nav a {
    color: var(--text-secondary);
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    transition: all 0.2s;
}

nav a:hover, nav a.active {
    background: var(--accent);
    color: white;
}

table {
    width: 100%;
    border-collapse: collapse;
    background: var(--bg-secondary);
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border);
}

th {
    background: var(--bg-tertiary);
    padding: 0.75rem 1rem;
    text-align: left;
    font-weight: 600;
    color: var(--text-secondary);
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 0.05em;
}

td {
    padding: 0.75rem 1rem;
    border-top: 1px solid var(--border);
    color: var(--text-primary);
}

td a {
    color: var(--accent-light);
    text-decoration: none;
    font-weight: 600;
}

td a:hover { text-decoration: underline; }

tr:hover { background: var(--bg-tertiary); }

section {
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: var(--bg-secondary);
    border-radius: 8px;
    border: 1px solid var(--border);
}

section h2 {
    color: var(--accent-light);
    margin-bottom: 1rem;
    font-size: 1.3rem;
}

section h3 {
    color: var(--crescent);
    margin-bottom: 0.5rem;
}

.two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
}

ul {
    padding-left: 1.5rem;
}

li {
    margin-bottom: 0.3rem;
    color: var(--text-secondary);
}

pre {
    background: var(--bg-primary);
    padding: 1rem;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 0.9rem;
    line-height: 1.5;
    white-space: pre-wrap;
    color: var(--text-secondary);
    border: 1px solid var(--border);
}

.journal-entry {
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: var(--bg-secondary);
    border-radius: 8px;
    border: 1px solid var(--border);
    border-left: 3px solid var(--crescent);
}

.journal-entry h3 {
    color: var(--crescent);
    margin-bottom: 1rem;
}

footer {
    text-align: center;
    padding: 2rem 0;
    border-top: 1px solid var(--border);
    margin-top: 2rem;
    color: var(--text-muted);
    font-size: 0.9rem;
}

footer a {
    color: var(--accent-light);
    text-decoration: none;
}

@media (max-width: 768px) {
    .container { padding: 1rem; }
    .stats { gap: 1.5rem; }
    .stat-value { font-size: 1.5rem; }
    .two-col { grid-template-columns: 1fr; }
    table { font-size: 0.85rem; }
}"""
        (self.docs_dir / "style.css").write_text(css, encoding="utf-8")

    def _write_nojekyll(self):
        """Tell GitHub Pages to serve the docs directory as plain static files."""
        (self.docs_dir / ".nojekyll").write_text("", encoding="utf-8")

    def _load_lineage(self) -> list:
        """Load lineage data from lineage.jsonl."""
        lineage_file = self.genome_dir / "lineage.jsonl"
        data = []
        if lineage_file.exists():
            for line in lineage_file.read_text(encoding="utf-8").strip().split("\n"):
                if line.strip():
                    try:
                        data.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        return data

    def _git_push(self, generation: int):
        """Commit and push docs to GitHub."""
        try:
            token = os.environ.get("GITHUB_TOKEN", "")
            if not token:
                print("  [PUBLISHER] No GITHUB_TOKEN set. Skipping push.")
                return

            # Configure git if needed
            subprocess.run(
                ["git", "config", "user.email", "crescent@crescent-agi.dev"],
                cwd=str(self.base_dir), capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Crescent AGI"],
                cwd=str(self.base_dir), capture_output=True,
            )

            # Add docs
            subprocess.run(
                ["git", "add", "docs/", "genome/", "journals/", "runs/"],
                cwd=str(self.base_dir), capture_output=True,
            )

            # Commit
            msg = f"🌙 Generation {generation} — auto-publish"
            result = subprocess.run(
                ["git", "commit", "-m", msg],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )

            if result.returncode == 0:
                # Push
                push_result = subprocess.run(
                    ["git", "push", "origin", self.branch],
                    cwd=str(self.base_dir), capture_output=True, text=True,
                )
                if push_result.returncode == 0:
                    print(f"  [PUBLISHER] Pushed generation {generation} to GitHub.")
                else:
                    print(f"  [PUBLISHER] Push failed: {push_result.stderr[:200]}")
            else:
                print(f"  [PUBLISHER] Nothing to commit or commit failed.")

        except Exception as e:
            print(f"  [PUBLISHER] Git error: {e}")

    def _git_push(self, generation: int):
        """Commit and push the tracked workspace to GitHub."""
        try:
            token = os.environ.get("GITHUB_TOKEN", "")
            if not token:
                print("  [PUBLISHER] No GITHUB_TOKEN set. Skipping push.")
                return

            subprocess.run(
                ["git", "config", "user.email", "crescent@crescent-agi.dev"],
                cwd=str(self.base_dir), capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Crescent AGI"],
                cwd=str(self.base_dir), capture_output=True,
            )

            push_url = self._build_push_url(token)
            if push_url:
                subprocess.run(
                    ["git", "remote", "set-url", "origin", push_url],
                    cwd=str(self.base_dir), capture_output=True, text=True,
                )

            add_result = subprocess.run(
                ["git", "add", "-A", "."],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )
            if add_result.returncode != 0:
                print(f"  [PUBLISHER] git add failed: {add_result.stderr[:200]}")
                return

            msg = f"Generation {generation} auto-publish"
            result = subprocess.run(
                ["git", "commit", "-m", msg],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )

            if result.returncode == 0:
                push_result = subprocess.run(
                    ["git", "push", "origin", self.branch],
                    cwd=str(self.base_dir), capture_output=True, text=True,
                )
                if push_result.returncode == 0:
                    print(f"  [PUBLISHER] Pushed generation {generation} to GitHub.")
                else:
                    print(f"  [PUBLISHER] Push failed: {push_result.stderr[:200]}")
            else:
                print("  [PUBLISHER] Nothing to commit or commit failed.")

        except Exception as e:
            print(f"  [PUBLISHER] Git error: {e}")

    def _build_push_url(self, token: str) -> str:
        """Build an authenticated push URL for the configured repo."""
        if not self.repo_url:
            return ""
        if self.repo_url.startswith("https://github.com/"):
            return self.repo_url.replace("https://", f"https://{token}@")
        return self.repo_url

    def _git_push(self, generation: int):
        """Commit and push the tracked workspace to GitHub."""
        try:
            token = os.environ.get("GITHUB_TOKEN", "")
            if not token:
                print("  [PUBLISHER] No GITHUB_TOKEN set. Skipping push.")
                return

            self._ensure_repo_exists(token)

            subprocess.run(
                ["git", "config", "user.email", "crescent@crescent-agi.dev"],
                cwd=str(self.base_dir), capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Crescent AGI"],
                cwd=str(self.base_dir), capture_output=True,
            )

            subprocess.run(
                ["git", "remote", "set-url", "origin", self.repo_url],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )

            push_url = self._build_push_url(token)
            if push_url:
                subprocess.run(
                    ["git", "remote", "set-url", "--push", "origin", push_url],
                    cwd=str(self.base_dir), capture_output=True, text=True,
                )

            add_result = subprocess.run(
                ["git", "add", "-A", "."],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )
            if add_result.returncode != 0:
                print(f"  [PUBLISHER] git add failed: {add_result.stderr[:200]}")
                return

            msg = f"Generation {generation} auto-publish"
            result = subprocess.run(
                ["git", "commit", "-m", msg],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )
            nothing_to_commit = "nothing to commit" in f"{result.stdout}\n{result.stderr}".lower()
            if result.returncode != 0 and not nothing_to_commit:
                print(f"  [PUBLISHER] Commit failed: {result.stderr[:200]}")
                return

            push_result = subprocess.run(
                ["git", "push", "origin", self.branch],
                cwd=str(self.base_dir), capture_output=True, text=True,
            )
            if push_result.returncode == 0:
                print(f"  [PUBLISHER] Pushed generation {generation} to GitHub.")
            else:
                print(f"  [PUBLISHER] Push failed: {push_result.stderr[:200]}")

        except Exception as e:
            print(f"  [PUBLISHER] Git error: {e}")

    def _ensure_repo_exists(self, token: str):
        """Ensure the configured GitHub repo exists before pushing."""
        owner_repo = self._github_owner_repo()
        if not owner_repo:
            return

        owner, repo = owner_repo
        repo_response = self._github_api_request(
            f"https://api.github.com/repos/{owner}/{repo}",
            token,
            method="GET",
            allowed_statuses={200, 404},
        )
        if repo_response["status"] == 200:
            return

        viewer = self._github_api_request(
            "https://api.github.com/user",
            token,
            method="GET",
            allowed_statuses={200},
        )
        viewer_login = viewer["json"].get("login", "")

        create_url = f"https://api.github.com/orgs/{owner}/repos"
        if owner == viewer_login:
            create_url = "https://api.github.com/user/repos"

        create_response = self._github_api_request(
            create_url,
            token,
            method="POST",
            body={"name": repo, "private": False},
            allowed_statuses={201, 422},
        )
        if create_response["status"] == 201:
            print(f"  [PUBLISHER] Created GitHub repo {owner}/{repo}.")
        elif create_response["status"] == 422:
            print(f"  [PUBLISHER] GitHub repo {owner}/{repo} already exists or cannot be recreated.")

    def _github_owner_repo(self):
        """Parse owner/repo from a GitHub HTTPS repo URL."""
        prefix = "https://github.com/"
        if not self.repo_url.startswith(prefix):
            return None
        path = self.repo_url[len(prefix):].removesuffix(".git").strip("/")
        parts = path.split("/")
        if len(parts) != 2:
            return None
        return parts[0], parts[1]

    def _github_api_request(self, url: str, token: str, method: str = "GET", body: dict | None = None, allowed_statuses=None):
        """Make a small GitHub API request with the configured token."""
        if allowed_statuses is None:
            allowed_statuses = {200}

        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")

        request = urllib_request.Request(
            url,
            method=method,
            data=data,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "crescent-agi",
                **({"Content-Type": "application/json"} if body is not None else {}),
            },
        )

        try:
            with urllib_request.urlopen(request, timeout=20) as response:
                payload = response.read().decode("utf-8")
                parsed = json.loads(payload) if payload else {}
                return {"status": response.status, "json": parsed}
        except urllib_error.HTTPError as e:
            payload = e.read().decode("utf-8")
            parsed = json.loads(payload) if payload else {}
            if e.code in allowed_statuses:
                return {"status": e.code, "json": parsed}
            raise

    @staticmethod
    def _escape_html(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
