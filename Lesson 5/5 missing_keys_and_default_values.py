import sys

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

try:
    birthdays["Dave"]
except:
    print(sys.exc_info())

input()

print("Do we have a birthday for Dave?", "Dave" in birthdays)

davesBirthday = birthdays.get("Dave", "Can't find a birthday for Dave, sorry")
print(davesBirthday)

input()

quote = "'What?' - Richard Nixon"
letterCountDict = {}

for character in quote:
    if character not in letterCountDict:
        letterCountDict[character] = 1
    else:
        letterCountDict[character] += 1

print(letterCountDict)

input()

quote = "GARCIN (enters, accompanied by the VALET, and glances around him): So here we are?"
letterCountDict = {}

for character in quote:
    letterCountDict.setdefault(character, 0)
    letterCountDict[character] += 1

print(letterCountDict)