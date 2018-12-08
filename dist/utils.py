from langdetect import detect

class TextUtils(object):

    def detect(self, text):
        if not text:
            return False

        lang = detect(text)
        if lang == 'no':
            return False

        elif lang == 'zh-cn':
            lang = 'cn'

        return lang
