import requests
import json
from datetime import datetime

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)
print()

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print()

print(response.json())

response = requests.get("http://api.open-notify.org/astros.json")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

parameters = {
    "lat": 40.71,
    "lon": -74
}
print()

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())

print()
pass_times = response.json()['response']
jprint(pass_times)
print()

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
