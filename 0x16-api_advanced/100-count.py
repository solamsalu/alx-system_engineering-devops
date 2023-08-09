#!/usr/bin/python3
"""
Module for task 100
"""

import requests


def count_words(subreddit, word_list, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                title = post["data"]["title"]
                process_title(title, word_list, count_dict)

            next_page = data["data"]["after"]

            if next_page is not None:
                count_words(subreddit, word_list, count_dict)
            else:
                print_results(count_dict)
        except KeyError:
            pass


def process_title(title, word_list, count_dict):
    words = title.lower().split()

    for word in words:
        if word.isalpha() and word in word_list:
            count_dict[word] = count_dict.get(word, 0) + 1


def print_results(count_dict):
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")
