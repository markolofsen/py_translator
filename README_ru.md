<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_ru.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <b>Russian</b></p>

---

# Расширенная библиотека для перевода текста из Google Translate API.

Версия = 2.0.0
Название библиотеки = py_translator
Название = Google Translate API (Python 3)
Ключевые слова = Google, Cloude, API

### Горячая установка

```sh
pip3 install py_translator==2.0.0
```


## Как пользоваться

1. Включите [Cloud Translation API] (https://cloud.google.com/translate/docs/quickstart?csw=1).
2. Скачать приватный ключ в виде JSON-файла.
3. Укажите путь к файлу в переменной &quot;creds_path&quot;

### Образец 1
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

s = Translate(creds_path=creds_path).translate(text="Hello new world!", target_language='cn')
print(s.text)
```

### Образец 2
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

html_str = '<p>Russian word</p>'
s = Translator(creds_path=creds_path).html(text=html_str, target_language='ru')
print(s.text)
```

### Образец 2
```python
from py_translator import TextUtils
s = TextUtils().detect('Detect my language please...')
print(s)
```



### Использование каких-либо переменных без перевода? - Легко!
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

text = "Hi, this is [[name]], waiting for $ [[number]] from you!"
s = Translator(creds_path=creds_path).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

Результат: «Привет, это [[name]], жду от тебя $ [[number]]!»

---

