#!/usr/bin/python3
"""
Module for task 1
"""

import json
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    headers = {"user-agent": "Custom User Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    subdata = requests.get(url, headers=headers)
    if subdata.status_code != 200:
        print("None")
        return
    data = json.loads(subdata.text).get('data').get('children')
    if not data:
        print("None")
        return
    for item in data[0:10]:
        print(item.get('data').get('title'))
