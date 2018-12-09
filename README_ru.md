<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_ru.png?raw=1" /></p><br />
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <b>Russian</b></p><br />
<br />
---<br />
<br />
# Расширенная библиотека для перевода текста из Google Translate API.<br />
<br />
Версия = 2.0.1<br />
Название библиотеки = py_translator<br />
Название = Google Translate API (Python 3)<br />
Ключевые слова = Google, Cloude, API<br />
<br />
### Горячая установка<br />
<br />
```sh<br />
pip3 install py_translator==2.0.1<br />
```<br />
<br />
<br />
## Как пользоваться<br />
<br />
1. Включите [Cloud Translation API] (https://cloud.google.com/translate/docs/quickstart?csw=1).<br />
2. Скачать приватный ключ в виде JSON-файла.<br />
3. Укажите путь к файлу в переменной &quot;creds_path&quot;<br />
<br />
### Образец 1<br />
```python<br />
import os<br />
from py_translator import Translator, TextUtils<br />
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')<br />
<br />
s = Translate(creds_path=creds_path).translate(text="Hello new world!", target_language='cn')<br />
print(s.text)<br />
```<br />
<br />
### Образец 2<br />
```python<br />
import os<br />
from py_translator import Translator, TextUtils<br />
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')<br />
<br />
html_str = '<p>Russian word</p>'<br />
s = Translator(creds_path=creds_path).html(text=html_str, target_language='ru')<br />
print(s.text)<br />
```<br />
<br />
### Образец 2<br />
```python<br />
from py_translator import TextUtils<br />
s = TextUtils().detect('Detect my language please...')<br />
print(s)<br />
```<br />
<br />
<br />
<br />
### Использование каких-либо переменных без перевода? - Легко!<br />
```python<br />
import os<br />
from py_translator import Translator, TextUtils<br />
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')<br />
<br />
text = "Hi, this is [[name]], waiting for $ [[number]] from you!"<br />
s = Translator(creds_path=creds_path).translate(text="Hello new world!", target_language='ru')<br />
print(s.text)<br />
```<br />
<br />
Результат: «Привет, это [[name]], жду от тебя $ [[number]]!»<br />
<br />
---<br />
<br />