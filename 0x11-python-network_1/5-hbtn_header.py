#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    X_Request_Id = response.headers['X-Request-Id']
    if X_Request_Id:
        print(X_Request_Id)
