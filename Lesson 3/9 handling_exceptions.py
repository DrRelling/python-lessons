def divide(x):
    try:
        result = 10 / x
        print(result)
        return result
    except ZeroDivisionError:
        print("That's never going to work, you can't divide by zero")

divide(1)
divide(20)
divide(0)

input()

try:
    unassignedVariable * 2
    1 / 0
except ZeroDivisionError:
    print("That's never going to work, you can't divide by zero")
except NameError:
    print("No")