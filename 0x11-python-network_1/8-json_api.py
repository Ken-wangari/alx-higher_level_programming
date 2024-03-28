#!/usr/bin/python3
"""A script that:
- should take in a letter then sends a POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


def search_user(letter):
    payload = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    return response


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = search_user(letter)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
