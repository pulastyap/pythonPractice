
x = 20

def scope_test():
    x += 30 
    a = 10
    print("Global:", x, "Local:", a)

scope_test()
print("Global:", x)