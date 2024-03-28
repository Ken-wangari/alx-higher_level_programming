#!/usr/bin/python3
"""A script that:
- the script must take in a Uniform Resource Locater
- then send a request
- and display the bosy of the response
"""


import sys
from urllib import request, error

def fetch_and_display(url):
    try:
        with request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except error.HTTPError as e:
        return f'Error code: {e.code}'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    content = fetch_and_display(url)
    print(content)
