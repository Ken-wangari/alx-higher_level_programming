#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests


def get_github_id(username, password):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    return response.json().get("id")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <username> <password>")
        sys.exit(1)

    username, password = sys.argv[1], sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)

