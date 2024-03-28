#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


def send_post_request(url, email):
    data = {"email": email}
    response = requests.post(url, data=data)
    return response.text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    
    response_body = send_post_request(url, email)
    print(response_body)

