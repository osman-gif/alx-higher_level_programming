#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':

    url = 'https://github.com/search'
    search = {'q': sys.argv[1], 'type': sys.argv[2]}
    response = requests.get(url, search)
    if response.status_code == 200:
        repos = response.text.split(',')
        for i in repos:
            print(i)
        #print(repos)
    else:
        print(None)
