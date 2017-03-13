# -*- coding: utf-8 -*-

import requests
from parameter import TransParam

s = requests.Session()
trans = TransParam()
res = ''

# HTTP2
try:
    from hyper.contrib import HTTP20Adapter
    s.mount(trans.url, HTTP20Adapter())
except:
    raise ImportWarning('hyper package recommended')

# Parser
try:
    from bs4 import BeautifulSoup
except:
    raise ImportError('BeautifulSoup import Error')

while True:
    sentence = trans.set_sentence()

    if sentence is 'q':
        break

    if sentence is 's':
        trans.swap(res)

    if sentence is 'c':
        trans.custom()
        continue

    # GET url parse
    r = s.get(trans.url, params=trans.build_params())
    #print(r.url)

    # Parser
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find(id='result_box').text
    print(res)



