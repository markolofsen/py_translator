import google.cloud.translate as translate
import os, json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Translator(object):

    translate_client = False

    def __init__(self, private_key, client_email):
        auth_arr = {
            "type": "service_account",
            "project_id": False,
            "private_key_id": False,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": False,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": False
        }

        creds_path = os.path.join(BASE_DIR, 'creds_tmp.json')
        with open(creds_path, 'w') as outfile:
            json.dump(auth_arr, outfile)

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

    def html(self, text='', target_language='en', source_language=False):
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
