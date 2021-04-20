import requests
import json
response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

obj = response.json()
obj = jprint(obj)
print("Current ISS information")
print(obj)

