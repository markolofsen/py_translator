<p align="center"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_en.png?raw=1" /></p>
<p align="center"><b>Languages:</b><br /><b>English</b> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_ru.md">Russian</a></p>

---

**Enriched library for translating text from the Google Translate API.
**

Version = 1.9.6
Library name = py_translator
Title = Google Translate API (Python 3)
Keywords = Google, Cloude, API

### Hot to install

```sh
pip3 install py_translator==1.9.6
```
                    

## How to use

1. Enable the [Cloud Translation API](https://cloud.google.com/translate/docs/quickstart?csw=1)
2. Download a private key as JSON-file.
3. Copy the variables "private_key" and "client_email" from JSON-file


### Connection example
```python
from py_translator import Translator, TextUtils

private_key = '-----BEGIN PRIVATE KEY----- *********** -----END PRIVATE KEY-----'
client_email = 'starting-account-***********.iam.gserviceaccount.com'
```

### Sample 1
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='cn')
print(s.text)
```

### Sample 2
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
html_str = '<p>Russian word</p>'
s = Translator(private_key=private_key, client_email=client_email).html(text=html_str, target_language='ru')
print(s.text)
```

### Sample 2
```python
from py_translator import TextUtils
s = TextUtils().detect('Detect my language please...')
print(s)
```



### How to use variables that are not translated?
```python
from py_translator import Translator, TextUtils
private_key = "****"
client_email = "****"
text = "Hi, this is [[name]], waiting for $ [[number]] from you!"
s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='ru')
print(s.text)
```

**Result:** "Привет, это [[name]], жду от тебя $ [[number]]!"


---

