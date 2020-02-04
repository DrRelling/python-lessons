def ratsNest():
    x = 10

    def secondLevel():
        def thirdLevel():
            # x = 30
            print(x)
        thirdLevel()
    secondLevel()

ratsNest()

input()















def timesTwo(x):
    print(x * 2)

delayedFunction = timesTwo

delayedFunction(10)

input()


















def closure():
    x = 1

    def innerFunc():
        nonlocal x
        print(x)
        x += 1
    return innerFunc

closureFunc = closure()
closureFunc()
closureFunc()
closureFunc()

input()

def closure2(x):

    def innerFunc():
        nonlocal x
        x += 1
        print(x)
    return innerFunc

closureFunc2 = closure2(5)
closureFunc2()
closureFunc2()
closureFunc2()
