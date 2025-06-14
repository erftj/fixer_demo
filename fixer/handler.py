import requests
import json


url = "d6448c8eb43b0aacf7c2711a7c775b5a"
base_path = "https://data.fixer.io/api/latest?access_key="


def get_rates(api_key):
    response = requests.get(base_path + api_key)
    if response.status_code == 200:
        return json.loads(response.text)
    return None
