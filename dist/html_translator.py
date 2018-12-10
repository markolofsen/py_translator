# from googletrans import Translator
# from py_translator import Translator
from .client import Translator
from bs4 import BeautifulSoup
from langdetect import detect

import threading, time, re, html
import random


MAX_TEXT_SIZE = 3000
ROTATING_PROXY_LIST = [
    # 'http://username:password@1.1.1.1:1234'
]

def getProxy():
    p = random.choice(ROTATING_PROXY_LIST)
    return {
        'http': p,
        'https': p,
    }

def setProxy(arr):
    global ROTATING_PROXY_LIST
    if arr and len(arr) > 0:
        ROTATING_PROXY_LIST = arr


def helperReplace(text):
    text = re.sub('биткойн',',биткоин', text, flags=re.IGNORECASE)

    return text


class massTranslator():

    iterator = 0
    is_html = False

    def threadTranslate(self, text, text_arr):

        text = helperReplace(text)

        def trans(item, index):
            if self.is_html:
                text_arr[index]['text'] = superTranslator().html(text=text, lang_to=item['lang'])
            else:
                text_arr[index]['text'] = superTranslator().text(text=text, lang_to=item['lang'])

            self.iterator += 1

        for index, item in enumerate(text_arr):
            threading.Thread(target=trans, args=(item, index,)).start()

        while self.iterator < len(text_arr):
            time.sleep(1)

        return text_arr


    def text(self, text, langs_arr):

        text_arr = [{'lang': lang, 'text': False} for lang in langs_arr]
        return self.threadTranslate(text, text_arr)


    def html(self, text, langs_arr):

        self.is_html = True
        text_arr = [{'lang': lang, 'text': False} for lang in langs_arr]

        return self.threadTranslate(text, text_arr)


class superTranslator():

    vars_arr = []
    tags_arr = []

    # BLOCK TRANSLATOR
    class multiTranslator:
        iterator = 0

        def blocks(self, text_arr, lang_to):
            def trans(text, index):
                if len(ROTATING_PROXY_LIST) > 0:
                    text_arr[index] = Translator(proxies=getProxy()).translate(text, dest=lang_to).text
                else:
                    text_arr[index] = Translator().translate(text, dest=lang_to).text
                self.iterator += 1

            for index, line in enumerate(text_arr):
                # trans(line, index)
                threading.Thread(target=trans, args=(line, index,)).start()

            while self.iterator < len(text_arr):
                time.sleep(1)

            return text_arr



    # REPLACE VARS BY NUMBERS
    def varRaplacer(self, direction, text):

        if direction == 'in':
            self.vars_arr = re.findall('\[.+?\]', text)

        for i, var in enumerate(self.vars_arr):
            if direction == 'in':
                text = text.replace(var, '({})'.format(i))
            elif direction == 'out':
                text_tmp = text.replace('（', '(').replace('）', ')')
                text_tmp = re.sub('\(.+?\)', lambda x: x.group(0).replace(' ',''), text_tmp)
                text = text.replace('({})'.format(i), var)

        return text


    # Hack for chinese language
    def langDetect(self, lang_to):
        return 'zh-CN' if lang_to == 'cn' else lang_to

    def text(self, text, lang_to):

        lang_to = self.langDetect(lang_to)
        try:
            if detect(text) == lang_to:
                return text
        except:
            pass

        # REPLACE VARS BY NUMBERS
        text = self.varRaplacer(direction='in', text=text)
        text = helperReplace(text)

        text_arr_tmp = []

        # SPLIT TEXT TO BLOCKS
        text_arr = text.splitlines()
        tmp = ''
        for i, t in enumerate(text_arr):
            tmp += t + '\r\n'
            if len(tmp) > MAX_TEXT_SIZE or i == len(text_arr) - 1:
                text_arr_tmp.append(tmp)
                tmp = ''


        text_arr_tmp = self.multiTranslator().blocks(text_arr=text_arr_tmp, lang_to=lang_to)


        # REPLACE VARS BY NUMBERS
        text = '\r\n'.join(text_arr_tmp)
        text = self.varRaplacer(direction='out', text=text)

        return text

    def tagsReplacer(self, direction, text):
        if direction == 'in':
            self.tags_arr = re.findall('<a .+?</a>|<img.+?>|<iframe.+?>|<script.+?script>', text)

        for i, link in enumerate(self.tags_arr):
            if direction == 'in':
                text = re.sub(link, '(111{})'.format(i), text)
            elif direction == 'out':
                text_tmp = text.replace('（', '(').replace('）', ')')
                text_tmp = re.sub('\(.+?\)', lambda x: x.group(0).replace(' ', ''), text_tmp)
                text = re.sub('\(111{}\)'.format(i), link, text_tmp)

        return text


    # def linksRaplacer_old(self, direction, text, nofollow_domain):
    #
    #     if direction == 'out':
    #         links_arr = re.findall('<a.+?>', text)
    #         for i, link in enumerate(links_arr):
    #             match = re.search("(?P<url>https?://[^\s]+)", link)
    #             if match is not None:
    #                 newlink = match.group("url")
    #                 newlink = re.sub('["”<>]','',newlink)
    #                 for word in ['target']:
    #                     newlink = re.sub(word, '', newlink)
    #
    #                 if nofollow_domain and nofollow_domain in newlink:
    #                     text = re.sub(link, '<a href="{}">'.format(newlink), text)
    #                 else:
    #                     text = re.sub(link, '<a href="{}" rel="nofollow">'.format(newlink), text)
    #
    #     return text


    def html(self, text, lang_to):

        lang_to = self.langDetect(lang_to)
        try:
            if detect(text) == lang_to:
                return text
        except:
            pass

        def htmlPrettify(text, strip=False):
            soup = BeautifulSoup(text, "lxml")
            result = soup.prettify()
            result = re.sub('<.*?html>', '', result)
            result = re.sub('<.*?body>', '', result)
            # result = re.sub(r"([\n ])\1*", r"\1", result)

            if strip:
                result = '\r\n'.join([r.strip() for r in result.splitlines() if len(r) > 1])

            return result


        # REPLACE VARS BY NUMBERS
        text = self.varRaplacer(direction='in', text=text)
        text = self.tagsReplacer(direction='in', text=text)

        # SPLIT TEXT BY TAGS
        text = htmlPrettify(text=text, strip=True)
        text_arr_tmp = []
        text_arr = text.splitlines()
        tmp = ''
        for i, t in enumerate(text_arr):
            tmp += ' {} '.format(t)
            if len(tmp) > MAX_TEXT_SIZE or i == len(text_arr) - 1:
                text_arr_tmp.append(tmp)
                tmp = ''

        text_arr_tmp = self.multiTranslator().blocks(text_arr=text_arr_tmp, lang_to=lang_to)

        # RECOVER TAGS AFTER TRANSLATION
        text = ' '.join(text_arr_tmp)
        text = re.sub('<.+?>', lambda x: x.group(0).lower(), text)
        text = re.sub('&.+?;', lambda x: html.unescape(x.group(0).replace(' ', '').lower()) if len(x.group(0)) < 10 else x.group(0), text)
        text = text.replace('< ', '<').replace(' >', '>').replace('</ ', '</')
        text = text.replace('р>', 'p>').replace('<p> </p>', '<p>&nbsp;</p>')
        text = htmlPrettify(text=text, strip=True) #hack for correct html after translation
        text = ' '.join([c for c in text.splitlines()])
        text = text.replace('<p> </p>', '<p>&nbsp;</p>')

        text = self.tagsReplacer(direction='out', text=text)
        # text = self.varRaplacer(direction='out', text=text)

        # text = htmlPrettify(text=text, strip=False)

        # print('*'*100)
        # print(text)

        return text




if __name__ == "__main__":
    text = '''
        <blockquote>
        <p>Напомним, что не так давно власти ——[sitename]—— начали регулировать деятельность незаконных ICO, а функции регулятора были переданы в <a href="https://en.wikipedia.org/wiki/U.S._Securities_and_Exchange_Commission" target="_blank">SEC</a> (комиссия по ценным бумагам и биржам США).</p>
        </blockquote>
        <a href="/adsf/a/sdfasdf" taget="_blank">asdasd</a>
        <p>Инвесторы обменивали свои [sitename] <br />деньги <b>на</b> валюты BitConnect, которая по мнению компании должна была вернуть хорошие дивиденды своим инвесторам.</p>
        <iframe src="cool" />
        <p>&nbsp;</p>
        <p> </p>
        <p><img alt="Купить Bitcoin онлайн" src="/media/uploads/admin/bitconnect_sec.png" style="width:100%" /></p>
    '''

    # print(superTranslator().html(text=text, lang_to='cn'))

    demotext = 'Это мой текст который надо перевести'

    lang_to_arr = ['ru','en','fr']
    p = massTranslator().html(text=demotext, langs_arr=lang_to_arr)
    print(p)