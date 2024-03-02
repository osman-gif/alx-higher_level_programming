#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':

    url = 'https://api.github.com/user'
    my_auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=my_auth)
    if response.status_code == 200:  
        print(response.text.split(',')[1].split(':')[1])
    else:
        print(None)
