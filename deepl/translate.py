import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_auth_key = os.getenv("DEEPL_API_AUTH_KEY")

def translate(text,target_lang):
        #url = "https://api-free.deepl.com/v2/translate"
        url = "https://api.deepl.com/v2/translate"
        data = {
                'auth_key' : api_auth_key,
                'text' : text,
                'target_lang' : target_lang
        }
        response = requests.post(url,data=data)
        #print(response.status_code)
        #print(response.text)
        #print(response.json())

        trans_text = response.json()["translations"][0]["text"]
        return trans_text