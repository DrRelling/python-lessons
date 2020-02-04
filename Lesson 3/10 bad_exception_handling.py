import sys

def divide(x):
    try:
        result = 10 / x
        return result
    except:
        print(sys.exc_info())
        print("That's never going to work, you can't divide by zero")
        raise sys.exc_info()[1]

divide(10)