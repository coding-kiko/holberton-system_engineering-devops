#!/usr/bin/python3
'''task 1'''

import requests


def top_ten(subreddit):
    '''get top 10 hottest posts subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'}).json()
    try:
        count = 0
        for title in r["data"]["children"]:
            print(title["data"]["title"])
            if count == 9:
                break
    except:
        return None
