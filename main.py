#!/usr/bin/python3

import requests
from xml.etree import ElementTree

# Define query for API
baseURL = "http://www.boardgamegeek.com/xmlapi2/"
headers = { 'Content-Type': 'text/xml; charset="UTF-8"' }
testQuery = baseURL + "search?query=Lords%20of%20Waterdeep"

# Call the API
response = requests.get(testQuery, headers=headers)

# Show results
if response.status_code == 500 or not response.ok:
    print("There was an error calling the API")

root = ElementTree.fromstring(response.content)

for child in root:
    print(child.tag, child.attrib)
