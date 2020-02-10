x = 10
y = x
y = 2000

print("X", x)
print("Y", y)

input()


originalList = [1, 2, 3]
newList = originalList
newList[0] = "Hello world"

print("Original list", originalList)
print("New list     ", newList)

input()


import copy

originalList = [1, 2, 3]
newList = copy.deepcopy(originalList)
newList[2] = "Hello world"

print("Original list", originalList)
print("New list     ", newList)

input()

originalList = [1, 2, 3]
newList = originalList[:]
newList[0] = "Hello world"

print("Original list", originalList)
print("New list     ", newList)

input()


originalList = [1, 2, [3, 4, 5]]
newList = originalList[:]
newList[2][0] = "Hello world"

print("Original list", originalList)
print("New list     ", newList)

input()

originalList = [1, 2, [3, 4, 5]]
newList = copy.deepcopy(originalList)
newList[2][0] = "Hello world"

print("Original list", originalList)
print("New list     ", newList)




