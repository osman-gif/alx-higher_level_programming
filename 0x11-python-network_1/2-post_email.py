#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

from urllib import parse
from urllib.request import urlopen, Request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    email = parse.urlencode(value)
    req = Request(url, email.encode('ascii'))
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
