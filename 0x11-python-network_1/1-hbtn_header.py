#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response """

import sys
from urllib import request

if __name__ == "__main__":

    arg1 = sys.argv[1]
    with request.urlopen("{}".format(sys.argv[1])) as url:
        print(url.headers.get['X-Request-Id'])
