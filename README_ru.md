<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://kupi.net"><img src="https://github.com/markolofsen/py_translator//blob/master/.banners/banner_ru.png?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/py_translator/blob/master/README_de.md">🇩🇪 Deutsch</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README.md">🇬🇧 English</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_es.md">🇪🇸 Spanish</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_fr.md">🇫🇷 French</a> | <a href="https://github.com/markolofsen/py_translator/blob/master/README_it.md">🇮🇹 Italian</a> | <b>🇷🇺 Russian</b></p>

---

Версия = 2.1.5 <br />
Название библиотеки = py_translator <br />
Название = Free Google Translate API <br />
Ключевые слова = Google API Cloud Translate, google api translate free <br />

### Информация
Конечная цель - простое приложение для перевода текста в терминале. Текст может быть сгенерирован интерактивно или программно в среде оболочки. Посредством аргументов командной строки, файловых дескрипторов или каналов, генерирующих переведенный вывод, который может быть передан в файл или отображен на терминале.

<b>Кроме того, вы можете проверить нашу дополнительную библиотеку с Google Cloud API</b>

https://pypi.org/project/google-api-translate/


### Характеристики
* Сделано для Python 3, но все еще работает на Python 2
* Быстрый и простой в установке, простой в использовании
* Поддерживает перевод с любого языка
* Композитный интерфейс, мощь Unix-каналов и фильтров.
* Простой API и документация

### Горячая установка

```sh
pip3 install py_translator==2.1.5
```


### Как пользоваться
```python
from py_translator import Translator
s = Translator().translate(text='Hello my friend', dest='es').text
print(s)
```

### с прокси
```python
from py_translator import Translator
proxy = {
        'http': 'http://username:password@1.1.1.1:1234',
        'https': 'http://username:password@1.1.1.1:1234',
}
s = Translator(proxies=proxy).translate(text='Hello my friend', dest='es').text
print(s)
```

### Ракушка
```shell
translate [--flags] [source] dest
```


# перевод html

### Питон
```python
from py_translator import TEXTLIB
s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

### с прокси
```python
from py_translator import TEXTLIB
proxy = [
    'http://username:password@1.1.1.1:1234',
    'http://username:password@1.1.1.1:1234',
]

s = TEXTLIB().translator(is_html=False, text='Hello my friend', lang_to='cn', proxy=proxy)
print(s)
```

### с многопоточностью
```python
from py_translator import TEXTLIB

#with massTranslator()
s = TEXTLIB().massTranslator(is_html=False, text='Hello my friend', lang_to='cn', proxy=False)
print(s)
```

--------
# Примеры
Hello World с английского на традиционный китайский
```sh
$ translate en zh-TW <<< 'Hello World!'
你好世界！
Just as easily specify a source language by providing it as first argument
```

```sh
#Translate Hello from French to English
$ translate fr en <<< 'Bonjour, comment allez-vous!'
Hello, how are you?
```

### Smart Language Detection
Пропустив исходный язык, постараюсь обнаружить его на основе текстового содержимого.
```sh
$ translate fr <<< 'I think therefore I am'
Je pense donc je suis
```


### Романизированная транслитерация
```sh
$ translate --translit en ko <<< 'Want to fight!'
ssaugo sip-eo!

$ translate --translit en zh-TW <<< 'Kidding, we should be friends'
Kāiwánxiào, wǒmen yīnggāi shì péngyǒu
```


### Перенаправление из файла
```sh
$ translate zh-TW < 'alice.txt'

阿麗思道：「你不是說你要告訴你的歷史嗎？告訴我你為甚麼恨—那個—那些—C和D，」
她末了兩個字母輕輕兒地說的，怕回來又得罪了牠。

那老鼠對著阿麗思嘆了一口氣道，「唉﹗我的身世說來可真是又長又苦又委屈呀—」

阿麗思聽了，瞧著那老鼠的尾巴說，「你這尾是曲啊﹗可是為甚麼又叫它苦呢﹗」
她就一頭聽著那老鼠說話，一頭在在心上納悶，所以她聽的那老鼠講的「尾曲」
的歷史是差不多像這個樣了的
....
```

### Цепные трубы
```sh
#Multiple Chaining
$ echo 'What is love?' | translate en zh-TW | translate zh-TW ko | translate ko fr | translate fr en
What is love?
```

### Будь креативным!
```sh
#Grocery List
$ cat << BUY | translate ko
Celery
Milk
Eggs
Bread
Cereal
BUY

셀러리
우유
달걀
빵
시리얼
```

# Служба поддержки
Вот список платформ Python, которые официально поддерживаются.
Python 3

---

<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="https://gitupload.com">GitUpload</a>.</b></p>