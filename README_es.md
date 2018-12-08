<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_es.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <b>Spanish</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

Biblioteca enriquecida para traducir texto de la API de Google Translate.

Versión = 1.9.5
Nombre de la biblioteca = py_translator
Título = Google Translate API (Python 3)
Palabras clave = Google, Cloude, API

### Caliente para instalar

```sh
pip3 install py_translator==1.9.5
```


## Cómo utilizar

1. Habilite el [Cloud Translation API] (https://cloud.google.com/translate/docs/quickstart?csw=1)
2. Descargue una clave privada como archivo JSON.
3. Copie las variables &quot;private_key&quot; y &quot;client_email&quot; del archivo JSON


### Ejemplo de conexión
```python
from py_translator import Translator, TextUtils

private_key = '-----BEGIN PRIVATE KEY----- *********** -----END PRIVATE KEY-----'
client_email = 'starting-account-***********.iam.gserviceaccount.com'
```

### Muestra 1
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='cn')
print(s.text)
```

### Muestra 2
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
html_str = '<p>Russian word</p>'
s = Translator(private_key=private_key, client_email=client_email).html(text=html_str, target_language='ru')
print(s.text)
```

### Muestra 2
```python
from py_translator import TextUtils
s = TextUtils().detect('Detect my language please...')
print(s)
```



### ¿Cómo usar variables que no están traducidas?
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
text = "Hi, this is [[name]], waiting for $ [[number]] from you!"
s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

** Resultado: ** &quot;Привет, это [[name]], жду от тебя $ [[number]]!&quot;

---

