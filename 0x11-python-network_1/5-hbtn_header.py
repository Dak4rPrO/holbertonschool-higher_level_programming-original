#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header """

import requests
import sys

if __name__ == "__main__":
    arg1 = sys.argv[1]
    with urllib.request.urlopen(arg1) as url:
        response = url.read()

        print(url.headers.get('X-Request-Id'))
