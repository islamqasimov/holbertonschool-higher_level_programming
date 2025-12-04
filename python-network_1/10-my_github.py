#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


import requests
import sys


def main():
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    rsp = requests.get(url, auth=(username, token))

    if rsp.status_code == 200:
        user_data = rsp.json()
        print(user_data.get('id'))
    else:
        print(None)


if __name__ == '__main__':
    main()
