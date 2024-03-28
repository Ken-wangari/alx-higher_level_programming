#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

import urllib.request

def fetch_status():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        return content.decode('utf-8')

if __name__ == '__main__':
    status_content = fetch_status()
    print("Body response:")
    print("\t- type: {}".format(type(status_content)))
    print("\t- content: {}".format(status_content))

