<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>
<p align="center"><a href="https://kupi.net"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_de.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><b>🇩🇪 Deutsch</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README.md">🇬🇧 English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Version = 2.1.5 <br />
Bibliotheksname = py_translator <br />
Titel = Free Google Translate API <br />
Schlüsselwörter = Google API Cloud Translate, google api translate free <br />

### Info
Das Endziel ist eine einfache Anwendung zum Übersetzen von Text im Terminal. Text kann interaktiv oder programmgesteuert in der Shell-Umgebung generiert werden. Über Befehlszeilenargumente, Dateideskriptoren oder Pipes werden übersetzte Ausgaben generiert, die in eine Datei geleitet oder auf dem Terminal angezeigt werden können.

<b>Sie können auch unsere zusätzliche Bibliothek mit der Google Cloud-API überprüfen</b>

https://pypi.org/project/google-api-translate/


### Eigenschaften
* Für Python 3 gemacht, funktioniert aber immer noch mit Python 2
* Schnell und einfach zu installieren, einfach zu bedienen
* Unterstützt Übersetzungen aus jeder Sprache
* Hochkomposierbare Schnittstelle, die Leistung von Unix-Pipes und -Filtern.
* Einfache API und Dokumentation

### Heiß zu installieren

```sh
pip3 install py_translator==2.1.5
```


### Wie benutzt man
```python
from py_translator import Translator
s = Translator().translate(text='Hello my friend', dest='es').text
print(s)
```

### Mit Proxy
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


# HTML-Übersetzung

### Python
```python
from py_translator import TEXTLIB
s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

### Mit Proxy
```python
from py_translator import TEXTLIB
proxy = [
    'http://username:password@1.1.1.1:1234',
    'http://username:password@1.1.1.1:1234',
]

s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=proxy)
print(s)
```

### Mit Multithreading
```python
from py_translator import TEXTLIB

#with massTranslator()
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

--------
# Beispiele
Hallo Welt vom Englischen zum Traditionellen Chinesisch
(fünfzehn)]

```sh
#Translate Hello from French to English
$ translate fr en <<< 'Bonjour, comment allez-vous!'
Hello, how are you?
```

### Intelligente Spracherkennung
Wenn Sie die Ausgangssprache nicht angeben, wird versucht, sie anhand des Textinhalts zu ermitteln
```sh
$ translate fr <<< 'I think therefore I am'
Je pense donc je suis
```


### Romanifizierte Transliteration
```sh
$ translate --translit en ko <<< 'Want to fight!'
ssaugo sip-eo!

$ translate --translit en zh-TW <<< 'Kidding, we should be friends'
Kāiwánxiào, wǒmen yīnggāi shì péngyǒu
```


### Umleitung von Datei
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

### Verketten von Rohren
```sh
#Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### Seien Sie kreativ!
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

# Unterstützung
Hier ist eine Liste von Python-Plattformen, die offiziell unterstützt werden.
Python 3

---

<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>