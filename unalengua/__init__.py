from dataclasses import dataclass
import requests
import ua_generator

_languages = {
    'Spanish': 'es-US',
    'English': 'en-US',
    'Italian': 'it-IT',
    'French': 'fr-FR',
    'Portuguese': 'pt-PT',
    'German': 'de-DE',
    'Romanian': 'ro-RO',
    'Russian': 'ru-RU'
}

_headers = {
    'Host': 'api2.unalengua.com',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://unalengua.com/',
}

@dataclass
class IPA:
    detected: str
    ipa: str
    lang: str
    spelling: str

    def __str__(self):
        return self.ipa

def show_languages():
    """
    Show supported languages.
    """
    return _languages

class Unalengua:
    def __init__(self, lang: str = 'English', user_agent: str = None):
        """
        Class constructor.

        :param lang: Language to use. Default is English.
        :param user_agent: User-Agent to use. Default is random
        """
        self.ua = ua_generator.generate().text if not user_agent else user_agent
        
        if lang not in _languages:
            raise ValueError(f'Language {lang} is not supported.')
        self.lang = _languages[lang]

    def translate(self, text: str) -> IPA:
        """
        Get IPA for a given text.

        :param text: Text to get IPA for.
        """
        _headers['User-Agent'] = self.ua
        response = requests.post(
            'https://api2.unalengua.com/ipav3',
            headers=_headers,
            json={
                'text': text,
                'lang': self.lang,
                'mode': True
            }
        )
        if response.status_code != 200:
            raise Exception(f'Failed to get IPA for {text}.')
        data = response.json()
        return IPA(**data)