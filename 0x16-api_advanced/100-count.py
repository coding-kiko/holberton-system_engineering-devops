#!/usr/bin/python3
'''advanced task'''

import requests


def count_words(subreddit, word_list, pos=0):
    '''count word occurences in hot post titles'''
    print(word_list)
    """ url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'},
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    try:
        hot_list.append(r.json()['data']['children'][pos]['data']['title'])
    except IndexError:
        return hot_list
    return (recurse(subreddit, hot_list, pos+1)) """
