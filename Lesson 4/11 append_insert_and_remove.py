animals = ["badger", "cat"]

animals.append("dog")

print(animals)

input()

animals.append(["elephant", "fox"])

print(animals)

input()


animals.insert(0, "aardvark")

print(animals)

animals.insert(2, "cow")

print(animals)

input()


animals.remove("cow")

print(animals)

input()

try:
    animals.remove(["elephant", "fox"])
except AttributeError:
    print("Can't find that value in the list")

print(animals)

input()


x = [1,2,3]
x += x
print(x)

input()

y = [1,2,3]
y.append(y)
print(y)
print(y[3])
print(y[3][3])
print(y[3][3][3][3][3][3][3][3][3][3])






