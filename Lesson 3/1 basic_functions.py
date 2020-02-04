import datetime

def exampleFunction():
    print("This is an example function.")
    print("The time now is " + str(datetime.datetime.now()))
    print("Exciting, huh?")

exampleFunction()

exampleFunction()

exampleFunction()

input()

###############################################
# Define, Call, Pass, Parameter, Argument

def exampleFunction2(x):
    print("You passed in the value " + str(x) + " as an argument for parameter x")

exampleFunction2("Hello world")
exampleFunction2(42)

input()

###############################################

def xTimesY(x, y):
    return x * y

z = xTimesY(5, 10)
print(z)

input()

xTimesY(2, 10)

input()

##############################################

def functionThatReturnsHalfway(x):
    print("Doing something.")
    if x % 2 == 0:
        print("Bored now! Returning early")
        return
    if x % 3 == 0:
        print("x is divisible by 3. Returning the value")
        return x
    print("Still doing something")
    print("Done, returning None")
    # implied "return None" here