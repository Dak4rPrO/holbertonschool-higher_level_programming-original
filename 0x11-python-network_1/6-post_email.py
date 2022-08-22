#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response """

import requests
import sys

if __name__ == "__main__":

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    email = {'email': arg2}
    response = requests.post(arg1, email)
    print(response.text)
