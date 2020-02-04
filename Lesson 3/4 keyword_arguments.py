print("Hello", end="-")
print("World")

input()

def myFunctionWithKwargs(first=1, second="two", third=False):
    print(first, second, third)

myFunctionWithKwargs()
myFunctionWithKwargs(first=1, second="two", third=True)
myFunctionWithKwargs(1, "two", True)
myFunctionWithKwargs(first=2, second="one")
myFunctionWithKwargs(third=True, first=9)

input()

def myFunctionWithStars(x, *args, y=True):
    print(x)
    print(*args)
    print(y)

myFunctionWithStars(1, 2, 3, 4, 5)