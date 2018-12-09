<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_es.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <b>Spanish</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

# Biblioteca enriquecida para traducir texto de la API de Google Translate.

Versión = 2.0.0
Nombre de la biblioteca = py_translator
Título = Google Translate API (Python 3)
Palabras clave = Google, Cloude, API

### Caliente para instalar

```sh
pip3 install py_translator==2.0.0
```


## Cómo utilizar

1. Habilite el [Cloud Translation API] (https://cloud.google.com/translate/docs/quickstart?csw=1)
2. Descargue una clave privada como archivo JSON.
3. Especifique la ruta al archivo en la variable &quot;creds_path&quot;

### Muestra 1
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

s = Translate(creds_path=creds_path).translate(text="Hello new world!", target_language='cn')
print(s.text)
```

### Muestra 2
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

html_str = '<p>Russian word</p>'
s = Translator(creds_path=creds_path).html(text=html_str, target_language='ru')
print(s.text)
```

### Muestra 2
```python
from py_translator import TextUtils
s = TextUtils().detect('Detect my language please...')
print(s)
```



### ¿Usando alguna variable sin traducción? - fácil!
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

text = "Hi, this is [[name]], waiting for $ [[number]] from you!"
s = Translator(creds_path=creds_path).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

Resultado: «Привет, это [[name]], жду от тебя $ [[number]]!»

---

