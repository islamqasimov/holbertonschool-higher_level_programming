#!/usr/bin/python3
"""
Script that sends POST request with email header
"""


import urllib.request
import urllib.parse
import sys


def main():
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)

if __name__ == '__main__':
    main()
