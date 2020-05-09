import json
import requests
from main.src.api.config import *


def get(route, query='', headers=''):
    request = API_CONFIG.get('url') + route
    res = requests.get(request, params=query, headers=headers)
    return res
