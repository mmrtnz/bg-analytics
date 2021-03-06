#!/usr/bin/python3

import requests
from xml.etree import ElementTree

baseURL = "http://www.boardgamegeek.com/xmlapi2/"
headers = { 'Content-Type': 'text/xml; charset="UTF-8"' }

def search(name):
    transformNodeData = lambda n: {
        'id': n.get('id'),
        'name': n.find('name').get('value'),
        'year': n.find('yearpublished').get('value'),
    }
    query = baseURL + "search?exact=1&query=" + name.replace(' ', '+')
    response = requests.get(query, headers=headers)
    
    if response.status_code == 500 or not response.ok:
        return { 
            'hasError': True,
            'results': None
        }
    else:
        root = ElementTree.fromstring(response.content)
        # Excludes things like expansions, accessories, apps, etc. from search results 
        nodes = root.findall("./item/[@type='boardgame']")
        # Convert xml objects to python objects with minimal data
        results = list(map(transformNodeData, nodes))
        return { 
            'hasError': False,
            'results': results
        }


def lookUpGameById(id):
    query = baseURL + "thing?id=" + str(id)
    response = requests.get(query, headers=headers)
    if response.status_code == 500 or not response.ok:
        return { 
            'hasError': True,
            'id': id,
            'mechanics': None
        }
    else:
        root = ElementTree.fromstring(response.content)
        # Get mechanics of game using xpath notation
        # There will always be only one child because we're searching with a specific id
        nodes = root.findall("./item/link[@type='boardgamemechanic']")
        # Convert list of xml node objects into list of strings
        mechanics = list(map(lambda m: m.get('value'), nodes))
        return {
            'hasError': False,
            'id': id,
            'mechanics': mechanics
        }
