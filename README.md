<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_en.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><b>English</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

# Enriched library for translating text from the Google Translate API (for Python 3)!

Library version = 2.0.4
Library name = py_translator
Title = Google Translate API (Python 3)
Keywords = Google, Cloude, API

### Hot to install

```sh
pip3 install py_translator==2.0.4
```
                    

## How to use

1. Enable the [Cloud Translation API](https://cloud.google.com/translate/docs/quickstart?csw=1)
2. Download a private key as JSON-file.
3. Specify path to the file in variable "creds_path"

### Sample 1
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

s = Translate(creds_path=creds_path).translate(text="Hello new world!", target_language='cn')
print(s.text)
```

### Sample 2
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

html_str = '<p>Russian word</p>'
s = Translator(creds_path=creds_path).html(text=html_str, target_language='ru')
print(s.text)
```

### Sample 2
```python
from py_translator import TextUtils
s = TextUtils().detect('Detect my language please...')
print(s)
```



### Using any variables without translation? — Easy!
```python
import os
from py_translator import Translator, TextUtils
creds_path = os.path.join(os.path.dirname(__file__), 'creds.json')

text = "Hi, this is [[name]], waiting for $ 1 from you!"
s = Translator(creds_path=creds_path).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

Result: «Привет, это [[name]], жду от тебя $ 1!»


---

