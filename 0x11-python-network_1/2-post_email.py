#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


def send_post_request(url, email):
    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    
    response_body = send_post_request(url, email)
    print(response_body)

