import random

people = ["Alice", "Bob", "Carol", "David"]

random.shuffle(people)

print("Shuffled:    ", people)

people.sort()

print("Sorted:      ", people)

people.sort(reverse=True)

print("Reverse sort:", people)

input()

people = ["Alice", "bob", "Carol", "david"]

people.sort()

print(people)

input()

people.sort(key=str.lower)

print(people)


input()

x = [1, 2, 3, "a", "b", "c"]
try:
    x.sort()
except TypeError:
    print("Can't sort numbers and letters as they can't be compared")

input()

x.sort(key=str)
print(x)