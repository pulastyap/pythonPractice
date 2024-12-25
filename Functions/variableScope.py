x = 30
a = 10

def scope_test():
    a = 20
    print(x, a)

scope_test()

print(x,a)