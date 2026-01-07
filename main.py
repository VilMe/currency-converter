import json
from typing import Final
import requests
import os



# Contstants
# BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
# API_KEY: Final[str] = os.environ['EXCHANGE_RATE_API_KEY']



def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)
        
    payload: dict = {'access_key': API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    # had this code to get the rates, then commented out so don't use up API calls
    # with open('rates.json', 'w') as file:
    #     json.dump(data, file)
    

    return data


# made this call with mock = false which is defaults get rates and json dump into file rates.json
# get_rates()

def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'"{currency}" is not a valid currency. maybe you missed a letter or mixed a letter :)')


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)


    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})')


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')

    convert_currency(100, 'USD', 'JPY', rates=rates)

if __name__ == '__main__':
    main()