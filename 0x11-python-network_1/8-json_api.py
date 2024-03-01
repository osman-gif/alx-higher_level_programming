#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import sys
import requests

url = 'http://0.0.0.0:5000/search_user'

if len(sys.argv) < 2:
    letter = ""
else:
    letter = sys.argv[1]

paylod = {'q': letter}

try:
    response = requests.post(url, paylod).json()

    if response:
        print(f"[{response.get('id')}] {response.get('name')}")
    else:
        print('No result')

except ValueError as e:
    print('Not a valid JSON')
