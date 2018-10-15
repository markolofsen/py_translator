py_translator

[![Google HTML translator](https://github.com/markolofsen/py_translator/blob/master/teaser.png?raw=true)](https://github.com/markolofsen/py_translator)

=========================

[[TAG1]]

The end goal is a simple application for translating text in the terminal.
Text can be generated interactively or programmatically in the
shell environment. Through command line arguments, file descriptors or
pipes generating translated output that can be piped to a file or
displayed on the terminal.

Features
----------

- Made for Python 3 but still works on Python 2
- Fast and easy to install, easy to use
- Supports translation from any language
- Highly composable interface, the power of Unix pipes and filters.
- Simple API and documentation

Installation
------------

### From PyPI with `pip`

```sh
$ pip3 install py_translator==1.8.4
```

## Python
```python3
from py_translator import Translator
s = Translator().translate(text='Hello my friend', dest='es').text
print(s)
```

## With proxy
```python3
from py_translator import Translator
proxy = {
        'http': 'http://username:password@1.1.1.1:1234',
        'https': 'http://username:password@1.1.1.1:1234',
}
s = Translator(proxies=proxy).translate(text='Hello my friend', dest='es').text
print(s)
```

## Shell
```python3
translate [--flags] [source] dest
```


### Arguments

| **Positional**     |                                                       |
|--------------------|-------------------------------------------------------|
| dest               | Destination language code                             |
| source             | Source language code                                  |
| **Optional**       |                                                       |
| -h,--help          | Show this help message and exit                       |
| -v, --version      | Show program’s version number and exit                |
| -l,--list _[code]_ | Enumerate the name of country and language code pair. |
|                    | [_Optionally specify output language format_]         |
| --translit         | Print out the transliteration of the text             |


---

# html translation

### Python
```python
from py_translator import TEXTLIB
s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

### With proxy
```python
from py_translator import TEXTLIB

proxy = [
    'http://username:password@1.1.1.1:1234',
    'http://username:password@1.1.1.1:1234',
]

s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=proxy)
print(s)
```

### With multithreading
##### with `massTranslator()`
```python
from py_translator import TEXTLIB
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

---
Examples
--------

Hello World from English to Traditional Chinese

```sh
$ translate en zh-TW <<< 'Hello World!'
你好世界！

```

![Hello World][hello]

- Just as easily specify a source language by providing it as first argument

```sh
# Translate Hello from French to English
$ translate fr en <<< 'Bonjour, comment allez-vous!'
Hello, how are you?
```

### Smart Language Detection
Omitting the source language will try to detect it based on the text content

```sh
$ translate fr <<< 'I think therefore I am'
Je pense donc je suis
```

### Romanified Transliteration

```sh
$ translate --translit en ko <<< 'Want to fight!'
ssaugo sip-eo!

$ translate --translit en zh-TW <<< 'Kidding, we should be friends'
Kāiwánxiào, wǒmen yīnggāi shì péngyǒu
```

### Redirect from File

```sh
$ translate zh-TW < 'alice.txt'

阿麗思道：「你不是說你要告訴你的歷史嗎？告訴我你為甚麼恨—那個—那些—C和D，」
她末了兩個字母輕輕兒地說的，怕回來又得罪了牠。

那老鼠對著阿麗思嘆了一口氣道，「唉﹗我的身世說來可真是又長又苦又委屈呀—」

阿麗思聽了，瞧著那老鼠的尾巴說，「你這尾是曲啊﹗可是為甚麼又叫它苦呢﹗」
她就一頭聽著那老鼠說話，一頭在在心上納悶，所以她聽的那老鼠講的「尾曲」
的歷史是差不多像這個樣了的
....
```

### Chaining together Pipes

```sh
# Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### Be Creative!

```sh
# Grocery List
$ cat << BUY | translate ko
Celery
Milk
Eggs
Bread
Cereal
BUY

셀러리
우유
달걀
빵
시리얼
```

Support
--------

Here’s a list of Python platforms that are officially supported.

- Python 3.4
- Python 3.3
- Python 3.2
- Python 2.7
- Python 2.6
- PyPy 2 (Latest)
- PyPy 3 (latest)

Documentation
-------------

Find the latest documentation http://pythonhosted.org/py-translate/