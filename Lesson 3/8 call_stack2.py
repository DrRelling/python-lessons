stack = ""

def a():
    global stack
    stack += "a"
    print("a() starts (stack: " + stack + ")")
    b()
    d()
    stack = stack[:-1]
    print("a() returns (stack: " + stack + ")")

def b():
    global stack
    stack += "b"
    print("b() starts (stack: " + stack + ")")
    c()
    stack = stack[:-1]
    print("b() returns (stack: " + stack + ")")

def c():
    global stack
    stack += "c"
    print("c() starts (stack: " + stack + ")")
    stack = stack[:-1]
    print("c() returns (stack: " + stack + ")")

def d():
    global stack
    stack += "d"
    print("d() starts (stack: " + stack + ")")
    stack = stack[:-1]
    print("d() returns (stack: " + stack + ")")

a()