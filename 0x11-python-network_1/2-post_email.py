#!/usr/bi/python3
""" Python script that takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and displays the body of
    the response """
    
import urllib
import sys    

if __name__ == "__main__":
    
    arg1 = sys.argv[1]
    with urllib.request.urlopen(arg1) as url:
        response = url.read()
        
        