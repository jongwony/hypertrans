# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from parameter import TransParam

from hyper import HTTP20Connection
from bs4 import BeautifulSoup

trans = TransParam()
res = ''


while True:
    # stdin once
    try:
        sentence = trans.set_sentence()
    except EOFError:
        break

    # Option
    if sentence in ['q', 'ㅂ']:
        break

    if sentence.endswith('``') or sentence is '':
        continue

    if sentence in ['c', 'ㅊ']:
        trans.custom()
        continue

    if sentence in ['s', 'ㄴ']:
        trans.swap(res)

    res = trans.translate()
    print(res)
