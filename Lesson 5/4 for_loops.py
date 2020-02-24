myPet = {"size": "short", "species": "royal", "intelligence": "stupid"}

print("For in dictionary keys")
for key in myPet.keys():
    print(key)

print("\nFor in dictionary")
for key in myPet:
    print(key)

input()

print("\nFor in dictionary values")
for value in myPet.values():
    print(value)

input()

print("\nFor in dictionary items (key and value)")
for keyAndValue in myPet.items():
    print(keyAndValue)

input()

print("\nFor in dictionary items with multiple assignment")
for key, value in myPet.items():
    print("Key = " + key + ", value = " + value)