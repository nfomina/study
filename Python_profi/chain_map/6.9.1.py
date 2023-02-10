from collections import ChainMap
import json

with open('zoo.json') as file:
    print(sum(ChainMap(*json.loads(file.read())).values()))
