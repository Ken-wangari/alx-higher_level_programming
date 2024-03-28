#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


def get_recent_commits(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repo_owner> <repo_name>")
        sys.exit(1)

    repo_owner, repo_name = sys.argv[1], sys.argv[2]
    commits = get_recent_commits(repo_owner, repo_name)
    
    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")

