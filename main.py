#!/usr/bin/python3

from api import search, lookUpGameById

# results = lookUpGameById(110327)
# print(results['mechanics'])

results = search('Secret Hitler')
print(results)
