# -*- coding: utf-8 -*-

from urllib.parse import urlencode
from parameter import TransParam
from hyper import HTTP20Connection
from bs4 import BeautifulSoup

trans = TransParam()
res = ''



while True:
    sentence = trans.set_sentence()

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

    # HTTP/2
    with HTTP20Connection(trans.url, port=443) as conn:
        conn.request('GET', '/?' + urlencode(trans.build_params()))
        data = conn.get_response().read()

    # tag Parser
    soup = BeautifulSoup(data, 'html.parser')
    res = soup.find(id='result_box').text
    print(res)
