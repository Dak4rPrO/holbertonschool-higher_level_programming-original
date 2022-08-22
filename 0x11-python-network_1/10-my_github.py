#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwrd = sys.argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(user, passwrd))
    print("{}".format(req.json().get('id')))
