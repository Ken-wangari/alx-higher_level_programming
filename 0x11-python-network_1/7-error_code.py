#!/usr/bin/python3
"""A script that
- takes in a URL then sends a request to it
- should then display the response body afterwards
"""
import sys
import requests


def fetch_and_display(url):
    response = requests.get(url)
    if response.status_code >= 400:
        return "Error code: {}".format(response.status_code)
    else:
        return response.text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    content = fetch_and_display(url)
    print(content)
