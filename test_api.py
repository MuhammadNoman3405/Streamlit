import requests
import json

API_KEY = "5a4cb3067ff4231fd3bee05e5aaa714a"
BASE_URL = "http://api.weatherstack.com/current"

params = {
    "access_key": API_KEY,
    "query": "Taxila, Pakistan",
    "units": "m",
}

print(f"Testing for city: {params['query']}")
try:
    response = requests.get(BASE_URL, params=params)
    print(f"Status Code: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=2))
    except:
        print(f"Raw Response: {response.text}")
except Exception as e:
    print(f"Exception: {e}")
