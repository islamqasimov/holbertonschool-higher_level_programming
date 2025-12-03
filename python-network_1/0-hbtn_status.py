#!/usr/bin/python3
import urllib.request
url = "https://intranet.hbtn.io/status"
req = urllib.request.Request(url, headers={'cfclearance': 'true'})
with urllib.request.urlopen(req) as resp:
    body = resp.read()
    print("Body response:")
    print("\t- type: ", type(body))
    print("\t- content: ", body)
    print("\t- utf8: ", body.decode('utf-8'))
