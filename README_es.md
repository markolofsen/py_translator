
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <b>Spanish</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

¡Hola amigo!
Variable de muestra para repo: [[any_repo_var]]

Versión = 1.9.3
Nombre de la biblioteca = py_translator
Título = Google Translate API (Python 3)
Palabras clave = Google, Cloude, API

### Caliente para instalar

```sh
pip3 install py_translator==1.9.3
```


### Cómo utilizar

```python
from py_translator import py_translator

private_key = '-----BEGIN PRIVATE KEY----- *********** -----END PRIVATE KEY-----'
client_email = 'starting-account-***********.iam.gserviceaccount.com'

s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='cn')
print(s.text)

```



---

