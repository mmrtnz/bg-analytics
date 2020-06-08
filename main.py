#!/usr/bin/python3

from api import search, lookUpGameById
from chord import Chord

class BoardGame:
    def __init__(self, id, name, mechanics=[]):
        self.id = id
        self.name = name
        self.mechanics = mechanics
    def __str__(self):
        return 'id: {0}\tname: {1}\nmechanics: {2}'.format(self.id, self.name, self.mechanics)


# Cache board game data so we don't have to call the API many times
myBoardGames = [
    BoardGame(188834, 'Secret Hitler', ['Hidden Roles', 'Player Elimination', 'Team-Based Game', 'Traitor Game', 'Voting']),
    BoardGame(161936, 'Pandemic Legacy: Season 1', ['Action Points', 'Cooperative Game', 'Hand Management', 'Legacy Game', 'Point to Point Movement', 'Set Collection', 'Trading', 'Variable Player Powers']),
    BoardGame(218603, 'Photosynthesis', ['Action Points']),
    BoardGame(143519, 'Quantum', ['Area Majority / Influence', 'Dice Rolling', 'Grid Movement', 'Modular Board', 'Square Grid']),
    BoardGame(123540, 'Tokaido', ['Point to Point Movement', 'Set Collection', 'Time Track', 'Variable Player Powers']),
    BoardGame(164840, 'Monopoly Deal', ['Hand Management', 'Set Collection', 'Take That']),
    BoardGame(172225, 'Exploding Kittens', ['Hand Management', 'Hot Potato', 'Player Elimination', 'Push Your Luck', 'Set Collection', 'Take That']),
    BoardGame(1198, 'Set', ['Pattern Recognition', 'Set Collection']),
    BoardGame(9220, 'Saboteur', ['Hand Management', 'Map Addition', 'Network and Route Building', 'Take That', 'Team-Based Game', 'Traitor Game']),
    # BoardGame(178900, 'Codenames', ['Communication Limits', 'Memory', 'Push Your Luck', 'Team-Based Game']),
    # BoardGame(230802, 'Azul', ['Drafting', 'End Game Bonuses', 'Pattern Building', 'Set Collection', 'Tile Placement', 'Turn Order: Claim Action']),
    # BoardGame(46213, 'Telestrations', ['Paper-and-Pencil']),
    # BoardGame(13, 'The Settlers of Catan', ['Dice Rolling', 'Hexagon Grid', 'Income', 'Modular Board', 'Network and Route Building', 'Race', 'Random Production', 'Trading', 'Variable Setup']),
    # BoardGame(167791, 'Terraforming Mars', ['Card Drafting', 'End Game Bonuses', 'Hand Management', 'Hexagon Grid', 'Income', 'Set Collection', 'Solo / Solitaire Game', 'Take That', 'Tile Placement', 'Turn Order: Progressive', 'Variable Player Powers']),
    # BoardGame(113924, 'Zombicide', ['Action Points', 'Cooperative Game', 'Dice Rolling', 'Grid Movement', 'Hand Management', 'Modular Board', 'Player Elimination', 'Scenario / Mission / Campaign Game', 'Variable Player Powers']),
    # BoardGame(110327, 'Lords of Waterdeep', ['Card Drafting', 'Contracts', 'Hidden Roles', 'Increase Value of Unchosen Resources', 'Ownership', 'Set Collection', 'Take That', 'Turn Order: Claim Action', 'Worker Placement']),
]

# Get mechanics for each board game
# Note: I only did this once in order to cache the results
# def getBoardGameData():
#     for game in myBoardGames:
#         data = lookUpGameById(game.id)
#         if data['hasError'] == False:
#             game.mechanics = data['mechanics']

uniqueMechanics = set()
for game in myBoardGames:
    for m in game.mechanics:
        uniqueMechanics.add(m)

# Alphabetize and cast to make uniqueMechanics orderd
uniqueMechanics = list(sorted(uniqueMechanics))
n = len(uniqueMechanics)

# Create an empty square 2D array of zeros
# A more readable approach would have been [[0] * n] * n, but that copies the same reference
matrix = [[0 for j in range(n)] for i in range(n)]

# Count every pairing
for game in myBoardGames:
    mechanics = game.mechanics
    for mechanicA in mechanics:
        for mechanicB in mechanics:
            i = uniqueMechanics.index(mechanicA)
            j = uniqueMechanics.index(mechanicB)
            if i != j:
                matrix[i][j] += 1

Chord(matrix, uniqueMechanics).to_html()