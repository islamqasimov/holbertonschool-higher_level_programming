#!/usr/bin/python3
"""
Working with jsonplaceholder and csv
"""


import requests
import csv
import json


API_URL = 'https://jsonplaceholder.typicode.com/posts'


def main():
    pass


def fetch_and_print_posts():
    rsp = requests.get(API_URL)
    print("Status code:", rsp.status_code)

    for data in rsp.json():
        print(data.get('title'))


def fetch_and_save_posts():
    rsp = requests.get(API_URL)
    all_data = []

    for data in rsp.json():
        tmp = {'id': data['id'], 'title': data['title'], 'body': data['body']}
        all_data.append(tmp)
    print(all_data[0].keys())

    with open('posts.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_data[0].keys())

        writer.writeheader()
        writer.writerows(all_data)


if __name__ == '__main__':
    main()
