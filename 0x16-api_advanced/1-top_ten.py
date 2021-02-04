#!/usr/bin/python3
"""
list all the hot titles in json file from URL
"""
import requests


def top_ten(subreddit):
    url_req = requests.get("https://www.reddit.com/r/{}.json".format(
        subreddit), headers={"User-Agent": "new_user_agent 1.0"})
    # print((url_req.json().get('data').get('children'))[0].get('data').get('title'))
    try:
        for obj in url_req.json().get('data').get('children')[:10]:
            print(obj.get('data').get('title'))
    except Exception:
        print(None)
