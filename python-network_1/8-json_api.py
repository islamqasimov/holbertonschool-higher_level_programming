#!/usr/bin/python3
"""
Script that takes a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as parameter q.
Displays the result depending on JSON content.
"""

import sys
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"

    # If no argument → q=""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        return

    if json_data:
        print(f"[{json_data.get('id')}] {json_data.get('name')}")
    else:
        print("No result")


if __name__ == "__main__":
    main()
