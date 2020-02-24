print("Basic dictionary")

myPet = {"size": "short", "species": "royal", "intelligence": "stupid"}

print(myPet["species"])

input()

print("Dictionary with numbers as keys")

myPet = {1: "short", 5: "royal", 2: "stupid"}

print(myPet[2])

input()

print("Dictionary with strange keys")

key = "species"

myPet = {None: "short", key: "royal", True: "stupid"}

print(myPet[None])
print(myPet[key])
print(myPet["species"])
print(myPet[True])