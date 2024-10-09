import json
from pprint import pprint
with open("data.json","r") as file:
    data = json.load(file)

print(data)
for key, value in data.items:
    print(key, value)