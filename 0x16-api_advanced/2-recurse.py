#!/usr/bin/python3
"""
recurse hot_list
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""

    url_req = requests.get("https://www.reddit.com/r/{}/hot/.json"
                           .format(subreddit),
                           params={"count": count, "after": after},
                           headers={"User-Agent": "My-User-Agent"},
                           allow_redirects=False)
    if url_req.status_code >= 400:
        return None
    url_req_rec = url_req.json()
    for obj in url_req.json().get("data").get("children"):
        hot_list.append(obj.get("data").get("title"))
    if url_req_rec.get("data").get("after") is not None:
        return recurse(subreddit, hot_list,
                       url_req_rec.get("data").get("count"),
                       url_req_rec.get("data").get("after"))
    return (hot_list)
