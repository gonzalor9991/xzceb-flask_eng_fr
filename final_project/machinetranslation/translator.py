import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
"""
This module translates text from English to French and vice versa
"""
load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['URL']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')


class Translator:
    """
    Class that translates text from English to French and vice versa
    """
    def english_to_french(self, text):
        """Translates text from English to French"""
        translation = language_translator.translate(
            text=text,
            model_id='en-fr').get_result()
        return translation['translations'][0]['translation']

    def french_to_english(self, text):
        """Translates text from French to English"""
        translation = language_translator.translate(
            text=text,
            model_id='fr-en').get_result()
        return translation['translations'][0]['translation']
