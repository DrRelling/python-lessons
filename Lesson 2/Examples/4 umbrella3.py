raining = True
haveUmbrella = False

print("Is it raining?")
print("Raining: " + str(raining))

print("Do you have an umbrella?")
print("Have umbrella: " + str(haveUmbrella))

if raining and haveUmbrella or not raining:
    print("Go outside!")
else:
    print("It's raining and you don't have an umbrella, looks like you're staying indoors.")