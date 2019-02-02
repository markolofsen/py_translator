<p align="center"><b>🛠️ Questo repository è stato creato usando <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_it.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_fr.md">French</a> | <b>Italian</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

Versione = 2.1.9 <br />
Nome libreria = py_translator <br />
Titolo = Free Google Translate API <br />
Parole chiave = Google API Cloud Translate, google api translate free <br />

### Informazioni
L&#39;obiettivo finale è una semplice applicazione per la traduzione di testo nel terminale. Il testo può essere generato in modo interattivo o programmatico nell&#39;ambiente della shell. Tramite gli argomenti della riga di comando, i descrittori di file o le pipe che generano l&#39;output tradotto che può essere reindirizzato a un file o visualizzato sul terminale.

<b>Inoltre, puoi consultare la nostra libreria aggiuntiva con Google Cloud API</b>

https://pypi.org/project/google-api-translate/


### Caratteristiche
* Realizzato per Python 3, ma funziona ancora su Python 2
* Veloce e facile da installare, facile da usare
* Supporta la traduzione da qualsiasi lingua
* Interfaccia altamente componibile, la potenza dei tubi e dei filtri Unix.
* API e documentazione semplici

### Caldo da installare

```sh
pip3 install py_translator==2.1.9
```


### Come usare
```python
from py_translator import Translator
s = Translator().translate(text='Hello my friend', dest='es').text
print(s)
```

### Con proxy
```python
from py_translator import Translator
proxy = {
        'http': 'http://username:password@1.1.1.1:1234',
        'https': 'http://username:password@1.1.1.1:1234',
}
s = Translator(proxies=proxy).translate(text='Hello my friend', dest='es').text
print(s)
```

### Conchiglia
```shell
translate [--flags] [source] dest
```


# traduzione HTML

### Python
```python
from py_translator import TEXTLIB
s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

### Con proxy
```python
from py_translator import TEXTLIB
proxy = [
    'http://username:password@1.1.1.1:1234',
    'http://username:password@1.1.1.1:1234',
]

s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=proxy)
print(s)
```

### Con il multithreading
```python
from py_translator import TEXTLIB

#with massTranslator()
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

--------
# Esempi
Ciao mondo dall&#39;inglese al cinese tradizionale
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

### Rilevamento intelligente della lingua
L&#39;omissione della lingua di partenza proverà a rilevarla in base al contenuto del testo
```sh
$ translate fr <<< 'I think therefore I am'
Je pense donc je suis
```


### Traslitterazione romanificata
```sh
$ translate --translit en ko <<< 'Want to fight!'
ssaugo sip-eo!

$ translate --translit en zh-TW <<< 'Kidding, we should be friends'
Kāiwánxiào, wǒmen yīnggāi shì péngyǒu
```


### Reindirizza dal file
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

### Incatenare i tubi
```sh
#Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### Essere creativo!
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

# Supporto
Python 3

# Documentazione
Trova la documentazione più recente http://pythonhosted.org/py-translate/


---

<p align="center"><b>🛠️ Questo repository è stato creato usando <a href="https://gitupload.com">GitUpload</a>.</b></p>