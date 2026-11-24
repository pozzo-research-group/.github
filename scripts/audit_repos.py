"""Yearly audit of pozzo-research-group repositories (plan step 4.3).

Checks every public, non-archived repository against REPOSITORY_GUIDE.md and
prints a Markdown report. The yearly workflow posts the report as an issue in
the .github repository.

    python scripts/audit_repos.py            # print the report
    python scripts/audit_repos.py out.md     # also write it to out.md

Reads GITHUB_TOKEN from the environment if set. With the Actions token, only
public repositories are visible, so private repositories are not audited.
Standard library only.
"""
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request

ORG = "pozzo-research-group"
STALE_MONTHS = 24                  # guide §10
LARGE_FILE_MB = 50                 # GitHub warns at 50 MiB (guide §8)
LARGE_REPO_MB = 1000               # GitHub: ideally under 1 GB (guide §8)
OLD_PR_DAYS = 90
CATEGORY_TOPICS = {"analysis", "data-management", "automation", "open-hardware",
                   "paper", "project", "teaching"}
# Not group content: skipped entirely.
EXCLUDE = {".github", "awesome-self-driving-labs"}
# Kept off the front page on purpose, so no category topic is expected.
NO_CATEGORY_OK = {"template-python-package", "template-paper"}

TOKEN = os.environ.get("GITHUB_TOKEN")


def api(path):
    url = path if path.startswith("http") else f"https://api.github.com/{path}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (404, 409):   # missing file, or empty repository
            return None
        raise


def paged(path):
    out, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        batch = api(f"{path}{sep}per_page=100&page={page}") or []
        out += batch
        if len(batch) < 100:
            return out
        page += 1


def audit(now):
    stale_before = now - dt.timedelta(days=round(STALE_MONTHS * 30.44))
    rows = {k: [] for k in ("stale", "readme", "license", "citation", "description",
                            "category", "large", "prs")}
    repos = [r for r in paged(f"orgs/{ORG}/repos?type=public")
             if not r["archived"] and not r["private"] and r["name"] not in EXCLUDE]
    for r in sorted(repos, key=lambda r: r["name"].lower()):
        name, full, branch = r["name"], r["full_name"], r["default_branch"]
        link = f"[{name}]({r['html_url']})"

        commits = api(f"repos/{full}/commits?sha={branch}&per_page=1")
        if commits:
            last = dt.datetime.fromisoformat(
                commits[0]["commit"]["committer"]["date"].replace("Z", "+00:00"))
            if last < stale_before:
                rows["stale"].append(f"| {link} | {last:%Y-%m-%d} |")

        if api(f"repos/{full}/readme") is None:
            rows["readme"].append(f"| {link} |")
        if not r.get("license"):
            rows["license"].append(f"| {link} |")
        if api(f"repos/{full}/contents/CITATION.cff?ref={branch}") is None:
            topics = ", ".join(r.get("topics") or []) or "none"
            rows["citation"].append(f"| {link} | {topics} |")
        if not (r.get("description") or "").strip():
            rows["description"].append(f"| {link} |")
        if name not in NO_CATEGORY_OK and not CATEGORY_TOPICS & set(r.get("topics") or []):
            rows["category"].append(f"| {link} |")

        size_mb = r["size"] / 1024
        big = []
        tree = api(f"repos/{full}/git/trees/{branch}?recursive=1")
        if tree:
            big = [f"`{t['path']}` ({t['size'] / 2**20:.0f} MiB)"
                   for t in tree.get("tree", [])
                   if t.get("type") == "blob" and t.get("size", 0) > LARGE_FILE_MB * 2**20]
        if size_mb > LARGE_REPO_MB or big:
            rows["large"].append(f"| {link} | {size_mb:,.0f} MB | {'; '.join(big[:5]) or '-'} |")

        old_prs = [p for p in paged(f"repos/{full}/pulls?state=open")
                   if now - dt.datetime.fromisoformat(p["created_at"].replace("Z", "+00:00"))
                   > dt.timedelta(days=OLD_PR_DAYS)]
        if old_prs:
            bots = sum(p["user"]["type"] == "Bot" for p in old_prs)
            rows["prs"].append(f"| {link} | {len(old_prs)} | {bots} |")
    return len(repos), rows


SECTIONS = [
    ("stale", f"No commits on the default branch for {STALE_MONTHS} months (guide §10)",
     "Ask the maintainer whether it is still in use; if not, archive it.",
     "| Repository | Last commit |\n|---|---|"),
    ("readme", "No README (guide §4)", "", "| Repository |\n|---|"),
    ("license", "No license detected (guide §5)",
     "New repositories use MIT or BSD-3-Clause.", "| Repository |\n|---|"),
    ("citation", "No CITATION.cff (guide §7)",
     "Required for repositories tied to a paper and for packages.",
     "| Repository | Topics |\n|---|---|"),
    ("description", "No description (guide §3)", "", "| Repository |\n|---|"),
    ("category", "No category topic (guide §3)", "", "| Repository |\n|---|"),
    ("large", f"Large repository or files over {LARGE_FILE_MB} MiB (guide §8)",
     "Move data to Zenodo; don't rewrite history of cited repositories.",
     "| Repository | Size | Large files |\n|---|---|---|"),
    ("prs", f"Pull requests open for more than {OLD_PR_DAYS} days (guide §9)",
     "Merge or close them, including bot pull requests.",
     "| Repository | Open PRs | From bots |\n|---|---|---|"),
]


def report(now, n, rows):
    out = [f"Automated yearly check of the {n} public, non-archived repositories in "
           f"{ORG} against the [repository guide]"
           f"(https://github.com/{ORG}/.github/blob/main/REPOSITORY_GUIDE.md). "
           f"Run on {now:%Y-%m-%d}. Private repositories are not included.",
           "",
           "Maintainers: fix what applies to your repositories and tick it off in a comment. "
           "Lilo decides on archiving.", ""]
    for key, title, note, header in SECTIONS:
        items = rows[key]
        out.append(f"### {title}: {len(items)}")
        if note:
            out.append(f"_{note}_")
        out.append("")
        out.append("\n".join([header, *items]) if items else "None.")
        out.append("")
    return "\n".join(out)


def main():
    now = dt.datetime.now(dt.timezone.utc)
    n, rows = audit(now)
    text = report(now, n, rows)
    print(text)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(text)


if __name__ == "__main__":
    main()
