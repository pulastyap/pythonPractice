x = 30
a = 10

def scope_test():
    global a
    a = 0
    print(x, a)

scope_test()

print(x,a)