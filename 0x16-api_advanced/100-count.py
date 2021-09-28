#!/usr/bin/python3
'''advanced task'''

import requests


def count_words(subreddit, word_list, pos=0, dict_count={}):
    '''count word occurences in hot post titles'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'},
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    try:
        for search in word_list:
            if search.lower() in r.json()['data']['children'][pos]['data']['title'].lower().split():
                print(r.json()['data']['children'][pos]['data']['title'])
                if search not in dict_count:
                    dict_count[search] = 1
                else:
                    dict_count[search] += 1
    except IndexError:
        return dict_count
    return (count_words(subreddit, word_list, pos+1))
