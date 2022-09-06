import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator)
language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/6f6acd70-d4d2-4c67-a4a2-2fd13c1ee9f1')

def englishtofrench(englishText):
    """Takes english text and translates it to french"""
    #write the code here
    translation = language_translator.translate(
        text= englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    json.dumps(frenchText, indent=2)

    return frenchText



def frenchtoenglish(frenchText):
    """Takes french text and translates it to english"""
    #write the code here
    translation = language_translator.translate(
        text= frenchText,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    json.dumps(englishText, indent=2)
    return englishText
    