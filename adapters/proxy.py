import requests
import json

from config import properties

def relay_request(headers, data):
    url = properties.get('RELAY_URL')
    requests.post(url, json.dumps(data), headers=headers)
