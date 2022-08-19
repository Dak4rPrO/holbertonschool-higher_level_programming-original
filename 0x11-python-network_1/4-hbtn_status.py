#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
    You must use the package requests """

import requests

if __name__ == "__main__":
    
    URL = 'https://intranet.hbtn.io/status'
    response = requests.get(url = URL)

    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(response), response)

