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
    if sentence is 'q':
        break

    if sentence is 's':
        trans.swap(res)

    if sentence is 'c':
        trans.custom()
        continue

    # HTTP/2
    with HTTP20Connection(trans.url, port=443) as conn:
        conn.request('GET', '/?' + urlencode(trans.build_params()))
        data = conn.get_response().read()

    # tag Parser
    soup = BeautifulSoup(data, 'html.parser')
    res = soup.find(id='result_box').text
    print(res)



