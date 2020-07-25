import json
import requests

url = "https://api.github.com/events"
# Using the request library to grab some data for further use:
r = requests.get(url)

r.encoding = 'ISO-8859-1'
path = r'Insert\your\path'

with open(fr"{path}\sample.json", "w") as outfile:
    json.dump(r.json(), outfile)
