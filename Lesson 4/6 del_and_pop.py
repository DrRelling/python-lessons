spam = ['cat', 'bat', 'rat', 'elephant']

print("Before del:", spam)

del spam[2]

print("After del :", spam)

input()

print("Before pop:  ", spam)

poppedValue = spam.pop()
print("Popped value:", poppedValue)
print("After pop:   ", spam)

poppedValue = spam.pop()
print("Popped value:", poppedValue)
print("After pop:   ", spam)

input()

x = 10

print("X", x)

del x

print(x)
