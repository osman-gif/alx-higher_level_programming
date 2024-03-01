#!/usr/bin/python3
from urllib.request import Request, urlopen
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        res = response.read()
        cls_type = type(res)
        utf = res.decode('utf-8')

        print(f'Body response:')
        print(f'\t- type: {cls_type}')
        print(f'\t- content: {res}')
        print(f'\t- utf8 content: {utf}')
