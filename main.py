import json
from typing import Final
import requests
import os



# Contstants
BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = os.environ['EXCHANGE_RATE_API_KEY']



def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)
        
    payload: dict = {'access_key': API_KEY}
    request = requests.ge(url=BASE_URL, params=payload)
    data: dict = request.json()

    with open('rates.json', 'w') as file:
        json.dump(data, file)
    

    return data


get_rates()