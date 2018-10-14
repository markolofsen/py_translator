from .html_translator import superTranslator, massTranslator, setProxy

import re
from slugify import slugify
from langdetect import detect


class TEXTLIB():

    def removeLinksByDomains(self, text, domains_arr):
        for domain in domains_arr:
            text = re.sub('<a[^>]+href=["\'](.*{DOMAIN}.*)["\']>(.+?)</a>'.format(DOMAIN=domain), lambda x: re.search('>(.+?)</', x.group(0)).group(1), text, flags=re.IGNORECASE)
        return text

    def slug(self, text):
        return slugify(text, to_lower=True)

    def detect(self, text):
        if not text:
            return False

        lang = detect(text)
        if lang == 'zh-cn':
            lang = 'cn'
        elif lang == 'no':
            lang = False

        return lang


    def textToHtml(self, text):
        if not text:
            return False
        return '<p>{HTML}</p>'.format(HTML='<br/>'.join(text.splitlines()))


    def translator(self, is_html, text, lang_to, proxy):
        if not text:
            return False

        setProxy(proxy)
        if is_html:
            return superTranslator().html(text, lang_to)
        else:
            return superTranslator().text(text, lang_to)

    def massTranslator(self, is_html, text, langs_arr, proxy):
        if not text:
            return False

        setProxy(proxy)
        if is_html:
            return massTranslator().html(text, langs_arr)
        else:
            return massTranslator().text(text, langs_arr)


if __name__ == '__main__':
    pass

    text = '''
        <blockquote>
        <p>Напомним, что не так давно власти ——[sitename]—— начали регулировать деятельность незаконных ICO., а функции регулятора были переданы в <a href="https://en.wikipedia.org/wiki/U.S._Securities_and_Exchange_Commission" target="_blank">SEC</a> (комиссия по ценным бумагам и биржам США).</p>
        </blockquote>
        <a href="/adsf/a/sdfasdf" taget="_blank">asdasd</a>
        <p>Инвесторы обменивали свои [sitename] <br />деньги <b>на</b> валюты BitConnect, которая по мнению компании должна была вернуть хорошие дивиденды своим инвесторам.</p>
        <iframe src="cool" />
        <p>&nbsp;</p>
        <p> </p>
        <p><img alt="Купить Bitcoin онлайн" src="/media/uploads/admin/bitconnect_sec.png" style="width:100%" /></p>
    '''

    # p = TEXTLIB().crosslinker(text=text, rules=crosslinks_arr)
    # print(p)

    print('*'*100)

    proxy = [
        'http://username:password@1.1.1.1:1234',
        'http://username:password@1.1.1.1:1234',
    ]

    t = TEXTLIB().translator(is_html=True, text=text, lang_to='cn', proxy=proxy)
    print(t)
