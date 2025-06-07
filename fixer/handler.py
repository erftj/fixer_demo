import requests
import json


url = "http://data.fixer.io/api/latest?access_key=d6448c8eb43b0aacf7c2711a7c775b5a"


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None