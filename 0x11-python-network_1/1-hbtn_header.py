#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

from urllib.request import Request, urlopen
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    print(url)
    with urlopen(url) as response:
        print(response.headers['X-Request-Id'])
