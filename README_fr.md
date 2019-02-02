<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_fr.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <b>French</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

Version = 2.1.9 <br />
Nom de la bibliothèque = py_translator <br />
Titre = Free Google Translate API <br />
Mots-clés = Google API Cloud Translate, google api translate free <br />

### Info
L&#39;objectif final est une application simple pour traduire du texte dans le terminal. Le texte peut être généré de manière interactive ou par programme dans l&#39;environnement shell. Par le biais d’arguments de ligne de commande, de descripteurs de fichier ou de canaux générant une sortie traduite pouvant être redirigée vers un fichier ou affichée sur le terminal.

<b>Vous pouvez également consulter notre bibliothèque supplémentaire avec Google Cloud API.</b>

https://pypi.org/project/google-api-translate/


### Caractéristiques
* Conçu pour Python 3 mais fonctionne toujours sur Python 2
* Rapide et facile à installer, facile à utiliser
* Prend en charge la traduction de n&#39;importe quelle langue
* Interface hautement composable, la puissance des pipes et filtres Unix.
* API simple et documentation

### Chaud à installer

```sh
pip3 install py_translator==2.1.9
```


### Comment utiliser
```python
from py_translator import Translator
s = Translator().translate(text='Hello my friend', dest='es').text
print(s)
```

### Avec proxy
(dix)]

### Coquille
```shell
translate [--flags] [source] dest
```


traduction html

### Python
```python
from py_translator import TEXTLIB
s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

### Avec proxy
```python
from py_translator import TEXTLIB
proxy = [
    'http://username:password@1.1.1.1:1234',
    'http://username:password@1.1.1.1:1234',
]

s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=proxy)
print(s)
```

### Avec multithreading
```python
from py_translator import TEXTLIB

#with massTranslator()
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

--------
# Exemples
Bonjour tout le monde de l&#39;anglais au chinois traditionnel
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

### Détection intelligente de la langue
L&#39;omission de la langue source tentera de la détecter en fonction du contenu du texte
```sh
$ translate fr <<< 'I think therefore I am'
Je pense donc je suis
```


### Translittération romanifiée
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

### Chaînage de tuyaux
```sh
#Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### Sois créatif!
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

# Soutien
Python 3

# Documentation
Retrouvez la dernière documentation http://pythonhosted.org/py-translate/


---

<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>