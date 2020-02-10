supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for item in supplies:
    print("Item:", item)

input()

for index in range(len(supplies)):
    print("Item", supplies[index], "is at index", index)

input()

for index, item in enumerate(supplies):
    print("Item", item, "is at index", index)

input()

for enumeration in enumerate(supplies):
    print(enumeration)