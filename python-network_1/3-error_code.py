#!/usr/bin/python3
"""
Script that displays body of the error code
"""


import urllib.error
import urllib.request
import sys


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    main()
