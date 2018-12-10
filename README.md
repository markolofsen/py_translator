<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://kupi.net"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_en.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README_de.md">🇩🇪 Deutsch</a> | <b>🇬🇧 English</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Version = 2.1.7 <br />
Library name = py_translator <br />
Title = Free Google Translate API <br />
Keywords = Google API Cloud Translate, google api translate free <br />

### Info
The end goal is a simple application for translating text in the terminal. Text can be generated interactively or programmatically in the shell environment. Through command line arguments, file descriptors or pipes generating translated output that can be piped to a file or displayed on the terminal.

<b>Also, you can check our additional library with Google Cloud API</b> 

https://pypi.org/project/google-api-translate/


### Features
* Made for Python 3 but still works on Python 2
* Fast and easy to install, easy to use
* Supports translation from any language
* Highly composable interface, the power of Unix pipes and filters.
* Simple API and documentation

### Hot to install

```sh
pip3 install py_translator==2.1.7
```
                    

### How to use
```python
from py_translator import Translator
s = Translator().translate(text='Hello my friend', dest='es').text
print(s)
```

### With proxy
```python
from py_translator import Translator
proxy = {
        'http': 'http://username:password@1.1.1.1:1234',
        'https': 'http://username:password@1.1.1.1:1234',
}
s = Translator(proxies=proxy).translate(text='Hello my friend', dest='es').text
print(s)
```

### Shell
```shell
translate [--flags] [source] dest
```


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
```python
from py_translator import TEXTLIB

#with massTranslator()
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

--------
# Examples
Hello World from English to Traditional Chinese
```sh
$ translate en zh-TW <<< 'Hello World!'
你好世界！
Just as easily specify a source language by providing it as first argument
```

```sh
#Translate Hello from French to English
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
#Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### Be Creative!
```sh
#Grocery List
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

# Support
Python 3

# Documentation
Find the latest documentation http://pythonhosted.org/py-translate/



---

<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>