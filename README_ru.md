
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">Spanish</a> | <b>Russian</b></p>

---

Привет друг!
Пример переменной для репо: [[any_repo_var]]

Версия = 1.9.3
Название библиотеки = py_translator
Название = Google Translate API (Python 3)
Ключевые слова = Google, Cloude, API

### Горячая установка

```sh
pip3 install py_translator==1.9.3
```


### Как пользоваться

```python
from py_translator import py_translator

private_key = '-----BEGIN PRIVATE KEY----- *********** -----END PRIVATE KEY-----'
client_email = 'starting-account-***********.iam.gserviceaccount.com'

s = py_translator(private_key=private_key, client_email=client_email).translate(text="Hello new world!", target_language='cn')
print(s.text)

```



---

