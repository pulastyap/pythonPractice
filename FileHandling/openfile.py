
with open("/Users/pulastya/Downloads/test.txt", "+r") as file:
    lines = file.readlines()
    print(lines)


'''
file = open("/Users/pulastya/Downloads/test.txt", "+r")

print(file.readlines())
print(type(file))
file.close()
'''