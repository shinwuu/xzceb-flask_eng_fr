"""
Sinsandra Nov 1/2/2023
Python for AI & Application Development Final Project
translator.py module
doc-string
"""
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
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Add function englishToFrench which takes englishTExt as a string argument'''
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2))
    return french_text['translations'][0]['translation']
    

def french_to_english(french_text):
    '''Add function frenchToEnglish which takes in the frenchText as a string argument'''
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2))
    return english_text['translations'][0]['translation']
