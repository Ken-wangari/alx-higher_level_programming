#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


def get_x_request_id(url):
    response = requests.get(url)
    return response.headers.get("X-Request-Id")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)

