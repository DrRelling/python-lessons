while True:
    print("Please enter a number between 1 and 10: ")

    userInput = input()
    userInputInt = int(userInput)

    if (userInputInt >= 1 and userInputInt <= 10):
        print("Thank you! Your number was: " + str(userInputInt))
        break
    else:
        print("RTFM and try again...")


############################################

input()

while True:
    print("Please enter a number between 1 and 10:")
    userInput = input()

    if not userInput.isnumeric():
        print("No, please enter a NUMBER")
        continue

    userInputInt = int(userInput)
    if (userInputInt >= 1 and userInputInt <= 10):
        print("Thank you! Your number was: " + str(userInputInt))
        break
    else:
        print("RTFM and try again...")