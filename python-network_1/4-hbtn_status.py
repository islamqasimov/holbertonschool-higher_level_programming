#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""


import requests

def main():
    url = 'https://intranet.hbtn.io/status'
    rsp = requests.get(url)

    print("Body response:")
    print("\t- type:", type(rsp.text))
    print("\t- content:", rsp.text)
    


if __name__ == '__main__':
    main()
