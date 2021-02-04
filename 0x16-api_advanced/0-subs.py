#!/usr/bin/python3
"""
take number of subscriber from URL with User_Agent
"""
import requests


def number_of_subscribers(subreddit):

    url_response = (requests.get(
        "https://www.reddit.com/r/{}/about.json".format(
            subreddit), headers={"User-Agent": "new_user_agent 1.0"}))
    if url_response.status_code is not 200:
        return 0
    # print(url_response.status_code)
    return((url_response.json()).get("data").get("subscribers"))
