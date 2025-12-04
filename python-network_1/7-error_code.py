#!/usr/bin/python3
"""
Python script that takes in a URL, sends
a request to the URL and displays the body of the response
"""


import requests
import sys


def main():
    url = sys.argv[1]

    try:
        rsp = requests.get(url)
        rsp.raise_for_status()
        print(rsp.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", rsp.status_code)


if __name__ == '__main__':
    main()
