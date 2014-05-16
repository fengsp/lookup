#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    lookup
    ~~~~~~

    Look up words via the command line.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD, see LICENSE for more details.
"""
import sys
import random

try:
    from urllib import getproxies
except ImportError:
    from urllib.request import getproxies

try:
    from urllib.parse import quote as url_quote
except ImportError:
    from urllib import quote as url_quote

import requests
from pyquery import PyQuery as pq


PY2 = sys.version_info[0] == 2
SEARCH_URL = 'http://www.iciba.com/{0}'
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',)
RESULT_HEADER = 'iCIBA: {0}\n-------'


def get_proxies():
    proxies = getproxies()
    filtered_proxies = {}
    for key, value in proxies.items():
        if key.startswith('http'):
            if not value.startswith('http'):
                filtered_proxies[key] = 'http://%s' % value
            else:
                filtered_proxies[key] = value
    return filtered_proxies


def get_result(url):
    return requests.get(url, headers={'User-Agent': random.choice(USER_AGENTS)
                        }, proxies=get_proxies()).text


def get_output(word):
    result = get_result(SEARCH_URL.format(url_quote(word)))
    html = pq(result)
    return html('.net_paraphrase:first .clear:first')


def format_output(output):
    return output.text()


def lookup(word):
    return format_output(get_output(word))


def command_line():
    if len(sys.argv) < 2:
        print("usage: lookup [WORD]")
        sys.exit(0)
    
    word = sys.argv[1]
    print(RESULT_HEADER.format(word) + '-' * len(word))
    if PY2:
        print(lookup(word).encode('utf-8', 'ignore'))
    else:
        print(lookup(word))


if __name__ == "__main__":
    command_line()
