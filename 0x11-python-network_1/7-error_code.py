#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.post(url)
    if response.ok:
        body = response.text
        print(body)
    else:
        print(f"Error code:{response.status_code}")