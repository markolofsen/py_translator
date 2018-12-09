import google.cloud.translate as translate
from bs4 import BeautifulSoup
import os, json, re, html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Translator(object):

    translate_client = False

    def __init__(self, creds_path):
        # auth_arr = {
        #     "type": "service_account",
        #     "project_id": False,
        #     "private_key_id": False,
        #     "private_key": private_key,
        #     "client_email": client_email,
        #     "client_id": False,
        #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #     "token_uri": "https://oauth2.googleapis.com/token",
        #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #     "client_x509_cert_url": False
        # }

        # creds_path = os.path.join(BASE_DIR, 'creds_tmp.json')
        # with open(creds_path, 'w') as outfile:
        #     json.dump(auth_arr, outfile)

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path
        self.translate_client = translate.Client()


    def target_language(self, lang):
        if lang == 'cn':
            return 'zh-cn'
        return lang

    def translate(self, text='', target_language='en', source_language=False):
        source_language = source_language if source_language else ''
        target_language = self.target_language(target_language)
        t = self.translate_client.translate(text, target_language=target_language, source_language=source_language)
        detect = self.translate_client.detect_language(text)

        self.all = t
        self.lang = t['detectedSourceLanguage'] if 'detectedSourceLanguage' in t else detect['language']
        trans = t['translatedText'].strip()
        trans = '{}{}'.format(trans[:1].upper(), trans[1:])  # Up first letter
        self.text = trans

        return self



    # *************
    # HTML MAGIC
    # *************

    vars_arr = []
    tags_arr = []


    # REPLACE VARS BY NUMBERS
    def varRaplacer(self, direction, text):

        if direction == 'in':
            self.vars_arr = re.findall('\[.+?\]', text)

        for i, var in enumerate(self.vars_arr):
            if direction == 'in':
                text = text.replace(var, '({})'.format(i))
            elif direction == 'out':
                text_tmp = text.replace('（', '(').replace('）', ')')
                text_tmp = re.sub('\(.+?\)', lambda x: x.group(0).replace(' ', ''), text_tmp)
                text = text.replace('({})'.format(i), var)

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


    def html(self, **kwargs):

        def helperReplace(text):
            text = re.sub('биткойн', ',биткоин', text, flags=re.IGNORECASE)
            return text

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
        text = re.sub('\n', '<br />', kwargs['text'])
        text = self.varRaplacer(direction='in', text=text)


        # TRANSLATION...
        kwargs['text'] = text
        text = self.translate(**kwargs).text


        # BACK REPLACING VARS BY NUMBERS
        text = helperReplace(text)
        text = self.varRaplacer(direction='out', text=text)
        text = re.sub('<br />', '\r\n', text)


        # RECOVER TAGS AFTER TRANSLATION
        # text = re.sub('<.+?>', lambda x: x.group(0).lower(), text)
        # text = re.sub('&.+?;',
        #               lambda x: html.unescape(x.group(0).replace(' ', '').lower()) if len(x.group(0)) < 10 else x.group(
        #                   0), text)
        # text = text.replace('< ', '<').replace(' >', '>').replace('</ ', '</')
        # text = text.replace('р>', 'p>').replace('<p> </p>', '<p>&nbsp;</p>')
        # text = htmlPrettify(text=text, strip=True)  # hack for correct html after translation
        # text = ' '.join([c for c in text.splitlines()])
        # text = text.replace('<p> </p>', '<p>&nbsp;</p>')
        # text = self.tagsReplacer(direction='out', text=text)


        # REMOVE SPACES FROM START
        text = '\r\n'.join([c.strip() for c in text.splitlines()])

        # RESPONSE
        self.text = text
        return self
