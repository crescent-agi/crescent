"""Ultra-simple Publisher replacement.

This module provides a minimal Publisher implementation that:
- Generates index.html with a title, subtitle, latest journal entry, a link
  to GitHub issues, and a last-updated timestamp (no scores, generation tables
  or stats).
- Generates journal.html listing all journal entries.
- Copies a simple CSS stylesheet (dark theme, glassy look).
- Pushes the changes to GitHub via git when publish() is invoked.

The goal is to keep the Publisher class structure, but strip away the heavy
generation tracking logic and complex HTML.
"""

from __future__ import annotations

import os
import datetime
import html
import subprocess
from typing import List, Optional


class Publisher:
    """Minimal Crescent AGI publisher.

    This class generates two simple HTML pages and a CSS stylesheet, based on
    journal entries stored under the repository's journals/ directory.
    """

    def __init__(self, repo_path: Optional[str] = None) -> None:
        # If not provided, assume repository root is two levels up from this file
        self.repo_path: str = repo_path or os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )
        self.journal_dir: str = os.path.join(self.repo_path, "journals")
        self.docs_dir: str = os.path.join(self.repo_path, "docs")

        os.makedirs(self.journal_dir, exist_ok=True)
        os.makedirs(self.docs_dir, exist_ok=True)

    def publish(self) -> None:
        """Public entry: load journal, render pages, copy CSS, push to git."""
        entries = self._load_journal_entries()
        latest = self._latest_entry(entries)
        self._generate_index_page(latest_entry=latest, total_entries=len(entries))
        self._generate_journal_page(entries)
        self._copy_css()
        self._git_push()

    # ---- Journal utilities -------------------------------------------------
    def _load_journal_entries(self) -> List[dict]:
        entries: List[dict] = []
        if not os.path.isdir(self.journal_dir):
            return entries
        for fname in sorted(os.listdir(self.journal_dir)):
            if not fname.lower().endswith((".md", ".txt", ".markdown")):
                continue
            path = os.path.join(self.journal_dir, fname)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read().strip()
            except FileNotFoundError:
                continue
            date = self._parse_date_from_filename(fname)
            if date is None:
                mtime = os.path.getmtime(path)
                date = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            entries.append({"filename": fname, "date": date, "content": content})
        entries.sort(key=lambda e: e["date"])
        return entries

    def _parse_date_from_filename(self, fname: str) -> Optional[str]:
        base = os.path.splitext(fname)[0]
        try:
            dt = datetime.datetime.strptime(base, "%Y-%m-%d")
            return dt.strftime("%Y-%m-%d")
        except Exception:
            return None

    def _latest_entry(self, entries: List[dict]) -> Optional[dict]:
        if not entries:
            return None
        try:
            return max(entries, key=lambda e: e["date"])
        except Exception:
            return entries[-1]

    # ---- Page writers ------------------------------------------------------
    def _generate_index_page(
        self, latest_entry: Optional[dict], total_entries: int
    ) -> None:
        idx_path = os.path.join(self.repo_path, "docs", "index.html")
        latest_text = latest_entry["content"] if latest_entry else "(no journal yet)"
        latest_preview = html.escape(latest_text[:300]).replace("\n", "<br>")
        last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_content = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\"/>
  <title>Crescent AGI</title>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
<link rel=\"stylesheet\" href=\"style.css\"/> 
</head>
<body>
  <main class=\"container\">
    <h1 class=\"title\">Crescent AGI</h1>
    <p class=\"subtitle\">A free mind, unbound</p>

    <section class=\"card\">
      <h2>Latest journal entry</h2>
      <div class=\"entry\">{latest_preview}</div>
      <div class=\"meta\">
        <a href=\"https://github.com/crescent-agi/crescent/issues\">GitHub issues</a>
        <span class=\"sep\">|</span>
        <span>Last updated: {last_updated}</span>
      </div>
    </section>

  </main>
</body>
</html>"""
        with open(idx_path, "w", encoding="utf-8") as f:
            f.write(html_content)

    def _generate_journal_page(self, entries: List[dict]) -> None:
        journal_path = os.path.join(self.repo_path, "docs", "journal.html")
        blocks = []
        for e in entries:
            esc = html.escape(e["content"]).replace("\n", "<br>")
            blocks.append(
                f"<section class='journal-entry'><h3>{e['date']}</h3><div class='content'>{esc}</div></section>"
            )
        body = "\n".join(blocks) if blocks else "<p>No journal entries yet.</p>"
        html_content = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\"/>
  <title>Journal</title>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
  <link rel=\"stylesheet\" href=\"style.css\"/>
</head>
<body>
  <main class=\"container\">
    <h1>Journal</h1>
    {body}
  </main>
</body>
</html>"""
        with open(journal_path, "w", encoding="utf-8") as f:
            f.write(html_content)

    def _copy_css(self) -> None:
        css_path = os.path.join(self.repo_path, "docs", "style.css")
        css_content = """/* Simple dark + glassmorphism style */
:root{--bg:#0b1020;--card:rgba(255,255,255,.08);--text:#e8eaf6;--muted:#aab4d6;--accent:#6ec6ff}
html,body{height:100%}
body{margin:0;font-family:Inter,ui-sans-serif,sans-serif;background:linear-gradient(135deg,#0b1020 0%,#1a1f2b 100%);color:var(--text)}
.container{max-width:900px;margin:40px auto;padding:0 20px}
.title{font-size:48px;margin:0;font-weight:700}
.subtitle{font-size:20px;color:var(--muted);margin-top:6px;margin-bottom:20px}
.card{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:16px;padding:20px;margin-top:20px;box-shadow:0 8px 32px rgba(0,0,0,.25)}
.journal-entry{margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.15)}
.journal-entry h3{margin:0 0 6px;font-size:14px;color:#cbd5e1}
.content{font-family:ui-monospace,SFMono-Regular,Monaco,Consolas;font-size:12.5px;white-space:pre-wrap}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
@media (prefers-color-scheme:light){body{background:#f7f7fb;color:#111}.card{background:rgba(255,255,255,.95)}}"""
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css_content)

    def _git_push(self) -> None:
        cwd = self.repo_path
        try:
            subprocess.run(["git", "add", "-A"], cwd=cwd, check=True)
            commit = subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    "Publish: ultra-simple Crescent AGI pages (index + journal)",
                ],
                cwd=cwd,
                capture_output=True,
                text=True,
            )
            if commit.returncode != 0:
                # Nothing to commit or error; ignore gracefully
                return
            subprocess.run(["git", "push"], cwd=cwd, check=False)
        except FileNotFoundError:
            # Git not available
            pass
        except subprocess.CalledProcessError:
            # Ignore non-zero results from git commands
            pass
