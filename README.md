## hypertrans

[Google Translate](//translate.google.com) + HTTP/2

Google Translate with Python interactive console.
Python 콘솔로 구글 번역

HTTP/2를 통해 Python 콘솔로 translate.google.com을 우회합니다.

## Requirements

```
hyper==0.7.0
beautifulsoup4==4.5.3
```

#### Virtualenv install

```
pip install virtualenv
virtualenv _hypertrans

(Windows) `.\_hypertrans\Scripts\activate`

pip install hyper
pip install beautifulsoup4

pip freeze
```

## Setup

```
export PATH=$PATH:$HOME/.local/bin
python setup.py install --user
```

## Usage

```
python google_trans
```

#### Options

| Option | key |  
|:---|:---|  
| Quit | 'q' |  
| Swap | 's' |  
| Custom | 'c' |

```
en->ko: i am great
나는 잘 지내고있어
en->ko: s
I'm doing well.
ko->en: s
나는 잘하고 있어요.
en->ko: c
Source Language: 
Destination Language: ja
en->ja: i'm doing well
私はうまくやってる
```

## requests library bug

[`with` context manager `close()` bug in *requests* library](//github.com/Lukasa/hyper/issues/306)

## Reference

- [Google Translation API](//cloud.google.com/translate/docs/)  
- [Quickstart requests](//docs.python-requests.org/en/master/user/quickstart/)  
- [Quickstart hyper](//hyper.readthedocs.io/en/latest/quickstart.html)  
- [GitHub: py-googletrans](//github.com/ssut/py-googletrans)