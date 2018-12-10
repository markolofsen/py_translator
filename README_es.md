<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://kupi.net"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_es.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README_de.md">🇩🇪 Deutsch</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README.md">🇬🇧 English</a> | <b>🇪🇸 Spanish</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

Versión = 2.1.5 <br />
Nombre de la biblioteca = py_translator <br />
Título = Free Google Translate API <br />
Palabras clave = Google API Cloud Translate, google api translate free <br />

### Info
El objetivo final es una aplicación sencilla para traducir texto en el terminal. El texto se puede generar de forma interactiva o programática en el entorno de shell. A través de la línea de comandos, los descriptores de archivos o los conductos generan resultados traducidos que se pueden canalizar a un archivo o mostrar en el terminal.

<b>Además, puede consultar nuestra biblioteca adicional con Google Cloud API</b>

https://pypi.org/project/google-api-translate/


### Caracteristicas
* Hecho para Python 3 pero aún funciona en Python 2
* Rápido y fácil de instalar, fácil de usar
* Soporta la traducción de cualquier idioma.
* Interfaz altamente componible, el poder de las tuberías y filtros Unix.
* API simple y documentación.

### Caliente para instalar

```sh
pip3 install py_translator==2.1.5
```


### Cómo utilizar
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

### Cáscara
```shell
translate [--flags] [source] dest
```


# traducción html

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

### con multiproceso
```python
from py_translator import TEXTLIB

#with massTranslator()
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

--------
# Ejemplos
Hola mundo de inglés a chino tradicional
```sh
$ translate en zh-TW <<< 'Hello World!'
你好世界！
Just as easily specify a source language by providing it as first argument
```

(dieciséis)]

### Detección inteligente de lenguaje
La omisión del idioma de origen intentará detectarlo en función del contenido del texto
```sh
$ translate fr <<< 'I think therefore I am'
Je pense donc je suis
```


### Transliteración romanificada
```sh
$ translate --translit en ko <<< 'Want to fight!'
ssaugo sip-eo!

$ translate --translit en zh-TW <<< 'Kidding, we should be friends'
Kāiwánxiào, wǒmen yīnggāi shì péngyǒu
```


### Redirigir desde archivo
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

### Encadenando tuberías
```sh
#Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### ¡Ser creativo!
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

# Soporte
Aquí hay una lista de plataformas Python que son oficialmente compatibles.
Python 3

---

<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>