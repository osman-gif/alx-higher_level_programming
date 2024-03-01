#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print(
    f'Body response:\n\
        \t- type: {type(response.text)}\n\t- content: {response.text}')
