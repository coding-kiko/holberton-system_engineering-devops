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
            a = r.json()['data']['children'][pos]['data']['title'].lower().split()
            if search.lower() in a:
                if search not in dict_count:
                    dict_count[search] = 1
                else:
                    dict_count[search] += 1
    except IndexError:
        key_sort = dict(sorted(dict_count.items(), key=lambda x: x[0].upper()))
        value_sort = sorted(key_sort, key=key_sort.get, reverse=True)
        for k in value_sort:
            print('{}: {}'.format(k, value_sort[k]))
        return
    return (count_words(subreddit, word_list, pos+1))
