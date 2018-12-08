<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_ru.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <b>Russian</b></p>

---

Расширенная библиотека для перевода текста из Google Translate API.

Версия = 1.9.5
Название библиотеки = py_translator
Название = Google Translate API (Python 3)
Ключевые слова = Google, Cloude, API

### Горячая установка

```sh
pip3 install py_translator==1.9.5
```


## Как пользоваться

1. Включите [Cloud Translation API] (https://cloud.google.com/translate/docs/quickstart?csw=1).
2. Скачать приватный ключ в виде JSON-файла.
3. Скопируйте переменные &quot;private_key&quot; и &quot;client_email&quot; из JSON-файла


### Пример подключения
```python
from py_translator import Translator, TextUtils

private_key = '-----BEGIN PRIVATE KEY----- *********** -----END PRIVATE KEY-----'
client_email = 'starting-account-***********.iam.gserviceaccount.com'
```

### Образец 1
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='cn')
print(s.text)
```

### Образец 2
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
html_str = '<p>Russian word</p>'
s = Translator(private_key=private_key, client_email=client_email).html(text=html_str, target_language='ru')
print(s.text)
```

### Образец 2
```python
from py_translator import TextUtils
s = TextUtils().detect('Detect my language please...')
print(s)
```



### Как использовать переменные, которые не переведены?
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
text = "Hi, this is [[name]], waiting for $ [[number]] from you!"
s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

** Результат: ** &quot;Привет, это [[name]], жду от тебя $ [[number]]!&quot;

---

