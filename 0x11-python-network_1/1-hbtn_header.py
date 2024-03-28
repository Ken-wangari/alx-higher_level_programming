#!/usr/bin/python3
"""A script that:
- sends a request to the URL and therefore displays a value thats
- in the header of the response
- takes in a URL
"""
import sys
import urllib.request

def get_x_request_id(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        return headers.get("X-Request-Id")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")
