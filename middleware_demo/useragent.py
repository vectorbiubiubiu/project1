#encoding: utf-8

# requests:
# pip install requests

import requests

headers = {
    'User-Agent': ''
}

response = requests.get('http://127.0.0.1:8000/')
print(response.text)