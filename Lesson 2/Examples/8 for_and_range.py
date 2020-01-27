counter = 0

print("While")
while counter < 5:
    print("Counter=" + str(counter))
    counter += 1

input()

print("For, with a range")
for counter in [0, 1, 2, 3, 4]:
    print("Counter=" + str(counter))

input()

print("For, with a range with a start and stop")
for counter in range(5, 10):
    print("Counter=" + str(counter))

input()

print("For, with a range with a start, stop and step")
for counter in range(5, 10, 2):
    print("Counter=" + str(counter))

input()

print("For, with a range with a start, stop and step, counting backwards")
for counter in range(10, 5, -2):
    print("Counter=" + str(counter))

input()

print("For, with a range which doesn't work")
for counter in range(10, 5, 2):
    print("Counter=" + str(counter))