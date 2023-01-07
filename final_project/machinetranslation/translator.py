""" translate thing """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-01-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """ translates english text to french text """
    return language_translator.translate(text = englishText, model_id = "en-fr") \
        .get_result() \
        .get("translations")[0] \
        .get("translation")

def frenchToEnglish(frenchText):
    """ translates french text to english text """
    return language_translator.translate(text = frenchText, model_id = "fr-en") \
        .get_result() \
        .get("translations")[0] \
        .get("translation")
