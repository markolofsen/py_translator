<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_es.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <b>Spanish</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

# Biblioteca enriquecida para traducir texto de la API de Google Translate. Versión = [[VERSIÓN]] Nombre de la biblioteca = py_translator Título = [[TÍTULO]] Palabras clave = [[PALABRAS CLAVE]] ### Instalación rápida [[código_0]] ## Cómo usar 1. Habilitar la [ API de traducción en la nube] (https://cloud.google.com/translate/docs/quickstart?csw=1) 2. Descargue una clave privada como archivo JSON. 3. Copie las variables &quot;private_key&quot; y &quot;client_email&quot; del archivo JSON ### Muestra 1 [[código_1]] ### Muestra 2 [[código_2]] ### Muestra 2 [[código_3]] ### Cómo ¿Usar variables que no están traducidas? ```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

text = "Hi, this is [[name]], waiting for $ [[number]] from you!"
s = Translator(creds_path=creds_path).translate(text="Hello new world!", target_language='ru')
print(s.text)
``` Resultado: &quot;Привет, это [[name]], жду от тебя $ [[number]]!&quot;

---

