#!/usr/bin/python3
"""Script to get X-Request-Id"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        data = response.info()
        print(data.get('X-Request-Id'))
