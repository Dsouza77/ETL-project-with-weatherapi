import requests
import time
from api import api_key

def get_request(city):
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        paramters = {
            "key":api_key,
            "q":city,
            "lang:":"pt",
            "tz_id":"America/Sao_Paulo"
        }
        response = requests.get(url, params=paramters)
        if response.status_code == 200:
            data = response.json()
            print("[SYSTEM]: Request made and completed successfully.")
            return data
        elif response.status_code == 400:
            print(f"[SYSTEM]: Error code: {response.status_code}, City not found or you didint write the name of any city!")
        else:
            print(f"[SYSTEM]: Request error, code: {response.status_code}")
    except Exception as error:
        print(f"[SYSTEM]: System error, code infor: {error}")
        

