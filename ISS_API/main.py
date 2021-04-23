import requests
import json
response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
key = 's'
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

print("Current ISS information")
while True:
    obj = response.json()
    obj = jprint(obj)
    print(obj)
    print("Press x to stop the program or s to retrieve information from ISS again")
    key = input()
    if key == 'x':
        break

