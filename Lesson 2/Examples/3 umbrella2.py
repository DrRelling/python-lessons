raining = False
haveUmbrella = False

print("Is it raining?")
print("Raining: " + str(raining))

print("Do you have an umbrella?")
print("Have umbrella: " + str(haveUmbrella))

if raining:
    if haveUmbrella:
        print("You have an umbrella, go outside.")
    else:
        print("Since you don't have an umbrella, looks like you're staying indoors.")
else:
    print("Great, it's not raining - go enjoy the sunshine!")