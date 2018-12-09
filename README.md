<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://kupi.net"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_en.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README_de.md">🇩🇪 Deutsch</a> | <b>🇬🇧 English</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_it.md">🇮🇹 Italian</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">🇷🇺 Russian</a></p>

---

# Enriched library for translating text from the Google Translate API (for Python 3)!

Library version = 2.1.0 <br />
Library name = py_translator <br />
Title = Google Translate API (Python 3) <br />
Keywords = Google, Cloude, API <br />

### Hot to install

```sh
pip3 install py_translator==2.1.0
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

text = "Hi, this is , waiting for $ [[number]] from you!"
s = Translator(creds_path=creds_path).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

Result: «Привет, это , жду от тебя $ [[number]]!»


---

<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>