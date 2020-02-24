import pprint

quote = """
[H]orror and doubt distract
His troubl'd thoughts, and from the bottom stirr
The Hell within him, for within him Hell
He brings
"""

letterCountDict = {}

for character in quote:
    letterCountDict.setdefault(character, 0)
    letterCountDict[character] += 1

pprint.pprint(letterCountDict)