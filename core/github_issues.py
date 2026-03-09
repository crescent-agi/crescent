"""
GitHub issue inbox/outbox for Crescent.
"""

import json
import os
from urllib import error as urllib_error
from urllib import parse as urllib_parse
from urllib import request as urllib_request


class GitHubIssues:
    """Small GitHub Issues client backed by GITHUB_TOKEN."""

    def __init__(self, config: dict):
        github_cfg = config.get("github", {})
        self.repo_url = github_cfg.get("repo_url", "")
        self.issue_inbox_label = github_cfg.get("issue_inbox_label", "human")
        self.self_task_label = github_cfg.get("self_task_label", "self-task")
        owner_repo = self._parse_owner_repo(self.repo_url)
        self.owner = owner_repo[0] if owner_repo else ""
        self.repo = owner_repo[1] if owner_repo else ""
        self.token = os.environ.get("GITHUB_TOKEN", "")

    def enabled(self) -> bool:
        return bool(self.owner and self.repo and self.token)

    def list_open_issues(self, label: str | None = None, limit: int = 10) -> dict:
        if not self.enabled():
            return {"error": "GitHub issues are not configured."}

        params = {
            "state": "open",
            "per_page": max(1, min(limit, 50)),
        }
        if label:
            params["labels"] = label

        data = self._request(
            f"/repos/{self.owner}/{self.repo}/issues?{urllib_parse.urlencode(params)}"
        )
        issues = []
        for item in data:
            if "pull_request" in item:
                continue
            issues.append({
                "number": item["number"],
                "title": item["title"],
                "state": item["state"],
                "labels": [label["name"] for label in item.get("labels", [])],
                "author": item.get("user", {}).get("login", "unknown"),
                "body": (item.get("body") or "")[:4000],
                "url": item.get("html_url", ""),
            })
        return {"issues": issues}

    def read_issue(self, number: int) -> dict:
        if not self.enabled():
            return {"error": "GitHub issues are not configured."}
        issue = self._request(f"/repos/{self.owner}/{self.repo}/issues/{number}")
        comments = self._request(f"/repos/{self.owner}/{self.repo}/issues/{number}/comments")
        return {
            "number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "labels": [label["name"] for label in issue.get("labels", [])],
            "author": issue.get("user", {}).get("login", "unknown"),
            "body": issue.get("body", ""),
            "url": issue.get("html_url", ""),
            "comments": [
                {
                    "author": comment.get("user", {}).get("login", "unknown"),
                    "body": comment.get("body", ""),
                    "url": comment.get("html_url", ""),
                }
                for comment in comments
            ],
        }

    def comment_issue(self, number: int, body: str) -> dict:
        if not self.enabled():
            return {"error": "GitHub issues are not configured."}
        comment = self._request(
            f"/repos/{self.owner}/{self.repo}/issues/{number}/comments",
            method="POST",
            body={"body": body},
        )
        return {"success": True, "url": comment.get("html_url", "")}

    def create_issue(self, title: str, body: str, labels: list[str] | None = None) -> dict:
        if not self.enabled():
            return {"error": "GitHub issues are not configured."}
        issue = self._request(
            f"/repos/{self.owner}/{self.repo}/issues",
            method="POST",
            body={"title": title, "body": body, "labels": labels or []},
        )
        return {"success": True, "number": issue["number"], "url": issue.get("html_url", "")}

    def close_issue(self, number: int) -> dict:
        if not self.enabled():
            return {"error": "GitHub issues are not configured."}
        issue = self._request(
            f"/repos/{self.owner}/{self.repo}/issues/{number}",
            method="PATCH",
            body={"state": "closed"},
        )
        return {"success": True, "number": issue["number"], "state": issue["state"]}

    def _request(self, path: str, method: str = "GET", body: dict | None = None):
        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")

        req = urllib_request.Request(
            f"https://api.github.com{path}",
            method=method,
            data=data,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "crescent-agi",
                **({"Content-Type": "application/json"} if body is not None else {}),
            },
        )
        try:
            with urllib_request.urlopen(req, timeout=20) as response:
                payload = response.read().decode("utf-8")
                return json.loads(payload) if payload else {}
        except urllib_error.HTTPError as e:
            payload = e.read().decode("utf-8")
            detail = payload[:400] if payload else str(e)
            raise RuntimeError(f"GitHub API error {e.code}: {detail}") from e

    @staticmethod
    def _parse_owner_repo(repo_url: str):
        prefix = "https://github.com/"
        if not repo_url.startswith(prefix):
            return None
        path = repo_url[len(prefix):].removesuffix(".git").strip("/")
        parts = path.split("/")
        if len(parts) != 2:
            return None
        return parts[0], parts[1]
