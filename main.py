import json
from typing import Final
import requests
import os



# Contstants
BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = os.environ['EXCHANGE_RATE_API_KEY']