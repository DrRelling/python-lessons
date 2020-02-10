import random

people = ["Alice", "Bob", "Carol", "David"]

print(random.choice(people))
print(random.choice(people))
print(random.choice(people))

print(people[random.randint(0, len(people) - 1)])

input()

print("Unshuffled:", people)

random.shuffle(people)

print("Shuffled:  ", people)