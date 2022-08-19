#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and displays the body of
    the response """
from urllib import request, parse
import sys

if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    emails = {'email': arg2}
    data = urllib.parse.urlencode(emails).encode('ascii')
    req = urllib.request.Request(arg1, data)
    with urllib.request.urlopen(req) as url:
        response = url.read().decoded('utd-8')
    print(response)
